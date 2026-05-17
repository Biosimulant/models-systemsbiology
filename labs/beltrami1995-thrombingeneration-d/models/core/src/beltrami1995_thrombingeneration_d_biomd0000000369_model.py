# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Beltrami1995_ThrombinGeneration_D."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Beltrami1995ThrombingenerationDBiomd0000000369Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Beltrami1995_ThrombinGeneration_D."""

    _SBML_ID = 'BIOMD0000000369'
    _TITLE = 'Beltrami1995_ThrombinGeneration_D'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Z1', 'Z2', 'Z4', 'E1', 'E2', 'E3', 'E4']
    _SPECIES_LABELS = {'Z1': 'Z1', 'Z2': 'Z2', 'Z4': 'Z4', 'E1': 'E1', 'E2': 'E2', 'E3': 'E3', 'E4': 'E4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_z4': ('Z4', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z4`.'), 'initial_model_state_z2': ('Z2', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z2`.'), 'initial_model_state_z1': ('Z1', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z1`.'), 'initial_model_state_e4': ('E4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E4`.'), 'initial_model_state_e3': ('E3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E3`.'), 'initial_model_state_e2': ('E2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2`.')}
    _HEADLINE_OUTPUTS = {'model_state_z4': ('Z4', 'native SBML value', 'Z4. Maps to SBML symbol `Z4`.'), 'model_state_z2': ('Z2', 'native SBML value', 'Z2. Maps to SBML symbol `Z2`.'), 'model_state_z1': ('Z1', 'native SBML value', 'Z1. Maps to SBML symbol `Z1`.'), 'model_state_e4': ('E4', 'native SBML value', 'E4. Maps to SBML symbol `E4`.'), 'model_state_e3': ('E3', 'native SBML value', 'E3. Maps to SBML symbol `E3`.'), 'model_state_e2': ('E2', 'native SBML value', 'E2. Maps to SBML symbol `E2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000369.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
