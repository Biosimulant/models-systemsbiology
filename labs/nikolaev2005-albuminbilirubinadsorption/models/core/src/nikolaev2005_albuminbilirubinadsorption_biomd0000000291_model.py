# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nikolaev2005_AlbuminBilirubinAdsorption."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nikolaev2005AlbuminbilirubinadsorptionBiomd0000000291Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nikolaev2005_AlbuminBilirubinAdsorption."""

    _SBML_ID = 'BIOMD0000000291'
    _TITLE = 'Nikolaev2005_AlbuminBilirubinAdsorption'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'A0', 'B0', 'C0']
    _SPECIES_LABELS = {'x1': 'AlB', 'x2': 'BC', 'x3': 'AlCn', 'x4': 'AlB2', 'x5': 'Al', 'x6': 'B', 'x7': 'C', 'A0': 'A0', 'B0': 'B0', 'C0': 'C0'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_c': ('x7', 1.174, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x7`.'), 'initial_model_state_al': ('x5', 0.4615385, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x5`.'), 'initial_model_state_b': ('x6', 0.1754386, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x6`.'), 'initial_model_state_bc': ('x2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x2`.'), 'initial_al_cn': ('x3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_al_b2': ('x4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x4`.')}
    _HEADLINE_OUTPUTS = {'model_state_c': ('x7', 'native SBML value', 'C. Maps to SBML symbol `x7`.'), 'model_state_al': ('x5', 'native SBML value', 'Al. Maps to SBML symbol `x5`.'), 'model_state_b': ('x6', 'native SBML value', 'B. Maps to SBML symbol `x6`.'), 'model_state_bc': ('x2', 'native SBML value', 'BC. Maps to SBML symbol `x2`.'), 'al_cn': ('x3', 'native SBML value', 'AlCn. Maps to SBML symbol `x3`.'), 'al_b2': ('x4', 'native SBML value', 'AlB2. Maps to SBML symbol `x4`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000291.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
