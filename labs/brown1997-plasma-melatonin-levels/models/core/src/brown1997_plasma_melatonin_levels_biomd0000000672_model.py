# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Brown1997 - Plasma Melatonin Levels."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Brown1997PlasmaMelatoninLevelsBiomd0000000672Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Brown1997 - Plasma Melatonin Levels."""

    _SBML_ID = 'BIOMD0000000672'
    _TITLE = 'Brown1997 - Plasma Melatonin Levels'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['H1', 'H2']
    _SPECIES_LABELS = {'H1': 'H1', 'H2': 'H2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_h2': ('H2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H2`.'), 'initial_model_state_h1': ('H1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H1`.')}
    _HEADLINE_OUTPUTS = {'model_state_h2': ('H2', 'native SBML value', 'H2. Maps to SBML symbol `H2`.'), 'model_state_h1': ('H1', 'native SBML value', 'H1. Maps to SBML symbol `H1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000672.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
