# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lo2016 – IBD Response to Anti-TNFα treatment."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lo2016IbdResponseToAntiTnfTreatmentModel2505090001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lo2016 – IBD Response to Anti-TNFα treatment."""

    _SBML_ID = 'MODEL2505090001'
    _TITLE = 'Lo2016 – IBD Response to Anti-TNFα treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ig_0', 'M1_0', 'I2_0', 'T1_0', 'I4_0', 'T2_0', 'M2_0', 'I21_0', 'M_0', 'I6_0', 'Ia_0', 'T17_0', 'Tr_0', 'Ib_0', 'I10_0', 'I12_0', 'M0']
    _SPECIES_LABELS = {'Ig_0': 'Ig', 'M1_0': 'M1', 'I2_0': 'I2', 'T1_0': 'T1', 'I4_0': 'I4', 'T2_0': 'T2', 'M2_0': 'M2', 'I21_0': 'I21', 'M_0': 'M', 'I6_0': 'I6', 'Ia_0': 'Ia', 'T17_0': 'T17', 'Tr_0': 'Tr', 'Ib_0': 'Ib', 'I10_0': 'I10', 'I12_0': 'I12', 'M0': 'M0'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_t17': ('T17_0', 20.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T17_0`.'), 'initial_model_state_tr': ('Tr_0', 0.0605999999999999, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tr_0`.'), 'initial_model_state_m': ('M_0', 0.0483999999999999, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_0`.'), 'initial_model_state_t1': ('T1_0', 0.0458, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1_0`.'), 'initial_model_state_m2': ('M2_0', 0.025, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M2_0`.'), 'initial_model_state_m1': ('M1_0', 0.0233999999999999, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M1_0`.')}
    _HEADLINE_OUTPUTS = {'t17': ('T17_0', 'substance', 'T17. Maps to SBML symbol `T17_0`.'), 'model_state_tr': ('Tr_0', 'substance', 'Tr. Maps to SBML symbol `Tr_0`.'), 'model_state_m': ('M_0', 'substance', 'M. Maps to SBML symbol `M_0`.'), 'model_state_t1': ('T1_0', 'substance', 'T1. Maps to SBML symbol `T1_0`.'), 'model_state_m2': ('M2_0', 'substance', 'M2. Maps to SBML symbol `M2_0`.'), 'model_state_m1': ('M1_0', 'substance', 'M1. Maps to SBML symbol `M1_0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2505090001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
