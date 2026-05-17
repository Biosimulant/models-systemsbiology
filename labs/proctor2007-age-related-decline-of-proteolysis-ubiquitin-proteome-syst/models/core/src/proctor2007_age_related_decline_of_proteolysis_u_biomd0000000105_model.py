# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2007 - Age related decline of proteolysis, ubiquitin-proteome system."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2007AgeRelatedDeclineOfProteolysisUBiomd0000000105Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2007 - Age related decline of proteolysis, ubiquitin-proteome system."""

    _SBML_ID = 'BIOMD0000000105'
    _TITLE = 'Proctor2007 - Age related decline of proteolysis, ubiquitin-proteome system'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NatP', 'MisP', 'Ub', 'E1', 'E2', 'E3', 'DUB', 'Proteasome', 'ROS', 'E1_Ub', 'E2_Ub', 'E3_MisP', 'MisP_Ub', 'MisP_Ub2', 'MisP_Ub3', 'MisP_Ub4', 'MisP_Ub5', 'MisP_Ub6', 'MisP_Ub7', 'MisP_Ub8', 'MisP_Ub4_Proteasome', 'MisP_Ub5_Proteasome', 'MisP_Ub6_Proteasome', 'MisP_Ub7_Proteasome', 'MisP_Ub8_Proteasome', 'ATP', 'ADP', 'AMP', 'Source', 'degUb4', 'degUb5', 'degUb6', 'degUb7', 'degUb8', 'totMisP', 'refNatP', 'AggP', 'SeqAggP', 'AggP_Proteasome']
    _SPECIES_LABELS = {'NatP': 'NatP', 'MisP': 'MisP', 'Ub': 'Ub', 'E1': 'E1', 'E2': 'E2', 'E3': 'E3', 'DUB': 'DUB', 'Proteasome': 'Proteasome', 'ROS': 'ROS', 'E1_Ub': 'E1 Ub', 'E2_Ub': 'E2 Ub', 'E3_MisP': 'E3 MisP', 'MisP_Ub': 'MisP Ub', 'MisP_Ub2': 'MisP UB2', 'MisP_Ub3': 'MisP UB3', 'MisP_Ub4': 'MisP UB4', 'MisP_Ub5': 'MisP UB5', 'MisP_Ub6': 'MisP UB6', 'MisP_Ub7': 'MisP UB7', 'MisP_Ub8': 'MisP UB8', 'MisP_Ub4_Proteasome': 'MisP UB4 Proteasome', 'MisP_Ub5_Proteasome': 'MisP UB5 Proteasome', 'MisP_Ub6_Proteasome': 'MisP UB6 Proteasome', 'MisP_Ub7_Proteasome': 'MisP UB7 Proteasome', 'MisP_Ub8_Proteasome': 'MisP UB8 Proteasome', 'ATP': 'ATP', 'ADP': 'ADP', 'AMP': 'AMP', 'Source': 'Source', 'degUb4': 'DegUb4', 'degUb5': 'DegUb5', 'degUb6': 'DegUb6', 'degUb7': 'DegUb7', 'degUb8': 'DegUb8', 'totMisP': 'TotMisP', 'refNatP': 'RefNatP', 'AggP': 'AggP', 'SeqAggP': 'SeqAggP', 'AggP_Proteasome': 'AggP Proteasome'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('ATP', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_amp': ('AMP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AMP`.'), 'initial_model_state_adp': ('ADP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_ub': ('Ub', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ub`.'), 'initial_nat_p': ('NatP', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NatP`.'), 'initial_model_state_dub': ('DUB', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DUB`.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'amp': ('AMP', 'native SBML value', 'AMP. Maps to SBML symbol `AMP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'model_state_ub': ('Ub', 'native SBML value', 'Ub. Maps to SBML symbol `Ub`.'), 'nat_p': ('NatP', 'native SBML value', 'NatP. Maps to SBML symbol `NatP`.'), 'dub': ('DUB', 'native SBML value', 'DUB. Maps to SBML symbol `DUB`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000105.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
