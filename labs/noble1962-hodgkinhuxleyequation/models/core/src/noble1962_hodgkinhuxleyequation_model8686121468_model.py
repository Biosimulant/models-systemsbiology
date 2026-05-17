# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Noble1962_HodgkinHuxleyEquation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Noble1962HodgkinhuxleyequationModel8686121468Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Noble1962_HodgkinHuxleyEquation."""

    _SBML_ID = 'MODEL8686121468'
    _TITLE = 'Noble1962_HodgkinHuxleyEquation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V_membrane', 'm', 'h', 'n']
    _SPECIES_LABELS = {'V_membrane': 'V Membrane', 'm': 'M', 'h': 'H', 'n': 'N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_model_state_n': ('n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.'), 'initial_model_state_m': ('m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m`.'), 'initial_model_state_h': ('h', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 'model_state_n': ('n', 'native SBML value', 'N. Maps to SBML symbol `n`.'), 'model_state_m': ('m', 'native SBML value', 'M. Maps to SBML symbol `m`.'), 'model_state_h': ('h', 'native SBML value', 'H. Maps to SBML symbol `h`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL8686121468.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
