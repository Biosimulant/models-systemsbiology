# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mitrophanov2016 - Extended Mitrophanov2011 Blood Coagulation Model (additional thrombin reactions)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mitrophanov2016ExtendedMitrophanov2011BloodCModel1806280001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mitrophanov2016 - Extended Mitrophanov2011 Blood Coagulation Model (additional thrombin reactions)."""

    _SBML_ID = 'MODEL1806280001'
    _TITLE = 'Mitrophanov2016 - Extended Mitrophanov2011 Blood Coagulation Model (additional thrombin reactions)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'TF_VII', 'VII', 'TF_VIIa', 'VIIa', 'Xa', 'IIa', 'TF_VIIa_X', 'X', 'TF_VIIa_Xa', 'IX', 'TF_VIIa_IX', 'IXa', 'II', 'VIII', 'VIIIa', 'IXa_VIIIa', 'IXa_VIIIa_X', 'VIIIa1_L', 'VIIIa2', 'V', 'Va', 'Xa_Va', 'Xa_Va_II', 'mIIa', 'TFPI', 'Xa_TFPI', 'TF_VIIa_Xa_TFPI', 'ATIII', 'Xa_ATIII', 'mIIa_ATIII', 'IXa_ATIII', 'IIa_ATIII', 'TF_VIIa_ATIII', 'FS', 'FS_conv', 'IIa_FS', 'IIa_alpha_2_M', 'alpha_2_M', 'IIa_alpha_2_M_FS', 'IIa_Serpins', 'Serpins', 'rVIIa']
    _SPECIES_LABELS = {'TF': 'TF', 'TF_VII': 'TF_VII', 'VII': 'VII', 'TF_VIIa': 'TF_VIIa', 'VIIa': 'VIIa', 'Xa': 'Xa', 'IIa': 'IIa', 'TF_VIIa_X': 'TF_VIIa_X', 'X': 'X', 'TF_VIIa_Xa': 'TF_VIIa_Xa', 'IX': 'IX', 'TF_VIIa_IX': 'TF_VIIa_IX', 'IXa': 'IXa', 'II': 'II', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IXa_VIIIa': 'IXa_VIIIa', 'IXa_VIIIa_X': 'IXa_VIIIa_X', 'VIIIa1_L': 'VIIIa1_L', 'VIIIa2': 'VIIIa2', 'V': 'V', 'Va': 'Va', 'Xa_Va': 'Xa_Va', 'Xa_Va_II': 'Xa_Va_II', 'mIIa': 'mIIa', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa_TFPI', 'TF_VIIa_Xa_TFPI': 'TF_VIIa_Xa_TFPI', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa_ATIII', 'mIIa_ATIII': 'mIIa_ATIII', 'IXa_ATIII': 'IXa_ATIII', 'IIa_ATIII': 'IIa_ATIII', 'TF_VIIa_ATIII': 'TF_VIIa_ATIII', 'FS': 'FS', 'FS_conv': 'FS_conv', 'IIa_FS': 'IIa:FS', 'IIa_alpha_2_M': 'IIa:alpha_2_M', 'alpha_2_M': 'alpha_2_M', 'IIa_alpha_2_M_FS': 'IIa:alpha_2_M:FS', 'IIa_Serpins': 'IIa:Serpins', 'Serpins': 'Serpins', 'rVIIa': 'rVIIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha_2_m': ('alpha_2_M', 1.01e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha_2_M`.'), 'initial_r_vi_ia': ('rVIIa', 4.615e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rVIIa`.'), 'initial_m_i_ia_atiii': ('mIIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`.'), 'initial_m_i_ia': ('mIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`.'), 'initial_xa_va_ii': ('Xa_Va_II', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`.'), 'initial_xa_va': ('Xa_Va', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`.')}
    _HEADLINE_OUTPUTS = {'alpha_2_m': ('alpha_2_M', 'native SBML value', 'alpha_2_M. Maps to SBML symbol `alpha_2_M`.'), 'r_vi_ia': ('rVIIa', 'native SBML value', 'rVIIa. Maps to SBML symbol `rVIIa`.'), 'm_i_ia_atiii': ('mIIa_ATIII', 'native SBML value', 'mIIa_ATIII. Maps to SBML symbol `mIIa_ATIII`.'), 'm_i_ia': ('mIIa', 'native SBML value', 'mIIa. Maps to SBML symbol `mIIa`.'), 'xa_va_ii': ('Xa_Va_II', 'native SBML value', 'Xa_Va_II. Maps to SBML symbol `Xa_Va_II`.'), 'xa_va': ('Xa_Va', 'native SBML value', 'Xa_Va. Maps to SBML symbol `Xa_Va`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806280001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
