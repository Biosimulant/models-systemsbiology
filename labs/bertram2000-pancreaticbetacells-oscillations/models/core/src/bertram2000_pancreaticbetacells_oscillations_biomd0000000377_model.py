# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bertram2000_PancreaticBetaCells_Oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram2000PancreaticbetacellsOscillationsBiomd0000000377Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bertram2000_PancreaticBetaCells_Oscillations."""

    _SBML_ID = 'BIOMD0000000377'
    _TITLE = 'Bertram2000_PancreaticBetaCells_Oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'n', 's1', 's2']
    _SPECIES_LABELS = {'V': 'V', 'n': 'n', 's1': 's1', 's2': 's2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_s2': ('s2', 0.434, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s2`.'), 'initial_model_state_s1': ('s1', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_model_state_n': ('n', 0.03, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.'), 'initial_model_state_v': ('V', -43.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'model_state_s2': ('s2', 'native SBML value', 's2. Maps to SBML symbol `s2`.'), 'model_state_s1': ('s1', 'native SBML value', 's1. Maps to SBML symbol `s1`.'), 'model_state_n': ('n', 'native SBML value', 'n. Maps to SBML symbol `n`.'), 'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000377.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
