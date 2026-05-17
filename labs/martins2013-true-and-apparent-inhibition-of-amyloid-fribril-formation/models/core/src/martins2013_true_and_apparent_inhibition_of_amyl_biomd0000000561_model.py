# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Martins2013 - True and apparent inhibition of amyloid fribril formation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Martins2013TrueAndApparentInhibitionOfAmylBiomd0000000561Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Martins2013 - True and apparent inhibition of amyloid fribril formation."""

    _SBML_ID = 'BIOMD0000000561'
    _TITLE = 'Martins2013 - True and apparent inhibition of amyloid fribril formation'
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

    def __init__(self, model_path: str = 'data/BIOMD0000000561.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
