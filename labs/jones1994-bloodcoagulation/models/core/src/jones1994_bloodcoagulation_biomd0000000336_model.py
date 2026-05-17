# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Jones1994_BloodCoagulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jones1994BloodcoagulationBiomd0000000336Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Jones1994_BloodCoagulation."""

    _SBML_ID = 'BIOMD0000000336'
    _TITLE = 'Jones1994_BloodCoagulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IX', 'IX_TF_VIIa', 'TF_VIIa', 'IXa', 'X', 'X_TF_VIIa', 'Xa', 'VIIIa_IXa', 'X_VIIIa_IXa', 'V', 'Va', 'VIII', 'VIIIa', 'IIa', 'II', 'II_Va_Xa', 'Va_Xa', 'mIIa']
    _SPECIES_LABELS = {'IX': 'IX', 'IX_TF_VIIa': 'IX_TF_VIIa', 'TF_VIIa': 'TF_VIIa', 'IXa': 'IXa', 'X': 'X', 'X_TF_VIIa': 'X_TF_VIIa', 'Xa': 'Xa', 'VIIIa_IXa': 'VIIIa_IXa', 'X_VIIIa_IXa': 'X_VIIIa_IXa', 'V': 'V', 'Va': 'Va', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IIa': 'IIa', 'II': 'II', 'II_Va_Xa': 'II_Va_Xa', 'Va_Xa': 'Va_Xa', 'mIIa': 'mIIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tf_vi_ia': ('TF_VIIa', 5e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF_VIIa`.'), 'initial_m_i_ia': ('mIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`.'), 'initial_x_vii_ia_i_xa': ('X_VIIIa_IXa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_VIIIa_IXa`.'), 'initial_x_tf_vi_ia': ('X_TF_VIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_TF_VIIa`.'), 'initial_va_xa': ('Va_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_Xa`.'), 'initial_vii_ia_i_xa': ('VIIIa_IXa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIIa_IXa`.')}
    _HEADLINE_OUTPUTS = {'tf_vi_ia': ('TF_VIIa', 'native SBML value', 'TF_VIIa. Maps to SBML symbol `TF_VIIa`.'), 'm_i_ia': ('mIIa', 'native SBML value', 'mIIa. Maps to SBML symbol `mIIa`.'), 'x_vii_ia_i_xa': ('X_VIIIa_IXa', 'native SBML value', 'X_VIIIa_IXa. Maps to SBML symbol `X_VIIIa_IXa`.'), 'x_tf_vi_ia': ('X_TF_VIIa', 'native SBML value', 'X_TF_VIIa. Maps to SBML symbol `X_TF_VIIa`.'), 'va_xa': ('Va_Xa', 'native SBML value', 'Va_Xa. Maps to SBML symbol `Va_Xa`.'), 'vii_ia_i_xa': ('VIIIa_IXa', 'native SBML value', 'VIIIa_IXa. Maps to SBML symbol `VIIIa_IXa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000336.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
