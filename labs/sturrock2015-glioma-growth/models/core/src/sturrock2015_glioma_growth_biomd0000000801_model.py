# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sturrock2015 - glioma growth."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sturrock2015GliomaGrowthBiomd0000000801Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sturrock2015 - glioma growth."""

    _SBML_ID = 'BIOMD0000000801'
    _TITLE = 'Sturrock2015 - glioma growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'B', 'I', 'S']
    _SPECIES_LABELS = {'T': 'T', 'B': 'B', 'I': 'I', 'S': 'S'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_t': ('T', 0.14, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_s': ('S', 0.000439, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_b': ('B', 0.000392, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.'), 'initial_model_state_i': ('I', 0.000284, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'model_state_t': ('T', 'substance', 'T. Maps to SBML symbol `T`.'), 'model_state_s': ('S', 'substance', 'S. Maps to SBML symbol `S`.'), 'model_state_b': ('B', 'substance', 'B. Maps to SBML symbol `B`.'), 'model_state_i': ('I', 'substance', 'I. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000801.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
