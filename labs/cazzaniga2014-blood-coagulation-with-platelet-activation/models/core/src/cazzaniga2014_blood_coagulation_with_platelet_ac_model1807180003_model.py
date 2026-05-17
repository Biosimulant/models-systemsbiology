# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cazzaniga2014 - Blood Coagulation with Platelet Activation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cazzaniga2014BloodCoagulationWithPlateletAcModel1807180003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cazzaniga2014 - Blood Coagulation with Platelet Activation."""

    _SBML_ID = 'MODEL1807180003'
    _TITLE = 'Cazzaniga2014 - Blood Coagulation with Platelet Activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'TF_VII', 'VII', 'TF_VIIa', 'VIIa', 'Xa', 'IIa', 'TF_VIIa_X', 'X', 'TF_VIIa_Xa', 'IX', 'TF_VIIa_IX', 'IXa', 'II', 'VIII', 'VIIIa', 'IXa_VIIIa', 'IXa_VIIIa_X', 'VIIIa1_L', 'VIIIa2', 'V', 'Va', 'Xa_Va', 'Xa_Va_II', 'mIIa', 'TFPI', 'Xa_TFPI', 'TF_VIIa_Xa_TFPI', 'ATIII', 'Xa_ATIII', 'mIIa_ATIII', 'IXa_ATIII', 'IIa_ATIII', 'TF_VIIa_ATIII', 'XII', 'XIIa', 'XIIa_XII', 'PKal', 'XIIa_PKal', 'Kal', 'XII_Kal', 'Kal_i', 'C1inh', 'XIIa_C1inh', 'XIIa_ATIII', 'XI', 'XI_IIa', 'XIa', 'XIIa_XI', 'XIa_ATIII', 'XIa_C1inh', 'A1AT', 'XIa_A1AT', 'A2AP', 'XIa_A2AP', 'XIa_IX', 'IXa_X', 'Xa_VIII', 'VIIa_IX', 'VIIa_X', 'Fbg', 'Fbg_IIa', 'FPA', 'Fbn1', 'Fbn1_IIa', 'FPB', 'Fbn2', 'Fbn1_2', 'Fbn1_2_IIa', 'Fbn2_IIa']
    _SPECIES_LABELS = {'TF': 'TF', 'TF_VII': 'TF:VII', 'VII': 'VII', 'TF_VIIa': 'TF:VIIa', 'VIIa': 'VIIa', 'Xa': 'Xa', 'IIa': 'IIa', 'TF_VIIa_X': 'TF:VIIa:X', 'X': 'X', 'TF_VIIa_Xa': 'TF:VIIa:Xa', 'IX': 'IX', 'TF_VIIa_IX': 'TF:VIIa:IX', 'IXa': 'IXa', 'II': 'II', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IXa_VIIIa': 'IXa:VIIIa', 'IXa_VIIIa_X': 'IXa:VIIIa:X', 'VIIIa1_L': 'VIIIa1-L', 'VIIIa2': 'VIIIa2', 'V': 'V', 'Va': 'Va', 'Xa_Va': 'Xa:Va', 'Xa_Va_II': 'Xa:Va:II', 'mIIa': 'mIIa', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa:TFPI', 'TF_VIIa_Xa_TFPI': 'TF:VIIa:Xa:TFPI', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa:ATIII', 'mIIa_ATIII': 'mIIa:ATIII', 'IXa_ATIII': 'IXa:ATIII', 'IIa_ATIII': 'IIa:ATIII', 'TF_VIIa_ATIII': 'TF:VIIa:ATIII', 'XII': 'XII', 'XIIa': 'XIIa', 'XIIa_XII': 'XIIa:XII', 'PKal': 'PKal', 'XIIa_PKal': 'XIIa:PKal', 'Kal': 'Kal', 'XII_Kal': 'XII:Kal', 'Kal_i': 'Kal_i', 'C1inh': 'C1inh', 'XIIa_C1inh': 'XIIa:C1inh', 'XIIa_ATIII': 'XIIa:ATIII', 'XI': 'XI', 'XI_IIa': 'XI:IIa', 'XIa': 'XIa', 'XIIa_XI': 'XIIa:XI', 'XIa_ATIII': 'XIa:ATIII', 'XIa_C1inh': 'XIa:C1inh', 'A1AT': 'A1AT', 'XIa_A1AT': 'XIa:A1AT', 'A2AP': 'A2AP', 'XIa_A2AP': 'XIa:A2AP', 'XIa_IX': 'XIa:IX', 'IXa_X': 'IXa:X', 'Xa_VIII': 'Xa:VIII', 'VIIa_IX': 'VIIa:IX', 'VIIa_X': 'VIIa:X', 'Fbg': 'Fbg', 'Fbg_IIa': 'Fbg:IIa', 'FPA': 'FPA', 'Fbn1': 'Fbn1', 'Fbn1_IIa': 'Fbn1:IIa', 'FPB': 'FPB', 'Fbn2': 'Fbn2', 'Fbn1_2': 'Fbn1_2', 'Fbn1_2_IIa': 'Fbn1_2:IIa', 'Fbn2_IIa': 'Fbn2:IIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_m_i_ia_atiii': ('mIIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`.'), 'initial_m_i_ia': ('mIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`.'), 'initial_xa_va_ii': ('Xa_Va_II', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`.'), 'initial_xa_va': ('Xa_Va', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`.'), 'initial_xa_viii': ('Xa_VIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_VIII`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.')}
    _HEADLINE_OUTPUTS = {'m_i_ia_atiii': ('mIIa_ATIII', 'native SBML value', 'mIIa:ATIII. Maps to SBML symbol `mIIa_ATIII`.'), 'm_i_ia': ('mIIa', 'native SBML value', 'mIIa. Maps to SBML symbol `mIIa`.'), 'xa_va_ii': ('Xa_Va_II', 'native SBML value', 'Xa:Va:II. Maps to SBML symbol `Xa_Va_II`.'), 'xa_va': ('Xa_Va', 'native SBML value', 'Xa:Va. Maps to SBML symbol `Xa_Va`.'), 'xa_viii': ('Xa_VIII', 'native SBML value', 'Xa:VIII. Maps to SBML symbol `Xa_VIII`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa:TFPI. Maps to SBML symbol `Xa_TFPI`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1807180003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
