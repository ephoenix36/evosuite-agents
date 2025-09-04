"""Capability manifest schema & model."""
from __future__ import annotations
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class Capability(BaseModel):
    id: str = Field(..., description="Capability identifier e.g. code.refactor")
    input_schema: Optional[Dict[str, Any]] = Field(None, description="JSON Schema for input")
    output_schema: Optional[Dict[str, Any]] = Field(None, description="JSON Schema for output")


class CapabilityManifest(BaseModel):
    agent: str
    version: str
    capabilities: List[Capability]
    requires_core: str = Field(..., description="Semver range for evosuite-core")
    requires_providers: Optional[str] = Field(None, description="Semver range for evosuite-providers")
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def supports(self, capability_id: str) -> bool:
        return any(c.id == capability_id for c in self.capabilities)


__all__ = ["Capability", "CapabilityManifest"]