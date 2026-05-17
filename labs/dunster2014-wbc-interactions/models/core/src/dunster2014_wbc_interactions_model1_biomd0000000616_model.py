# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Dunster2014 - WBC Interactions (Model1)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dunster2014WbcInteractionsModel1Biomd0000000616Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Dunster2014 - WBC Interactions (Model1)."""

    _SBML_ID = 'BIOMD0000000616'
    _TITLE = 'Dunster2014 - WBC Interactions (Model1)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['n', 'c', 'a', 'm']
    _SPECIES_LABELS = {'n': 'n', 'c': 'c', 'a': 'a', 'm': 'm'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_n': ('n', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.'), 'initial_model_state_m': ('m', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m`.'), 'initial_model_state_c': ('c', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.'), 'initial_model_state_a': ('a', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a`.')}
    _HEADLINE_OUTPUTS = {'model_state_n': ('n', 'mole', 'n. Maps to SBML symbol `n`.'), 'model_state_m': ('m', 'mole', 'm. Maps to SBML symbol `m`.'), 'model_state_c': ('c', 'mole', 'c. Maps to SBML symbol `c`.'), 'model_state_a': ('a', 'mole', 'a. Maps to SBML symbol `a`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000616.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
