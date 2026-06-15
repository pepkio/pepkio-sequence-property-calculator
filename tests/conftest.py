"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "tool_id": "sequence-property-calculator",
        "title": "Sequence Property Calculator",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "mixed_fasta",
                "input": {
                    "mode": "sequence",
                    "fasta_text": (
                        ">dna_oligo\nATCGATCGATCGATCG\n"
                        ">insulin_b\nFVNQHLCGSHLVEALYLVCGERGFFYTPKT\n"
                    ),
                    "mass_type": "average",
                    "topology": "linear",
                },
            },
            {
                "name": "ligation_1to3",
                "input": {
                    "mode": "ligation",
                    "vector_length_bp": 5000,
                    "insert_length_bp": 1500,
                    "vector_mass_ng": 50,
                    "molar_ratio": 3,
                },
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_test123",
        "status": "completed",
        "result": {
            "mode": "sequence",
            "valid_count": 2,
            "rows": [
                {"name": "dna_oligo", "mw_da": 5000.0},
                {"name": "insulin_b", "mw_da": 3429.92},
            ],
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_test123",
        "permalink": "https://tools.pepkio.com/r/run_test123",
    }
