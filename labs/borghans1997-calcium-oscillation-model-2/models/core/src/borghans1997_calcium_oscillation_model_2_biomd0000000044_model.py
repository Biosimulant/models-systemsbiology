# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Borghans1997 - Calcium Oscillation - Model 2."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Borghans1997CalciumOscillationModel2Biomd0000000044Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Borghans1997 - Calcium Oscillation - Model 2."""

    _SBML_ID = 'BIOMD0000000044'
    _TITLE = 'Borghans1997 - Calcium Oscillation - Model 2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EC', 'Z', 'A', 'Y']
    _SPECIES_LABELS = {'EC': 'EC', 'Z': 'Z', 'A': 'A', 'Y': 'Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ec': ('EC', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`.'), 'initial_model_state_a': ('A', 0.45, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.'), 'initial_model_state_y': ('Y', 0.36, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_z': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.')}
    _HEADLINE_OUTPUTS = {'model_state_ec': ('EC', 'native SBML value', 'EC. Maps to SBML symbol `EC`.'), 'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.'), 'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.'), 'model_state_z': ('Z', 'native SBML value', 'Z. Maps to SBML symbol `Z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000044.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
