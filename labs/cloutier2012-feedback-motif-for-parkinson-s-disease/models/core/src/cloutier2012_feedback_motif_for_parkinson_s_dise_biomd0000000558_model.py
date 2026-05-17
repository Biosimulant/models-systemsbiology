# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cloutier2012 - Feedback motif for Parkinson's disease."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cloutier2012FeedbackMotifForParkinsonSDiseBiomd0000000558Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cloutier2012 - Feedback motif for Parkinson's disease."""

    _SBML_ID = 'BIOMD0000000558'
    _TITLE = "Cloutier2012 - Feedback motif for Parkinson's disease"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ROS', 'alpha_syn']
    _SPECIES_LABELS = {'ROS': 'ROS', 'alpha_syn': 'alpha-syn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha_syn': ('alpha_syn', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha_syn`.'), 'initial_model_state_ros': ('ROS', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ROS`.')}
    _HEADLINE_OUTPUTS = {'alpha_syn': ('alpha_syn', 'native SBML value', 'alpha-syn. Maps to SBML symbol `alpha_syn`.'), 'ros': ('ROS', 'native SBML value', 'ROS. Maps to SBML symbol `ROS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000558.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
