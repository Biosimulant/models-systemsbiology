# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cortes2019 - Optimality of the spontaneous prophage induction rate.."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cortes2019OptimalityOfTheSpontaneousProphagBiomd0000000884Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cortes2019 - Optimality of the spontaneous prophage induction rate.."""

    _SBML_ID = 'BIOMD0000000884'
    _TITLE = 'Cortes2019 - Optimality of the spontaneous prophage induction rate.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'U', 'V']
    _SPECIES_LABELS = {'L': 'L', 'U': 'U', 'V': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_u': ('U', 990000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `U`.'), 'initial_model_state_l': ('L', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_model_state_v': ('V', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'model_state_u': ('U', 'native SBML value', 'U. Maps to SBML symbol `U`.'), 'model_state_l': ('L', 'native SBML value', 'L. Maps to SBML symbol `L`.'), 'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000884.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
