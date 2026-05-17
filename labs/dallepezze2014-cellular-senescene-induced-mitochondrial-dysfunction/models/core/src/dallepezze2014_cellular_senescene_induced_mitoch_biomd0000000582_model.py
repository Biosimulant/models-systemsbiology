# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DallePezze2014 - Cellular senescene-induced mitochondrial dysfunction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dallepezze2014CellularSenesceneInducedMitochBiomd0000000582Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DallePezze2014 - Cellular senescene-induced mitochondrial dysfunction."""

    _SBML_ID = 'BIOMD0000000582'
    _TITLE = 'DallePezze2014 - Cellular senescene-induced mitochondrial dysfunction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Akt', 'Akt_pS473', 'AMPK', 'AMPK_pT172', 'mTORC1', 'mTORC1_pS2448', 'Mitophagy', 'FoxO3a', 'FoxO3a_pS253', 'CDKN1A', 'CDKN1B', 'JNK', 'JNK_pT183', 'ROS', 'DNA_damage', 'SA_beta_gal', 'IKKbeta', 'Mito_mass_new', 'Mito_mass_old', 'Mito_mass_turnover', 'Mito_membr_pot_new', 'Mito_membr_pot_old', 'Nil', 'Insulin', 'Amino_Acids', 'Irradiation', 'DNA_damage_gammaH2AX_obs', 'Akt_pS473_obs', 'mTOR_pS2448_obs', 'AMPK_pT172_obs', 'CDKN1A_obs', 'CDKN1B_obs', 'FoxO3a_pS253_obs', 'FoxO3a_total_obs', 'Mito_Mass_obs', 'Mito_Membr_Pot_obs', 'Mitophagy_obs', 'ROS_obs', 'JNK_pT183_obs', 'SA_beta_gal_obs']
    _SPECIES_LABELS = {'Akt': 'Akt', 'Akt_pS473': 'Akt_pS473', 'AMPK': 'AMPK', 'AMPK_pT172': 'AMPK_pT172', 'mTORC1': 'mTORC1', 'mTORC1_pS2448': 'mTORC1_pS2448', 'Mitophagy': 'Mitophagy', 'FoxO3a': 'FoxO3a', 'FoxO3a_pS253': 'FoxO3a_pS253', 'CDKN1A': 'CDKN1A', 'CDKN1B': 'CDKN1B', 'JNK': 'JNK', 'JNK_pT183': 'JNK_pT183', 'ROS': 'ROS', 'DNA_damage': 'DNA_damage', 'SA_beta_gal': 'SA_beta_gal', 'IKKbeta': 'IKKbeta', 'Mito_mass_new': 'Mito_mass_new', 'Mito_mass_old': 'Mito_mass_old', 'Mito_mass_turnover': 'Mito_mass_turnover', 'Mito_membr_pot_new': 'Mito_membr_pot_new', 'Mito_membr_pot_old': 'Mito_membr_pot_old', 'Nil': 'Nil', 'Insulin': 'Insulin', 'Amino_Acids': 'Amino_Acids', 'Irradiation': 'Irradiation', 'DNA_damage_gammaH2AX_obs': 'DNA_damage_gammaH2AX_obs', 'Akt_pS473_obs': 'Akt_pS473_obs', 'mTOR_pS2448_obs': 'mTOR_pS2448_obs', 'AMPK_pT172_obs': 'AMPK_pT172_obs', 'CDKN1A_obs': 'CDKN1A_obs', 'CDKN1B_obs': 'CDKN1B_obs', 'FoxO3a_pS253_obs': 'FoxO3a_pS253_obs', 'FoxO3a_total_obs': 'FoxO3a_total_obs', 'Mito_Mass_obs': 'Mito_Mass_obs', 'Mito_Membr_Pot_obs': 'Mito_Membr_Pot_obs', 'Mitophagy_obs': 'Mitophagy_obs', 'ROS_obs': 'ROS_obs', 'JNK_pT183_obs': 'JNK_pT183_obs', 'SA_beta_gal_obs': 'SA_beta_gal_obs'}
    _PARAMETER_INPUTS = {'akt_s473_phos_by_insulin': ('Akt_S473_phos_by_insulin', 0.588783148144923, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Akt_S473_phos_by_insulin`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'m_tor_p_s2448_obs': ('mTOR_pS2448_obs', 'native SBML value', 'mTOR_pS2448_obs. Maps to SBML symbol `mTOR_pS2448_obs`.'), 'm_torc1_p_s2448': ('mTORC1_pS2448', 'native SBML value', 'mTORC1_pS2448. Maps to SBML symbol `mTORC1_pS2448`.'), 'm_torc1': ('mTORC1', 'native SBML value', 'mTORC1. Maps to SBML symbol `mTORC1`.'), 'mito_mass_turnover': ('Mito_mass_turnover', 'native SBML value', 'Mito_mass_turnover. Maps to SBML symbol `Mito_mass_turnover`.'), 'fox_o3a_total_obs': ('FoxO3a_total_obs', 'native SBML value', 'FoxO3a_total_obs. Maps to SBML symbol `FoxO3a_total_obs`.'), 'mito_membr_pot_new': ('Mito_membr_pot_new', 'native SBML value', 'Mito_membr_pot_new. Maps to SBML symbol `Mito_membr_pot_new`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000582.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
