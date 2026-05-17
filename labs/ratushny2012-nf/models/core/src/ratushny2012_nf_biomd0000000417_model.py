# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ratushny2012_NF."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ratushny2012NfBiomd0000000417Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ratushny2012_NF."""

    _SBML_ID = 'BIOMD0000000417'
    _TITLE = 'Ratushny2012_NF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Target']
    _SPECIES_LABELS = {'Target': 'Target'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_target': ('Target', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Target`.')}
    _HEADLINE_OUTPUTS = {'target': ('Target', 'native SBML value', 'Target. Maps to SBML symbol `Target`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000417.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
