# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wierschem2004 - Electrical bursting activity in Pancreatic Islets."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wierschem2004ElectricalBurstingActivityInPaBiomd0000000682Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wierschem2004 - Electrical bursting activity in Pancreatic Islets."""

    _SBML_ID = 'BIOMD0000000682'
    _TITLE = 'Wierschem2004 - Electrical bursting activity in Pancreatic Islets'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['ADP', 'ATP', 'V_membrane', 'n', 'c']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'V_membrane': 'V Membrane', 'n': 'N', 'c': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_model_state_atp': ('ATP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_n': ('n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.'), 'initial_model_state_c': ('c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'model_state_n': ('n', 'native SBML value', 'N. Maps to SBML symbol `n`.'), 'model_state_c': ('c', 'native SBML value', 'C. Maps to SBML symbol `c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000682.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
