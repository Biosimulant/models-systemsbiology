# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Smallbone2015 - Michaelis Menten."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2015MichaelisMentenModel1503180002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Smallbone2015 - Michaelis Menten."""

    _SBML_ID = 'MODEL1503180002'
    _TITLE = 'Smallbone2015 - Michaelis Menten'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'E', 'ES', 'P']
    _SPECIES_LABELS = {'S': 'S', 'E': 'E', 'ES': 'ES', 'P': 'P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_es': ('ES', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ES`.'), 'initial_model_state_s': ('S', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_e': ('E', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.'), 'initial_model_state_p': ('P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'model_state_es': ('ES', 'native SBML value', 'ES. Maps to SBML symbol `ES`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_e': ('E', 'native SBML value', 'E. Maps to SBML symbol `E`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1503180002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
