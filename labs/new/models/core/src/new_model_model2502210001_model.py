# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for New Model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class NewModelModel2502210001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for New Model."""

    _SBML_ID = 'MODEL2502210001'
    _TITLE = 'New Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    _SPECIES_LABELS = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_a': ('A', 0.999999999999997, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.'), 'initial_model_state_k': ('K', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `K`.'), 'initial_model_state_j': ('J', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `J`.'), 'initial_model_state_i': ('I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_model_state_h': ('H', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`.'), 'initial_model_state_g': ('G', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G`.')}
    _HEADLINE_OUTPUTS = {'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.'), 'model_state_k': ('K', 'native SBML value', 'K. Maps to SBML symbol `K`.'), 'model_state_j': ('J', 'native SBML value', 'J. Maps to SBML symbol `J`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'model_state_h': ('H', 'native SBML value', 'H. Maps to SBML symbol `H`.'), 'model_state_g': ('G', 'native SBML value', 'G. Maps to SBML symbol `G`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2502210001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
