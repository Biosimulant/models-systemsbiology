# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Adams2003 - Thrombin Inhibitors."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Adams2003ThrombinInhibitorsModel1808150002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Adams2003 - Thrombin Inhibitors."""

    _SBML_ID = 'MODEL1808150002'
    _TITLE = 'Adams2003 - Thrombin Inhibitors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'TF_VII', 'VII', 'TF_VIIa', 'VIIa', 'Xa', 'IIa', 'TF_VIIa_X', 'X', 'TF_VIIa_Xa', 'IX', 'TF_VIIa_IX', 'IXa', 'II', 'VIII', 'VIIIa', 'IXa_VIIIa', 'IXa_VIIIa_X', 'VIIIa1_L', 'VIIIa2', 'V', 'Va', 'Xa_Va', 'Xa_Va_II', 'mIIa', 'TFPI', 'Xa_TFPI', 'TF_VIIa_Xa_TFPI', 'ATIII', 'Xa_ATIII', 'mIIa_ATIII', 'IXa_ATIII', 'IIa_ATIII', 'TF_VIIa_ATIII', 'Hirudin', 'Hirulog', 'Argatroban', 'Melagatran', 'Efegatran', 'Hirudin_IIa', 'Hirulog_IIa', 'Argatroban_IIa', 'Melagatran_IIa', 'Efegatran_IIa', 'Hirudin_mIIa', 'Hirulog_mIIa', 'Argatroban_mIIa', 'Melagatran_mIIa', 'Efegatran_mIIa']
    _SPECIES_LABELS = {'TF': 'TF', 'TF_VII': 'TF_VII', 'VII': 'VII', 'TF_VIIa': 'TF_VIIa', 'VIIa': 'VIIa', 'Xa': 'Xa', 'IIa': 'IIa', 'TF_VIIa_X': 'TF_VIIa_X', 'X': 'X', 'TF_VIIa_Xa': 'TF_VIIa_Xa', 'IX': 'IX', 'TF_VIIa_IX': 'TF_VIIa_IX', 'IXa': 'IXa', 'II': 'II', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IXa_VIIIa': 'IXa_VIIIa', 'IXa_VIIIa_X': 'IXa_VIIIa_X', 'VIIIa1_L': 'VIIIa1_L', 'VIIIa2': 'VIIIa2', 'V': 'V', 'Va': 'Va', 'Xa_Va': 'Xa_Va', 'Xa_Va_II': 'Xa_Va_II', 'mIIa': 'mIIa', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa_TFPI', 'TF_VIIa_Xa_TFPI': 'TF_VIIa_Xa_TFPI', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa_ATIII', 'mIIa_ATIII': 'mIIa_ATIII', 'IXa_ATIII': 'IXa_ATIII', 'IIa_ATIII': 'IIa_ATIII', 'TF_VIIa_ATIII': 'TF_VIIa_ATIII', 'Hirudin': 'Hirudin', 'Hirulog': 'Hirulog', 'Argatroban': 'Argatroban', 'Melagatran': 'Melagatran', 'Efegatran': 'Efegatran', 'Hirudin_IIa': 'Hirudin:IIa', 'Hirulog_IIa': 'Hirulog:IIa', 'Argatroban_IIa': 'Argatroban:IIa', 'Melagatran_IIa': 'Melagatran:IIa', 'Efegatran_IIa': 'Efegatran:IIa', 'Hirudin_mIIa': 'Hirudin:mIIa', 'Hirulog_mIIa': 'Hirulog:mIIa', 'Argatroban_mIIa': 'Argatroban:mIIa', 'Melagatran_mIIa': 'Melagatran:mIIa', 'Efegatran_mIIa': 'Efegatran:mIIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_m_i_ia_atiii': ('mIIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`.'), 'initial_m_i_ia': ('mIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`.'), 'initial_xa_va_ii': ('Xa_Va_II', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`.'), 'initial_xa_va': ('Xa_Va', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_xa_atiii': ('Xa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`.')}
    _HEADLINE_OUTPUTS = {'m_i_ia_atiii': ('mIIa_ATIII', 'native SBML value', 'mIIa_ATIII. Maps to SBML symbol `mIIa_ATIII`.'), 'm_i_ia': ('mIIa', 'native SBML value', 'mIIa. Maps to SBML symbol `mIIa`.'), 'xa_va_ii': ('Xa_Va_II', 'native SBML value', 'Xa_Va_II. Maps to SBML symbol `Xa_Va_II`.'), 'xa_va': ('Xa_Va', 'native SBML value', 'Xa_Va. Maps to SBML symbol `Xa_Va`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa_TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa_ATIII. Maps to SBML symbol `Xa_ATIII`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808150002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
