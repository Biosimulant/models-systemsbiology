# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mittler1998_HIV1_interactingTargetCells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mittler1998Hiv1InteractingtargetcellsModel1006230055Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mittler1998_HIV1_interactingTargetCells."""

    _SBML_ID = 'MODEL1006230055'
    _TITLE = 'Mittler1998_HIV1_interactingTargetCells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['I', 'VI', 'VNI', 'E1', 'E2', 'E3', 'E4']
    _SPECIES_LABELS = {'I': 'I', 'VI': 'VI', 'VNI': 'VNI', 'E1': 'E1', 'E2': 'E2', 'E3': 'E3', 'E4': 'E4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_vni': ('VNI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VNI`.'), 'initial_model_state_vi': ('VI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VI`.'), 'initial_model_state_e4': ('E4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E4`.'), 'initial_model_state_e3': ('E3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E3`.'), 'initial_model_state_e2': ('E2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2`.'), 'initial_model_state_e1': ('E1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E1`.')}
    _HEADLINE_OUTPUTS = {'vni': ('VNI', 'native SBML value', 'VNI. Maps to SBML symbol `VNI`.'), 'model_state_vi': ('VI', 'native SBML value', 'VI. Maps to SBML symbol `VI`.'), 'model_state_e4': ('E4', 'native SBML value', 'E4. Maps to SBML symbol `E4`.'), 'model_state_e3': ('E3', 'native SBML value', 'E3. Maps to SBML symbol `E3`.'), 'model_state_e2': ('E2', 'native SBML value', 'E2. Maps to SBML symbol `E2`.'), 'model_state_e1': ('E1', 'native SBML value', 'E1. Maps to SBML symbol `E1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230055.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
