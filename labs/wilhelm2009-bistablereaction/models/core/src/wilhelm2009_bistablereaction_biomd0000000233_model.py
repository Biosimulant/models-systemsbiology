# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wilhelm2009_BistableReaction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wilhelm2009BistablereactionBiomd0000000233Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wilhelm2009_BistableReaction."""

    _SBML_ID = 'BIOMD0000000233'
    _TITLE = 'Wilhelm2009_BistableReaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'P', 'X', 'Y']
    _SPECIES_LABELS = {'S': 'S', 'P': 'P', 'X': 'X', 'Y': 'Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y': ('Y', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_x': ('X', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_model_state_s': ('S', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_p': ('P', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'model_state_y': ('Y', 'substance', 'Y. Maps to SBML symbol `Y`.'), 'model_state_x': ('X', 'substance', 'X. Maps to SBML symbol `X`.'), 'model_state_s': ('S', 'substance', 'S. Maps to SBML symbol `S`.'), 'model_state_p': ('P', 'substance', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000233.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
