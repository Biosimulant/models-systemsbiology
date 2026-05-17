# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tyson1999_CircClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tyson1999CircclockBiomd0000000036Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tyson1999_CircClock."""

    _SBML_ID = 'BIOMD0000000036'
    _TITLE = 'Tyson1999_CircClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EmptySet', 'M', 'P']
    _SPECIES_LABELS = {'EmptySet': 'EmptySet', 'M': 'M', 'P': 'Pt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pt': ('P', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_empty_set': ('EmptySet', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EmptySet`.'), 'initial_model_state_m': ('M', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_pt': ('P', 'native SBML value', 'Pt. Maps to SBML symbol `P`.'), 'empty_set': ('EmptySet', 'native SBML value', 'EmptySet. Maps to SBML symbol `EmptySet`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000036.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
