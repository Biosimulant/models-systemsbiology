# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Golomb2006_SomaticBursting_nonzero[Ca]."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Golomb2006SomaticburstingNonzeroCaBiomd0000000119Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Golomb2006_SomaticBursting_nonzero[Ca]."""

    _SBML_ID = 'BIOMD0000000119'
    _TITLE = 'Golomb2006_SomaticBursting_nonzero[Ca]'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ca']
    _SPECIES_LABELS = {'Ca': 'Ca'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ca': ('Ca', 0.000787, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca`.')}
    _HEADLINE_OUTPUTS = {'model_state_ca': ('Ca', 'native SBML value', 'Ca. Maps to SBML symbol `Ca`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000119.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
