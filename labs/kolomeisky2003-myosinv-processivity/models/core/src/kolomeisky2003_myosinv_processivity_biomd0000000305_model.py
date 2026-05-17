# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kolomeisky2003_MyosinV_Processivity."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kolomeisky2003MyosinvProcessivityBiomd0000000305Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kolomeisky2003_MyosinV_Processivity."""

    _SBML_ID = 'BIOMD0000000305'
    _TITLE = 'Kolomeisky2003_MyosinV_Processivity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S0', 'ATP', 'S1', 'Pi_', 'ADP', 'fwd_step1', 'fwd_step2', 'back_step1', 'back_step2']
    _SPECIES_LABELS = {'S0': 'S0', 'ATP': 'ATP', 'S1': 'S1', 'Pi_': 'Pi', 'ADP': 'ADP', 'fwd_step1': 'Fwd Step1', 'fwd_step2': 'Fwd Step2', 'back_step1': 'Back Step1', 'back_step2': 'Back Step2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('ATP', 20.0, 'umole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 0.0, 'umole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_s0': ('S0', 10.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S0`.'), 'initial_model_state_s1': ('S1', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S1`.'), 'initial_model_state_pi': ('Pi_', 0.0, 'umole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi_`.'), 'initial_fwd_step2': ('fwd_step2', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fwd_step2`.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'umole', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'umole', 'ADP. Maps to SBML symbol `ADP`.'), 'model_state_s0': ('S0', 'substance', 'S0. Maps to SBML symbol `S0`.'), 'model_state_s1': ('S1', 'substance', 'S1. Maps to SBML symbol `S1`.'), 'model_state_pi': ('Pi_', 'umole', 'Pi. Maps to SBML symbol `Pi_`.'), 'fwd_step2': ('fwd_step2', 'substance', 'Fwd Step2. Maps to SBML symbol `fwd_step2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000305.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
