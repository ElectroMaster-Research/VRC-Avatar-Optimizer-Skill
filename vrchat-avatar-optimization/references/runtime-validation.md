# Runtime validation

Use this reference when optimization can affect retained behavior, appearance, or deformation.
AV3 means the Lyuma Av3 Emulator. FT means face tracking.
Emulator acceptance does not establish tracker input, OSC transport, audible audio, networking, client persistence, or in-game behavior.
Plan coverage in Stage 1. Execute verification and permitted repairs iteratively within Stage 2.
Stage 3 reports the evidence. It is not a deferred verification stage.

## Establish the baseline

Duplicate the user's customized source instance, not an unrelated stock prefab.
Preserve the source hierarchy, prefab connections, shared assets, and authored active states.
If the user authorizes feature removal before optimization, use this order:

1. Remove only the authorized features from the copy.
2. Remove functionality that exclusively belongs to those features.
3. Audit remaining menus, parameters, bindings, components, and references.
4. Isolate the candidate before runtime preprocessing starts.
5. Capture the processed manifest, behavior, visuals, and metrics.
6. Freeze the accepted post-removal baseline before optimization.

A pre-removal snapshot protects the source. It is not the optimization comparison baseline.
An intermediate checkpoint or reconstructed diagnostic reference does not replace that baseline.
For optimization without removals, freeze the customized candidate's initial state instead.

Derive the test catalogue from the processed avatar.
Record menu fields, submenu topology, parameter types, defaults, saved flags, expression cost, and startup inputs.
Do not reuse another avatar's control count or generated parameter names.
Pin the baseline reports and raw inputs by hash.
Create uniquely labeled evidence files. Do not overwrite completed runs.

## Validation scope and cadence

Choose checks from changed dependencies, failure risk, and the user's acceptance criteria.
Record the planned checks before the trial.
Lightweight trial checks reject unsuitable candidates. They do not establish final acceptance.

| Checkpoint | Evidence and scope |
|---|---|
| Read-only audit | Inspect available records and files. Report gaps without invoking side-effecting runtime or Build helpers. |
| Each trial | Check relevant counts, references, compilation, topology, data contracts, and other inexpensive rejection criteria. |
| Selected candidate or meaningful phase | Check affected runtime behavior, actual control transitions, native images, deformation, and processed metrics. |
| Final delivery | Check all applicable SDK categories, SDK validation, fresh bundle sizes, preservation, save/reload, and the agreed acceptance coverage. |

Do not run every expensive suite after every minor trial without a dependency-based reason.
Do not omit a final requirement merely because trial checks passed.
Run fresh tests when the user explicitly requires them.
Do not replace mandatory AV3 acceptance with static checks, dependency hashes, or another emulator.
Reuse earlier evidence only when the acceptance criteria permit reuse and the dependency audit supports it.
Label reused evidence explicitly.

Use this table to identify affected checks. It does not limit broader user-required coverage.

| Changed dependency | Affected checks to consider |
|---|---|
| Texture or importer settings | Material variants, close/distant detail, masks, transparency, and mip behavior |
| Renderer or material consolidation | Remapped controls, visibility combinations, animation paths, blendshapes, bounds, and sorting |
| Topology or skin data | Exposed surfaces, relevant shapes, folded poses, clothing fit, and transitions |
| Bones or PhysBones | Changed chains, attachments, transient/settled motion, collisions, and retained interaction |
| Controllers or parameters | Changed controls, defaults, saved/reset behavior, gestures, FT ownership, and mode transitions |

For an unchanged dependency, document why its earlier evidence still applies.
For a new or changed dependency, execute checks that can detect its relevant failure modes.
If a required tool is unavailable, report the blocked gate instead of narrowing acceptance silently.
Repair detected regressions within the approved scope, then repeat affected checks.
Do not request another approval for routine repairs or tests already covered by the Stage 1 plan.
Keep test cadence separate from the user's progress-delivery cadence.
Final-report-only mode suppresses optional messages, not verification, evidence capture, or accurate blocker records.

## Choose behavior coverage

Select suites from retained features and proposed changes.
Cover every retained menu control and every relevant control combination in the agreed acceptance scope.
Do not replace required full control coverage with a convenience sample.
Use actual menu operations when claiming menu behavior.
Resolve parameters through the processed runtime's supported mappings.
Test informational controls separately without opening external websites.

| Suite | Evidence to retain |
|---|---|
| Controls | OFF/ON outputs, navigation, actual visibility, and restoration |
| Saved/default reset | Saved values, default-only reset, and values reacquired after each reset |
| Gestures | Relevant left/right combinations, early frames, settled outputs, and facial inhibition |
| FT | Supported inputs, extremes, eye/mouth ownership, native fallback, and mode transitions |
| Clothing | Compatible combinations, dependent shapes, FT modes, transition timing, and exposed surfaces |
| Poses/accessories | Relevant low poses, locks, accessories, occluders, and restoration |
| Physics | Changed chains, repeatability, transient motion, settled motion, and corresponding geometry |

Test every retained FT mode relevant to clothing or gestures.
Include held gestures across mode changes when ownership can change.
Record inherited limitations. Do not modify retained behavior merely to satisfy new assertions.

## Own runtime state and timing

Assign one operator to Unity state changes.
Run one suite at a time with a completion record and an ownership marker.
Do not erase a marker while its callback can still execute.
Check older runners separately if they lack that marker.

