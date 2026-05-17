# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Razumova2000_MyofilamentContractileBehaviour."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Razumova2000MyofilamentcontractilebehaviourModel7909395757Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Razumova2000_MyofilamentContractileBehaviour."""

    _SBML_ID = 'MODEL7909395757'
    _TITLE = 'Razumova2000_MyofilamentContractileBehaviour'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['D', 'A_1', 'A_2']
    _SPECIES_LABELS = {'D': 'D', 'A_1': 'A 1', 'A_2': 'A 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_a_2': ('A_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_2`.'), 'initial_model_state_a_1': ('A_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_1`.'), 'initial_model_state_d': ('D', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'a_2': ('A_2', 'native SBML value', 'A 2. Maps to SBML symbol `A_2`.'), 'a_1': ('A_1', 'native SBML value', 'A 1. Maps to SBML symbol `A_1`.'), 'model_state_d': ('D', 'native SBML value', 'D. Maps to SBML symbol `D`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL7909395757.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
