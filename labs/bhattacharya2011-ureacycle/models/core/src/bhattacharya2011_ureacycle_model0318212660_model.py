# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bhattacharya2011_UreaCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhattacharya2011UreacycleModel0318212660Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bhattacharya2011_UreaCycle."""

    _SBML_ID = 'MODEL0318212660'
    _TITLE = 'Bhattacharya2011_UreaCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Node1', 'Node2', 'Node3', 'Node4', 'Node6', 'Node7', 'Node8', 'Node9', 'Node10', 'Node11', 'Node12', 'Node13', 'Node14', 'Node15', 'Node0']
    _SPECIES_LABELS = {'Node1': 'Node1', 'Node2': 'Node2', 'Node3': 'Node3', 'Node4': 'Node4', 'Node6': 'Node6', 'Node7': 'Node7', 'Node8': 'Node8', 'Node9': 'Node9', 'Node10': 'Node10', 'Node11': 'Node11', 'Node12': 'Node12', 'Node13': 'Node13', 'Node14': 'Node14', 'Node15': 'Node15', 'Node0': 'Node0'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_node9': ('Node9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node9`.'), 'initial_node8': ('Node8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node8`.'), 'initial_node7': ('Node7', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node7`.'), 'initial_node6': ('Node6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node6`.'), 'initial_node4': ('Node4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node4`.'), 'initial_node3': ('Node3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Node3`.')}
    _HEADLINE_OUTPUTS = {'node9': ('Node9', 'native SBML value', 'Node9. Maps to SBML symbol `Node9`.'), 'node8': ('Node8', 'native SBML value', 'Node8. Maps to SBML symbol `Node8`.'), 'node7': ('Node7', 'native SBML value', 'Node7. Maps to SBML symbol `Node7`.'), 'node6': ('Node6', 'native SBML value', 'Node6. Maps to SBML symbol `Node6`.'), 'node4': ('Node4', 'native SBML value', 'Node4. Maps to SBML symbol `Node4`.'), 'node3': ('Node3', 'native SBML value', 'Node3. Maps to SBML symbol `Node3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0318212660.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
