# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte response."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2007CytomegalovirusInfectionModelWithBiomd0000000687Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte response."""

    _SBML_ID = 'BIOMD0000000687'
    _TITLE = 'Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_0', 'y_0', 'y_1', 'L_0', 'v_0', 'z_a', 'm_0_0', 'm_1_0', 'm_2_0', 'm_3_0', 'm_4_0', 'm_5_0', 'm_6_0', 'm_7_0', 'm_8_0']
    _SPECIES_LABELS = {'x_0': 'x', 'y_0': 'y_0', 'y_1': 'y_1', 'L_0': 'L', 'v_0': 'v', 'z_a': 'z_a', 'm_0_0': 'm_0', 'm_1_0': 'm_1', 'm_2_0': 'm_2', 'm_3_0': 'm_3', 'm_4_0': 'm_4', 'm_5_0': 'm_5', 'm_6_0': 'm_6', 'm_7_0': 'm_7', 'm_8_0': 'm_8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_z_a': ('z_a', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z_a`.'), 'initial_model_state_x': ('x_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x_0`.'), 'initial_model_state_v': ('v_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `v_0`.'), 'initial_model_state_m_0': ('m_0_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m_0_0`.'), 'initial_model_state_y_1': ('y_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_1`.'), 'initial_model_state_y_0': ('y_0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_0`.')}
    _HEADLINE_OUTPUTS = {'z_a': ('z_a', 'native SBML value', 'z_a. Maps to SBML symbol `z_a`.'), 'model_state_x': ('x_0', 'native SBML value', 'x. Maps to SBML symbol `x_0`.'), 'model_state_v': ('v_0', 'native SBML value', 'v. Maps to SBML symbol `v_0`.'), 'm_0': ('m_0_0', 'native SBML value', 'm_0. Maps to SBML symbol `m_0_0`.'), 'y_1': ('y_1', 'native SBML value', 'y_1. Maps to SBML symbol `y_1`.'), 'y_0': ('y_0', 'native SBML value', 'y_0. Maps to SBML symbol `y_0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000687.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
