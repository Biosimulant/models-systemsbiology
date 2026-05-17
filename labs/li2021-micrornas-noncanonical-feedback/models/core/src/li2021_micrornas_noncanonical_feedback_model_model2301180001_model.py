# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Li2021-MicroRNAs noncanonical feedback model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Li2021MicrornasNoncanonicalFeedbackModelModel2301180001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Li2021-MicroRNAs noncanonical feedback model."""

    _SBML_ID = 'MODEL2301180001'
    _TITLE = 'Li2021-MicroRNAs noncanonical feedback model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'c1', 'r', 'c2']
    _SPECIES_LABELS = {'R': 'R', 'c1': 'c1', 'r': 'r', 'c2': 'c2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_c2': ('c2', 0.399200613736717, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c2`.'), 'initial_model_state_c1': ('c1', 0.00263388662752573, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c1`.'), 'initial_model_state_r': ('r', 0.263707264821585, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r`.'), 'initial_model_state_r_2': ('R', 0.000919996619981075, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.')}
    _HEADLINE_OUTPUTS = {'model_state_c2': ('c2', 'substance', 'c2. Maps to SBML symbol `c2`.'), 'model_state_c1': ('c1', 'substance', 'c1. Maps to SBML symbol `c1`.'), 'model_state_r': ('r', 'substance', 'r. Maps to SBML symbol `r`.'), 'model_state_r_2': ('R', 'substance', 'R. Maps to SBML symbol `R`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2301180001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
