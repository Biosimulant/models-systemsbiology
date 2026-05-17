# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for mahaney2000_SERCAregulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mahaney2000SercaregulationModel4816599063Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for mahaney2000_SERCAregulation."""

    _SBML_ID = 'MODEL4816599063'
    _TITLE = 'mahaney2000_SERCAregulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E2', 'E1', 'Ca2plus', 'Ca_E1', 'Ca_E1prime', 'Ca2_E1prime', 'ATP', 'ATP_Ca2_E1prime', 'ADP', 'EP', 'EPi', 'Pi']
    _SPECIES_LABELS = {'E2': 'E2', 'E1': 'E1', 'Ca2plus': 'Ca2plus', 'Ca_E1': 'Ca_E1', 'Ca_E1prime': 'Ca_E1prime', 'Ca2_E1prime': 'Ca2_E1prime', 'ATP': 'ATP', 'ATP_Ca2_E1prime': 'ATP_Ca2_E1prime', 'ADP': 'ADP', 'EP': 'EP', 'EPi': 'EPi', 'Pi': 'Pi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp_ca2_e1prime': ('ATP_Ca2_E1prime', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP_Ca2_E1prime`.'), 'initial_model_state_atp': ('ATP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_ca_e1prime': ('Ca_E1prime', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_E1prime`.'), 'initial_ca_e1': ('Ca_E1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_E1`.'), 'initial_ca2_e1prime': ('Ca2_E1prime', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca2_E1prime`.')}
    _HEADLINE_OUTPUTS = {'atp_ca2_e1prime': ('ATP_Ca2_E1prime', 'native SBML value', 'ATP_Ca2_E1prime. Maps to SBML symbol `ATP_Ca2_E1prime`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'ca_e1prime': ('Ca_E1prime', 'native SBML value', 'Ca_E1prime. Maps to SBML symbol `Ca_E1prime`.'), 'ca_e1': ('Ca_E1', 'native SBML value', 'Ca_E1. Maps to SBML symbol `Ca_E1`.'), 'ca2_e1prime': ('Ca2_E1prime', 'native SBML value', 'Ca2_E1prime. Maps to SBML symbol `Ca2_E1prime`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL4816599063.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
