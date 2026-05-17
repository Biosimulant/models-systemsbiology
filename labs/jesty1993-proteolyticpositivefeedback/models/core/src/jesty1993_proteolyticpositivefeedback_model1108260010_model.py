# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Jesty1993_ProteolyticPositiveFeedback."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jesty1993ProteolyticpositivefeedbackModel1108260010Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Jesty1993_ProteolyticPositiveFeedback."""

    _SBML_ID = 'MODEL1108260010'
    _TITLE = 'Jesty1993_ProteolyticPositiveFeedback'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Z1', 'Z2', 'E1', 'E2']
    _SPECIES_LABELS = {'Z1': 'Z1', 'Z2': 'Z2', 'E1': 'E1', 'E2': 'E2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_z2': ('Z2', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z2`.'), 'initial_model_state_z1': ('Z1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z1`.'), 'initial_model_state_e2': ('E2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2`.'), 'initial_model_state_e1': ('E1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E1`.')}
    _HEADLINE_OUTPUTS = {'model_state_z2': ('Z2', 'native SBML value', 'Z2. Maps to SBML symbol `Z2`.'), 'model_state_z1': ('Z1', 'native SBML value', 'Z1. Maps to SBML symbol `Z1`.'), 'model_state_e2': ('E2', 'native SBML value', 'E2. Maps to SBML symbol `E2`.'), 'model_state_e1': ('E1', 'native SBML value', 'E1. Maps to SBML symbol `E1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1108260010.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
