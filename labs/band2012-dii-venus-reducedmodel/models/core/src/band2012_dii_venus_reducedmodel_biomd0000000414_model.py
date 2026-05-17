# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Band2012_DII-Venus_ReducedModel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Band2012DiiVenusReducedmodelBiomd0000000414Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Band2012_DII-Venus_ReducedModel."""

    _SBML_ID = 'BIOMD0000000414'
    _TITLE = 'Band2012_DII-Venus_ReducedModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VENUS']
    _SPECIES_LABELS = {'VENUS': 'VENUS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_venus': ('VENUS', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VENUS`.')}
    _HEADLINE_OUTPUTS = {'venus': ('VENUS', 'native SBML value', 'VENUS. Maps to SBML symbol `VENUS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000414.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
