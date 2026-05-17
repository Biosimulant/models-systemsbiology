# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Plant1981_BurstingNerveCells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Plant1981BurstingnervecellsBiomd0000000304Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Plant1981_BurstingNerveCells."""

    _SBML_ID = 'BIOMD0000000304'
    _TITLE = 'Plant1981_BurstingNerveCells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V_membrane', 'h1', 'x1', 'n1', 'c']
    _SPECIES_LABELS = {'V_membrane': 'V', 'h1': 'h1', 'x1': 'x1', 'n1': 'n1', 'c': 'c'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_v': ('V_membrane', -55.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_model_state_h1': ('h1', 0.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h1`.'), 'initial_model_state_x1': ('x1', 0.27, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_model_state_n1': ('n1', 0.03, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n1`.'), 'initial_model_state_c': ('c', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.')}
    _HEADLINE_OUTPUTS = {'model_state_v': ('V_membrane', 'native SBML value', 'V. Maps to SBML symbol `V_membrane`.'), 'model_state_h1': ('h1', 'native SBML value', 'h1. Maps to SBML symbol `h1`.'), 'model_state_x1': ('x1', 'native SBML value', 'x1. Maps to SBML symbol `x1`.'), 'model_state_n1': ('n1', 'native SBML value', 'n1. Maps to SBML symbol `n1`.'), 'model_state_c': ('c', 'native SBML value', 'c. Maps to SBML symbol `c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000304.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
