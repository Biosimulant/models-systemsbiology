# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Smoke tests for systems-biology visualisation modules."""
from __future__ import annotations

from pathlib import Path
import sys

_MODEL_DIR = Path(__file__).resolve().parents[1]
if str(_MODEL_DIR) not in sys.path:
    sys.path.insert(0, str(_MODEL_DIR))

def _find_bsim_src(start: Path) -> Path | None:
    for parent in [start, *start.parents]:
        for candidate in (parent / "biosim" / "src", parent / "bsim-active" / "biosim" / "src"):
            if (candidate / "biosim").is_dir():
                return candidate
    return None

_BSIM_SRC = _find_bsim_src(_MODEL_DIR)
if _BSIM_SRC is not None and str(_BSIM_SRC) not in sys.path:
    sys.path.insert(0, str(_BSIM_SRC))

from biosim import BioModule

from src.systemsbiology_visualisation import SystemsBiologyVisualisationModel  # noqa: E402


def test_visualisation_is_biomodule() -> None:
    model = SystemsBiologyVisualisationModel(
        lab_title="test",
        question="Which source-defined system states dominate this SBML model trajectory?",
        answer_focus="Q/A table plus timeseries.",
        sources=[{"alias": "core", "title": "core", "observables": [{"id": "x", "label": "X", "group": "core_system_state"}]}],
    )
    assert isinstance(model, BioModule)
    assert "core_state" in model.inputs()
    assert model.outputs() == {}
