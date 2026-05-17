# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Baldwin1994 - Nondimensionalized Model of Thrombin Production."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Baldwin1994NondimensionalizedModelOfThrombinModel1806010001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Baldwin1994 - Nondimensionalized Model of Thrombin Production."""

    _SBML_ID = 'MODEL1806010001'
    _TITLE = 'Baldwin1994 - Nondimensionalized Model of Thrombin Production'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
    _SPECIES_LABELS = {'x1': 'x1', 'x2': 'x2', 'x3': 'x3', 'x4': 'x4', 'x5': 'x5', 'x6': 'x6', 'x7': 'x7', 'x8': 'x8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x7': ('x7', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x7`.'), 'initial_model_state_x5': ('x5', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x5`.'), 'initial_model_state_x3': ('x3', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_model_state_x1': ('x1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_model_state_x8': ('x8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x8`.'), 'initial_model_state_x6': ('x6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x6`.')}
    _HEADLINE_OUTPUTS = {'model_state_x7': ('x7', 'native SBML value', 'x7. Maps to SBML symbol `x7`.'), 'model_state_x5': ('x5', 'native SBML value', 'x5. Maps to SBML symbol `x5`.'), 'model_state_x3': ('x3', 'native SBML value', 'x3. Maps to SBML symbol `x3`.'), 'model_state_x1': ('x1', 'native SBML value', 'x1. Maps to SBML symbol `x1`.'), 'model_state_x8': ('x8', 'native SBML value', 'x8. Maps to SBML symbol `x8`.'), 'model_state_x6': ('x6', 'native SBML value', 'x6. Maps to SBML symbol `x6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806010001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
