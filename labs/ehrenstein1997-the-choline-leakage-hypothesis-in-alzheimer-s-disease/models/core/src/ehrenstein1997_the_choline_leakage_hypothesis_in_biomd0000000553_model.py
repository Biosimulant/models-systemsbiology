# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ehrenstein1997 - The choline-leakage hypothesis in Alzheimer's disease."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ehrenstein1997TheCholineLeakageHypothesisInBiomd0000000553Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ehrenstein1997 - The choline-leakage hypothesis in Alzheimer's disease."""

    _SBML_ID = 'BIOMD0000000553'
    _TITLE = "Ehrenstein1997 - The choline-leakage hypothesis in Alzheimer's disease"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['a', 'b', 'aRel']
    _SPECIES_LABELS = {'a': 'a', 'b': 'b', 'aRel': 'aRel'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_a_rel': ('aRel', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `aRel`.'), 'initial_model_state_a': ('a', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a`.'), 'initial_model_state_b': ('b', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `b`.')}
    _HEADLINE_OUTPUTS = {'a_rel': ('aRel', 'native SBML value', 'aRel. Maps to SBML symbol `aRel`.'), 'model_state_a': ('a', 'native SBML value', 'a. Maps to SBML symbol `a`.'), 'model_state_b': ('b', 'native SBML value', 'b. Maps to SBML symbol `b`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000553.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
