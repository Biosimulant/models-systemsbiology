# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nelson2000- HIV-1 general model 1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nelson2000Hiv1GeneralModel1Biomd0000000875Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nelson2000- HIV-1 general model 1."""

    _SBML_ID = 'BIOMD0000000875'
    _TITLE = 'Nelson2000- HIV-1 general model 1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'T_i', 'V_I', 'V_NI']
    _SPECIES_LABELS = {'T': 'T', 'T_i': 'T*', 'V_I': 'V_I', 'V_NI': 'V_NI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_v_i': ('V_I', 134000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_I`.'), 'initial_model_state_t': ('T_i', 1675.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_i`.'), 'initial_v_ni': ('V_NI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_NI`.'), 'initial_model_state_t_2': ('T', 180000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'v_i': ('V_I', 'native SBML value', 'V_I. Maps to SBML symbol `V_I`.'), 'model_state_t': ('T_i', 'native SBML value', 'T*. Maps to SBML symbol `T_i`.'), 'v_ni': ('V_NI', 'native SBML value', 'V_NI. Maps to SBML symbol `V_NI`.'), 'model_state_t_2': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000875.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
