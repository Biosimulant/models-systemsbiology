# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Martinez-Guimera2017 - Generic negative feedforward circuit (Model 5)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class MartinezGuimera2017GenericNegativeFeedforwarModel1710260004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Martinez-Guimera2017 - Generic negative feedforward circuit (Model 5)."""

    _SBML_ID = 'MODEL1710260004'
    _TITLE = 'Martinez-Guimera2017 - Generic negative feedforward circuit (Model 5)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Nil', 'O', 'S', 'A', 'F', 'N', 'R', 'S2']
    _SPECIES_LABELS = {'Nil': 'Nil', 'O': 'O', 'S': 'S', 'A': 'A', 'F': 'F', 'N': 'N', 'R': 'R', 'S2': 'S2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_s2': ('S2', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S2`.'), 'initial_model_state_nil': ('Nil', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nil`.'), 'initial_model_state_s': ('S', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_r': ('R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.'), 'initial_model_state_o': ('O', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O`.'), 'initial_model_state_n': ('N', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.')}
    _HEADLINE_OUTPUTS = {'model_state_s2': ('S2', 'native SBML value', 'S2. Maps to SBML symbol `S2`.'), 'nil': ('Nil', 'native SBML value', 'Nil. Maps to SBML symbol `Nil`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_r': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.'), 'model_state_o': ('O', 'native SBML value', 'O. Maps to SBML symbol `O`.'), 'model_state_n': ('N', 'native SBML value', 'N. Maps to SBML symbol `N`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1710260004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