Keep reference avatars inactive during isolated testing.
Restore their authored active states before saving.
Capture entry state before each suite. Establish required modes through real controls.
Wait for a stable runtime and settled Animator state.
Reacquire runtime objects and parameters after startup or reset when their identities change.

Count distinct observed frames, not repeated reads in one Unity frame.
Declare settling criteria, time limits, and restoration limits.
Reject skipped frames when the fixture requires frame correspondence.
Restore changed controls, inputs, root poses, timing settings, and temporary objects after success or failure when possible.
Record restoration failure independently from case results.

## Correct fixtures without changing the acceptance contract

Diagnose a failing baseline assertion before changing the avatar.
Separate inherited behavior, incorrect expectations, wrong entry state, fixture timing, and candidate regression.
Preserve the failed evidence and create a new labeled run after correction.
Do not relax thresholds, delete fields, or change expected outputs merely to obtain a pass.

For example, a mode suite can pass settled cases while failing initial-state and restoration comparisons.
Reestablish the baseline mode through its actual menu control before repeating the unchanged suite.
Similarly, startup values captured before Animator settlement can produce a false restoration failure.

Inspect installed runtime behavior for ownership-sensitive inputs.
Check whether tracking ownership prevents the emulator from applying a requested input.
Establish the required ownership through supported controls before comparing outputs.
Inspect the installed emulator instead of assuming a fixed delay or API behavior.

## Compare semantics explicitly

Compare menu schemas and contracts exactly.
Declare numeric tolerances before candidate comparison.
Keep run labels, paths, timestamps, and absolute Unity frame numbers separate as telemetry.
Continue to compare observed-frame indices, transition timing, skipped frames, visibility, and output states.

Pair observations by complete case identity, phase, view, and occurrence where necessary.
Reject missing records, incomplete runs, ambiguous duplicates, and mapping collisions.
Keep timing-derived blink fields in raw evidence.
If deterministic restoration excludes them, declare the exact exclusion and retain visual review.

After renderer consolidation, require an executed source-to-result map.
Include semantic roles, shape names, vertex ranges, proxies, and material-slot ownership.
Measure actual mapped output. Do not infer visibility from a menu parameter or merged renderer activation.
Reject partially switched slots and missing renderers, bones, or shapes.

Accept material aliases only through completed private-copy and binding reports.
Check effective material settings beyond the authorized replacements.
For later approved removals, use a pinned adapter that changes only an expected copy.
Preserve raw differences. Limit the adapter to authorized fields, identities, and derived counts.
Unknown evidence kinds must fail. Retained timing and behavior remain comparable.

## Review visuals and physics separately

Correct shape weights do not prove correct deformation.
Parameter equality does not prove garment fit, outlines, transparent sorting, or physical motion.
Pixel statistics do not grant visual acceptance.

Capture matched cameras, lighting, poses, control states, and inputs for the final before/after visual pairs.
Include protected default-disabled toggles in their visible states when relevant to the optimization.
Use still pictures for static comparisons and animated GIFs for relevant motion that still pictures cannot establish.
Record dimensions, hashes, missing pairs, camera differences, and unsynchronized shader or blink timing.
Inspect native images at useful distances and exposed views.
Distinguish contact-sheet coverage from native-image coverage.
State resolution, occlusion, and sampling limits.
Keep uncropped evidence. Enlargement cannot recover absent detail.
When verification produces fixes, retain representative issue-before/repair-after captures in the same failing state.
Show these examples with the baseline/final comparison in the Stage 3 report.
Explain appearance and behavior tradeoffs alongside an overall quality comparison.
If evidence capture is blocked, name the cause and missing comparisons. Do not claim complete visual acceptance.
Do not substitute a text-only final for the required visual report or fabricate capture evidence.

Use fixed eligibility, core, guard, and silhouette regions when a local repair needs quantitative coverage checks.
Define those regions before judging the candidate.
Do not move a failed boundary or weaken a protection gate to accept a repair.
Use same-capture comparisons for exact local pixel claims.
Retest changed surfaces and relevant intermediate deformations.

Check physics-fixture repeatability before interpreting reference-to-candidate differences.
An unchanged configuration must reproduce itself within the declared limits.
Record solver hooks, fixed timestep, capture rate, input frames, missed frames, and restoration.
Use installed-version evidence when selecting a solver-completion hook.
Do not assume an Editor update callback represents one solver step.

Use vertex correspondence only when topology and vertex identity remain compatible.
After topology changes, use valid bone comparisons and a justified geometry method.
A reconstructed runtime reference needs identity proof and restoration checks.
It supplements the baseline without replacing it.
Match physics claims to actual radius, colliders, grabbing, posing, and output configuration.
Do not claim collision or grabbing acceptance from motion-only tests.

## Reuse evidence through dependency proof

Repeat affected tests, not every unchanged suite automatically.
An explicit requirement for a fresh run takes precedence over evidence reuse.
Reuse earlier results only after these checks:

1. Identify the exact accepted checkpoint and claim scope.
2. Check hashes for accepted reports and all supporting raw inputs.
3. Identify each claim's authored dependencies.
4. Compare those dependencies and metadata with the new checkpoint.
5. Compare scene and avatar snapshots with exact permitted deltas.
6. List claims that remain applicable and claims that require fresh evidence.

Label reused evidence as reused, not rerun.
Separate generated caches from authored dependencies without claiming cache equality.
A scoped dependency audit does not replace a complete file inventory.
New surfaces, fresh SDK metrics, and bundle sizes need their own checks.
Preserve failed diagnostics, accepted tradeoffs, and unverified external behavior in the final report.
