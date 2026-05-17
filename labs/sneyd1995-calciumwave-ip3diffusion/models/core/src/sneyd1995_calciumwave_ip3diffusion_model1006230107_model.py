# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sneyd1995_CalciumWave_IP3diffusion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sneyd1995CalciumwaveIp3diffusionModel1006230107Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sneyd1995_CalciumWave_IP3diffusion."""

    _SBML_ID = 'MODEL1006230107'
    _TITLE = 'Sneyd1995_CalciumWave_IP3diffusion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['P', 'c', 'h']
    _SPECIES_LABELS = {'P': 'P', 'c': 'C', 'h': 'H'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p': ('P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_model_state_h': ('h', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h`.'), 'initial_model_state_c': ('c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.')}
    _HEADLINE_OUTPUTS = {'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.'), 'model_state_h': ('h', 'native SBML value', 'H. Maps to SBML symbol `h`.'), 'model_state_c': ('c', 'native SBML value', 'C. Maps to SBML symbol `c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230107.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
