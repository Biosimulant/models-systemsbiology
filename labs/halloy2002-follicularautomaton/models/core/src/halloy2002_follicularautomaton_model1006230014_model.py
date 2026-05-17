# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Halloy2002_FollicularAutomaton."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Halloy2002FollicularautomatonModel1006230014Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Halloy2002_FollicularAutomaton."""

    _SBML_ID = 'MODEL1006230014'
    _TITLE = 'Halloy2002_FollicularAutomaton'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['L', 'A', 'T', 'M']
    _SPECIES_LABELS = {'L': 'L', 'A': 'A', 'T': 'T', 'M': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_t': ('T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_m': ('M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.'), 'initial_model_state_l': ('L', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_model_state_a': ('A', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.')}
    _HEADLINE_OUTPUTS = {'model_state_t': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.'), 'model_state_l': ('L', 'native SBML value', 'L. Maps to SBML symbol `L`.'), 'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230014.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
