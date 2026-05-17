# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Qu2017 - A mumps model with seasonal fluctuations in China."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Qu2017AMumpsModelWithSeasonalFluctuationsModel1808280011Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Qu2017 - A mumps model with seasonal fluctuations in China."""

    _SBML_ID = 'MODEL1808280011'
    _TITLE = 'Qu2017 - A mumps model with seasonal fluctuations in China'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'V', 'E', 'I', 'L', 'H', 'R', 'N']
    _SPECIES_LABELS = {'S': 'S', 'V': 'V', 'E': 'E', 'I': 'I', 'L': 'L', 'H': 'H', 'R': 'R', 'N': 'N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_n': ('N', 374.565585, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.'), 'initial_model_state_s': ('S', 370.21, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_r': ('R', 4.0217, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.'), 'initial_model_state_i': ('I', 0.12245, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_model_state_l': ('L', 0.072075, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_model_state_e': ('E', 0.055003, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.')}
    _HEADLINE_OUTPUTS = {'model_state_n': ('N', 'native SBML value', 'N. Maps to SBML symbol `N`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_r': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'model_state_l': ('L', 'native SBML value', 'L. Maps to SBML symbol `L`.'), 'model_state_e': ('E', 'native SBML value', 'E. Maps to SBML symbol `E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808280011.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
