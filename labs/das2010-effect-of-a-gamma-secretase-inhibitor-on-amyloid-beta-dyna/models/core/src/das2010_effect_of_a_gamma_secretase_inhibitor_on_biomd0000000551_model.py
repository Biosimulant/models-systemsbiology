# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Das2010 - Effect of a gamma-secretase inhibitor on Amyloid-beta dynamics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Das2010EffectOfAGammaSecretaseInhibitorOnBiomd0000000551Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Das2010 - Effect of a gamma-secretase inhibitor on Amyloid-beta dynamics."""

    _SBML_ID = 'BIOMD0000000551'
    _TITLE = 'Das2010 - Effect of a gamma-secretase inhibitor on Amyloid-beta dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'P']
    _SPECIES_LABELS = {'C': 'C', 'P': 'P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p': ('P', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_model_state_c': ('C', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`.')}
    _HEADLINE_OUTPUTS = {'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.'), 'model_state_c': ('C', 'native SBML value', 'C. Maps to SBML symbol `C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000551.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
