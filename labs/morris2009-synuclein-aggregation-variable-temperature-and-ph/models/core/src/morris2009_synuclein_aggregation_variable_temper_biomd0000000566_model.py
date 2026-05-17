# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Morris2009 - α-Synuclein aggregation variable temperature and pH."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Morris2009SynucleinAggregationVariableTemperBiomd0000000566Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Morris2009 - α-Synuclein aggregation variable temperature and pH."""

    _SBML_ID = 'BIOMD0000000566'
    _TITLE = 'Morris2009 - α-Synuclein aggregation variable temperature and pH'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['B', 'A']
    _SPECIES_LABELS = {'B': 'B', 'A': 'A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_a': ('A', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.'), 'initial_model_state_b': ('B', -4.44089209850063e-16, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.')}
    _HEADLINE_OUTPUTS = {'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.'), 'model_state_b': ('B', 'native SBML value', 'B. Maps to SBML symbol `B`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000566.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
