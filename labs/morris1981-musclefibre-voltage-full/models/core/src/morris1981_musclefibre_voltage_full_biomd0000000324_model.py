# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Morris1981_MuscleFibre_Voltage_full."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Morris1981MusclefibreVoltageFullBiomd0000000324Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Morris1981_MuscleFibre_Voltage_full."""

    _SBML_ID = 'BIOMD0000000324'
    _TITLE = 'Morris1981_MuscleFibre_Voltage_full'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V', 'N', 'M']
    _SPECIES_LABELS = {'V': 'V', 'N': 'N', 'M': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_v': ('V', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_model_state_n': ('N', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.'), 'initial_model_state_m': ('M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.'), 'model_state_n': ('N', 'native SBML value', 'N. Maps to SBML symbol `N`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000324.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
