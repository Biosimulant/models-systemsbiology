# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DePaor1986_CirculatoryAutoregulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depaor1986CirculatoryautoregulationModel1172940336Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DePaor1986_CirculatoryAutoregulation."""

    _SBML_ID = 'MODEL1172940336'
    _TITLE = 'DePaor1986_CirculatoryAutoregulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['r', 'x1', 'x2', 'x3', 'h']
    _SPECIES_LABELS = {'r': 'R', 'x1': 'X1', 'x2': 'X2', 'x3': 'X3', 'h': 'H'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x3': ('x3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_model_state_x2': ('x2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2`.'), 'initial_model_state_x1': ('x1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_model_state_r': ('r', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r`.'), 'initial_model_state_h': ('h', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h`.')}
    _HEADLINE_OUTPUTS = {'model_state_x3': ('x3', 'native SBML value', 'X3. Maps to SBML symbol `x3`.'), 'model_state_x2': ('x2', 'native SBML value', 'X2. Maps to SBML symbol `x2`.'), 'model_state_x1': ('x1', 'native SBML value', 'X1. Maps to SBML symbol `x1`.'), 'model_state_r': ('r', 'native SBML value', 'R. Maps to SBML symbol `r`.'), 'model_state_h': ('h', 'native SBML value', 'H. Maps to SBML symbol `h`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1172940336.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
