# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Komarova2003_BoneRemodeling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Komarova2003BoneremodelingBiomd0000000148Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Komarova2003_BoneRemodeling."""

    _SBML_ID = 'BIOMD0000000148'
    _TITLE = 'Komarova2003_BoneRemodeling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x1_bar', 'x2_bar', 'z', 'y1', 'y2']
    _SPECIES_LABELS = {'x1': 'Osteoclast', 'x2': 'Osteoblast', 'x1_bar': 'Steady state osteoclast', 'x2_bar': 'Steady state osteoblast', 'z': 'Bone mass', 'y1': 'Cells actively resorbing bone', 'y2': 'Cells actively forming bone'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_steady_state_osteoclast': ('x1_bar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1_bar`.'), 'initial_steady_state_osteoblast': ('x2_bar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2_bar`.'), 'initial_osteoblast': ('x2', 212.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2`.'), 'initial_osteoclast': ('x1', 11.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_cells_actively_resorbing_bone': ('y1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y1`.'), 'initial_cells_actively_forming_bone': ('y2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y2`.')}
    _HEADLINE_OUTPUTS = {'steady_state_osteoclast': ('x1_bar', 'native SBML value', 'Steady state osteoclast. Maps to SBML symbol `x1_bar`.'), 'steady_state_osteoblast': ('x2_bar', 'native SBML value', 'Steady state osteoblast. Maps to SBML symbol `x2_bar`.'), 'osteoblast': ('x2', 'native SBML value', 'Osteoblast. Maps to SBML symbol `x2`.'), 'osteoclast': ('x1', 'native SBML value', 'Osteoclast. Maps to SBML symbol `x1`.'), 'cells_actively_resorbing_bone': ('y1', 'native SBML value', 'Cells actively resorbing bone. Maps to SBML symbol `y1`.'), 'cells_actively_forming_bone': ('y2', 'native SBML value', 'Cells actively forming bone. Maps to SBML symbol `y2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000148.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
