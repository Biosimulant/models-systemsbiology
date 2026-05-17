# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Reidl2006_CalciumOscillationInCilia."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reidl2006CalciumoscillationinciliaModel7908934508Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Reidl2006_CalciumOscillationInCilia."""

    _SBML_ID = 'MODEL7908934508'
    _TITLE = 'Reidl2006_CalciumOscillationInCilia'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['CNG_o', 'Ca', 'CaM4', 'CNG_i']
    _SPECIES_LABELS = {'CNG_o': 'CNG O', 'Ca': 'Ca', 'CaM4': 'CaM4', 'CNG_i': 'CNG I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_m4': ('CaM4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaM4`.'), 'initial_model_state_ca': ('Ca', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca`.'), 'initial_cng_o': ('CNG_o', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CNG_o`.'), 'initial_cng_i': ('CNG_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CNG_i`.')}
    _HEADLINE_OUTPUTS = {'ca_m4': ('CaM4', 'native SBML value', 'CaM4. Maps to SBML symbol `CaM4`.'), 'model_state_ca': ('Ca', 'native SBML value', 'Ca. Maps to SBML symbol `Ca`.'), 'cng_o': ('CNG_o', 'native SBML value', 'CNG O. Maps to SBML symbol `CNG_o`.'), 'cng_i': ('CNG_i', 'native SBML value', 'CNG I. Maps to SBML symbol `CNG_i`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL7908934508.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
