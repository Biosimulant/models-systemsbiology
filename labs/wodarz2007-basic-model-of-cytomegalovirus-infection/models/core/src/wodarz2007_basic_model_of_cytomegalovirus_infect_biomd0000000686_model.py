# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wodarz2007 - Basic Model of Cytomegalovirus Infection."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2007BasicModelOfCytomegalovirusInfectBiomd0000000686Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wodarz2007 - Basic Model of Cytomegalovirus Infection."""

    _SBML_ID = 'BIOMD0000000686'
    _TITLE = 'Wodarz2007 - Basic Model of Cytomegalovirus Infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['x', 'y0', 'y1', 'L', 'v']
    _SPECIES_LABELS = {'x': 'X', 'y0': 'Y0', 'y1': 'Y1', 'L': 'L', 'v': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_y1': ('y1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y1`.'), 'initial_model_state_y0': ('y0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y0`.'), 'initial_model_state_x': ('x', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.'), 'initial_model_state_v': ('v', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `v`.'), 'initial_model_state_l': ('L', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.')}
    _HEADLINE_OUTPUTS = {'model_state_y1': ('y1', 'native SBML value', 'Y1. Maps to SBML symbol `y1`.'), 'model_state_y0': ('y0', 'native SBML value', 'Y0. Maps to SBML symbol `y0`.'), 'model_state_x': ('x', 'native SBML value', 'X. Maps to SBML symbol `x`.'), 'model_state_v': ('v', 'native SBML value', 'V. Maps to SBML symbol `v`.'), 'model_state_l': ('L', 'native SBML value', 'L. Maps to SBML symbol `L`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000686.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
