# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wang2016/2 - oncolytic efficacy of M1 virus-SNT model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wang20162OncolyticEfficacyOfM1VirusSntMoBiomd0000000781Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wang2016/2 - oncolytic efficacy of M1 virus-SNT model."""

    _SBML_ID = 'BIOMD0000000781'
    _TITLE = 'Wang2016/2 - oncolytic efficacy of M1 virus-SNT model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'N', 'T']
    _SPECIES_LABELS = {'S': 'S', 'N': 'N', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_n': ('N', 0.2, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.'), 'initial_model_state_t': ('T', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_s': ('S', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.')}
    _HEADLINE_OUTPUTS = {'model_state_n': ('N', 'substance', 'N. Maps to SBML symbol `N`.'), 'model_state_t': ('T', 'substance', 'T. Maps to SBML symbol `T`.'), 'model_state_s': ('S', 'substance', 'S. Maps to SBML symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000781.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
