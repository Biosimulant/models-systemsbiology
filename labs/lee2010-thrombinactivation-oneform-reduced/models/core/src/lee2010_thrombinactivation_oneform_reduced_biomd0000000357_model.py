# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lee2010_ThrombinActivation_OneForm_reduced."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2010ThrombinactivationOneformReducedBiomd0000000357Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lee2010_ThrombinActivation_OneForm_reduced."""

    _SBML_ID = 'BIOMD0000000357'
    _TITLE = 'Lee2010_ThrombinActivation_OneForm_reduced'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'E_P_1', 'P', 'M', 'E_M', 'T', 'E_P_2', 'P2', 'E_P2']
    _SPECIES_LABELS = {'E': 'E', 'E_P_1': 'E_P_1', 'P': 'P', 'M': 'M', 'E_M': 'E_M', 'T': 'T', 'E_P_2': 'E_P_2', 'P2': 'P2', 'E_P2': 'E_P2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_e_p_2': ('E_P_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P_2`.'), 'initial_e_p_1': ('E_P_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P_1`.'), 'initial_e_p2': ('E_P2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P2`.'), 'initial_model_state_e_m': ('E_M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_M`.'), 'initial_model_state_p2': ('P2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`.'), 'initial_model_state_p': ('P', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'e_p_2': ('E_P_2', 'native SBML value', 'E_P_2. Maps to SBML symbol `E_P_2`.'), 'e_p_1': ('E_P_1', 'native SBML value', 'E_P_1. Maps to SBML symbol `E_P_1`.'), 'e_p2': ('E_P2', 'native SBML value', 'E_P2. Maps to SBML symbol `E_P2`.'), 'e_m': ('E_M', 'native SBML value', 'E_M. Maps to SBML symbol `E_M`.'), 'model_state_p2': ('P2', 'native SBML value', 'P2. Maps to SBML symbol `P2`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000357.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
