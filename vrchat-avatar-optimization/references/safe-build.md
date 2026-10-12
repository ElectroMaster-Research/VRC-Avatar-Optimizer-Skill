# Safe local Build and final handoff

Use this reference before local SDK bundle creation and final delivery.
A successful Build proves neither retained behavior nor visual acceptance.
Keep runtime, visual, processed-metric, size, preservation, and cleanup gates separate.
Perform Build checks, repairs, and restoration within Stage 2. Report their results in Stage 3.
An authorized diagnostic Build can gather missing processed texture evidence under the same authority, ownership, and dirty-state safeguards.
Post-Build inventory completeness is a condition for complete-budget claims, not a prerequisite for collecting that evidence.

## Verify the installed Build path

Inspect the installed SDK API and registered callbacks before execution.
Record SDK, Unity, processor versions, target platform, and candidate identity.
Recheck source or assembly behavior after relevant dependency changes.

In inspected SDK 3.10.5, `IVRCSdkAvatarBuilderApi.Build(GameObject)` returned `Task<string>` containing the bundle path.
That API required an open SDK panel, an AvatarDescriptor, and a PipelineManager.
That public path did not call upload or `BuildAndTest`.
Do not infer the same guarantee for another SDK or third-party callback without inspection.
Client testing, remote ID operations, and upload require separate authority.

The inspected exporter modified its supplied target before creating the processing clone.
It changed descriptor and PipelineManager fields, marked the target scene dirty, and saved that scene.
Use a complete authoring copy in an owned validation scene when those writes could affect the deliverable.
Do not pass an already preprocessed emulator clone.
An explicitly requested manual-bake workflow needs the separate [persistence and callback analysis](manual-bake.md).
Do not assume a manually baked NDMF duplicate includes all SDK preprocessors or cannot be processed again.
Keep scratch identifiers and generated blueprint IDs off the authored candidate.

Capture `ActiveBuildType` before changing it.
In SDK 3.10.5, stale Publish state rejected blank blueprint IDs.
Test state could assign a local ID to the disposable target.
Test state plus `Build(target)` was not `BuildAndTest`.
VRCFury also observed build type, so None was not equivalent for every callback.
Treat these as installed-version mechanisms, not fixed defaults.

## Admit dirty state before global saves

A scratch scene does not isolate global `AssetDatabase.SaveAssets()` calls.
Inspected VRCFury and NDMF callbacks invoked that operation.
It can persist unrelated loaded dirty assets.
Require exclusive validation ownership and a known dirty-object state before Build.

Separate authored dirty assets, importer settings, reviewed live cache differences, and unexplained state.
Stop for unreviewed identities or settings.
Do not clear dirty flags, replace serialized content, or reimport assets to force admission.
Do not assume a package save filter protects unrelated packages.
Native save behavior remains uncertain when managed source cannot establish its effects.

For dirty Shaders or importers that need a detailed review:

1. Pin source, metadata, and resolved dependency bytes.
2. Record complete object identities and serialized JSON.
3. Compare matched objects with their earlier reviewed captures.
4. Enumerate exact permitted leaf paths and old/new values.
5. Review new objects through complete current pins and persisted importer settings.
6. Read live importer settings immediately before Build.
7. Check that getters did not change the captured state.
8. Capture the complete dirty set after those getters.
9. Require one-to-one equality with the reviewed set at Build entry.

Do not exempt the Shader type or the complete `m_CompileInfo` field.
That field can contain code, include hashes, platform data, variants, and code hashes.
A reviewed code-hash delta does not authorize changes to other leaves.
Unknown live-only importer fields remain unknown, not automatically harmless cache.

Global saves can clear dirty flags normally.
Therefore, do not reuse the pre-Build dirty-state test as the post-Build preservation test.
Compare authored bytes and persisted importer settings afterward.
If protected data changes, preserve the changed version and stop success reporting.

## Prepare a preservation transaction

Create a recovery checkpoint for the selected candidate and its current private dependencies.
Record serialized snapshots of the candidate and protected reference roots.
Pin prefab connections, scene bytes, source assets, private assets, metadata, and relevant settings.
Use a complete file inventory where the Build can affect project-wide assets.

Record exact temporary paths before creation.
Reject preexisting scratch targets that the task does not own.
Preserve earlier bundles and reports before another Build can rotate or delete them.
Capture selection, task-opened SDK panels, build type, preferences, fog settings, callbacks, and session bundle paths as applicable.
Check the installed wrapper's early-error cleanup behavior.
Do not assume normal completion restores every changed setting.

Prefer targeted saves for private asset preparation.
An unavoidable global save still requires the dirty-state review.
Keep old private assets while recovery checkpoints or accepted evidence reference them.

