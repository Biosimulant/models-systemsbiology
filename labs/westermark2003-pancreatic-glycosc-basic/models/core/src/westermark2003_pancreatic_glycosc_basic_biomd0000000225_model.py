# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Westermark2003_Pancreatic_GlycOsc_basic."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Westermark2003PancreaticGlycoscBasicBiomd0000000225Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Westermark2003_Pancreatic_GlycOsc_basic."""

    _SBML_ID = 'BIOMD0000000225'
    _TITLE = 'Westermark2003_Pancreatic_GlycOsc_basic'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLC', 'G6P_F6P', 'F6P', 'FBP', 'G3P']
    _SPECIES_LABELS = {'GLC': 'GLC', 'G6P_F6P': 'G6P_F6P', 'F6P': 'F6P', 'FBP': 'FBP', 'G3P': 'G3P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_g6_p_f6_p': ('G6P_F6P', 3.71728, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6P_F6P`.'), 'initial_model_state_glc': ('GLC', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GLC`.'), 'initial_model_state_fbp': ('FBP', 0.00063612, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FBP`.'), 'initial_g3_p': ('G3P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3P`.'), 'initial_f6_p': ('F6P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `F6P`.')}
    _HEADLINE_OUTPUTS = {'g6_p_f6_p': ('G6P_F6P', 'native SBML value', 'G6P_F6P. Maps to SBML symbol `G6P_F6P`.'), 'glc': ('GLC', 'native SBML value', 'GLC. Maps to SBML symbol `GLC`.'), 'fbp': ('FBP', 'native SBML value', 'FBP. Maps to SBML symbol `FBP`.'), 'g3_p': ('G3P', 'native SBML value', 'G3P. Maps to SBML symbol `G3P`.'), 'f6_p': ('F6P', 'native SBML value', 'F6P. Maps to SBML symbol `F6P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000225.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
