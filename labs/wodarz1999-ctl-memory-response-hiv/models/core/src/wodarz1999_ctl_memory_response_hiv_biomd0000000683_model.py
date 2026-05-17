# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wodarz1999 CTL memory response HIV."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz1999CtlMemoryResponseHivBiomd0000000683Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wodarz1999 CTL memory response HIV."""

    _SBML_ID = 'BIOMD0000000683'
    _TITLE = 'Wodarz1999 CTL memory response HIV'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['w', 'x', 'y', 'z']
    _SPECIES_LABELS = {'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x': ('x', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.'), 'initial_model_state_y': ('y', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`.'), 'initial_model_state_w': ('w', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `w`.'), 'initial_model_state_z': ('z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.')}
    _HEADLINE_OUTPUTS = {'model_state_x': ('x', 'native SBML value', 'x. Maps to SBML symbol `x`.'), 'model_state_y': ('y', 'native SBML value', 'y. Maps to SBML symbol `y`.'), 'model_state_w': ('w', 'native SBML value', 'w. Maps to SBML symbol `w`.'), 'model_state_z': ('z', 'native SBML value', 'z. Maps to SBML symbol `z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000683.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
