# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Xu2002 - Blood Coagulation Model of Activated Factors with Platelet Activation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Xu2002BloodCoagulationModelOfActivatedFactModel1806130001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Xu2002 - Blood Coagulation Model of Activated Factors with Platelet Activation."""

    _SBML_ID = 'MODEL1806130001'
    _TITLE = 'Xu2002 - Blood Coagulation Model of Activated Factors with Platelet Activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    _SPECIES_LABELS = {'x1': 'x1', 'x2': 'x2', 'x3': 'x3', 'x4': 'x4', 'x5': 'x5', 'x6': 'x6'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x5': ('x5', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x5`.'), 'initial_model_state_x4': ('x4', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x4`.'), 'initial_model_state_x2': ('x2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2`.'), 'initial_model_state_x6': ('x6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x6`.'), 'initial_model_state_x3': ('x3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_model_state_x1': ('x1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.')}
    _HEADLINE_OUTPUTS = {'model_state_x5': ('x5', 'native SBML value', 'x5. Maps to SBML symbol `x5`.'), 'model_state_x4': ('x4', 'native SBML value', 'x4. Maps to SBML symbol `x4`.'), 'model_state_x2': ('x2', 'native SBML value', 'x2. Maps to SBML symbol `x2`.'), 'model_state_x6': ('x6', 'native SBML value', 'x6. Maps to SBML symbol `x6`.'), 'model_state_x3': ('x3', 'native SBML value', 'x3. Maps to SBML symbol `x3`.'), 'model_state_x1': ('x1', 'native SBML value', 'x1. Maps to SBML symbol `x1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806130001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
