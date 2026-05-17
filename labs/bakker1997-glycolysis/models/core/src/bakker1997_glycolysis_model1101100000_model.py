# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bakker1997_Glycolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bakker1997GlycolysisModel1101100000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bakker1997_Glycolysis."""

    _SBML_ID = 'MODEL1101100000'
    _TITLE = 'Bakker1997_Glycolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23', 's24', 's25', 's26', 's27', 's28', 's29', 's30', 's31', 's32', 's33', 's39', 's44', 's45', 's46', 's47']
    _SPECIES_LABELS = {'s1': 'GLU', 's2': 'GLU6P', 's3': 'ATP', 's4': 'ADP', 's5': '2.7.1.1', 's6': 'FRU6P', 's7': '2DOGLP', 's8': '5.3.1.9', 's9': 'FRU16DP', 's10': 'CITRATE', 's11': 'cAMP', 's12': 'AMP', 's13': 'FRU26DP', 's14': '2.7.1.11', 's15': 'DHAP', 's16': 'G3P', 's17': '4.1.2.7', 's18': '5.3.1.1', 's19': '13DPG', 's20': '1.2.1.12', 's21': 'IODACTE', 's22': 'NAD', 's23': 'NAD', 's24': '3PG', 's25': '2.7.2.3', 's26': '2PG', 's27': '5.4.2.1', 's28': 'PEP', 's29': '4.2.1.11', 's30': 'H_sub_2_endsub_O', 's31': 'FLURIDE', 's32': 'PHOSPHATE', 's33': 'PYRUVATE', 's39': 's38', 's44': 'ALANIN', 's45': 'ACETYLCOA', 's46': 'Ca_super_2+_endsuper_', 's47': '2.7.1.40'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_camp': ('s11', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s11`.'), 'initial_ca_super_2_endsuper': ('s46', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s46`.'), 'initial_model_state_adp': ('s4', 1.4, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s4`.'), 'initial_model_state_4_1_2_7': ('s17', 1.23, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s17`.'), 'initial_dhap': ('s15', 0.61, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s15`.'), 'initial_model_state_pep': ('s28', 0.57, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s28`.')}
    _HEADLINE_OUTPUTS = {'camp': ('s11', 'substance', 'cAMP. Maps to SBML symbol `s11`.'), 'ca_super_2_endsuper': ('s46', 'substance', 'Ca_super_2+_endsuper_. Maps to SBML symbol `s46`.'), 'adp': ('s4', 'substance', 'ADP. Maps to SBML symbol `s4`.'), 'model_state_4_1_2_7': ('s17', 'substance', '4.1.2.7. Maps to SBML symbol `s17`.'), 'dhap': ('s15', 'substance', 'DHAP. Maps to SBML symbol `s15`.'), 'pep': ('s28', 'substance', 'PEP. Maps to SBML symbol `s28`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1101100000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
