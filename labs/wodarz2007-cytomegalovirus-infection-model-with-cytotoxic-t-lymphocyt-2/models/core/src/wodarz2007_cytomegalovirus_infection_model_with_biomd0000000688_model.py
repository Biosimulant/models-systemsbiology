# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte and natural killer cell response."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2007CytomegalovirusInfectionModelWithBiomd0000000688Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte and natural killer cell response."""

    _SBML_ID = 'BIOMD0000000688'
    _TITLE = 'Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte and natural killer cell response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y_0', 'y_1', 'L', 'v', 'z_a', 'm_0', 'm_1', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'z_i']
    _SPECIES_LABELS = {'x': 'x', 'y_0': 'y_0', 'y_1': 'y_1', 'L': 'L', 'v': 'v', 'z_a': 'z_a', 'm_0': 'm_0', 'm_1': 'm_1', 'm_2': 'm_2', 'm_3': 'm_3', 'm_4': 'm_4', 'm_5': 'm_5', 'm_6': 'm_6', 'm_7': 'm_7', 'm_8': 'm_8', 'z_i': 'z_i'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_z_a': ('z_a', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z_a`.'), 'initial_model_state_z_i': ('z_i', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z_i`.'), 'initial_model_state_y_1': ('y_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_1`.'), 'initial_model_state_y_0': ('y_0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_0`.'), 'initial_model_state_m_8': ('m_8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m_8`.'), 'initial_model_state_m_7': ('m_7', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m_7`.')}
    _HEADLINE_OUTPUTS = {'z_a': ('z_a', 'native SBML value', 'z_a. Maps to SBML symbol `z_a`.'), 'z_i': ('z_i', 'native SBML value', 'z_i. Maps to SBML symbol `z_i`.'), 'y_1': ('y_1', 'native SBML value', 'y_1. Maps to SBML symbol `y_1`.'), 'y_0': ('y_0', 'native SBML value', 'y_0. Maps to SBML symbol `y_0`.'), 'm_8': ('m_8', 'native SBML value', 'm_8. Maps to SBML symbol `m_8`.'), 'm_7': ('m_7', 'native SBML value', 'm_7. Maps to SBML symbol `m_7`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000688.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
