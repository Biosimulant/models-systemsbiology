# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Clancy2002_CardiacSodiumChannel_WT."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Clancy2002CardiacsodiumchannelWtBiomd0000000126Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Clancy2002_CardiacSodiumChannel_WT."""

    _SBML_ID = 'BIOMD0000000126'
    _TITLE = 'Clancy2002_CardiacSodiumChannel_WT'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C1', 'C2', 'C3', 'IC3', 'IC2', 'IM1', 'IM2', 'O', 'IF']
    _SPECIES_LABELS = {'C1': 'C1', 'C2': 'C2', 'C3': 'C3', 'IC3': 'IC3', 'IC2': 'IC2', 'IM1': 'IM1', 'IM2': 'IM2', 'O': 'open states', 'IF': 'IF'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_open_states': ('O', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O`.'), 'initial_model_state_c3': ('C3', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C3`.'), 'initial_model_state_im2': ('IM2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IM2`.'), 'initial_model_state_im1': ('IM1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IM1`.'), 'initial_if_value': ('IF', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IF`.'), 'initial_model_state_ic3': ('IC3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IC3`.')}
    _HEADLINE_OUTPUTS = {'open_states': ('O', 'native SBML value', 'open states. Maps to SBML symbol `O`.'), 'model_state_c3': ('C3', 'native SBML value', 'C3. Maps to SBML symbol `C3`.'), 'im2': ('IM2', 'native SBML value', 'IM2. Maps to SBML symbol `IM2`.'), 'im1': ('IM1', 'native SBML value', 'IM1. Maps to SBML symbol `IM1`.'), 'if_value': ('IF', 'native SBML value', 'IF. Maps to SBML symbol `IF`.'), 'ic3': ('IC3', 'native SBML value', 'IC3. Maps to SBML symbol `IC3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000126.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
