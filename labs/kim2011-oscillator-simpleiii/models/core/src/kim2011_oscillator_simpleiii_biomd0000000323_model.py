# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kim2011_Oscillator_SimpleIII."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2011OscillatorSimpleiiiBiomd0000000323Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kim2011_Oscillator_SimpleIII."""

    _SBML_ID = 'BIOMD0000000323'
    _TITLE = 'Kim2011_Oscillator_SimpleIII'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3']
    _SPECIES_LABELS = {'species_1': 'x1', 'species_2': 'x2', 'species_3': 'x3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x3': ('species_3', 0.33, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_model_state_x2': ('species_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.'), 'initial_model_state_x1': ('species_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.')}
    _HEADLINE_OUTPUTS = {'model_state_x3': ('species_3', 'native SBML value', 'x3. Maps to SBML symbol `species_3`.'), 'model_state_x2': ('species_2', 'native SBML value', 'x2. Maps to SBML symbol `species_2`.'), 'model_state_x1': ('species_1', 'native SBML value', 'x1. Maps to SBML symbol `species_1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000323.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
