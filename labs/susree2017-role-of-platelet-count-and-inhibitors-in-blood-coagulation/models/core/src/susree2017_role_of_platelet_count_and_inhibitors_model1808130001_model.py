# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Susree2017 - Role of platelet count and inhibitors in blood coagulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Susree2017RoleOfPlateletCountAndInhibitorsModel1808130001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Susree2017 - Role of platelet count and inhibitors in blood coagulation."""

    _SBML_ID = 'MODEL1808130001'
    _TITLE = 'Susree2017 - Role of platelet count and inhibitors in blood coagulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'VII', 'TF_VII', 'VIIa', 'TF_VIIa', 'IX', 'IXa', 'IXa_m', 'X', 'Xa', 'X_m', 'Xa_m', 'II', 'IIa', 'II_m', 'IIa_m', 'PL', 'AP', 'VIII', 'VIIIa', 'VIII_m', 'VIIIa_m', 'VIIIa_m_IXa_m', 'V', 'Va', 'V_m', 'Va_m', 'Xa_m_Va_m', 'I', 'Ia', 'TFPI', 'Xa_TFPI', 'ATIII', 'IX_m']
    _SPECIES_LABELS = {'TF': 'TF', 'VII': 'VII', 'TF_VII': 'TF:VII', 'VIIa': 'VIIa', 'TF_VIIa': 'TF:VIIa', 'IX': 'IX', 'IXa': 'IXa', 'IXa_m': 'IXa_m', 'X': 'X', 'Xa': 'Xa', 'X_m': 'X_m', 'Xa_m': 'Xa_m', 'II': 'II', 'IIa': 'IIa', 'II_m': 'II_m', 'IIa_m': 'IIa_m', 'PL': 'PL', 'AP': 'AP', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'VIII_m': 'VIII_m', 'VIIIa_m': 'VIIIa_m', 'VIIIa_m_IXa_m': 'VIIIa_m:IXa:m', 'V': 'V', 'Va': 'Va', 'V_m': 'V_m', 'Va_m': 'Va_m', 'Xa_m_Va_m': 'Xa_m:Va:m', 'I': 'I', 'Ia': 'Ia', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa:TFPI', 'ATIII': 'ATIII', 'IX_m': 'IX_m'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_xa_m_va_m': ('Xa_m_Va_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_m_Va_m`.'), 'initial_xa_m': ('Xa_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_m`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_model_state_x_m': ('X_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_m`.'), 'initial_va_m': ('Va_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_m`.'), 'initial_model_state_v_m': ('V_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_m`.')}
    _HEADLINE_OUTPUTS = {'xa_m_va_m': ('Xa_m_Va_m', 'native SBML value', 'Xa_m:Va:m. Maps to SBML symbol `Xa_m_Va_m`.'), 'xa_m': ('Xa_m', 'native SBML value', 'Xa_m. Maps to SBML symbol `Xa_m`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa:TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'x_m': ('X_m', 'native SBML value', 'X_m. Maps to SBML symbol `X_m`.'), 'va_m': ('Va_m', 'native SBML value', 'Va_m. Maps to SBML symbol `Va_m`.'), 'v_m': ('V_m', 'native SBML value', 'V_m. Maps to SBML symbol `V_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808130001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
