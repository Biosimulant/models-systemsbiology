# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wang2016/1 - oncolytic efficacy of M1 virus-SNTM model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wang20161OncolyticEfficacyOfM1VirusSntmMBiomd0000000780Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wang2016/1 - oncolytic efficacy of M1 virus-SNTM model."""

    _SBML_ID = 'BIOMD0000000780'
    _TITLE = 'Wang2016/1 - oncolytic efficacy of M1 virus-SNTM model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'N', 'T', 'M']
    _SPECIES_LABELS = {'S': 'S', 'N': 'N', 'T': 'T', 'M': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_n': ('N', 0.2, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.'), 'initial_model_state_t': ('T', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_s': ('S', 0.1, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_m': ('M', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_n': ('N', 'substance', 'N. Maps to SBML symbol `N`.'), 'model_state_t': ('T', 'substance', 'T. Maps to SBML symbol `T`.'), 'model_state_s': ('S', 'substance', 'S. Maps to SBML symbol `S`.'), 'model_state_m': ('M', 'substance', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000780.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
