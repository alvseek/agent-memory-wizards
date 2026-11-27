"""Compile ``procedures/*.md`` into install-ready ``output/*.md``.

The shared composer expands Format 2 for the Markdown backend. Template links are
checked separately and preserved: the installed procedure needs their paths to
copy the files at runtime.

Usage: python setup-scripts/compile-procedures.py [--out DIR] [--quiet] [--strict]
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

from procedure_composer import Catalog, CompositionError, FileSource

# Repo root (this script lives at setup-scripts/compile-procedures.py).
_ROOT = Path(__file__).resolve().parents[1]

_TEMPLATE_DIRNAMES = ("plan-templates", "templates")

# A template reference anywhere (link or backtick code-path form) → its bare name.
_TPL_REF = re.compile(r"/(?:plan-templates|templates)/([a-z-]+)\.md")


@dataclass
class Report:
    """What one compiled procedure pulled in, and anything it could not resolve."""

    name: str
    out_path: Path
    components: list[str] = field(default_factory=list)
    templates: list[str] = field(default_factory=list)
    missing_templates: list[str] = field(default_factory=list)

    @property
    def clean(self) -> bool:
        return not self.missing_templates


def find_template(name: str, root: Path) -> Path | None:
    """Locate a template by bare name across the template dirs, in precedence order."""
    for dirname in _TEMPLATE_DIRNAMES:
        candidate = root / dirname / f"{name}.md"
        if candidate.is_file():
            return candidate
    return None


def template_names_in(text: str) -> list[str]:
    """Bare template names referenced in ``text`` — unique, in order of first appearance."""
    seen: dict[str, None] = {}
    for name in _TPL_REF.findall(text):
        seen.setdefault(name, None)
    return list(seen)


def collect_templates(text: str, root: Path) -> tuple[list[str], list[str]]:
    """Template names referenced by ``text``, collected transitively in discovery order.

    Returns ``(order, missing)`` without altering the text or adding template bodies.
    """
    order: list[str] = []
    missing: list[str] = []
    seen: set[str] = set()
    queue: list[str] = []

    for name in template_names_in(text):
        if name not in seen:
            seen.add(name)
            order.append(name)
            queue.append(name)

    index = 0
    while index < len(queue):
        name = queue[index]
        index += 1
        path = find_template(name, root)
        if path is None:
            missing.append(name)
            continue
        for nested in template_names_in(path.read_text(encoding="utf-8")):
            if nested not in seen:
                seen.add(nested)
                order.append(nested)
                queue.append(nested)

    return order, missing


def compile_one(src: Path, out_dir: Path, root: Path) -> Report:
    """Compile a single procedure into ``out_dir``."""
    return _compile(src, out_dir, root, Catalog(FileSource(root)))


def _compile(src: Path, out_dir: Path, root: Path, catalog: Catalog) -> Report:
    try:
        rendered = catalog.compose(src.stem, "markdown")
    except CompositionError as exc:
        raise CompositionError(f"{src.relative_to(root).as_posix()}: {exc}") from exc

    templates, missing_templates = collect_templates(rendered.text, root)
    component_refs = dict.fromkeys(
        (span.document_id, span.id) for span in rendered.spans if span.kind == "component"
    )
    out_path = out_dir / src.name
    out_path.write_bytes(rendered.text.encode("utf-8"))
    return Report(
        name=src.stem,
        out_path=out_path,
        components=[name for name, _reference_id in component_refs],
        templates=templates,
        missing_templates=missing_templates,
    )


def compile_all(
    root: Path | str = _ROOT,
    out_dir: Path | str | None = None,
    verbose: bool = True,
) -> list[Report]:
    """Compile every procedure. Returns one ``Report`` per compiled file, in name order."""
    root = Path(root)
    proc_dir = root / "procedures"
    out_dir = Path(out_dir) if out_dir else root / "output"

    if not proc_dir.is_dir():
        raise FileNotFoundError(f"procedures/ not found at {proc_dir}")

    catalog = Catalog(FileSource(root))
    sources = sorted(proc_dir.glob("*.md"))
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(
            f"Compiling {len(sources)} procedures "
            f"(inlining components, resolving templates) -> {out_dir} ..."
        )

    reports: list[Report] = []
    for i, src in enumerate(sources, start=1):
        if verbose:
            print(f"  [{i}/{len(sources)}] {src.name}")
        reports.append(_compile(src, out_dir, root, catalog))
    return reports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", help="output directory (default: <repo>/output)")
    parser.add_argument("--quiet", action="store_true", help="only print the summary")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="also exit non-zero on unresolved template references",
    )
    args = parser.parse_args(argv)

    try:
        reports = compile_all(_ROOT, args.out, verbose=not args.quiet)
    except CompositionError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    out_dir = Path(args.out) if args.out else _ROOT / "output"
    print(f"Compiled {len(reports)} procedures -> {out_dir}")

    unresolved = [r for r in reports if not r.clean]
    for r in unresolved:
        for name in r.missing_templates:
            print(f"  WARNING: {r.name}: template not found: {name}.md", file=sys.stderr)
    if unresolved:
        print(f"  {len(unresolved)} procedure(s) with unresolved references.", file=sys.stderr)
        if args.strict:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
