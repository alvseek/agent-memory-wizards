# Level Selection (plan component)

Which wizard a piece of work belongs to, decided by what that work holds rather than by how large it feels. **This is a component, not a standalone skill** — an orchestrating wizard reads and follows it at the step where it assigns a protocol to a child.

*Consumed by `/forge-of-covenant`, `/rite-of-creation` and `/council-of-wizards`, the three wizards that choose a protocol for their children. The leaf wizards (`/high-wizard`, `/pixel-wizard`, `/quick-wizard`) never choose a child, so each states the unit it carries in its own opening instead of reading this.*

---

## The units

Each level owns exactly one unit, and a level is the right answer when its unit is what the work holds.

| Level | Unit | What the unit is |
|-------|------|------------------|
| `/forge-of-covenant` | **Milestone** | a release boundary: the point at which a deliverable becomes available to its consumers |
| `/rite-of-creation` | **Phase** | work of a kind that gates the next kind — design before build, build before verify, verify before release |
| `/council-of-wizards` | **Sub-plan** | one deliverable that closes on its own and is released with its siblings |
| `/high-wizard`, `/pixel-wizard` | **Deliverable** | the largest piece that can be built, checked and handed over as one thing |
| `/quick-wizard` | **Change** | one small change, below the deliverable: too little to hand over on its own |

## The test

Ask what the work holds, and the first line that matches is the answer.

- **One deliverable, and releasing it finishes the work** → `/high-wizard`, or `/pixel-wizard` when the deliverable is design-led.
- **One deliverable, and reaching its consumers needs phases that gate each other** → `/rite-of-creation`.
- **Several deliverables that close independently** → `/council-of-wizards`.
- **Several kinds of work that must be done in order** — design, then build, then verify, then release → `/rite-of-creation`, with `/council-of-wizards` or `/high-wizard` carrying each phase.

Deliverables that must be done in a particular order are still deliverables: `/council-of-wizards` owns that with its dependency graph. The difference is between *different things* and *different kinds of work*, and only the second is `/rite-of-creation`.

## Two floors

- **A change is not a milestone.** `/quick-wizard` sits below the release boundary, so a single small change is never a milestone of its own: it is a phase inside `/rite-of-creation` or a sub-plan inside `/council-of-wizards`. Making each small change its own release is the waste batching exists to remove.
- **A milestone is not a deliverable.** The milestone is the dated promise; the deliverable is the build. A milestone holding one deliverable is ordinary, and it is run by the wizard that carries a deliverable.

## Where the release happens

A deploy belongs inside the wizard when *done* for this project includes deployed: then whoever finished the work also ships it, on whatever environment the project runs. When a separate, later act decides that the work goes live, that act sits outside every wizard, and the milestone ends at it. Which case a project is in is a fact about the project, not about these procedures.
