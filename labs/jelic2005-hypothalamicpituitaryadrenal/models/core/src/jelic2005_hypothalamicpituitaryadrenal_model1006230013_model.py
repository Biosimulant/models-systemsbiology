# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Jelic2005_HypothalamicPituitaryAdrenal."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jelic2005HypothalamicpituitaryadrenalModel1006230013Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Jelic2005_HypothalamicPituitaryAdrenal."""

    _SBML_ID = 'MODEL1006230013'
    _TITLE = 'Jelic2005_HypothalamicPituitaryAdrenal'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['a', 'g']
    _SPECIES_LABELS = {'a': 'A', 'g': 'G'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_g': ('g', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `g`.'), 'initial_model_state_a': ('a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a`.')}
    _HEADLINE_OUTPUTS = {'model_state_g': ('g', 'native SBML value', 'G. Maps to SBML symbol `g`.'), 'model_state_a': ('a', 'native SBML value', 'A. Maps to SBML symbol `a`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230013.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
