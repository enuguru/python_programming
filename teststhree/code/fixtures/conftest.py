# fixtures/conftest.py

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_requests_get(monkeypatch):

    def patched_get(*args, **kwargs):
        raise RuntimeError("Bad! No network for you!")

    monkeypatch.setattr(requests, "get", patched_get)
