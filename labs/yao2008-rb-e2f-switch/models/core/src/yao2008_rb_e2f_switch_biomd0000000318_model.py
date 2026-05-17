# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Yao2008_Rb_E2F_Switch."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yao2008RbE2fSwitchBiomd0000000318Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Yao2008_Rb_E2F_Switch."""

    _SBML_ID = 'BIOMD0000000318'
    _TITLE = 'Yao2008_Rb_E2F_Switch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['MC', 'EF', 'CD', 'CE', 'RB', 'RE', 'RP']
    _SPECIES_LABELS = {'MC': 'Myc', 'EF': 'E2F', 'CD': 'CycD', 'CE': 'CycE', 'RB': 'Rb', 'RE': 'Rb-E2F complex', 'RP': 'phosphorylated Rb'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rb_e2_f_complex': ('RE', 0.55, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RE`.'), 'initial_phosphorylated_rb': ('RP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RP`.'), 'initial_model_state_rb': ('RB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RB`.'), 'initial_model_state_myc': ('MC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MC`.'), 'initial_e2_f': ('EF', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EF`.'), 'initial_cyc_e': ('CE', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CE`.')}
    _HEADLINE_OUTPUTS = {'rb_e2_f_complex': ('RE', 'native SBML value', 'Rb-E2F complex. Maps to SBML symbol `RE`.'), 'phosphorylated_rb': ('RP', 'native SBML value', 'phosphorylated Rb. Maps to SBML symbol `RP`.'), 'model_state_rb': ('RB', 'native SBML value', 'Rb. Maps to SBML symbol `RB`.'), 'myc': ('MC', 'native SBML value', 'Myc. Maps to SBML symbol `MC`.'), 'e2_f': ('EF', 'native SBML value', 'E2F. Maps to SBML symbol `EF`.'), 'cyc_e': ('CE', 'native SBML value', 'CycE. Maps to SBML symbol `CE`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000318.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
