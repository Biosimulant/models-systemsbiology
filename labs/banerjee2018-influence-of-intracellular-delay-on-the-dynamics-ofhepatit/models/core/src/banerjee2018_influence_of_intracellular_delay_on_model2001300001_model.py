# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Banerjee2018 - Influence of Intracellular Delay on the Dynamics ofHepatitis C Virus."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Banerjee2018InfluenceOfIntracellularDelayOnModel2001300001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Banerjee2018 - Influence of Intracellular Delay on the Dynamics ofHepatitis C Virus."""

    _SBML_ID = 'MODEL2001300001'
    _TITLE = 'Banerjee2018 - Influence of Intracellular Delay on the Dynamics ofHepatitis C Virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'V_I', 'V_NI']
    _SPECIES_LABELS = {'T': 'T', 'I': 'I', 'V_I': 'V_I', 'V_NI': 'V_NI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_ni': ('V_NI', 10000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_NI`.'), 'initial_model_state_v_i': ('V_I', 10000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_I`.'), 'initial_model_state_t': ('T', 10000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_i': ('I', 10000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'v_ni': ('V_NI', 'native SBML value', 'V_NI. Maps to SBML symbol `V_NI`.'), 'v_i': ('V_I', 'native SBML value', 'V_I. Maps to SBML symbol `V_I`.'), 'model_state_t': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001300001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
