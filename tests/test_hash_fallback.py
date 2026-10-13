"""Regression tests for SHA-256 fallback on non-JSON-serializable values."""

import hashlib

from agent_eval import AgentEval


def test_non_serializable_input_fallback_hash():
    payload = {3, 1, 2}
    expected = hashlib.sha256(str(payload).encode()).hexdigest()[:16]
    assert AgentEval._hash(payload) == expected
    assert len(AgentEval._hash(payload)) == 16


def test_none_is_empty_hash():
    assert AgentEval._hash(None) == ""
