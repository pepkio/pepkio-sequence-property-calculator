"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_sequence_property_calculator.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "sequence-property-calculator"
    names = live_client.list_examples()
    assert "mixed_fasta" in names


def test_run_mixed_fasta(live_client: PepkioClient):
    inp = live_client.get_example_input("mixed_fasta")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("mode") == "sequence"
    assert result.result.get("valid_count", 0) >= 2
    rows = result.result.get("rows")
    assert isinstance(rows, list)
    assert result.error is None


def test_run_protein_insulin_b(live_client: PepkioClient):
    inp = live_client.get_example_input("protein_insulin_b")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("valid_count") == 1
    rows = result.result.get("rows")
    assert isinstance(rows, list)
    assert len(rows) >= 1
    assert rows[0].get("mw_da") == pytest.approx(3429.92, abs=1.0)
    assert result.error is None


def test_run_dilution_simple(live_client: PepkioClient):
    inp = live_client.get_example_input("dilution_simple")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("mode") == "dilution"
    protocol_steps = result.result.get("protocol_steps")
    assert isinstance(protocol_steps, list)
    assert len(protocol_steps) > 0
    assert result.error is None


def test_run_ligation_1to3(live_client: PepkioClient):
    inp = live_client.get_example_input("ligation_1to3")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("mode") == "ligation"
    assert result.result.get("insert_mass_ng") == pytest.approx(45, abs=1.0)
    assert result.error is None
