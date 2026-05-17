# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mukandavire2009 - Model for HIV-Malaria co-infection."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mukandavire2009ModelForHivMalariaCoInfectiModel1805230001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mukandavire2009 - Model for HIV-Malaria co-infection."""

    _SBML_ID = 'MODEL1805230001'
    _TITLE = 'Mukandavire2009 - Model for HIV-Malaria co-infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_H', 'E_M', 'I_M', 'I_H', 'E_H_M', 'I_H_M', 'A_H', 'E_A_M', 'A_H_M', 'S_V', 'E_V', 'I_V']
    _SPECIES_LABELS = {'S_H': 'S_H', 'E_M': 'E_M', 'I_M': 'I_M', 'I_H': 'I_H', 'E_H_M': 'E_H,M', 'I_H_M': 'I_H,M', 'A_H': 'A_H', 'E_A_M': 'E_A,M', 'A_H_M': 'A_H,M', 'S_V': 'S_V', 'E_V': 'E_V', 'I_V': 'I_V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_s_v': ('S_V', 25000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S_V`.'), 'initial_model_state_s_h': ('S_H', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S_H`.'), 'initial_model_state_e_v': ('E_V', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_V`.'), 'initial_model_state_e_m': ('E_M', 150.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_M`.'), 'initial_model_state_i_v': ('I_V', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_V`.'), 'initial_model_state_i_m': ('I_M', 25.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_M`.')}
    _HEADLINE_OUTPUTS = {'s_v': ('S_V', 'native SBML value', 'S_V. Maps to SBML symbol `S_V`.'), 's_h': ('S_H', 'native SBML value', 'S_H. Maps to SBML symbol `S_H`.'), 'e_v': ('E_V', 'native SBML value', 'E_V. Maps to SBML symbol `E_V`.'), 'e_m': ('E_M', 'native SBML value', 'E_M. Maps to SBML symbol `E_M`.'), 'i_v': ('I_V', 'native SBML value', 'I_V. Maps to SBML symbol `I_V`.'), 'i_m': ('I_M', 'native SBML value', 'I_M. Maps to SBML symbol `I_M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1805230001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
