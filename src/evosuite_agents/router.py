"""Basic agent router to select an agent capable of a requested capability."""
from __future__ import annotations
from typing import Optional
from .registry import AgentRegistry
from .capabilities.schema import CapabilityManifest


class AgentRouter:
    def __init__(self, registry: AgentRegistry) -> None:
        self.registry = registry

    def select(self, capability_id: str) -> Optional[CapabilityManifest]:
        candidates = self.registry.find_supporting(capability_id)
        if not candidates:
            return None
        # Placeholder selection strategy (first match)
        return candidates[0]


__all__ = ["AgentRouter"]