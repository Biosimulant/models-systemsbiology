# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Khanin1998 - Mathematical Model of Blood Coagulation Prothrombin Time Test."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khanin1998MathematicalModelOfBloodCoagulatiModel1806120001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Khanin1998 - Mathematical Model of Blood Coagulation Prothrombin Time Test."""

    _SBML_ID = 'MODEL1806120001'
    _TITLE = 'Khanin1998 - Mathematical Model of Blood Coagulation Prothrombin Time Test'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VII_TF', 'VIIa_TF', 'Xa', 'X', 'II', 'IIa', 'Xa_Va_PL', 'I', 'Ia', 'V', 'Va', 'VIII', 'VIIIa', 'IX', 'IXa', 'IXa_VIIIa_PL', 'PL', 'Va_Xa', 'VIIIa_IXa', 'TF', 'VII', 'ATIII', 'VIIa_TF_ATIII', 'Xa_ATIII', 'IIa_ATIII', 'TFPI', 'VIIa_TF_Xa_TFPI', 'Xa_TFPI']
    _SPECIES_LABELS = {'VII_TF': 'VII:TF', 'VIIa_TF': 'VIIa:TF', 'Xa': 'Xa', 'X': 'X', 'II': 'II', 'IIa': 'IIa', 'Xa_Va_PL': 'Xa:Va:PL', 'I': 'I', 'Ia': 'Ia', 'V': 'V', 'Va': 'Va', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IX': 'IX', 'IXa': 'IXa', 'IXa_VIIIa_PL': 'IXa:VIIIa:PL', 'PL': 'PL', 'Va_Xa': 'Va:Xa', 'VIIIa_IXa': 'VIIIa:IXa', 'TF': 'TF', 'VII': 'VII', 'ATIII': 'ATIII', 'VIIa_TF_ATIII': 'VIIa:TF:ATIII', 'Xa_ATIII': 'Xa:ATIII', 'IIa_ATIII': 'IIa:ATIII', 'TFPI': 'TFPI', 'VIIa_TF_Xa_TFPI': 'VIIa:TF:Xa:TFPI', 'Xa_TFPI': 'Xa:TFPI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vii_tf': ('VII_TF', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VII_TF`.'), 'initial_i_xa_vii_ia_pl': ('IXa_VIIIa_PL', 1e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IXa_VIIIa_PL`.'), 'initial_xa_va_pl': ('Xa_Va_PL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_PL`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_xa_atiii': ('Xa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`.'), 'initial_va_xa': ('Va_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_Xa`.')}
    _HEADLINE_OUTPUTS = {'vii_tf': ('VII_TF', 'native SBML value', 'VII:TF. Maps to SBML symbol `VII_TF`.'), 'i_xa_vii_ia_pl': ('IXa_VIIIa_PL', 'native SBML value', 'IXa:VIIIa:PL. Maps to SBML symbol `IXa_VIIIa_PL`.'), 'xa_va_pl': ('Xa_Va_PL', 'native SBML value', 'Xa:Va:PL. Maps to SBML symbol `Xa_Va_PL`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa:TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa:ATIII. Maps to SBML symbol `Xa_ATIII`.'), 'va_xa': ('Va_Xa', 'native SBML value', 'Va:Xa. Maps to SBML symbol `Va_Xa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806120001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
