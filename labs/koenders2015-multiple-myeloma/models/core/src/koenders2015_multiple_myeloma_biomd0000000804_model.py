# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Koenders2015 - multiple myeloma."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koenders2015MultipleMyelomaBiomd0000000804Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Koenders2015 - multiple myeloma."""

    _SBML_ID = 'BIOMD0000000804'
    _TITLE = 'Koenders2015 - multiple myeloma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'B', 'T']
    _SPECIES_LABELS = {'C': 'C', 'B': 'B', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_b': ('B', 208.00838230519, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.'), 'initial_model_state_t': ('T', 10.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_c': ('C', 1.14404610267855, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`.')}
    _HEADLINE_OUTPUTS = {'model_state_b': ('B', 'substance', 'B. Maps to SBML symbol `B`.'), 'model_state_t': ('T', 'substance', 'T. Maps to SBML symbol `T`.'), 'model_state_c': ('C', 'substance', 'C. Maps to SBML symbol `C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000804.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
