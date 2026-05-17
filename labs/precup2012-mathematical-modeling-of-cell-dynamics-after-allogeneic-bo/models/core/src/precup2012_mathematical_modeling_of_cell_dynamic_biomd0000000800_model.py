# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Precup2012 - Mathematical modeling of cell dynamics after allogeneic bone marrow transplantation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Precup2012MathematicalModelingOfCellDynamicBiomd0000000800Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Precup2012 - Mathematical modeling of cell dynamics after allogeneic bone marrow transplantation."""

    _SBML_ID = 'BIOMD0000000800'
    _TITLE = 'Precup2012 - Mathematical modeling of cell dynamics after allogeneic bone marrow transplantation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z']
    _SPECIES_LABELS = {'x': 'x', 'y': 'y', 'z': 'z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_z': ('z', 400000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.'), 'initial_model_state_x': ('x', 200000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.'), 'initial_model_state_y': ('y', 100000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`.')}
    _HEADLINE_OUTPUTS = {'model_state_z': ('z', 'native SBML value', 'z. Maps to SBML symbol `z`.'), 'model_state_x': ('x', 'native SBML value', 'x. Maps to SBML symbol `x`.'), 'model_state_y': ('y', 'native SBML value', 'y. Maps to SBML symbol `y`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000800.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
