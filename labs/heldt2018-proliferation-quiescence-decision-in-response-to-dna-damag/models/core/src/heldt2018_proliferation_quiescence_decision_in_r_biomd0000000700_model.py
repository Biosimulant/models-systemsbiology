# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Heldt2018 - Proliferation-quiescence decision in response to DNA damage."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heldt2018ProliferationQuiescenceDecisionInRBiomd0000000700Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Heldt2018 - Proliferation-quiescence decision in response to DNA damage."""

    _SBML_ID = 'BIOMD0000000700'
    _TITLE = 'Heldt2018 - Proliferation-quiescence decision in response to DNA damage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Rb', 'pRb', 'E2f', 'RbE2f', 'E1', 'C1', 'pC1', 'E1C1', 'P21', 'Ce', 'Ca', 'CeP21', 'CaP21', 'aPcna', 'iPcna', 'Rc', 'pRc', 'aRc', 'iRc', 'Dna', 'P53', 'Dam', 'Pr', 'tRb', 'tE2f', 'tE1', 'tC1', 'tCe', 'tCa', 'tP21']
    _SPECIES_LABELS = {'Rb': 'Retinoblastoma_protein', 'pRb': 'Retinoblastoma_protein_hyperphosphorylated', 'E2f': 'E2f_active', 'RbE2f': 'Retinoblastoma_protein_E2f_complex_inactive', 'E1': 'Emi1', 'C1': 'Cdh1_C_APC_active', 'pC1': 'C_Cdh1_APC_phosphorylated_inactive', 'E1C1': 'Emi1_C_Cdh1_complex_inactive', 'P21': 'P21', 'Ce': 'CyclinE_Cdk2_active', 'Ca': 'CyclinA_Cdk2', 'CeP21': 'CyclinE_Cdk2_P21_complex_inactive', 'CaP21': 'CyclinA_Cdk2_P21_complex_inactive', 'aPcna': 'Pcna_nuclear_active', 'iPcna': 'PCNA_Nuclear_inactive', 'Rc': 'Pre_Replication_complex', 'pRc': 'Pre_Replication_complex_primed', 'aRc': 'Pre_Replication_complex_active', 'iRc': 'Pre_Replication_complex_inactive', 'Dna': 'Dna', 'P53': 'P53', 'Dam': 'Dna_damage', 'Pr': 'Activity_probe_of_APC_C_Cdh1', 'tRb': 'Retinoblastoma_protein_total', 'tE2f': 'E2f_total', 'tE1': 'Emi1_total', 'tC1': 'C_Cdh1_APC_total', 'tCe': 'CyclinE_Cdk2_total', 'tCa': 'CyclinA_Cdk2_total', 'tP21': 'P21_total'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cyclin_a_cdk2_total': ('tCa', 1.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tCa`.'), 'initial_retinoblastoma_protein_total': ('tRb', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tRb`.'), 'initial_retinoblastoma_protein_hyperphosphorylated': ('pRb', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pRb`.'), 'initial_cyclin_a_cdk2': ('Ca', 1.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca`.'), 'initial_cyclin_e_cdk2_total': ('tCe', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tCe`.'), 'initial_cyclin_e_cdk2_active': ('Ce', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ce`.')}
    _HEADLINE_OUTPUTS = {'cyclin_a_cdk2_total': ('tCa', 'native SBML value', 'CyclinA_Cdk2_total. Maps to SBML symbol `tCa`.'), 'retinoblastoma_protein_total': ('tRb', 'native SBML value', 'Retinoblastoma_protein_total. Maps to SBML symbol `tRb`.'), 'retinoblastoma_protein_hyperphosphorylated': ('pRb', 'native SBML value', 'Retinoblastoma_protein_hyperphosphorylated. Maps to SBML symbol `pRb`.'), 'cyclin_a_cdk2': ('Ca', 'native SBML value', 'CyclinA_Cdk2. Maps to SBML symbol `Ca`.'), 'cyclin_e_cdk2_total': ('tCe', 'native SBML value', 'CyclinE_Cdk2_total. Maps to SBML symbol `tCe`.'), 'cyclin_e_cdk2_active': ('Ce', 'native SBML value', 'CyclinE_Cdk2_active. Maps to SBML symbol `Ce`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000700.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
