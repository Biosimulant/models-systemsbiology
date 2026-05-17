# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ma2005-digital response of p53 to DNA damage-ATM Activation Module."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ma2005DigitalResponseOfP53ToDnaDamageAtmModel2005130001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ma2005-digital response of p53 to DNA damage-ATM Activation Module."""

    _SBML_ID = 'MODEL2005130001'
    _TITLE = 'Ma2005-digital response of p53 to DNA damage-ATM Activation Module'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ATM_D', 'ATM', 'ATM_star']
    _SPECIES_LABELS = {'ATM_D': 'ATM_D', 'ATM': 'ATM', 'ATM_star': 'ATM_star'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atm_star': ('ATM_star', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATM_star`.'), 'initial_atm_d': ('ATM_D', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATM_D`.'), 'initial_model_state_atm': ('ATM', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATM`.')}
    _HEADLINE_OUTPUTS = {'atm_star': ('ATM_star', 'native SBML value', 'ATM_star. Maps to SBML symbol `ATM_star`.'), 'atm_d': ('ATM_D', 'native SBML value', 'ATM_D. Maps to SBML symbol `ATM_D`.'), 'atm': ('ATM', 'native SBML value', 'ATM. Maps to SBML symbol `ATM`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2005130001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
