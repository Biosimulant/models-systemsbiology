# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Auer2010 - Correlation between lag time and aggregation rate in protein aggregation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Auer2010CorrelationBetweenLagTimeAndAggregBiomd0000000555Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Auer2010 - Correlation between lag time and aggregation rate in protein aggregation."""

    _SBML_ID = 'BIOMD0000000555'
    _TITLE = 'Auer2010 - Correlation between lag time and aggregation rate in protein aggregation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Amyloid']
    _SPECIES_LABELS = {'Amyloid': 'Amyloid'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_amyloid': ('Amyloid', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Amyloid`.')}
    _HEADLINE_OUTPUTS = {'amyloid': ('Amyloid', 'native SBML value', 'Amyloid. Maps to SBML symbol `Amyloid`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000555.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
