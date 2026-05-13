from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from llm_client import LLMClient


class BaseLLMAdapter(ABC):
    """Abstract base class for LLM provider adapters."""

    def __init__(self, model_name: str, temperature: float = 0.1) -> None:
        self._model_name = model_name
        self._temperature = temperature

    @abstractmethod
    def create_llm(self) -> Any:
        """Return an instantiated LangChain chat model."""

    @property
    def model_name(self) -> str:
        return self._model_name

    @property
    def temperature(self) -> float:
        return self._temperature


class UnifiedLLMAdapter(BaseLLMAdapter):
    """Adapter that uses llm_client for multiple providers."""

    def __init__(
        self,
        provider: str,
        model_name: str,
        temperature: float = 0.1,
        **adapter_kwargs: Any,
    ) -> None:
        super().__init__(model_name=model_name, temperature=temperature)
        self._provider = provider
        self._adapter_kwargs = adapter_kwargs

    def create_llm(self) -> Any:
        client = LLMClient(
            provider=self._provider,
            model=self.model_name,
            temperature=self.temperature,
            **self._adapter_kwargs,
        )
        return client.get_langchain_model()


def create_llm_adapter(
    provider: str,
    model_name: str,
    temperature: float = 0.1,
    **adapter_kwargs: Any,
) -> BaseLLMAdapter:
    """Factory function that returns an adapter for the requested provider."""
    return UnifiedLLMAdapter(
        provider=provider,
        model_name=model_name,
        temperature=temperature,
        **adapter_kwargs,
    )


__all__ = [
    "BaseLLMAdapter",
    "UnifiedLLMAdapter",
    "create_llm_adapter",
]
