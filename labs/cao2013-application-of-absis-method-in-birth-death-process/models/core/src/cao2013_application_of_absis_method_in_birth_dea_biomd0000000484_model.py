# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cao2013 - Application of ABSIS method in birth-death process."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2013ApplicationOfAbsisMethodInBirthDeaBiomd0000000484Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cao2013 - Application of ABSIS method in birth-death process."""

    _SBML_ID = 'BIOMD0000000484'
    _TITLE = 'Cao2013 - Application of ABSIS method in birth-death process'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'ES']
    _SPECIES_LABELS = {'S': 'S', 'ES': 'ES'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_es': ('ES', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ES`.'), 'initial_model_state_s': ('S', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.')}
    _HEADLINE_OUTPUTS = {'model_state_es': ('ES', 'native SBML value', 'ES. Maps to SBML symbol `ES`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000484.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
