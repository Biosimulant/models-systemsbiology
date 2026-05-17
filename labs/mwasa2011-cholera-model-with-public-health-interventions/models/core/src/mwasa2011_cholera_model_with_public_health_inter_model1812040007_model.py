# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mwasa2011 - Cholera model with public health interventions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mwasa2011CholeraModelWithPublicHealthInterModel1812040007Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mwasa2011 - Cholera model with public health interventions."""

    _SBML_ID = 'MODEL1812040007'
    _TITLE = 'Mwasa2011 - Cholera model with public health interventions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'E', 'V', 'I', 'Q', 'T', 'R', 'B']
    _SPECIES_LABELS = {'S': 'S', 'E': 'E', 'V': 'V', 'I': 'I', 'Q': 'Q', 'T': 'T', 'R': 'R', 'B': 'B'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_b': ('B', 1000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.'), 'initial_model_state_s': ('S', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_e': ('E', 900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.'), 'initial_model_state_v': ('V', 800.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_model_state_i': ('I', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_model_state_q': ('Q', 390.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Q`.')}
    _HEADLINE_OUTPUTS = {'model_state_b': ('B', 'native SBML value', 'B. Maps to SBML symbol `B`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_e': ('E', 'native SBML value', 'E. Maps to SBML symbol `E`.'), 'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'model_state_q': ('Q', 'native SBML value', 'Q. Maps to SBML symbol `Q`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812040007.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
