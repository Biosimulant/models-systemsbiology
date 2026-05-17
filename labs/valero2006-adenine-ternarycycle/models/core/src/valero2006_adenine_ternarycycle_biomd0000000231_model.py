# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Valero2006_Adenine_TernaryCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Valero2006AdenineTernarycycleBiomd0000000231Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Valero2006_Adenine_TernaryCycle."""

    _SBML_ID = 'BIOMD0000000231'
    _TITLE = 'Valero2006_Adenine_TernaryCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ATP', 'AMP', 'ADP', 'Pyr', 'NADH', 'Lac']
    _SPECIES_LABELS = {'ATP': 'ATP', 'AMP': 'AMP', 'ADP': 'ADP', 'Pyr': 'Pyr', 'NADH': 'NADH', 'Lac': 'Lac'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nadh': ('NADH', 256.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADH`.'), 'initial_model_state_atp': ('ATP', 16.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_pyr': ('Pyr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pyr`.'), 'initial_model_state_lac': ('Lac', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lac`.'), 'initial_model_state_amp': ('AMP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AMP`.')}
    _HEADLINE_OUTPUTS = {'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'pyr': ('Pyr', 'native SBML value', 'Pyr. Maps to SBML symbol `Pyr`.'), 'lac': ('Lac', 'native SBML value', 'Lac. Maps to SBML symbol `Lac`.'), 'amp': ('AMP', 'native SBML value', 'AMP. Maps to SBML symbol `AMP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000231.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
