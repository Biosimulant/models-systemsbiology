# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Gall1999_CalciumBursting_BetaCellModel_A."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gall1999CalciumburstingBetacellmodelAModel1201070000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Gall1999_CalciumBursting_BetaCellModel_A."""

    _SBML_ID = 'MODEL1201070000'
    _TITLE = 'Gall1999_CalciumBursting_BetaCellModel_A'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V_membrane', 'n', 'Ca_i']
    _SPECIES_LABELS = {'V_membrane': 'V Membrane', 'n': 'N', 'Ca_i': 'Ca I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_ca_i': ('Ca_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_i`.'), 'initial_model_state_n': ('n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 'ca_i': ('Ca_i', 'native SBML value', 'Ca I. Maps to SBML symbol `Ca_i`.'), 'model_state_n': ('n', 'native SBML value', 'N. Maps to SBML symbol `n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1201070000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
