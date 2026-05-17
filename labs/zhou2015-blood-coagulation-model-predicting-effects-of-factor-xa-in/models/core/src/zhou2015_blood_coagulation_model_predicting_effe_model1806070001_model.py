# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zhou2015 - Blood coagulation model predicting effects of factor Xa inhibitors."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhou2015BloodCoagulationModelPredictingEffeModel1806070001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zhou2015 - Blood coagulation model predicting effects of factor Xa inhibitors."""

    _SBML_ID = 'MODEL1806070001'
    _TITLE = 'Zhou2015 - Blood coagulation model predicting effects of factor Xa inhibitors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VIII', 'VIIIa', 'IIa', 'IX', 'IXa', 'XIa', 'XI', 'XIIa', 'VII', 'VIIa', 'X', 'Xa', 'V', 'Va', 'II', 'Xa_Va', 'F', 'Fg', 'DP', 'P', 'XF', 'XIIIa', 'XIII', 'Pg', 'TF', 'VIIa_TF', 'VII_TF', 'VIIa_TF_Xa_TFPI', 'Xa_TFPI', 'TFPI', 'CA', 'XII', 'K', 'PK', 'ATIII', 'Xa_ATIII', 'IXa_ATIII', 'IIa_ATIII', 'VIIa_TF_ATIII', 'XIIa_ATIII', 'XIa_ATIII', 'IXa_VIIIa', 'VIIa_Xa', 'Xa_Inhibitor', 'Xa_Xa_Inhibitor', 'Xa_Va_Xa_Inhibitor']
    _SPECIES_LABELS = {'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IIa': 'IIa', 'IX': 'IX', 'IXa': 'IXa', 'XIa': 'XIa', 'XI': 'XI', 'XIIa': 'XIIa', 'VII': 'VII', 'VIIa': 'VIIa', 'X': 'X', 'Xa': 'Xa', 'V': 'V', 'Va': 'Va', 'II': 'II', 'Xa_Va': 'Xa:Va', 'F': 'F', 'Fg': 'Fg', 'DP': 'DP', 'P': 'P', 'XF': 'XF', 'XIIIa': 'XIIIa', 'XIII': 'XIII', 'Pg': 'Pg', 'TF': 'TF', 'VIIa_TF': 'VIIa:TF', 'VII_TF': 'VII:TF', 'VIIa_TF_Xa_TFPI': 'VIIa:TF:Xa:TFPI', 'Xa_TFPI': 'Xa:TFPI', 'TFPI': 'TFPI', 'CA': 'CA', 'XII': 'XII', 'K': 'K', 'PK': 'PK', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa:ATIII', 'IXa_ATIII': 'IXa:ATIII', 'IIa_ATIII': 'IIa:ATIII', 'VIIa_TF_ATIII': 'VIIa:TF:ATIII', 'XIIa_ATIII': 'XIIa:ATIII', 'XIa_ATIII': 'XIa:ATIII', 'IXa_VIIIa': 'IXa:VIIIa', 'VIIa_Xa': 'VIIa:Xa', 'Xa_Inhibitor': 'Xa_Inhibitor', 'Xa_Xa_Inhibitor': 'Xa:Xa_Inhibitor', 'Xa_Va_Xa_Inhibitor': 'Xa:Va:Xa_Inhibitor'}
    _PARAMETER_INPUTS = {'drug': ('Drug', 0.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Drug`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'xa_xa_inhibitor': ('Xa_Xa_Inhibitor', 'native SBML value', 'Xa:Xa_Inhibitor. Maps to SBML symbol `Xa_Xa_Inhibitor`.'), 'xa_va_xa_inhibitor': ('Xa_Va_Xa_Inhibitor', 'native SBML value', 'Xa:Va:Xa_Inhibitor. Maps to SBML symbol `Xa_Va_Xa_Inhibitor`.'), 'xa_inhibitor': ('Xa_Inhibitor', 'native SBML value', 'Xa_Inhibitor. Maps to SBML symbol `Xa_Inhibitor`.'), 'xa_va': ('Xa_Va', 'native SBML value', 'Xa:Va. Maps to SBML symbol `Xa_Va`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa:TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa:ATIII. Maps to SBML symbol `Xa_ATIII`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806070001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
