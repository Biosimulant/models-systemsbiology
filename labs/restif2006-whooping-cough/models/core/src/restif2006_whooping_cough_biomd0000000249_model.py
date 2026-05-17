# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Restif2006 - Whooping cough."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Restif2006WhoopingCoughBiomd0000000249Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Restif2006 - Whooping cough."""

    _SBML_ID = 'BIOMD0000000249'
    _TITLE = 'Restif2006 - Whooping cough'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'S', 'I_1', 'I_2', 'R_1', 'R_2', 'I_1p', 'I_2p', 'R_p']
    _SPECIES_LABELS = {'N': 'N', 'S': 'S', 'I_1': 'I 1', 'I_2': 'I 2', 'R_1': 'R 1', 'R_2': 'R 2', 'I_1p': 'I 1P', 'I_2p': 'I 2P', 'R_p': 'R P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_r_1': ('R_1', 0.93733, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_1`.'), 'initial_model_state_i_1': ('I_1', 0.003775, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_1`.'), 'initial_model_state_i_2': ('I_2', 1e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_2`.'), 'initial_model_state_r_p': ('R_p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_p`.'), 'initial_model_state_r_2': ('R_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_2`.'), 'initial_i_2_p': ('I_2p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_2p`.')}
    _HEADLINE_OUTPUTS = {'r_1': ('R_1', 'native SBML value', 'R 1. Maps to SBML symbol `R_1`.'), 'i_1': ('I_1', 'native SBML value', 'I 1. Maps to SBML symbol `I_1`.'), 'i_2': ('I_2', 'native SBML value', 'I 2. Maps to SBML symbol `I_2`.'), 'r_p': ('R_p', 'native SBML value', 'R P. Maps to SBML symbol `R_p`.'), 'r_2': ('R_2', 'native SBML value', 'R 2. Maps to SBML symbol `R_2`.'), 'i_2_p': ('I_2p', 'native SBML value', 'I 2P. Maps to SBML symbol `I_2p`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000249.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