## Measure the processed artifact

Measure only the isolated processed candidate.
Do not sum scene roots or substitute a raw hierarchy estimate.
Record every SDK category, its definition, units, limit, rating, and measurement context.
Use installed limits for the requested platform and any stricter user ceilings.
Do not copy thresholds from another avatar or SDK version.

Apply [full texture inventory and accounting](full-texture-measurement.md) to the exact processed artifact.
Do not substitute the SDK's current-material scan for the full retained material union.
Include retained alternatives from supported source object curves and compiled PPtr bindings, plus generated and non-material references.
Reconcile current-material, alternate-material, menu/other, and unresolved partitions by actual object identity.
Count each retained object once, including preserved or skipped textures. Do not merge distinct objects by content hash.
Calculate supported nominal format payloads separately from SDK estimates, stored bytes, CPU storage, and residency.
Keep parser failures, unsupported layouts, unresolved pointers, and omitted scopes explicit.
Missing coverage blocks complete or passing-budget claims, not independent authorized checks or an admitted diagnostic Build.

Record renderer material entries, submeshes, unique materials, and measured draw calls separately.
Pin the installed scanner definition instead of treating its material statistic as a universal server/client count.

Keep emulator measurements and Build callback measurements when they differ.
Investigate concrete mechanisms such as descriptor contacts, processor-generated objects, or renderer bounds updates.
Do not manually alter one report to match another.
Record confirmed mechanisms separately from inferred lifecycle explanations.

Record editable authoring-hierarchy SDK metrics separately from final processed-build metrics.
AAO can optimize at build time while the editable hierarchy still shows SDK warnings.
Identify each measured artifact, platform, processor configuration, and retained runtime features, including initially disabled toggles.
Do not claim only “Poor” or treat an authoring warning as proof that processed optimization failed.
Do not dismiss that warning without processed-build evidence either.

## Report the build pipeline and metric comparison

Name each build-time optimization tool actually used, with its version, enabled operations, affected objects, and concrete effect.
For example, report AAO's executed renderer/submesh merges when those operations occurred.
Report explicit texture derivatives and TextureImporter settings separately from build-time passes.
Do not present these examples as automatic results or assume that installing a package activates every operation.
Separate confirmed effects from projected savings. Do not double-count savings from overlapping passes.
If per-tool attribution is unavailable, report the combined measured change and the attribution limit.

AAO passes and NDMF-hosted processing run in the editor's BUILD pipeline before any upload.
These optimization passes do not run inside the VRChat client.
NDMF coordinates editor-side passes. The selected optimizer performs each transformation.
The client uses the resulting avatar, including its retained controls and generated runtime behavior.
Editor previews or emulator preprocessing can also invoke processing, but they do not establish final SDK Build results.
The editable hierarchy can still show Very Poor because it retains authoring objects that build-time processing transforms.
TextureImporter changes apply during texture import before the Build, not as a VRChat client optimization pass.
The authoring input can therefore already include imported texture savings before build-time optimizers run.
Preserve historical tool attribution in existing evidence. A changed recommendation does not change what an earlier run used.

Show a compact table with this structure. Replace field descriptions with actual values and evidence labels, not invented results.

| Metric | Before: editable authoring input, before processing | After: exact final processed SDK Build |
|---|---|---|
| SDK material statistic | Versioned scanner count and definition | Processed SDK count and evidence link |
| Renderer material entries / submeshes / unique materials | Three separate counts | Corresponding counts and evidence links |
| Measured draw calls, when claimed | Measurement context or unavailable | Measurement context or unavailable |
| Skinned mesh renderers | Authoring count and evidence label | Processed count and evidence link |
| Triangles | Authoring count and evidence label | Processed count and evidence link |
| SDK texture estimate | Scanner scope, bytes/MiB, and evidence label | SDK scope, bytes/MiB, and evidence link |
| Full material-format payload | Current plus additional alternate-material union | Completed-artifact union, bytes, and inventory link |
| Menu/other texture payload and unresolved scope | Separate counts, bytes, and unknowns | Corresponding partitions and coverage limits |
| Stored texture bytes / CPU storage / resident GPU memory | Separate measured or estimated quantities, or unavailable | Same distinct labels and supporting evidence |
| Bones | SDK-counted bones or labeled projection | SDK-counted bones and evidence link |
| PhysBones | Components / affected transforms / colliders / collision checks | Same individual SDK values and evidence link |
| Other relevant physics/dynamics | Contacts, constraints, or other affected categories with units | Corresponding SDK values and evidence links |
| Overall rank | Authoring SDK rating or labeled estimate | Measured SDK rating, or unverified if unavailable |

