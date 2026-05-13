from unittest.mock import MagicMock, patch
from core.natural_language_processing.llm_adapters import UnifiedLLMAdapter, create_llm_adapter

def test_unified_adapter_create_llm():
    with patch('core.natural_language_processing.llm_adapters.LLMClient') as mock_client:
        mock_llm = MagicMock()
        mock_client.return_value.get_langchain_model.return_value = mock_llm

        adapter = UnifiedLLMAdapter(provider="openai", model_name="gpt-4", temperature=0.5)
        llm = adapter.create_llm()

        mock_client.assert_called_once_with(
            provider="openai",
            model="gpt-4",
            temperature=0.5
        )
        assert llm == mock_llm

def test_create_llm_adapter_factory():
    adapter = create_llm_adapter(provider="google", model_name="gemini-pro")
    assert isinstance(adapter, UnifiedLLMAdapter)
    assert adapter._provider == "google"
    assert adapter.model_name == "gemini-pro"
