# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cao2013 - Application of ABSIS method in the reversible isomerization model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2013ApplicationOfAbsisMethodInTheReverBiomd0000000486Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cao2013 - Application of ABSIS method in the reversible isomerization model."""

    _SBML_ID = 'BIOMD0000000486'
    _TITLE = 'Cao2013 - Application of ABSIS method in the reversible isomerization model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'B']
    _SPECIES_LABELS = {'A': 'A', 'B': 'B'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_b': ('B', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.'), 'initial_model_state_a': ('A', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.')}
    _HEADLINE_OUTPUTS = {'model_state_b': ('B', 'native SBML value', 'B. Maps to SBML symbol `B`.'), 'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000486.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
