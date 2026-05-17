# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Aguda1999_CellCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aguda1999CellcycleBiomd0000000169Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Aguda1999_CellCycle."""

    _SBML_ID = 'BIOMD0000000169'
    _TITLE = 'Aguda1999_CellCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Y3_1', 'Y4_1', 'Y11_1', 'Y2_1', 'Y1_1', 'Y5_1', 'Y6_1', 'Y7_1', 'Y8_1', 'Y10_1', 'Y9_1']
    _SPECIES_LABELS = {'Y3_1': 'pRB_E2F', 'Y4_1': 'E2F', 'Y11_1': 'pRB_P', 'Y2_1': 'i_cyclinE_CDK2', 'Y1_1': 'a_cyclinE_CDK2', 'Y5_1': 'pRB', 'Y6_1': 'CycD_CDK4', 'Y7_1': 'p27', 'Y8_1': 'cycE_CDK2_p27', 'Y10_1': 'p16', 'Y9_1': 'cycD_CDK4_p27'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p27': ('Y7_1', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y7_1`.'), 'initial_model_state_p16': ('Y10_1', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y10_1`.'), 'initial_p_rb_e2_f': ('Y3_1', 1.95, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y3_1`.'), 'initial_cyc_e_cdk2_p27': ('Y8_1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y8_1`.'), 'initial_p_rb': ('Y5_1', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y5_1`.'), 'initial_p_rb_p': ('Y11_1', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y11_1`.')}
    _HEADLINE_OUTPUTS = {'p27': ('Y7_1', 'native SBML value', 'p27. Maps to SBML symbol `Y7_1`.'), 'p16': ('Y10_1', 'native SBML value', 'p16. Maps to SBML symbol `Y10_1`.'), 'p_rb_e2_f': ('Y3_1', 'native SBML value', 'pRB_E2F. Maps to SBML symbol `Y3_1`.'), 'cyc_e_cdk2_p27': ('Y8_1', 'native SBML value', 'cycE_CDK2_p27. Maps to SBML symbol `Y8_1`.'), 'p_rb': ('Y5_1', 'native SBML value', 'pRB. Maps to SBML symbol `Y5_1`.'), 'p_rb_p': ('Y11_1', 'native SBML value', 'pRB_P. Maps to SBML symbol `Y11_1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000169.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
