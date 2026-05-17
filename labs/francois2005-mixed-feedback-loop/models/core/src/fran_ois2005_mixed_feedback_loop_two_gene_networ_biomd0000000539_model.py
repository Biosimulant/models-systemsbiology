# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for François2005 - Mixed Feedback Loop (two-gene network)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class FranOis2005MixedFeedbackLoopTwoGeneNetworBiomd0000000539Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for François2005 - Mixed Feedback Loop (two-gene network)."""

    _SBML_ID = 'BIOMD0000000539'
    _TITLE = 'François2005 - Mixed Feedback Loop (two-gene network)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'AgB', 'gB', 'rB', 'B', 'AB']
    _SPECIES_LABELS = {'A': 'A', 'AgB': 'AgB', 'gB': 'gB', 'rB': 'rB', 'B': 'B', 'AB': 'AB'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_g_b': ('gB', 1.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `gB`.'), 'initial_model_state_r_b': ('rB', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rB`.'), 'initial_ag_b': ('AgB', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AgB`.'), 'initial_model_state_ab': ('AB', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AB`.'), 'initial_model_state_a': ('A', 40.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.'), 'initial_model_state_b': ('B', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.')}
    _HEADLINE_OUTPUTS = {'g_b': ('gB', 'mole', 'gB. Maps to SBML symbol `gB`.'), 'r_b': ('rB', 'mole', 'rB. Maps to SBML symbol `rB`.'), 'ag_b': ('AgB', 'mole', 'AgB. Maps to SBML symbol `AgB`.'), 'model_state_ab': ('AB', 'mole', 'AB. Maps to SBML symbol `AB`.'), 'model_state_a': ('A', 'mole', 'A. Maps to SBML symbol `A`.'), 'model_state_b': ('B', 'mole', 'B. Maps to SBML symbol `B`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000539.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
