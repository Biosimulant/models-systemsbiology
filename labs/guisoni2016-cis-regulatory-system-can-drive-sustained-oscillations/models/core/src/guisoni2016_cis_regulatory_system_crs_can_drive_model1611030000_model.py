# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Guisoni2016 - Cis-regulatory system (CRS) can drive sustained oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Guisoni2016CisRegulatorySystemCrsCanDriveModel1611030000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Guisoni2016 - Cis-regulatory system (CRS) can drive sustained oscillations."""

    _SBML_ID = 'MODEL1611030000'
    _TITLE = 'Guisoni2016 - Cis-regulatory system (CRS) can drive sustained oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['r0', 'r1', 'r2', 'r3', 'ft']
    _SPECIES_LABELS = {'r0': 'r0', 'r1': 'r1', 'r2': 'r2', 'r3': 'r3', 'ft': 'ft'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ft': ('ft', 10.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ft`.'), 'initial_model_state_r3': ('r3', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r3`.'), 'initial_model_state_r2': ('r2', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r2`.'), 'initial_model_state_r1': ('r1', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r1`.'), 'initial_model_state_r0': ('r0', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r0`.')}
    _HEADLINE_OUTPUTS = {'model_state_ft': ('ft', 'substance', 'ft. Maps to SBML symbol `ft`.'), 'model_state_r3': ('r3', 'substance', 'r3. Maps to SBML symbol `r3`.'), 'model_state_r2': ('r2', 'substance', 'r2. Maps to SBML symbol `r2`.'), 'model_state_r1': ('r1', 'substance', 'r1. Maps to SBML symbol `r1`.'), 'model_state_r0': ('r0', 'substance', 'r0. Maps to SBML symbol `r0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1611030000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
