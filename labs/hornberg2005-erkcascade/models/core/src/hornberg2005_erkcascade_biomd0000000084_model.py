# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Hornberg2005_ERKcascade."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hornberg2005ErkcascadeBiomd0000000084Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Hornberg2005_ERKcascade."""

    _SBML_ID = 'BIOMD0000000084'
    _TITLE = 'Hornberg2005_ERKcascade'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'Rin', 'x1', 'x1p', 'x2', 'x2p', 'x3', 'x3p']
    _SPECIES_LABELS = {'R': 'R', 'Rin': 'Rin', 'x1': 'X1', 'x1p': 'X1P', 'x2': 'X2', 'x2p': 'X2P', 'x3': 'X3', 'x3p': 'X3P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x3': ('x3', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_model_state_x2': ('x2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2`.'), 'initial_model_state_x1': ('x1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_x3_p': ('x3p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3p`.'), 'initial_x2_p': ('x2p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2p`.'), 'initial_x1_p': ('x1p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1p`.')}
    _HEADLINE_OUTPUTS = {'model_state_x3': ('x3', 'native SBML value', 'X3. Maps to SBML symbol `x3`.'), 'model_state_x2': ('x2', 'native SBML value', 'X2. Maps to SBML symbol `x2`.'), 'model_state_x1': ('x1', 'native SBML value', 'X1. Maps to SBML symbol `x1`.'), 'x3_p': ('x3p', 'native SBML value', 'X3P. Maps to SBML symbol `x3p`.'), 'x2_p': ('x2p', 'native SBML value', 'X2P. Maps to SBML symbol `x2p`.'), 'x1_p': ('x1p', 'native SBML value', 'X1P. Maps to SBML symbol `x1p`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000084.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
