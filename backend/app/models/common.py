"""
Common Base Models and Schemas
"""

import re
from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field, model_validator


class CamelModel(BaseModel):
    """
    Base Pydantic model with bidirectional camelCase / snake_case interoperability.
    Supports attribute access and dict serialization with population by field name or alias.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )

    @model_validator(mode="before")
    @classmethod
    def _normalize_camel_input(cls, data: Any) -> Any:
        """Accept camelCase payloads for snake_case fields (dual-norm sync)."""
        if isinstance(data, dict):
            fields = set(cls.model_fields)
            for key in list(data):
                if not isinstance(key, str):
                    continue
                snake = re.sub(r"(?<!^)(?=[A-Z])", "_", key).lower()
                if snake != key and snake in fields and data.get(snake) is None:
                    data[snake] = data[key]
        return data


class HealthResponse(CamelModel):
    """Response payload for GET /api/health."""
    status: str = Field("ok", description="Health status string")
    service: str = Field("smartstudy-poc", description="Service identifier")
    version: str = Field("1.0.0", description="API semantic version")
    mode: str = Field("dual-mode", description="Diagnostic engine operation mode")
    has_api_key: bool = Field(False, description="Whether live LLM API key is detected")
    hasApiKey: Optional[bool] = Field(False, description="CamelCase alias for has_api_key")

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, data):
        if isinstance(data, dict):
            val = data.get("has_api_key") if "has_api_key" in data else data.get("hasApiKey", False)
            data["has_api_key"] = val
            data["hasApiKey"] = val
        return data

    @model_validator(mode="after")
    def sync_aliases(self) -> "HealthResponse":
        self.hasApiKey = self.has_api_key
        return self
