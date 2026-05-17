# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Goodwin1965_EnzymeControlProcess."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goodwin1965EnzymecontrolprocessModel0911532520Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Goodwin1965_EnzymeControlProcess."""

    _SBML_ID = 'MODEL0911532520'
    _TITLE = 'Goodwin1965_EnzymeControlProcess'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Xi', 'Yi']
    _SPECIES_LABELS = {'Xi': 'Xi', 'Yi': 'Yi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_yi': ('Yi', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Yi`.'), 'initial_model_state_xi': ('Xi', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xi`.')}
    _HEADLINE_OUTPUTS = {'model_state_yi': ('Yi', 'native SBML value', 'Yi. Maps to SBML symbol `Yi`.'), 'model_state_xi': ('Xi', 'native SBML value', 'Xi. Maps to SBML symbol `Xi`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0911532520.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
