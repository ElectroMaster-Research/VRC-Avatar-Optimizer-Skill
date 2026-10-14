# Shared Unity connection and project identity

Apply the [core prerequisite](../SKILL.md#prerequisite-configure-and-verify-unity-mcp) before dependent Unity work.
Discover the connector's current capabilities and schemas.
Tool names, namespaces, and APIs can change between versions.

For MCP for Unity, inspect advertised resources such as these:

| Resource | Evidence |
| --- | --- |
| `mcpforunity://instances` | Connected editor identities |
| `mcpforunity://project/info` | Project path, Unity version, active platform |
| `mcpforunity://custom-tools` | Project-specific capabilities |
| `mcpforunity://editor/state` | Scene, Edit/Play state, compilation, import activity |
| `mcpforunity://editor/selection` | Current selection, not proof of the intended avatar |

Use exact advertised URIs and server keys. Do not assume every integration supplies these resources.
Pin the requested instance when multiple editors are connected.
Verify its actual project path through a read-only query before substantive work.
The chat workspace, Unity project, and external asset library can be different folders.

Inspect the installed integration's setup instructions and compatibility before configuration changes.
Do not infer Unity 2022.3 support from another integration's Unity 6 requirements.
Do not replace a working third-party connection with Unity's CLI MCP merely because both use MCP.
Read [bootstrap.md](../bootstrap.md#unity-hub-and-unity-command-line-workflows) for those interface boundaries.

Find the avatar through its live descriptor, hierarchy, prefab connection, and renderer bindings.
Do not select it from a similar filename alone.
If live access remains unavailable, label unsaved state and current assignments as unverified.
Do not install a connector or import packages merely to discover contents.
Follow the core's explicit fallback procedure instead.
