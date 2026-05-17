# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Susree2018 - Effect of coated platelets on thrombin generation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Susree2018EffectOfCoatedPlateletsOnThrombiModel1808080001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Susree2018 - Effect of coated platelets on thrombin generation."""

    _SBML_ID = 'MODEL1808080001'
    _TITLE = 'Susree2018 - Effect of coated platelets on thrombin generation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TF', 'VII', 'TF_VII', 'VIIa', 'TF_VIIa', 'XI', 'XIa', 'IX', 'IXa', 'X', 'Xa', 'II', 'IIa', 'RP', 'AP', 'VIII', 'VIIIa', 'V', 'Va', 'I', 'Ia', 'TFPI', 'Xa_TFPI', 'ATIII', 'a1AT', 'CP', 'PS', 'IXa_m', 'VIIIa_m', 'Xa_Va_m', 'X_m', 'II_m', 'Va_m']
    _SPECIES_LABELS = {'TF': 'TF', 'VII': 'VII', 'TF_VII': 'TF:VII', 'VIIa': 'VIIa', 'TF_VIIa': 'TF:VIIa', 'XI': 'XI', 'XIa': 'XIa', 'IX': 'IX', 'IXa': 'IXa', 'X': 'X', 'Xa': 'Xa', 'II': 'II', 'IIa': 'IIa', 'RP': 'RP', 'AP': 'AP', 'VIII': 'VIII', 'VIIIa': 'VIIIa', 'V': 'V', 'Va': 'Va', 'I': 'I', 'Ia': 'Ia', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa:TFPI', 'ATIII': 'ATIII', 'a1AT': 'a1AT', 'CP': 'CP', 'PS': 'PS', 'IXa_m': 'IXa_m', 'VIIIa_m': 'VIIIa_m', 'Xa_Va_m': 'Xa_Va_m', 'X_m': 'X_m', 'II_m': 'II_m', 'Va_m': 'Va_m'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_a1_at': ('a1AT', 45000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a1AT`.'), 'initial_ii_m': ('II_m', 0.00156379040860618, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II_m`.'), 'initial_model_state_x_m': ('X_m', 0.000984485174386137, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_m`.'), 'initial_va_m': ('Va_m', 7.2112676056338e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_m`.'), 'initial_i_xa_m': ('IXa_m', 4.94269468434452e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IXa_m`.'), 'initial_vii_ia_m': ('VIIIa_m', 8.09330123752319e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIIa_m`.')}
    _HEADLINE_OUTPUTS = {'a1_at': ('a1AT', 'native SBML value', 'a1AT. Maps to SBML symbol `a1AT`.'), 'ii_m': ('II_m', 'native SBML value', 'II_m. Maps to SBML symbol `II_m`.'), 'x_m': ('X_m', 'native SBML value', 'X_m. Maps to SBML symbol `X_m`.'), 'va_m': ('Va_m', 'native SBML value', 'Va_m. Maps to SBML symbol `Va_m`.'), 'i_xa_m': ('IXa_m', 'native SBML value', 'IXa_m. Maps to SBML symbol `IXa_m`.'), 'vii_ia_m': ('VIIIa_m', 'native SBML value', 'VIIIa_m. Maps to SBML symbol `VIIIa_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808080001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
