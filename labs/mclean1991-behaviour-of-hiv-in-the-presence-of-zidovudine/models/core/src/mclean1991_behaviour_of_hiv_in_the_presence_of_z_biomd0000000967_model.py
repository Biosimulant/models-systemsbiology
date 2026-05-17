# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for McLean1991 - Behaviour of HIV in the presence of zidovudine."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mclean1991BehaviourOfHivInThePresenceOfZBiomd0000000967Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for McLean1991 - Behaviour of HIV in the presence of zidovudine."""

    _SBML_ID = 'BIOMD0000000967'
    _TITLE = 'McLean1991 - Behaviour of HIV in the presence of zidovudine'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'L', 'E', 'V']
    _SPECIES_LABELS = {'R': 'R', 'L': 'L', 'E': 'E', 'V': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_r': ('R', 100000000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.'), 'initial_model_state_v': ('V', 7000000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_model_state_l': ('L', 1000000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_model_state_e': ('E', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.')}
    _HEADLINE_OUTPUTS = {'model_state_r': ('R', 'substance', 'R. Maps to SBML symbol `R`.'), 'model_state_v': ('V', 'substance', 'V. Maps to SBML symbol `V`.'), 'model_state_l': ('L', 'substance', 'L. Maps to SBML symbol `L`.'), 'model_state_e': ('E', 'substance', 'E. Maps to SBML symbol `E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000967.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
