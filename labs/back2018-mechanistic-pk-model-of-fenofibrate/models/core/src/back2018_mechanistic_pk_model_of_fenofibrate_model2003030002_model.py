# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Back2018 - Mechanistic PK model of Fenofibrate."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Back2018MechanisticPkModelOfFenofibrateModel2003030002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Back2018 - Mechanistic PK model of Fenofibrate."""

    _SBML_ID = 'MODEL2003030002'
    _TITLE = 'Back2018 - Mechanistic PK model of Fenofibrate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X1', 'X2', 'X3', 'X4', 'X5']
    _SPECIES_LABELS = {'X1': 'X1', 'X2': 'X2', 'X3': 'X3', 'X4': 'X4', 'X5': 'X5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_x1': ('X1', 250.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X1`.'), 'initial_model_state_x3': ('X3', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X3`.'), 'initial_model_state_x2': ('X2', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X2`.'), 'initial_model_state_x5': ('X5', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X5`.'), 'initial_model_state_x4': ('X4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X4`.')}
    _HEADLINE_OUTPUTS = {'model_state_x1': ('X1', 'native SBML value', 'X1. Maps to SBML symbol `X1`.'), 'model_state_x3': ('X3', 'native SBML value', 'X3. Maps to SBML symbol `X3`.'), 'model_state_x2': ('X2', 'native SBML value', 'X2. Maps to SBML symbol `X2`.'), 'model_state_x5': ('X5', 'native SBML value', 'X5. Maps to SBML symbol `X5`.'), 'model_state_x4': ('X4', 'native SBML value', 'X4. Maps to SBML symbol `X4`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003030002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
