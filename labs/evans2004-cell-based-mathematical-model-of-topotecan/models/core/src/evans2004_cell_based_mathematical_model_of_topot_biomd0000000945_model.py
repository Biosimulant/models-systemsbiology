# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Evans2004 - Cell based mathematical model of topotecan."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Evans2004CellBasedMathematicalModelOfTopotBiomd0000000945Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Evans2004 - Cell based mathematical model of topotecan."""

    _SBML_ID = 'BIOMD0000000945'
    _TITLE = 'Evans2004 - Cell based mathematical model of topotecan'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L_m', 'H_m', 'L_c', 'H_c', 'L_n']
    _SPECIES_LABELS = {'L_m': 'L_m', 'H_m': 'H_m', 'L_c': 'L_c', 'H_c': 'H_c', 'L_n': 'L_n'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_l_m': ('L_m', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L_m`.'), 'initial_model_state_l_n': ('L_n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L_n`.'), 'initial_model_state_l_c': ('L_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L_c`.'), 'initial_model_state_h_m': ('H_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H_m`.'), 'initial_model_state_h_c': ('H_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H_c`.')}
    _HEADLINE_OUTPUTS = {'l_m': ('L_m', 'native SBML value', 'L_m. Maps to SBML symbol `L_m`.'), 'l_n': ('L_n', 'native SBML value', 'L_n. Maps to SBML symbol `L_n`.'), 'l_c': ('L_c', 'native SBML value', 'L_c. Maps to SBML symbol `L_c`.'), 'h_m': ('H_m', 'native SBML value', 'H_m. Maps to SBML symbol `H_m`.'), 'h_c': ('H_c', 'native SBML value', 'H_c. Maps to SBML symbol `H_c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000945.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
