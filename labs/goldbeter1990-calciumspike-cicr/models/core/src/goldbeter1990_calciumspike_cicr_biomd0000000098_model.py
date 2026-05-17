# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Goldbeter1990_CalciumSpike_CICR."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter1990CalciumspikeCicrBiomd0000000098Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Goldbeter1990_CalciumSpike_CICR."""

    _SBML_ID = 'BIOMD0000000098'
    _TITLE = 'Goldbeter1990_CalciumSpike_CICR'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Z', 'Y']
    _SPECIES_LABELS = {'Z': 'Z', 'Y': 'Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y': ('Y', 1.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_z': ('Z', 0.15, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.')}
    _HEADLINE_OUTPUTS = {'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.'), 'model_state_z': ('Z', 'native SBML value', 'Z. Maps to SBML symbol `Z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000098.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
