# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bertram1995_PancreaticBetaCell_CRAC."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram1995PancreaticbetacellCracBiomd0000000374Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bertram1995_PancreaticBetaCell_CRAC."""

    _SBML_ID = 'BIOMD0000000374'
    _TITLE = 'Bertram1995_PancreaticBetaCell_CRAC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V_membrane', 'n', 'jm', 'Ca_er_Ca_equations', 'Ca_i']
    _SPECIES_LABELS = {'V_membrane': 'V_membrane', 'n': 'n', 'jm': 'jm', 'Ca_er_Ca_equations': 'ca_er_ca_equations', 'Ca_i': 'Ca_i'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', -61.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_ca_er_ca_equations': ('Ca_er_Ca_equations', 9.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_er_Ca_equations`.'), 'initial_model_state_jm': ('jm', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `jm`.'), 'initial_ca_i': ('Ca_i', 0.11, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_i`.'), 'initial_model_state_n': ('n', 0.0005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V_membrane. Maps to SBML symbol `V_membrane`.'), 'ca_er_ca_equations': ('Ca_er_Ca_equations', 'native SBML value', 'ca_er_ca_equations. Maps to SBML symbol `Ca_er_Ca_equations`.'), 'model_state_jm': ('jm', 'native SBML value', 'jm. Maps to SBML symbol `jm`.'), 'ca_i': ('Ca_i', 'native SBML value', 'Ca_i. Maps to SBML symbol `Ca_i`.'), 'model_state_n': ('n', 'native SBML value', 'n. Maps to SBML symbol `n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000374.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
