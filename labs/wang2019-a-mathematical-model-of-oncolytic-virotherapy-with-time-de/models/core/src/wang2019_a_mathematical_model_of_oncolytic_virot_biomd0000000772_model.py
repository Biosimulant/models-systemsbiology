# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wang2019 - A mathematical model of oncolytic virotherapy with time delay."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wang2019AMathematicalModelOfOncolyticVirotBiomd0000000772Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wang2019 - A mathematical model of oncolytic virotherapy with time delay."""

    _SBML_ID = 'BIOMD0000000772'
    _TITLE = 'Wang2019 - A mathematical model of oncolytic virotherapy with time delay'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'I', 'y', 'z']
    _SPECIES_LABELS = {'x': 'x', 'I': 'I', 'y': 'y', 'z': 'z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y': ('y', 800.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`.'), 'initial_model_state_x': ('x', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.'), 'initial_model_state_z': ('z', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.'), 'initial_model_state_i': ('I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'model_state_y': ('y', 'native SBML value', 'y. Maps to SBML symbol `y`.'), 'model_state_x': ('x', 'native SBML value', 'x. Maps to SBML symbol `x`.'), 'model_state_z': ('z', 'native SBML value', 'z. Maps to SBML symbol `z`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000772.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
