# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lo2005 - Stochastic Modeling of Blood Coagulation Initiation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lo2005StochasticModelingOfBloodCoagulationModel1805160001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lo2005 - Stochastic Modeling of Blood Coagulation Initiation."""

    _SBML_ID = 'MODEL1805160001'
    _TITLE = 'Lo2005 - Stochastic Modeling of Blood Coagulation Initiation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'TF_VII', 'VII', 'TF_VIIa', 'VIIa', 'Xa', 'IIa', 'TF_VIIa_X', 'X', 'TF_VIIa_Xa', 'IX', 'TF_VIIa_IX', 'IXa', 'II', 'VIII', 'VIIIa', 'IXa_VIIIa', 'IXa_VIIIa_X', 'VIIIa_1_L', 'VIIIa_2', 'V', 'Va', 'Xa_Va', 'Xa_Va_II', 'mIIa', 'TFPI', 'Xa_TFPI', 'TF_VIIa_Xa_TFPI', 'ATIII', 'Xa_ATIII', 'mIIa_ATIII', 'IXa_ATIII', 'IIa_ATIII', 'TF_VIIa_ATIII']
    _SPECIES_LABELS = {'TF': 'TF', 'TF_VII': 'TF-VII', 'VII': 'VII', 'TF_VIIa': 'TF-VIIa', 'VIIa': 'VIIa', 'Xa': 'Xa', 'IIa': 'IIa', 'TF_VIIa_X': 'TF-VIIa-X', 'X': 'X', 'TF_VIIa_Xa': 'TF-VIIa-Xa', 'IX': 'IX', 'TF_VIIa_IX': 'TF-VIIa-IX', 'IXa': 'IXa', 'II': 'II', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IXa_VIIIa': 'IXa-VIIIa', 'IXa_VIIIa_X': 'IXa-VIIIa-X', 'VIIIa_1_L': 'VIIIa_1-L', 'VIIIa_2': 'VIIIa_2', 'V': 'V', 'Va': 'Va', 'Xa_Va': 'Xa-Va', 'Xa_Va_II': 'Xa-Va-II', 'mIIa': 'mIIa', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa-TFPI', 'TF_VIIa_Xa_TFPI': 'TF-VIIa-Xa-TFPI', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa-ATIII', 'mIIa_ATIII': 'mIIa-ATIII', 'IXa_ATIII': 'IXa-ATIII', 'IIa_ATIII': 'IIa-ATIII', 'TF_VIIa_ATIII': 'TF-VIIa-ATIII'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_m_i_ia_atiii': ('mIIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`.'), 'initial_m_i_ia': ('mIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`.'), 'initial_xa_va_ii': ('Xa_Va_II', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`.'), 'initial_xa_va': ('Xa_Va', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_xa_atiii': ('Xa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`.')}
    _HEADLINE_OUTPUTS = {'m_i_ia_atiii': ('mIIa_ATIII', 'native SBML value', 'mIIa-ATIII. Maps to SBML symbol `mIIa_ATIII`.'), 'm_i_ia': ('mIIa', 'native SBML value', 'mIIa. Maps to SBML symbol `mIIa`.'), 'xa_va_ii': ('Xa_Va_II', 'native SBML value', 'Xa-Va-II. Maps to SBML symbol `Xa_Va_II`.'), 'xa_va': ('Xa_Va', 'native SBML value', 'Xa-Va. Maps to SBML symbol `Xa_Va`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa-TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa-ATIII. Maps to SBML symbol `Xa_ATIII`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1805160001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
