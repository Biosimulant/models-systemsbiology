# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ratushny2012_SPF."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ratushny2012SpfBiomd0000000418Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ratushny2012_SPF."""

    _SBML_ID = 'BIOMD0000000418'
    _TITLE = 'Ratushny2012_SPF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P']
    _SPECIES_LABELS = {'P': 'P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p': ('P', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000418.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
