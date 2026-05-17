# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Phillips2008_AscendingArousalSystem_Baseline."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Phillips2008AscendingarousalsystemBaselineModel1006230110Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Phillips2008_AscendingArousalSystem_Baseline."""

    _SBML_ID = 'MODEL1006230110'
    _TITLE = 'Phillips2008_AscendingArousalSystem_Baseline'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Vv', 'Vm', 'H']
    _SPECIES_LABELS = {'Vv': 'Vv', 'Vm': 'Vm', 'H': 'H'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_vv': ('Vv', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vv`.'), 'initial_model_state_vm': ('Vm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm`.'), 'initial_model_state_h': ('H', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`.')}
    _HEADLINE_OUTPUTS = {'model_state_vv': ('Vv', 'native SBML value', 'Vv. Maps to SBML symbol `Vv`.'), 'model_state_vm': ('Vm', 'native SBML value', 'Vm. Maps to SBML symbol `Vm`.'), 'model_state_h': ('H', 'native SBML value', 'H. Maps to SBML symbol `H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230110.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
