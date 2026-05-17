# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tanos2008 - Blood coagulation and Snake Venom."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tanos2008BloodCoagulationAndSnakeVenomModel1806150001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tanos2008 - Blood coagulation and Snake Venom."""

    _SBML_ID = 'MODEL1806150001'
    _TITLE = 'Tanos2008 - Blood coagulation and Snake Venom'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['II', 'IIa', 'V', 'Va', 'VII', 'VIIa', 'VIII', 'VIIIa', 'IX', 'IXa', 'X', 'Xa', 'XI', 'XIa', 'XIIa', 'XIII', 'XIIIa', 'Pg', 'P', 'PC', 'APC', 'Tmod', 'TAT', 'IXa_VIIIa', 'Va_Xa', 'IIa_Tmod', 'Taipan', 'Fg', 'F', 'XF', 'DP', 'C1', 'C2', 'Antivenom']
    _SPECIES_LABELS = {'II': 'II', 'IIa': 'IIa', 'V': 'V', 'Va': 'Va', 'VII': 'VII', 'VIIa': 'VIIa', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'IX': 'IX', 'IXa': 'IXa', 'X': 'X', 'Xa': 'Xa', 'XI': 'XI', 'XIa': 'XIa', 'XIIa': 'XIIa', 'XIII': 'XIII', 'XIIIa': 'XIIIa', 'Pg': 'Pg', 'P': 'P', 'PC': 'PC', 'APC': 'APC', 'Tmod': 'Tmod', 'TAT': 'TAT', 'IXa_VIIIa': 'IXa:VIIIa', 'Va_Xa': 'Va:Xa', 'IIa_Tmod': 'IIa:Tmod', 'Taipan': 'Taipan', 'Fg': 'Fg', 'F': 'F', 'XF': 'XF', 'DP': 'DP', 'C1': 'C1', 'C2': 'C2', 'Antivenom': 'Antivenom'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_va_xa': ('Va_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_Xa`.'), 'initial_i_xa_vii_ia': ('IXa_VIIIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IXa_VIIIa`.'), 'initial_i_ia_tmod': ('IIa_Tmod', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_Tmod`.'), 'initial_model_state_fg': ('Fg', 8945.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fg`.'), 'initial_model_state_pg': ('Pg', 2154.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pg`.'), 'initial_model_state_ii': ('II', 1394.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II`.')}
    _HEADLINE_OUTPUTS = {'va_xa': ('Va_Xa', 'native SBML value', 'Va:Xa. Maps to SBML symbol `Va_Xa`.'), 'i_xa_vii_ia': ('IXa_VIIIa', 'native SBML value', 'IXa:VIIIa. Maps to SBML symbol `IXa_VIIIa`.'), 'i_ia_tmod': ('IIa_Tmod', 'native SBML value', 'IIa:Tmod. Maps to SBML symbol `IIa_Tmod`.'), 'model_state_fg': ('Fg', 'native SBML value', 'Fg. Maps to SBML symbol `Fg`.'), 'model_state_pg': ('Pg', 'native SBML value', 'Pg. Maps to SBML symbol `Pg`.'), 'model_state_ii': ('II', 'native SBML value', 'II. Maps to SBML symbol `II`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806150001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
