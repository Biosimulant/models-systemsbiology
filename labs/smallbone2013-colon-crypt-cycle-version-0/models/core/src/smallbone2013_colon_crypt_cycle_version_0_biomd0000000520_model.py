# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Smallbone2013 - Colon Crypt cycle - Version 0."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2013ColonCryptCycleVersion0Biomd0000000520Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Smallbone2013 - Colon Crypt cycle - Version 0."""

    _SBML_ID = 'BIOMD0000000520'
    _TITLE = 'Smallbone2013 - Colon Crypt cycle - Version 0'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N0', 'N1', 'N2']
    _SPECIES_LABELS = {'N0': 'N0', 'N1': 'N1', 'N2': 'N2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_n1': ('N1', 43.8146704098797, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N1`.'), 'initial_model_state_n2': ('N2', 27.4558812768926, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N2`.'), 'initial_model_state_n0': ('N0', 1.75444831412765, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N0`.')}
    _HEADLINE_OUTPUTS = {'model_state_n1': ('N1', 'native SBML value', 'N1. Maps to SBML symbol `N1`.'), 'model_state_n2': ('N2', 'native SBML value', 'N2. Maps to SBML symbol `N2`.'), 'model_state_n0': ('N0', 'native SBML value', 'N0. Maps to SBML symbol `N0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000520.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
