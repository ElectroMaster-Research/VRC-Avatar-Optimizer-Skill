# Proportional avatar validation

## Choose checks from changed dependencies

Define the acceptance checks before trials.
Respect the user's requested emulator, fresh-run requirement, and coverage.
Do not turn a material task into an unrelated performance audit or Build workflow.

| Change | Relevant checks |
| --- | --- |
| Tint or shader properties | Matched appearance under relevant lighting, saved values, shared users |
| Texture or importer | UV placement, channels, color space, detail, mips, alpha and affected variants |
| Shader family or locked program | Feature gates, render state, runtime properties, compilation, affected stereo paths |
| Spatial emission | Included and excluded regions, shared UVs, filtering, imported masks and native renders |
| AudioLink or material toggle | Defaults, off/on/re-enable, effective property blocks, signal behavior and unaffected channels |
| Slot assignments or animation bindings | Actual visibility, material swaps, clothing states, expressions and relevant FT modes |
| Rig, topology, bones or physics | Separate authorization and geometry/behavior validation beyond material comparison |

FT means face tracking. AV3 means the Lyuma Av3 Emulator when that tool is selected.
Do not substitute a parameter read or static inspection for requested runtime acceptance.

## Efficient cadence

For a substantial migration, capture one relevant overall control baseline before changes.
Run one overall final comparison after the selected changes.
Use narrow compile and visual checks between candidates.
Do not repeat the complete suite after every shader slider adjustment.

For a small change, select a smaller baseline and final test contract.
Derive control counts and test cases from this avatar's actual menus and dependencies.
Do not inherit another avatar's counts, parameter names, defects, or timing assumptions.

If the user adds later material-only work, preserve the completed evidence.
Check the dependencies before reusing control results.
Rerun only the affected appearance, shader, mask, and signal tests unless broader coverage is needed.
An explicit fresh-test request overrides reuse.

## Baseline and runtime evidence

Record the processed menu topology, parameter types, defaults, saved flags, and synchronization settings when controls matter.
Trace the actual parameter and material bindings through processors.
Use real menu operations when claiming menu behavior.
Inspect the resulting renderer visibility, blendshapes, bones, and effective shader values.
Input acceptance alone does not prove an output response.

Read renderer and indexed `MaterialPropertyBlock` values before falling back to shared material values.
An Animator can change a property block without changing the material asset.

Select poses, expressions, clothing combinations, and FT ownership modes affected by the work.
Include inactive wardrobe when it can become visible.
Record inherited failures without silently repairing them.
Do not open informational menu links just to count them as tested controls.

Declare settling criteria, timeouts, and restoration criteria.
Count distinct observed frames when frame timing matters.
Manual `PlayableGraph.Evaluate` steps are not Unity player frames or a physics simulation.
Describe that distinction in results.

Inspect preprocessing and Play-mode callbacks for side effects before running them.
Use an isolated target and one writer.
A preview scene alone does not protect unrelated dirty assets from a global save.

## Compare semantics without weakening the test

Keep the original baseline immutable.
Separate authorized material changes from geometry, control, and preservation checks.
Pair cases by complete identity, state, view, and occurrence.
Reject missing cases, unknown fields, ambiguous aliases, and incomplete runs.
Declare numeric tolerances before interpreting candidate differences.

Some processors generate new object names or identifiers on each run.
Do not erase those differences with an unrestricted regex.
Verify the generating code and construct an explicit mapping from stable structure or ordered references.
Require a bijection, consistent parent chains, and no collisions.
Continue comparing geometry, order, values, visibility, and timing.
Keep the failed comparison and the mapping evidence.

For large traces, use bounded summaries and lossless deduplication or compression.
Verify reconstructed states against hashes.
Do not print entire meshes or repeated states into the conversation.

## Repair a fixture failure

Distinguish wrong target, wrong entry state, stale bounds, camera error, timing, and real avatar regression.
Check whether the same failure exists in the baseline.
Do not change the rig to hide a camera or emulator defect.
Do not relax thresholds or drop unexplained fields to obtain a pass.

When only pictures failed, a focused replay can repair the visual evidence.
Require replayed state to match the recorded outputs.
Render matched material versions on the same posed geometry when appropriate.
Keep the original images labeled invalid.
Report fixture limitations that remain.

## Reuse contract

Before reusing a result:

1. Identify its accepted checkpoint and exact claim.
2. Verify hashes for its evidence and relevant authored dependencies.
3. Check meshes, controllers, parameters, bindings, and processor settings as applicable.
4. Check live scene and asset state against the permitted changes.
5. List which claims remain valid and which require new tests.

File hashes do not replace live-state checks.
Matched state does not replace visual review.
Preserved topology does not prove correct deformation or garment fit.

## State limits precisely

Report shader compile errors separately from temporary harness errors and existing Console entries.
Do not clear unrelated Console history to produce a clean-looking result.

Shader compilation does not prove headset stereo rendering.
Synthetic audio does not prove live-world AudioLink operation.
Editor tests do not establish OSC transport, networking, physics, persistence in the client, or upload eligibility.
Label executed, reused, failed, and untested checks separately.
