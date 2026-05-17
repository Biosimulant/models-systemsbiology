# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DallePezze2016 - Activation of AMPK and mTOR by amino acids (Model 2)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dallepezze2016ActivationOfAmpkAndMtorByAmModel1705030001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DallePezze2016 - Activation of AMPK and mTOR by amino acids (Model 2)."""

    _SBML_ID = 'MODEL1705030001'
    _TITLE = 'DallePezze2016 - Activation of AMPK and mTOR by amino acids (Model 2)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IR_beta', 'IR_beta_pY1146', 'IR_beta_refractory', 'IRS', 'IRS_p', 'IRS_pS636', 'AMPK', 'AMPK_pT172', 'Akt', 'Akt_pT308', 'Akt_pS473', 'Akt_pT308_pS473', 'TSC1_TSC2', 'TSC1_TSC2_pT1462', 'TSC1_TSC2_pS1387', 'mTORC1', 'mTORC1_pS2448', 'mTORC2', 'mTORC2_pS2481', 'p70_S6K', 'p70_S6K_pT389', 'PRAS40', 'PRAS40_pT246', 'PRAS40_pS183', 'PRAS40_pT246_pS183', 'PI3K_variant', 'PI3K_variant_p', 'PI3K_PDK1', 'PI3K_p_PDK1', 'Insulin', 'Amino_Acids', 'IR_beta_pY1146_obs', 'IRS_pS636_obs', 'AMPK_pT172_obs', 'Akt_pT308_obs', 'Akt_pS473_obs', 'TSC1_TSC2_pS1387_obs', 'mTOR_pS2448_obs', 'mTOR_pS2481_obs', 'p70_S6K_pT389_obs', 'PRAS40_pT246_obs', 'PRAS40_pS183_obs']
    _SPECIES_LABELS = {'IR_beta': 'IR_beta', 'IR_beta_pY1146': 'IR_beta_pY1146', 'IR_beta_refractory': 'IR_beta_refractory', 'IRS': 'IRS', 'IRS_p': 'IRS_p', 'IRS_pS636': 'IRS_pS636', 'AMPK': 'AMPK', 'AMPK_pT172': 'AMPK_pT172', 'Akt': 'Akt', 'Akt_pT308': 'Akt_pT308', 'Akt_pS473': 'Akt_pS473', 'Akt_pT308_pS473': 'Akt_pT308_pS473', 'TSC1_TSC2': 'TSC1_TSC2', 'TSC1_TSC2_pT1462': 'TSC1_TSC2_pT1462', 'TSC1_TSC2_pS1387': 'TSC1_TSC2_pS1387', 'mTORC1': 'mTORC1', 'mTORC1_pS2448': 'mTORC1_pS2448', 'mTORC2': 'mTORC2', 'mTORC2_pS2481': 'mTORC2_pS2481', 'p70_S6K': 'p70_S6K', 'p70_S6K_pT389': 'p70_S6K_pT389', 'PRAS40': 'PRAS40', 'PRAS40_pT246': 'PRAS40_pT246', 'PRAS40_pS183': 'PRAS40_pS183', 'PRAS40_pT246_pS183': 'PRAS40_pT246_pS183', 'PI3K_variant': 'PI3K_variant', 'PI3K_variant_p': 'PI3K_variant_p', 'PI3K_PDK1': 'PI3K_PDK1', 'PI3K_p_PDK1': 'PI3K_p_PDK1', 'Insulin': 'Insulin', 'Amino_Acids': 'Amino_Acids', 'IR_beta_pY1146_obs': 'IR_beta_pY1146_obs', 'IRS_pS636_obs': 'IRS_pS636_obs', 'AMPK_pT172_obs': 'AMPK_pT172_obs', 'Akt_pT308_obs': 'Akt_pT308_obs', 'Akt_pS473_obs': 'Akt_pS473_obs', 'TSC1_TSC2_pS1387_obs': 'TSC1_TSC2_pS1387_obs', 'mTOR_pS2448_obs': 'mTOR_pS2448_obs', 'mTOR_pS2481_obs': 'mTOR_pS2481_obs', 'p70_S6K_pT389_obs': 'p70_S6K_pT389_obs', 'PRAS40_pT246_obs': 'PRAS40_pT246_obs', 'PRAS40_pS183_obs': 'PRAS40_pS183_obs'}
    _PARAMETER_INPUTS = {'ir_beta_phos_by_insulin': ('IR_beta_phos_by_Insulin', 0.0203796, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `IR_beta_phos_by_Insulin`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'p70_s6_k': ('p70_S6K', 'native SBML value', 'p70_S6K. Maps to SBML symbol `p70_S6K`.'), 'm_torc2': ('mTORC2', 'native SBML value', 'mTORC2. Maps to SBML symbol `mTORC2`.'), 'm_torc1': ('mTORC1', 'native SBML value', 'mTORC1. Maps to SBML symbol `mTORC1`.'), 'tsc1_tsc2': ('TSC1_TSC2', 'native SBML value', 'TSC1_TSC2. Maps to SBML symbol `TSC1_TSC2`.'), 'pi3_k_variant': ('PI3K_variant', 'native SBML value', 'PI3K_variant. Maps to SBML symbol `PI3K_variant`.'), 'pi3_k_pdk1': ('PI3K_PDK1', 'native SBML value', 'PI3K_PDK1. Maps to SBML symbol `PI3K_PDK1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705030001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
