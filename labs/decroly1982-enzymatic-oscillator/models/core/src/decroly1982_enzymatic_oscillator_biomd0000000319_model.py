# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Decroly1982_Enzymatic_Oscillator."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Decroly1982EnzymaticOscillatorBiomd0000000319Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Decroly1982_Enzymatic_Oscillator."""

    _SBML_ID = 'BIOMD0000000319'
    _TITLE = 'Decroly1982_Enzymatic_Oscillator'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['alpha', 'beta', 'gamma']
    _SPECIES_LABELS = {'alpha': 'alpha', 'beta': 'beta', 'gamma': 'gamma'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_beta': ('beta', 188.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta`.'), 'initial_alpha': ('alpha', 29.19988, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha`.'), 'initial_gamma': ('gamma', 0.3367, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'beta': ('beta', 'native SBML value', 'beta. Maps to SBML symbol `beta`.'), 'alpha': ('alpha', 'native SBML value', 'alpha. Maps to SBML symbol `alpha`.'), 'gamma': ('gamma', 'native SBML value', 'gamma. Maps to SBML symbol `gamma`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000319.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
