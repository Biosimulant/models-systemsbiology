# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Chance1943_Peroxidase_ES_Kinetics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chance1943PeroxidaseEsKineticsBiomd0000000283Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Chance1943_Peroxidase_ES_Kinetics."""

    _SBML_ID = 'BIOMD0000000283'
    _TITLE = 'Chance1943_Peroxidase_ES_Kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'E', 'P', 'Q']
    _SPECIES_LABELS = {'X': 'X', 'E': 'E', 'P': 'P', 'Q': 'Q'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x': ('X', 8.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_model_state_e': ('E', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.'), 'initial_model_state_q': ('Q', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Q`.'), 'initial_model_state_p': ('P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.'), 'model_state_e': ('E', 'native SBML value', 'E. Maps to SBML symbol `E`.'), 'model_state_q': ('Q', 'native SBML value', 'Q. Maps to SBML symbol `Q`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000283.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