Identify the exact authoring input and processed avatar above the table.
Record the scene/root identity, input checkpoint, platform, SDK version, processor configuration, build identifier, and bundle/report paths and hashes.
Link the retained-feature manifest and relevant AV3 evidence, including default-disabled toggles available at runtime.
Keep the frozen baseline-to-final comparison separate when it differs from this same-build input/output comparison.
This compact summary does not replace the complete category report, SDK validation, or fresh size checks.

Use explicit evidence labels: measured authoring, measured final Build, estimate, or unavailable.
Label preview and emulator measurements by their actual context, not as measured final Build.
Prefer actual final SDK Build measurements over projections.
Never claim verified Poor or better from an estimate, a preview, or an incomplete set of SDK categories.
If final measurement is blocked, report projected rank as unverified and name the blocked operation.
A measured SDK texture-memory statistic remains the SDK's memory estimate. It is not a measurement of resident client VRAM.

## Require fresh sizes after Build completes

Wait for the current Build task to return successfully.
Measure compressed bytes from its returned bundle path.
Measure uncompressed packed bytes from the corresponding fresh build report.
Record report freshness, exact bytes, bundle hash, report hash, units, limits, and comparison results.

The processed-avatar callback can run before bundle completion.
Its size fields can be unavailable or refer to an earlier report.
`None` means unavailable, not zero.
Require a fresh `Library/LastBuild.buildreport` when the installed helper uses that report.
Do not rely only on a successful Boolean or a plausible old size.

In SDK 3.10.5, size-helper Booleans meant “limit exceeded,” not “measurement succeeded.”
Missing reports or exceptions could return false with zero bytes.
Its uncompressed helper summed packed contents plus overhead.
That value was distinct from texture memory, source-file totals, and compressed length.
Confirm current definitions and boundary comparisons in the installed version.

The inspected uncompressed helper wrote `Assets/Build AssetBundles.buildreport`.
It copied, imported, read, and deleted that fixed temporary asset.
Require the exact path and its metadata to be absent before that operation.
Do not let the helper overwrite a user asset.
Check for leftovers after errors. Do not describe that helper as read-only.

SDK labels can differ from their arithmetic units.
Report bytes and the actual divisor when distinguishing MB from MiB.
Preserve the successful bundle and report before later builds can replace them.

After completion, export the retained artifact's serialized material/texture graph when the parser supports it.
Record parser/version, input hashes, inventory/output hashes, format definitions, and errors.
Compare the completed artifact with processed-preview mappings. Explain retained originals, generated copies, and changed counting scope.
Use [Debug and troubleshoot notes](debug-and-troubleshoot-notes.md) for discrepancies rather than selecting the smaller total as proof.

When upload is separately authorized and completed, record the exact avatar version, file ID, and file version.
Correlate that server file's supported checksum and byte length with the exact completed local bundle.
Retain SHA-256 separately if the server uses another checksum. An embedded avatar ID alone is not upload proof.
Version client/server observations with timestamps, units, precision, and loaded-artifact evidence.
Protect credentials and signed URLs. A rounded match does not prove an unpublished server formula or measured GPU residency.

## Restore, audit, and hand off

Restore captured settings and authored reference-root states.
Remove only task-owned temporary objects, scenes, prefabs, and report files.
Check resolved paths and ownership before deletion.
Do not delete an entire cache directory to remove one failed build.
Retain recovery copies and diagnostic evidence until acceptance completes.

If cleanup fails, preserve that failure report.
Perform bounded recovery only within the authorized scope.
Report any recovery that cannot restore the original selection or panel state exactly.
Do not relabel recovered state as exact restoration.

Save and reload the intended scene after cleanup.
Capture fresh candidate and reference snapshots.
Check prefab connections and private-asset persistence.
Compare protected authored bytes and importer settings with the pre-Build records.
Include hidden files in the inventory or declare their exclusion.
Detect files that change during hashing.
Classify exact generated-cache paths separately. Do not exempt all package files.

A disk audit does not inspect unsaved Unity objects.
A serialized snapshot proves only the state captured at its recorded time.
Require fresh reload evidence and clean Edit mode before claiming a completed editor handoff.

Report final metrics, fresh sizes, saved artifact location, passed gates, accepted differences, failed diagnostics, and unverified behavior.
Include the [Stage 3 visual report](../SKILL.md#stage-3-final-report) with matched before/after pictures or relevant motion GIFs.
Include representative verification fixes when they occurred, concrete tradeoffs, and an overall quality comparison.
Report unavailable visual evidence as an incomplete acceptance gate, not a text-only substitute for completion.
Identify reused tests separately from fresh executions.
Confirm whether upload or client testing occurred.
Use required gates rather than an invented overall verification percentage.
Stop success reporting if preservation, restoration, or another required gate remains unresolved.
