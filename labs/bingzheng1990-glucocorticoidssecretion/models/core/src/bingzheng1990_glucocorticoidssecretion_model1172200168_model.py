# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bingzheng1990_GlucocorticoidsSecretion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bingzheng1990GlucocorticoidssecretionModel1172200168Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bingzheng1990_GlucocorticoidsSecretion."""

    _SBML_ID = 'MODEL1172200168'
    _TITLE = 'Bingzheng1990_GlucocorticoidsSecretion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['X1', 'X2', 'X3']
    _SPECIES_LABELS = {'X1': 'X1', 'X2': 'X2', 'X3': 'X3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x3': ('X3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X3`.'), 'initial_model_state_x2': ('X2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X2`.'), 'initial_model_state_x1': ('X1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X1`.')}
    _HEADLINE_OUTPUTS = {'model_state_x3': ('X3', 'native SBML value', 'X3. Maps to SBML symbol `X3`.'), 'model_state_x2': ('X2', 'native SBML value', 'X2. Maps to SBML symbol `X2`.'), 'model_state_x1': ('X1', 'native SBML value', 'X1. Maps to SBML symbol `X1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1172200168.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
