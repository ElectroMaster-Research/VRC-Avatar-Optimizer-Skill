# Ownership, removals, and baseline

## Identify the customized source

Resolve the running project and open scene instead of trusting a remembered path.
Record stable hierarchy identities, prefab sources, nested connections, descriptor, and active states.
Check unsaved scene changes before copying or reloading anything.
Do not discard another task's dirty state.

Duplicate the designated customized hierarchy instance, not an unmodified stock prefab.
Give the candidate an explicit name and private asset namespace.
Do not unpack connected instances when the user prohibits unpacking.
Use supported overrides or variants where possible.
If an operation requires unpacking, stop for a decision.
Never apply candidate overrides back to a shared source prefab without authorization.

## Recoverable changes

Before a risky phase, save an authorized recovery checkpoint outside the mutation path.
Record the scene, source snapshots, private dependencies, source hashes, and tool versions.
Keep the earlier accepted candidate recoverable.
Record protected roots separately from the mutable candidate.

Undo can restore scene objects but cannot prove restoration of files on disk.
Use bounded Undo groups where supported.
Check restored snapshots after an exception.
Keep newly created assets for inspection until their ownership and references are resolved.
Never delete a private folder merely because a phase failed.
Old private assets can remain dependencies of recovery scenes.

## Reference ownership

For each proposed asset change, inventory every relevant consumer:

- Scene objects, prefab instances, and prefab sources.
- Materials, shader-property aliases, and animated material assignments.
- Clips, BlendTrees, controllers, override controllers, masks, and synchronized layers.
- Expression menus, parameters, generated controls, and processor configuration.
- Meshes, renderer bone arrays, constraints, contacts, and PhysBones.

Create private derivatives only for affected shared assets.
Unchanged meshes, clips, materials, and textures can remain shared.
Map source GUIDs and hashes to private paths and GUIDs.
Reject an existing destination unless its ownership and current contents match the plan.
Do not overwrite a previous partial result blindly.

Preserve metadata and effective importer settings in ownership evidence.
Use targeted asset saves where sufficient.
Review dirty assets before any global save.
A file hash check does not inspect unsaved objects in Unity.
Combine disk evidence with live serialized snapshots and a save/reload check.

## Authorized feature removal

Resolve proposed removals during Stage 1, before execution begins.
Default to retaining and optimizing meshes. Offer removal as an optional alternative, not a requirement for starting work.
An inactive object or disabled renderer can be an intended runtime toggle.
Trace menus, animation bindings, parameters, external inputs, and processors before classifying an item as unused or unreachable.
Record protected features and their intended runtime availability.
Unknown reachability is not proof of non-use. Confirm intent with the user during Stage 1.
Even confirmed unused items require explicit removal authorization.

Resolve exact object and mesh names from the current hierarchy.
Similar wording does not establish that an object is the intended target.
Ask when more than one material interpretation remains.

For an authorized system removal, trace both direct and indirect references.
Inspect associated components, constraints, menus, parameters, animations, and processor configuration.
This procedure does not authorize removal of any feature by itself.

Classify each dependency as exclusive, shared, or unresolved.
Remove exclusive functionality from the candidate only.
Split a shared asset into a candidate-private derivative when needed.
Retain shared behavior and externally referenced dependencies.
Do not delete components merely because their names contain a keyword.

After cleanup, inspect authored and processed output for:

- Removed objects, generated components, and obsolete bindings.
- Missing scripts, broken references, and dangling menu controls.
- Remaining parameter declarations, drivers, transitions, and motion references.
- Preserved clothing, customization, face tracking, and unrelated controls.

An inactive toggle is not proof that removed functionality is absent.
Unused assets outside the candidate need not be deleted to prove removal from the built avatar.

## Freeze the correct baseline

Plan baseline coverage in Stage 1. Capture and freeze the comparison baseline in Stage 2 before optimization.
Capture the behavioral and visual baseline after authorized removals and complete dependency cleanup.
Without removals, use the candidate's initial customized state.
Record pre-removal metrics separately when useful.
Never compare final behavior against intentionally removed features.

Capture the processed menu catalogue and parameter schema.
Record default values, saved flags, reset behavior, gestures, tracking modes, clothing states, and relevant motion.
Include stable runtime restoration and appearance captures.
See [runtime validation](runtime-validation.md) for the test contract.

Pin baseline inputs, reports, images, and scripts with hashes.
Do not overwrite the baseline when a later candidate fails.
If the user later authorizes another removal, preserve the original raw evidence.
Record the new authorization and exact expected differences.
Use an explicit comparison adapter or separately versioned baseline contract.
Keep retained assertions, timing, and tolerances unchanged unless a distinct decision justifies a change.

## Concurrency

Assign one operator to Unity state changes.
Parallel workers can inspect evidence, research definitions, prepare code, or review images.
They must not start overlapping Play runs, imports, saves, or Builds.
Use an ownership marker for asynchronous test runners.
Do not clear the marker until callbacks complete or cancel safely.
Restore protected-root active states before saving the authoring scene.
