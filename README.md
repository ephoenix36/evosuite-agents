# EvoSuite Agents (Planned Layer)

MCP-based multi-agent orchestration layer for the EvoSuite ecosystem.

## Status
Early scaffold. Interfaces & data contracts will stabilize via ADRs before 0.2 alignment with core.

## Goals
- Capability-based agent registration & discovery
- Task routing to appropriate agent
- Provider integration via existing `evosuite-providers`
- Extensible capability manifest schema

## Components
| Module | Purpose |
|--------|---------|
| `capabilities/schema.py` | Pydantic models for capability & manifest |
| `registry.py` | In-memory manifest registry |
| `router.py` | Simple capability-based selection |
| `examples/capability_manifest_example.json` | Sample manifest |

## Quick Start (Dev)
```bash
pip install -e .
```

```python
from evosuite_agents.capabilities.schema import Capability, CapabilityManifest
from evosuite_agents.registry import AgentRegistry
from evosuite_agents.router import AgentRouter

manifest = CapabilityManifest(
    agent="refactor_assistant",
    version="0.1.0",
    capabilities=[Capability(id="code.refactor")],
    requires_core=">=0.2,<0.3"
)

registry = AgentRegistry()
registry.register(manifest)
router = AgentRouter(registry)
selected = router.select("code.refactor")
print(selected.agent if selected else "No agent")
```

## Roadmap
- [ ] JSON Schema export utility
- [ ] Agent session orchestration
- [ ] Provider mediated tool calls
- [ ] Policy & guard-rail hooks
- [ ] Memory adapter abstraction

## Versioning
`0.1.x` experimental → align with core `0.3.0` for first stable agent interface.

---
MIT License.
