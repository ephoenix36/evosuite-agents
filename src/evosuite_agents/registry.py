"""Simple in-memory agent capability registry."""
from __future__ import annotations
from typing import Dict, List, Optional
from .capabilities.schema import CapabilityManifest


class AgentRegistry:
    def __init__(self) -> None:
        self._manifests: Dict[str, CapabilityManifest] = {}

    def register(self, manifest: CapabilityManifest) -> None:
        self._manifests[manifest.agent] = manifest

    def unregister(self, agent: str) -> None:
        self._manifests.pop(agent, None)

    def get(self, agent: str) -> Optional[CapabilityManifest]:
        return self._manifests.get(agent)

    def find_supporting(self, capability_id: str) -> List[CapabilityManifest]:
        return [m for m in self._manifests.values() if m.supports(capability_id)]

    def list(self) -> List[CapabilityManifest]:
        return list(self._manifests.values())


__all__ = ["AgentRegistry"]