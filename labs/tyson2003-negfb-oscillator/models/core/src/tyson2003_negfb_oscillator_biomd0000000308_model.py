# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tyson2003_NegFB_Oscillator."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tyson2003NegfbOscillatorBiomd0000000308Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tyson2003_NegFB_Oscillator."""

    _SBML_ID = 'BIOMD0000000308'
    _TITLE = 'Tyson2003_NegFB_Oscillator'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Rp', 'X', 'Yp', 'S', 'Y', 'R']
    _SPECIES_LABELS = {'Rp': 'Rp', 'X': 'X', 'Yp': 'Yp', 'S': 'S', 'Y': 'Y', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_yp': ('Yp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Yp`.'), 'initial_model_state_rp': ('Rp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rp`.'), 'initial_model_state_y': ('Y', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_x': ('X', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_model_state_s': ('S', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_r': ('R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.')}
    _HEADLINE_OUTPUTS = {'model_state_yp': ('Yp', 'native SBML value', 'Yp. Maps to SBML symbol `Yp`.'), 'model_state_rp': ('Rp', 'native SBML value', 'Rp. Maps to SBML symbol `Rp`.'), 'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_r': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000308.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
