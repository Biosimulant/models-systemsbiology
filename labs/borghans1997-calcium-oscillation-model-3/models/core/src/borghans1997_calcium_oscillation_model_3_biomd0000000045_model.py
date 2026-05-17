# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Borghans1997 - Calcium Oscillation - Model 3."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Borghans1997CalciumOscillationModel3Biomd0000000045Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Borghans1997 - Calcium Oscillation - Model 3."""

    _SBML_ID = 'BIOMD0000000045'
    _TITLE = 'Borghans1997 - Calcium Oscillation - Model 3'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EC', 'Z', 'Y', 'X']
    _SPECIES_LABELS = {'EC': 'EC', 'Z': 'Z', 'Y': 'Y', 'X': 'X'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ec': ('EC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`.'), 'initial_model_state_x': ('X', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_model_state_z': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.'), 'initial_model_state_y': ('Y', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.')}
    _HEADLINE_OUTPUTS = {'model_state_ec': ('EC', 'native SBML value', 'EC. Maps to SBML symbol `EC`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.'), 'model_state_z': ('Z', 'native SBML value', 'Z. Maps to SBML symbol `Z`.'), 'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000045.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
