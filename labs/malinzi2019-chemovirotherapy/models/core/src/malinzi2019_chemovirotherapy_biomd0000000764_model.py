# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Malinzi2019 - chemovirotherapy."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Malinzi2019ChemovirotherapyBiomd0000000764Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Malinzi2019 - chemovirotherapy."""

    _SBML_ID = 'BIOMD0000000764'
    _TITLE = 'Malinzi2019 - chemovirotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V', 'C']
    _SPECIES_LABELS = {'U': 'U', 'I': 'I', 'V': 'V', 'C': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_u': ('U', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `U`.'), 'initial_model_state_v': ('V', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_model_state_c': ('C', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`.'), 'initial_model_state_i': ('I', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'model_state_u': ('U', 'substance', 'U. Maps to SBML symbol `U`.'), 'model_state_v': ('V', 'substance', 'V. Maps to SBML symbol `V`.'), 'model_state_c': ('C', 'substance', 'C. Maps to SBML symbol `C`.'), 'model_state_i': ('I', 'substance', 'I. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000764.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
