# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wajima2009_BloodCoagulation_warfarin_heparin."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wajima2009BloodcoagulationWarfarinHeparinBiomd0000000340Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wajima2009_BloodCoagulation_warfarin_heparin."""

    _SBML_ID = 'BIOMD0000000340'
    _TITLE = 'Wajima2009_BloodCoagulation_warfarin_heparin'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IIa', 'VIII', 'VIIIa', 'APC_PS', 'IX', 'IXa', 'XIa', 'XI', 'XIIa', 'VII', 'VIIa', 'X', 'Xa', 'IXa_VIIIa', 'V', 'Va', 'II', 'F', 'Fg', 'DP', 'P', 'XF', 'XIII', 'Pg', 'APC', 'IIa_Tmod', 'PC', 'Tmod', 'TF', 'VIIa_TF', 'VII_TF', 'Xa_TFPI', 'TFPI', 'PS', 'VKH2', 'Va_Xa', 'CA', 'XII', 'K', 'ATIII_Heparin', 'Xa_ATIII_Heparin', 'VK', 'C_warf', 'VKO', 'Pk', 'FDP', 'D', 'TAT', 'VIIa_TF_Xa_TFPI', 'XIIIa', 'IIa_ATIII_Heparin', 'IXa_ATIII_Heparin', 'A_warf', 'VK_p']
    _SPECIES_LABELS = {'IIa': 'IIa', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'APC_PS': 'APC_PS', 'IX': 'IX', 'IXa': 'IXa', 'XIa': 'XIa', 'XI': 'XI', 'XIIa': 'XIIa', 'VII': 'VII', 'VIIa': 'VIIa', 'X': 'X', 'Xa': 'Xa', 'IXa_VIIIa': 'IXa_VIIIa', 'V': 'V', 'Va': 'Va', 'II': 'II', 'F': 'F', 'Fg': 'Fg', 'DP': 'DP', 'P': 'P', 'XF': 'XF', 'XIII': 'XIII', 'Pg': 'Pg', 'APC': 'APC', 'IIa_Tmod': 'IIa_Tmod', 'PC': 'PC', 'Tmod': 'Tmod', 'TF': 'TF', 'VIIa_TF': 'VIIa_TF', 'VII_TF': 'VII_TF', 'Xa_TFPI': 'Xa_TFPI', 'TFPI': 'TFPI', 'PS': 'PS', 'VKH2': 'VKH2', 'Va_Xa': 'Va_Xa', 'CA': 'CA', 'XII': 'XII', 'K': 'K', 'ATIII_Heparin': 'ATIII_Heparin', 'Xa_ATIII_Heparin': 'Xa_ATIII_Heparin', 'VK': 'VK', 'C_warf': 'C_warf', 'VKO': 'VKO', 'Pk': 'Pk', 'FDP': 'FDP', 'D': 'D', 'TAT': 'TAT', 'VIIa_TF_Xa_TFPI': 'VIIa_TF_Xa_TFPI', 'XIIIa': 'XIIIa', 'IIa_ATIII_Heparin': 'IIa_ATIII_Heparin', 'IXa_ATIII_Heparin': 'IXa_ATIII_Heparin', 'A_warf': 'A_warf', 'VK_p': 'VK_p'}
    _PARAMETER_INPUTS = {'warfarin_daily_dose': ('warfarin_daily_dose', 4.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `warfarin_daily_dose`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'vk_p': ('VK_p', 'native SBML value', 'VK_p. Maps to SBML symbol `VK_p`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa_TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'xa_atiii_heparin': ('Xa_ATIII_Heparin', 'native SBML value', 'Xa_ATIII_Heparin. Maps to SBML symbol `Xa_ATIII_Heparin`.'), 'va_xa': ('Va_Xa', 'native SBML value', 'Va_Xa. Maps to SBML symbol `Va_Xa`.'), 'vi_ia_tf_xa_tfpi': ('VIIa_TF_Xa_TFPI', 'native SBML value', 'VIIa_TF_Xa_TFPI. Maps to SBML symbol `VIIa_TF_Xa_TFPI`.'), 'vi_ia_tf': ('VIIa_TF', 'native SBML value', 'VIIa_TF. Maps to SBML symbol `VIIa_TF`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000340.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
