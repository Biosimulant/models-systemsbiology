# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cao2013 - Application of ABSIS method in the bistable Schlögl model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2013ApplicationOfAbsisMethodInTheBistaBiomd0000000485Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cao2013 - Application of ABSIS method in the bistable Schlögl model."""

    _SBML_ID = 'BIOMD0000000485'
    _TITLE = 'Cao2013 - Application of ABSIS method in the bistable Schlögl model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'ES']
    _SPECIES_LABELS = {'X': 'X', 'ES': 'ES'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_es': ('ES', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ES`.'), 'initial_model_state_x': ('X', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.')}
    _HEADLINE_OUTPUTS = {'model_state_es': ('ES', 'native SBML value', 'ES. Maps to SBML symbol `ES`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000485.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
