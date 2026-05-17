# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kyrylov2005_HPAaxis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kyrylov2005HpaaxisModel0478740924Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kyrylov2005_HPAaxis."""

    _SBML_ID = 'MODEL0478740924'
    _TITLE = 'Kyrylov2005_HPAaxis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['y0', 'y1', 'y2', 'y3', 'y4']
    _SPECIES_LABELS = {'y0': 'Y0', 'y1': 'Y1', 'y2': 'Y2', 'y3': 'Y3', 'y4': 'Y4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y4': ('y4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y4`.'), 'initial_model_state_y3': ('y3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y3`.'), 'initial_model_state_y2': ('y2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y2`.'), 'initial_model_state_y1': ('y1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y1`.'), 'initial_model_state_y0': ('y0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y0`.')}
    _HEADLINE_OUTPUTS = {'model_state_y4': ('y4', 'native SBML value', 'Y4. Maps to SBML symbol `y4`.'), 'model_state_y3': ('y3', 'native SBML value', 'Y3. Maps to SBML symbol `y3`.'), 'model_state_y2': ('y2', 'native SBML value', 'Y2. Maps to SBML symbol `y2`.'), 'model_state_y1': ('y1', 'native SBML value', 'Y1. Maps to SBML symbol `y1`.'), 'model_state_y0': ('y0', 'native SBML value', 'Y0. Maps to SBML symbol `y0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0478740924.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
