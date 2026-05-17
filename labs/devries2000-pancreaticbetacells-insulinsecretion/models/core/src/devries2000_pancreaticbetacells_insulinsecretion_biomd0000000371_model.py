# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DeVries2000_PancreaticBetaCells_InsulinSecretion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Devries2000PancreaticbetacellsInsulinsecretionBiomd0000000371Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DeVries2000_PancreaticBetaCells_InsulinSecretion."""

    _SBML_ID = 'BIOMD0000000371'
    _TITLE = 'DeVries2000_PancreaticBetaCells_InsulinSecretion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V_membrane', 'n', 's']
    _SPECIES_LABELS = {'V_membrane': 'V_membrane', 'n': 'n', 's': 's'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', -65.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_model_state_n': ('n', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.'), 'initial_model_state_s': ('s', 0.025, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V_membrane. Maps to SBML symbol `V_membrane`.'), 'model_state_n': ('n', 'native SBML value', 'n. Maps to SBML symbol `n`.'), 'model_state_s': ('s', 'native SBML value', 's. Maps to SBML symbol `s`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000371.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
