# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2011_ProteinHomeostasis_NormalCondition."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2011ProteinhomeostasisNormalconditionBiomd0000000344Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2011_ProteinHomeostasis_NormalCondition."""

    _SBML_ID = 'BIOMD0000000344'
    _TITLE = 'Proctor2011_ProteinHomeostasis_NormalCondition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NatP', 'MisP', 'Hsp70', 'Hsp90', 'Hsp70_dam', 'Hsp90_dam', 'Hsp90_Proteasome', 'Hsp70_Proteasome', 'Hsp70Client', 'Hsp90Client', 'Hsp70_Hsp70Client', 'Hsp90_Hsp90Client', 'Akt', 'Akt_Hsp90', 'CHIP', 'Akt_CHIP_Hsp90', 'Akt_Proteasome', 'Hsf1', 'Hsf1_Hsp90', 'Hsp90_MisP', 'Hsp70_MisP', 'Hsf1_Hsf1_Hsf1', 'Hsf1_Hsf1_Hsf1_P', 'Hsf1_Hsf1', 'HSEHsp70', 'HSEHsp90', 'HSEHsp70_Hsf1_Hsf1_Hsf1', 'HSEHsp70_Hsf1_Hsf1_Hsf1_P', 'HSEHsp90_Hsf1_Hsf1_Hsf1', 'HSEHsp90_Hsf1_Hsf1_Hsf1_P', 'Jnk', 'Jnk_P', 'Ppx', 'Mkp1', 'Mkp1_P', 'Mkp1_Proteasome', 'Hsp70_Ppx', 'Pkc', 'p38', 'p38_P', 'Proteasome', 'MisP_Proteasome', 'AggP', 'SeqAggP', 'AggP_Proteasome', 'ROS', 'ATP', 'ADP', 'p38Death', 'JNKDeath', 'PIDeath', 'CellDeath']
    _SPECIES_LABELS = {'NatP': 'NatP', 'MisP': 'MisP', 'Hsp70': 'Hsp70', 'Hsp90': 'Hsp90', 'Hsp70_dam': 'Hsp70 Dam', 'Hsp90_dam': 'Hsp90 Dam', 'Hsp90_Proteasome': 'Hsp90 Proteasome', 'Hsp70_Proteasome': 'Hsp70 Proteasome', 'Hsp70Client': 'Hsp70Client', 'Hsp90Client': 'Hsp90Client', 'Hsp70_Hsp70Client': 'Hsp70 Hsp70Client', 'Hsp90_Hsp90Client': 'Hsp90 Hsp90Client', 'Akt': 'Akt', 'Akt_Hsp90': 'Akt Hsp90', 'CHIP': 'CHIP', 'Akt_CHIP_Hsp90': 'Akt CHIP Hsp90', 'Akt_Proteasome': 'Akt Proteasome', 'Hsf1': 'Hsf1', 'Hsf1_Hsp90': 'Hsf1 Hsp90', 'Hsp90_MisP': 'Hsp90 MisP', 'Hsp70_MisP': 'Hsp70 MisP', 'Hsf1_Hsf1_Hsf1': 'Hsf1 Hsf1 Hsf1', 'Hsf1_Hsf1_Hsf1_P': 'Hsf1 Hsf1 Hsf1 P', 'Hsf1_Hsf1': 'Hsf1 Hsf1', 'HSEHsp70': 'HSEHsp70', 'HSEHsp90': 'HSEHsp90', 'HSEHsp70_Hsf1_Hsf1_Hsf1': 'HSEHsp70 Hsf1 Hsf1 Hsf1', 'HSEHsp70_Hsf1_Hsf1_Hsf1_P': 'HSEHsp70 Hsf1 Hsf1 Hsf1 P', 'HSEHsp90_Hsf1_Hsf1_Hsf1': 'HSEHsp90 Hsf1 Hsf1 Hsf1', 'HSEHsp90_Hsf1_Hsf1_Hsf1_P': 'HSEHsp90 Hsf1 Hsf1 Hsf1 P', 'Jnk': 'Jnk', 'Jnk_P': 'Jnk P', 'Ppx': 'Ppx', 'Mkp1': 'Mkp1', 'Mkp1_P': 'Mkp1 P', 'Mkp1_Proteasome': 'Mkp1 Proteasome', 'Hsp70_Ppx': 'Hsp70 Ppx', 'Pkc': 'Pkc', 'p38': 'P38', 'p38_P': 'P38 P', 'Proteasome': 'Proteasome', 'MisP_Proteasome': 'MisP Proteasome', 'AggP': 'AggP', 'SeqAggP': 'SeqAggP', 'AggP_Proteasome': 'AggP Proteasome', 'ROS': 'ROS', 'ATP': 'ATP', 'ADP': 'ADP', 'p38Death': 'P38Death', 'JNKDeath': 'JNKDeath', 'PIDeath': 'PIDeath', 'CellDeath': 'CellDeath'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nat_p': ('NatP', 17600.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NatP`.'), 'initial_model_state_atp': ('ATP', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_pi_death': ('PIDeath', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIDeath`.'), 'initial_p38_death': ('p38Death', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p38Death`.'), 'initial_jnk_death': ('JNKDeath', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `JNKDeath`.')}
    _HEADLINE_OUTPUTS = {'nat_p': ('NatP', 'native SBML value', 'NatP. Maps to SBML symbol `NatP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'pi_death': ('PIDeath', 'native SBML value', 'PIDeath. Maps to SBML symbol `PIDeath`.'), 'p38_death': ('p38Death', 'native SBML value', 'P38Death. Maps to SBML symbol `p38Death`.'), 'jnk_death': ('JNKDeath', 'native SBML value', 'JNKDeath. Maps to SBML symbol `JNKDeath`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000344.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
