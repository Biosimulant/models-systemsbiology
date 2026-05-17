# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nelson1995_HIV1therapy_DIVadministraion_ModelA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nelson1995Hiv1therapyDivadministraionModelaModel1006230081Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nelson1995_HIV1therapy_DIVadministraion_ModelA."""

    _SBML_ID = 'MODEL1006230081'
    _TITLE = 'Nelson1995_HIV1therapy_DIVadministraion_ModelA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['T', 'T_1', 'T_2', 'T_D2', 'T_D1', 'D', 'V', 'V_']
    _SPECIES_LABELS = {'T': 'T', 'T_1': 'T 1', 'T_2': 'T 2', 'T_D2': 'T D2', 'T_D1': 'T D1', 'D': 'D', 'V': 'V', 'V_': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_v': ('V_', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_`.'), 'initial_t_d2': ('T_D2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_D2`.'), 'initial_t_d1': ('T_D1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_D1`.'), 'initial_model_state_t_2': ('T_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_2`.'), 'initial_model_state_t_1': ('T_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_1`.'), 'initial_model_state_v_2': ('V', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'model_state_v': ('V_', 'native SBML value', 'V. Maps to SBML symbol `V_`.'), 't_d2': ('T_D2', 'native SBML value', 'T D2. Maps to SBML symbol `T_D2`.'), 't_d1': ('T_D1', 'native SBML value', 'T D1. Maps to SBML symbol `T_D1`.'), 't_2': ('T_2', 'native SBML value', 'T 2. Maps to SBML symbol `T_2`.'), 't_1': ('T_1', 'native SBML value', 'T 1. Maps to SBML symbol `T_1`.'), 'model_state_v_2': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230081.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
