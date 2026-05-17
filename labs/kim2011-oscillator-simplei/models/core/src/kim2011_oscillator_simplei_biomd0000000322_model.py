# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kim2011_Oscillator_SimpleI."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2011OscillatorSimpleiBiomd0000000322Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kim2011_Oscillator_SimpleI."""

    _SBML_ID = 'BIOMD0000000322'
    _TITLE = 'Kim2011_Oscillator_SimpleI'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4']
    _SPECIES_LABELS = {'species_1': 'x', 'species_2': 'y', 'species_3': 'u', 'species_4': 'v'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y': ('species_2', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.'), 'initial_model_state_x': ('species_1', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_model_state_v': ('species_4', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_model_state_u': ('species_3', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.')}
    _HEADLINE_OUTPUTS = {'model_state_y': ('species_2', 'native SBML value', 'y. Maps to SBML symbol `species_2`.'), 'model_state_x': ('species_1', 'native SBML value', 'x. Maps to SBML symbol `species_1`.'), 'model_state_v': ('species_4', 'native SBML value', 'v. Maps to SBML symbol `species_4`.'), 'model_state_u': ('species_3', 'native SBML value', 'u. Maps to SBML symbol `species_3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000322.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
