# VRChat avatar optimization guidance

This package guides authorized optimization toward VRChat Poor or better while preserving retained appearance, behavior, and source assets.
It supports PC and Android workflows, with separate platform limits and acceptance requirements.
It is not a turnkey optimizer.

## Internal guide and shared package

Install the complete [vrchat-core package](../../README.md), not this specialist alone.
The [core entrypoint](../../SKILL.md) owns shared bootstrap, private preferences, Unity setup, and evidence helpers.
This internal guide has no independent discovery metadata.
Read [GUIDE.md](GUIDE.md) for the three-stage workflow and dependency preflight.
Use the specialist references for tools, texture measurement, geometry, Build evidence, and synthetic examples.
Use [experimental-optimization.md](experimental-optimization.md) for the unresolved reducer comparison.
The package does not supply an optimizer, AV3 harness, or general texture-accounting engine.
Disk hashes do not create backups. Capture metrics do not establish visual acceptance.

## Three-stage workflow

1. [STAGE 1: Investigation and planning](GUIDE.md#stage-1-investigation-and-planning) resolves identity, dependencies, feasibility, contributors, tradeoffs, and progress preference.
2. [STAGE 2: Execution, verification and repair](GUIDE.md#stage-2-execution-verification-and-repair) implements the approved plan through tests and repairs.
3. [STAGE 3: Final report](GUIDE.md#stage-3-final-report) delivers scoped evidence and unresolved limits.

For implemented optimization, include matched before/after visuals, metrics, and quality comparisons.
For read-only audits, report observations and missing evidence without unauthorized Builds or capture fixtures.

Stage 1 records protected runtime features and toggles, including default-disabled meshes.
Retention and optimization are the default. Removal is an optional alternative that requires explicit authorization.
The user acknowledges quality and behavior tradeoffs before execution.
Routine implementation, verification, and repairs then continue within that approved scope without repeated approval requests.

The [rank-driven policy](GUIDE.md#rank-driven-operation-selection-and-stopping) applies to all tools and custom optimization operations.
Measure processed/build-stage metrics first. Select only operations needed for actual gaps against the requested platform and rank.
Normally skip passing categories and recheck necessary coupled changes.
Stop optimization experiments when the entire avatar meets target, while completing required final verification and save/reload.
Keep unused operations disabled and retain processors responsible for the passing build.
Do not trial every tool or expand benchmarks after required checks pass without new evidence or authorized scope.

AAO and d4rk are supported options, not blanket enablement or guarantees of appearance preservation.
Stage 1 applies the [operation-level complexity gate](references/optimization-tools.md#operation-level-complexity-gate) after establishing actual need.
Use explicit persistent implementation for necessary operations rated 1/5 through 3/5.
Only necessary 4/5 or 5/5 operations permit AAO/d4rk import or use. A qualifying score does not require a tool.
The [shareable complexity table](references/optimization-tools.md#explicit-implementation-complexity) gives engineering estimates that include preservation and saved-output validation.
Record justified score adjustments and unavoidable coupled passes. Do not inflate scores or remove an existing required dependency automatically.
Their shared tools reference covers compatibility, overlapping operations, and targeted validation such as shader-toggle checks.
Do not add d4rk when AAO already meets the requested target.
Its presence beside AAO in the reference is not a reason to import it.

When geometry reduction is necessary, original upstream Meshia is the primary reducer and meshoptimizer is the conditional fallback.
The [reducer-selection policy](references/geometry.md#primary-reducer-and-conditional-fallback) requires proportional trials and concrete reasons for fallback.
Skip reduction when target metrics already pass. Do not repeat unproductive trials or treat either reducer as repair-free.
This is a workflow preference, not evidence that Meshia needs fewer repairs. Comparative experiments require separate scope.

Stage 1 also records progress delivery, such as every five minutes, every ten minutes, or final report only.
Use supported scheduling or heartbeat tools when available. Do not claim scheduled delivery when unavailable.
Preserve notification preferences, avoid duplicate monitors, and retire task-owned schedules at completion.
Final-report-only mode suppresses optional chatter and questions. It does not expand authority or remove required checks.
Higher-priority communication and tool constraints still apply.

Final reports for implemented optimization require matched still pictures or animated GIFs for relevant motion.
Include representative fixes when they occur.
Missing capture evidence prevents a complete visual acceptance claim. A text-only summary does not replace it.
Report editable authoring-hierarchy SDK metrics separately from final processed-build metrics.
Build-time AAO processing can leave authoring warnings visible. Rank claims must identify the measured artifact and retained runtime features.
These passes run during BUILD before any upload, not inside the running VRChat client.
NDMF coordinates editor-side passes. The editable hierarchy can retain a Very Poor SDK rating.
The final report names each tool used and its concrete effect.
The [compact comparison table](references/safe-build.md#report-the-build-pipeline-and-metric-comparison) emphasizes material slots and skinned mesh renderers.
It also covers triangles, textures, bones/physics, and overall rank, with explicit evidence labels.
Only measured final SDK Build results can support a verified build-rank claim. Estimates remain unverified.

The preferred texture method uses explicit Unity TextureImporter settings for platform maximum resolution and compression.
Maximum resolution is not a material property.
Reuse compatible shared materials and textures. Create only derivatives needed for differing optimized settings or isolated texture assignments.
Bind those derivatives only to the optimized avatar's affected materials and controls.
This policy reduces external dependencies. It does not establish a cause for unresolved metric discrepancies.
Do not copy all materials for unrelated appearance edits.
Inventory current and alternative material textures, menu/other references, and unknowns before making a complete texture-budget claim.
Keep preserved/skipped textures in the budget. An incomplete selection list must not become an exclusion policy.
Report SDK estimates, nominal format payload, stored bytes, CPU storage, and actual residency separately.
An authorized diagnostic Build can supply missing processed evidence without requiring that post-Build inventory in advance.

## Install and use

Use the [core README](../../README.md) for installation, migration, updates, and discovery limits.
Invoke `$vrchat-core` with the project, avatar source, platform, rank, and permitted changes.
The core routes rank work to this internal specialist.
Use the [shared private store](../../user-data/README.md) and [bootstrap](../../bootstrap.md).
Do not install this folder as another skill.

## Capabilities and dependencies

The agent must read project files and official documentation, inspect dependencies, and distinguish observations from unverified claims.
Implementation also requires authorized file editing, recovery, and a supported way to operate the intended Unity project.

Complete the [shared Unity MCP prerequisite](../../SKILL.md#prerequisite-configure-and-verify-unity-mcp) before substantive Unity inspection, edits, or tests.
Configure or reuse a compatible connection under applicable authorization.
Verify the intended project and editor through harmless, read-only MCP queries.
This prerequisite does not require MCP for every action.
Computer use remains allowed for setup, UI-only operations, visual inspection, and appropriate fallback.
Editor scripting or a cooperating human operator can also support authorized work.

If MCP setup or verification fails, report the concrete blocker and the available computer-use route.
Follow the entrypoint's explicit fallback-authorization procedure before continuing dependent Unity work without verified MCP.

No specific MCP implementation, model, provider, operating system, or personal project is prescribed.
Each selected tool still requires its own supported platform.

| Component | When required |
|---|---|
| Compatible Unity MCP integration | Upfront setup and project/editor identity verification. Follow the entrypoint's blocker and fallback procedure when unavailable. |
| Compatible Unity Editor, Avatars SDK, and target-platform support | Authoring, processed measurements, and local Build |
| Referenced shaders and authoring processors | When the retained avatar depends on them |
| Compatible AV3 emulator and a working test procedure | When the user requires AV3 acceptance |
| Blender or another geometry tool | Only when the selected method needs it |
| Python 3.9+ | Disk evidence and bootstrap checks use the standard library |
| Python 3.10+ and Pillow | Capture comparison and the complete shared test suite |
| Image tools, tracking devices, OSC, audio, or a client | Only for claims that require those tools or systems |

No runtime harness, Unity project, avatar, shader package, or geometry optimizer is bundled.
The agent must create or adapt project-specific tests before claiming their results.
Dependency preflight must identify missing, incompatible, or broken components.
Resolve required installation or correction decisions in Stage 1. Reuse existing specific authorization without repeated requests.
Do not install dependencies implicitly.
Missing required tools leave the corresponding acceptance gate blocked.

## Use outside Codex

Give the agent the complete core folder. Read its `SKILL.md` first.
Then read this guide and only the relevant routed references.
Other agents can ignore the core's `agents/openai.yaml` metadata.
Keep the host's instruction hierarchy, permissions, and user acceptance criteria in force.
Without Unity or tool access, use the documents for an audit or human-guided procedure, not a claimed implementation.

Use lightweight checks between trials. Run affected runtime and visual tests for selected candidates.
Complete requested final runtime, processed SDK, Build, preservation, and reload checks before declaring acceptance.
Explicit fresh-run requirements take precedence over evidence reuse.

## Scope, evidence, and licensing

The [worked example](references/synthetic-example.md) is synthetic and illustrative. It is not executed evidence.
The [rank reference](references/rank-and-platform.md) contains dated values and public citations. Verify current documentation and installed SDK behavior.
Methods require validation against each avatar and toolchain. This package does not guarantee universal results.

Keep generated logs, snapshots, images, reports, and avatar assets outside the distributable package.
They can contain private paths or project information.
The helper's checks were exercised on Windows. Verify its behavior on other target systems before relying on it.

No distribution license is specified in this package. No license was selected on the author's behalf.
Third-party software and assets retain their own terms.
