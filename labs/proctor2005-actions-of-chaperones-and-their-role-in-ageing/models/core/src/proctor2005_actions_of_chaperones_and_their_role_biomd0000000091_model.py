# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2005 - Actions of chaperones and their role in ageing."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2005ActionsOfChaperonesAndTheirRoleBiomd0000000091Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2005 - Actions of chaperones and their role in ageing."""

    _SBML_ID = 'BIOMD0000000091'
    _TITLE = 'Proctor2005 - Actions of chaperones and their role in ageing'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Hsp90', 'HCom', 'HSF1', 'MisP', 'MCom', 'TriH', 'DiH', 'NatP', 'AggP', 'HSE', 'HSETriH', 'X', 'ROS', 'ATP', 'ADP', 'source']
    _SPECIES_LABELS = {'Hsp90': 'Hsp90', 'HCom': 'HCom', 'HSF1': 'HSF1', 'MisP': 'MisP', 'MCom': 'MCom', 'TriH': 'TriH', 'DiH': 'DiH', 'NatP': 'NatP', 'AggP': 'AggP', 'HSE': 'HSE', 'HSETriH': 'HSETriH', 'X': 'X', 'ROS': 'ROS', 'ATP': 'ATP', 'ADP': 'ADP', 'source': 'source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nat_p': ('NatP', 6000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NatP`.'), 'initial_model_state_atp': ('ATP', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_source': ('source', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `source`.'), 'initial_hsp90': ('Hsp90', 300000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Hsp90`.'), 'initial_h_com': ('HCom', 5900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HCom`.')}
    _HEADLINE_OUTPUTS = {'nat_p': ('NatP', 'native SBML value', 'NatP. Maps to SBML symbol `NatP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'source': ('source', 'native SBML value', 'source. Maps to SBML symbol `source`.'), 'hsp90': ('Hsp90', 'native SBML value', 'Hsp90. Maps to SBML symbol `Hsp90`.'), 'h_com': ('HCom', 'native SBML value', 'HCom. Maps to SBML symbol `HCom`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000091.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
