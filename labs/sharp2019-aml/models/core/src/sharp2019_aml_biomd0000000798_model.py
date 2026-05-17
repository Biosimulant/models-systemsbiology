# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sharp2019 - AML."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sharp2019AmlBiomd0000000798Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sharp2019 - AML."""

    _SBML_ID = 'BIOMD0000000798'
    _TITLE = 'Sharp2019 - AML'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'A', 'D', 'L', 'T']
    _SPECIES_LABELS = {'S': 'S', 'A': 'A', 'D': 'D', 'L': 'L', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_s': ('S', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_l': ('L', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_model_state_t': ('T', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_d': ('D', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `D`.'), 'initial_model_state_a': ('A', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.')}
    _HEADLINE_OUTPUTS = {'model_state_s': ('S', 'substance', 'S. Maps to SBML symbol `S`.'), 'model_state_l': ('L', 'substance', 'L. Maps to SBML symbol `L`.'), 'model_state_t': ('T', 'substance', 'T. Maps to SBML symbol `T`.'), 'model_state_d': ('D', 'substance', 'D. Maps to SBML symbol `D`.'), 'model_state_a': ('A', 'substance', 'A. Maps to SBML symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000798.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
