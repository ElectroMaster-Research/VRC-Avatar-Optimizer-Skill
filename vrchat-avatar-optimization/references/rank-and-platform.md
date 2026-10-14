# Rank, metric definitions, and platform eligibility

## Verify current requirements

This reference records official pages retrieved on **2026-09-24** and installed SDK **3.10.5** behavior.
It is not a claim about every future SDK or client.
Refresh the relevant pages for each new task.
Compare them with the installed rank assets, scanner, comparator, and validators.
Record retrieval date, SDK version, build target, inspected files, and discrepancies.

Official sources:

- [Performance ranking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)
- [Avatar size limits](https://creators.vrchat.com/avatars/avatar-size-limits/)
- [Android limitations](https://creators.vrchat.com/platforms/android/quest-content-limitations/)
- [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones/)
- [Contacts](https://creators.vrchat.com/avatars/avatar-dynamics/contacts/)
- [Constraints](https://creators.vrchat.com/common-components/constraints/)
- [Raycasts](https://creators.vrchat.com/avatars/avatar-components/raycast/)

The inspected package stores thresholds beneath `Resources/Validation/Performance/StatsLevels/Windows` and `Quest`.
Resolve the actual package path in the recipient's project.
Inspect binaries read-only when source does not establish a version-sensitive fact.
Do not execute inspected SDK methods during a read-only audit.

## All Poor maxima in the verified snapshot

Numeric maxima are inclusive. The worst graded category determines overall rank.
A value at a Poor maximum can also meet a better rank's threshold.
One passing triangle count does not establish an overall pass.

| Category | PC | Android/mobile | Installed field |
|---|---:|---:|---|
| Triangles | 70,000 | 20,000 | `polyCount` |
| Bounds, full size in metres | 5 × 6 × 5 | 5 × 6 × 5 | `aabb` |
| Texture memory, MiB estimate | 150 | 40 | `textureMegabytes` |
| Skinned meshes | 16 | 2 | `skinnedMeshCount` |
| Basic meshes | 24 | 2 | `meshCount` |
| Material slots | 32 | 4 | `materialCount` |
| PhysBone components | 32 | 8 | `physBone.componentCount` |
| PhysBone affected transforms | 256 | 64 | `physBone.transformCount` |
| PhysBone colliders | 32 | 16 | `physBone.colliderCount` |
| PhysBone collision checks | 512 | 64 | `physBone.collisionCheckCount` |
| Ranked contacts | 32 | 16 | `contactCount` |
| Constraint count | 350 | 150 | `constraintsCount` |
| Constraint dependency depth | 100 | 50 | `constraintDepth` |
| Animators | 32 | 2 | `animatorCount` |
| Bones | 400 | 150 | `boneCount` |
| Lights | 1 | Unsupported | `lightCount` |
| Particle systems | 16 | 2 | `particleSystemCount` |
| Maximum active particles | 2,500 | 200 | `particleTotalCount` |
| Mesh-particle triangles | 5,000 | 400 | `particleMaxMeshPolyCount` |
| Particle trails enabled | True allowed | True allowed | `particleTrailsEnabled` |
| Particle collision enabled | True allowed | True allowed | `particleCollisionEnabled` |
| Trail renderers | 8 | 1 | `trailRendererCount` |
| Line renderers | 8 | 1 | `lineRendererCount` |
| Raycasts | 15 | 8 | `raycastCount` |
| Cloth components | 1 | Unsupported | `clothCount` |
| Total Cloth vertices | 200 | Unsupported | `clothMaxVertices` |
| Physics colliders | 8 | Unsupported | `physicsColliderCount` |
| Physics rigidbodies | 8 | Unsupported | `physicsRigidbodyCount` |
| Audio sources | 8 | Unsupported | `audioSourceCount` |

The official mobile table omits six unsupported categories. The inspected Quest asset stores zero for those fields.
Do not interpret those zeros as permission to retain unsupported functionality.

## Definitions and boundary comparisons

- The official texture label says MB. SDK 3.10.5 divides estimated bytes by 1,048,576, which means MiB.
- Preserve exact bytes when a user imposes a decimal MB ceiling. Do not silently treat MB and MiB as identical.
- Numeric comparison delegates use `observed - threshold`. A positive result advances to a worse rank.
- Bounds assets store half-size extents `(2.5, 3, 2.5)`, not full size `(5, 6, 5)`.
- Each bounds axis must pass. The inspected comparator accepts a negative difference or `Mathf.Approximately(difference, 0)`.
- Use the SDK bounds result near boundaries. Do not invent an independent epsilon or compare full size with extents.
- Inactive objects and disabled components still count. EditorOnly filtering depends on processing context.
- Mesh slots use `sharedMesh.subMeshCount`, not unique materials or only `sharedMaterials.Length`.
- Particle, trail, and line scanners can contribute additional material slots.
- Bone count includes unique non-null bones referenced by scanned skinned renderers. Hierarchy-transform count is not a substitute.
  Shared references after [Merge Armature](optimization-tools.md#modular-avatar-merge-armature) can reduce this count without shortening bone arrays.
  In SDK 3.10.5, this count does not inspect vertex weights or add `rootBone` and ancestors independently.
  Compare array entries and positive-weight influences separately when explaining a discrepancy.
- Texture scanning deduplicates referenced texture objects. The inspected scanner includes Texture2D mips and excludes RenderTextures.
- Texture memory is an SDK estimate, not total resident VRAM, frame time, or source-file size.
- Particle totals use configured `maxParticles`, not the number visible in a quiet frame.
- Cloth vertices sum coefficient-array lengths. The field name does not mean a per-component maximum.
- PhysBone affected transforms come from initialized PhysBone chains, including the scanner's overlap and endpoint rules.
- PhysBone colliders use the union of referenced and global colliders in the inspected SDK.
- Collision checks depend on child counts, multi-child mode, endpoints, and collider entries. Avoid a universal multiplication formula.
- Constraints need refreshed dependency groups before SDK measurement. Depth is the longest chain, not a sum of independent chains.
- Local Only Contacts do not count toward rank in the inspected SDK. They still count toward the total-contact hard cap.

Keep unknown values unknown. Missing size or category data is not zero.
Compare unrounded values and retain the SDK category ratings.
Document processing differences instead of editing raw reports to agree.
The inspected SDK 3.10.5 texture scan uses currently assigned renderer materials, not the complete union of animated alternatives.
Use [full texture measurement](full-texture-measurement.md) for complete-budget claims and [Debug and troubleshoot notes](debug-and-troubleshoot-notes.md) for versioned discrepancies.
Keep nominal format payload, SDK estimates, server/client statistics, and residency distinct.
Likewise, SDK submesh-based material statistics do not establish renderer-array entries or measured draw calls.

## Separate bundle limits

These inspected byte maxima are inclusive:

| Platform | Compressed bundle | Uncompressed packed data |
|---|---:|---:|
| PC | 209,715,200 | 524,288,000 |
| Android | 10,485,760 | 41,943,040 |

Official labels are 200/500 MB and 10/40 MB respectively.
Uncompressed packed data does not mean fully decoded texture memory.
Use the returned bundle and fresh report from the same completed Build.
Build & Test does not establish bundle-size eligibility.
See [safe Build](safe-build.md) before measuring sizes.

## Additional hard limits

The 2026-09-24 sources and SDK inspection establish these separate constraints:

| Limit | Maximum and evidence |
|---|---|
| Transforms in one PhysBone | 256, official PhysBones page |
| Global PhysBone colliders | 4, official page and SDK |
| All Contacts, including Local Only | 256, official page and SDK |
| Combined VRCRaycast and FinalIK components | 80, official Raycast page and SDK |
| PhysBone components | 256, installed SDK validation |
| Used PhysBone colliders | 256, installed SDK validation |
| Constraints | 2,000, installed SDK validation |

Contacts also have scaled shape limits: 3 m radius and 6 m width/height/depth.
Only the first 16 contact tags apply.
PhysBone interaction bounds are limited to 10 × 10 × 10 m.
These restrictions are not extra rank categories.
Complete SDK validation must also check rig, parameters, materials, textures, and other supported-avatar requirements.

Mesh Read/Write is required. An unreadable mesh can cause Very Poor and block upload.
Do not disable it as an optimization.
The inspected SDK also rejects texture importer sizes above 8,192.
Recheck these version-sensitive requirements before relying on them.

## Android compatibility and filtering

Android requires permitted shaders supplied by the SDK.
A shader name with a `VRChat/Mobile` prefix does not alone prove eligibility.
PC lilToon appearance does not transfer unchanged to Android.
The SDK accepts Toon Standard (Outline), but the mobile client uses its non-outline variant.
Do not promise a mobile outline.

Android avatar restrictions include Dynamic Bones, Cloth, Cameras, Lights, post-processing, AudioSources, rigidbodies, physics colliders, joints, and custom FinalIK.
Inspect the current whitelist and official page before choosing replacements.
Particle systems have additional limits.
World component permissions do not establish avatar permissions.

If any mobile dynamics cap exceeds its maximum, VRChat removes all PhysBones, Contacts, and VRChat Constraints together.
Those caps are the seven mobile PhysBone, Contact, and constraint thresholds in the table.
Show Avatar does not override that removal.

Performance filtering is separate from rank and upload validation.
Current documentation gives PC a default display threshold of Very Poor and mobile a default threshold of Medium.
Users can select stricter thresholds. Bounds alone does not cause performance blocking.
Do not promise universal visibility merely because the avatar meets Poor.

## Documented discrepancies

The performance page mentions Local Only receivers, while the newer Contacts page exempts senders and receivers.
The inspected SDK checks the common `localOnly` field and separately counts all Contacts.

The Android page disables Unity constraints, while the Constraints page describes automatic conversion to VRChat constraints.
The inspected whitelist places Unity constraints under `UNITY_STANDALONE`.
Use and validate VRChat Constraints directly for Android.
Flag this discrepancy instead of promising automatic conversion.

The official collider wording describes scripts, while the inspected scanner counts referenced and global colliders.
The final rank claim must use the SDK statistic.

## Reproduce the requirement check

Use the public sources above and the recipient's installed SDK.
Record current page retrieval dates, package versions, relevant source or assembly hashes, and observed discrepancies.
Inspect platform rank assets and the corresponding scanner and comparator.
Record the exact source of each limit or implementation claim in the task's own evidence.
Do not treat this dated reference as proof of a later installation's behavior.
