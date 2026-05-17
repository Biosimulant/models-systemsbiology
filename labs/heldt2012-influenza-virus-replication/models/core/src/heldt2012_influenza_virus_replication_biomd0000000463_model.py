# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Heldt2012 - Influenza Virus Replication."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heldt2012InfluenzaVirusReplicationBiomd0000000463Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Heldt2012 - Influenza Virus Replication."""

    _SBML_ID = 'BIOMD0000000463'
    _TITLE = 'Heldt2012 - Influenza Virus Replication'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33', 'species_34', 'species_35', 'species_36', 'species_37', 'species_38', 'species_39']
    _SPECIES_LABELS = {'species_1': 'Bhi', 'species_2': 'VattHi', 'species_3': 'Vex', 'species_4': 'Blo', 'species_5': 'VattLo', 'species_6': 'Ven', 'species_7': 'Vfus', 'species_8': 'VpCyt', 'species_9': 'VpNuc', 'species_10': 'Rc', 'species_11': 'P_Rdrp', 'species_12': 'RcRdrp', 'species_13': 'P_Np', 'species_14': 'P_M1', 'species_15': 'VpNucM1', 'species_16': 'VpCytM1', 'species_17': 'Cp', 'species_18': 'Rv', 'species_19': 'RvRdrp', 'species_20': 'Rm1', 'species_21': 'Rm2', 'species_22': 'Rm3', 'species_23': 'Rm4', 'species_24': 'Rm5', 'species_25': 'Rm6', 'species_26': 'Rm7', 'species_27': 'Rm8', 'species_28': 'P_Pb1', 'species_29': 'P_Pb2', 'species_30': 'P_Pa', 'species_31': 'P_Nep', 'species_32': 'P_Ha', 'species_33': 'P_Na', 'species_34': 'P_M2', 'species_35': 'Vrel', 'species_36': 'total cRNA', 'species_37': 'total cRNA of a segment', 'species_38': 'total vRNA', 'species_39': 'total vRNA of a segment'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_total_v_rna_of_a_segment': ('species_39', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_39`.'), 'initial_total_v_rna': ('species_38', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_38`.'), 'initial_total_c_rna_of_a_segment': ('species_37', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_37`.'), 'initial_total_c_rna': ('species_36', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_36`.'), 'initial_model_state_blo': ('species_4', 1000.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_model_state_bhi': ('species_1', 150.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.')}
    _HEADLINE_OUTPUTS = {'total_v_rna_of_a_segment': ('species_39', 'mole', 'total vRNA of a segment. Maps to SBML symbol `species_39`.'), 'total_v_rna': ('species_38', 'mole', 'total vRNA. Maps to SBML symbol `species_38`.'), 'total_c_rna_of_a_segment': ('species_37', 'mole', 'total cRNA of a segment. Maps to SBML symbol `species_37`.'), 'total_c_rna': ('species_36', 'mole', 'total cRNA. Maps to SBML symbol `species_36`.'), 'blo': ('species_4', 'mole', 'Blo. Maps to SBML symbol `species_4`.'), 'bhi': ('species_1', 'mole', 'Bhi. Maps to SBML symbol `species_1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000463.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
