# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Vempati2007_MMP9_Regulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vempati2007Mmp9RegulationModel7888000034Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Vempati2007_MMP9_Regulation."""

    _SBML_ID = 'MODEL7888000034'
    _TITLE = 'Vempati2007_MMP9_Regulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['pM9', 'M3', 'M3_pM9', 'T1', 'M3_T1', 'pM9_T1', 'M3_pM9_T1', 'M9_T1_star', 'M9', 'M9_T1', 'pM9_T1_M3', 'M3_pM9_T1_M3', 'M9_T1_M3', 'Tr', 'Tr_pM9', 'Tr_pM9_T1', 'Tr_pM9_T1_M3']
    _SPECIES_LABELS = {'pM9': 'PM9', 'M3': 'M3', 'M3_pM9': 'M3 PM9', 'T1': 'T1', 'M3_T1': 'M3 T1', 'pM9_T1': 'PM9 T1', 'M3_pM9_T1': 'M3 PM9 T1', 'M9_T1_star': 'M9 T1 Star', 'M9': 'M9', 'M9_T1': 'M9 T1', 'pM9_T1_M3': 'PM9 T1 M3', 'M3_pM9_T1_M3': 'M3 PM9 T1 M3', 'M9_T1_M3': 'M9 T1 M3', 'Tr': 'Tr', 'Tr_pM9': 'Tr PM9', 'Tr_pM9_T1': 'Tr PM9 T1', 'Tr_pM9_T1_M3': 'Tr PM9 T1 M3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tr_pm9_t1_m3': ('Tr_pM9_T1_M3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tr_pM9_T1_M3`.'), 'initial_tr_pm9_t1': ('Tr_pM9_T1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tr_pM9_T1`.'), 'initial_tr_pm9': ('Tr_pM9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tr_pM9`.'), 'initial_model_state_tr': ('Tr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tr`.'), 'initial_model_state_t1': ('T1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1`.'), 'initial_pm9_t1_m3': ('pM9_T1_M3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pM9_T1_M3`.')}
    _HEADLINE_OUTPUTS = {'tr_pm9_t1_m3': ('Tr_pM9_T1_M3', 'native SBML value', 'Tr PM9 T1 M3. Maps to SBML symbol `Tr_pM9_T1_M3`.'), 'tr_pm9_t1': ('Tr_pM9_T1', 'native SBML value', 'Tr PM9 T1. Maps to SBML symbol `Tr_pM9_T1`.'), 'tr_pm9': ('Tr_pM9', 'native SBML value', 'Tr PM9. Maps to SBML symbol `Tr_pM9`.'), 'model_state_tr': ('Tr', 'native SBML value', 'Tr. Maps to SBML symbol `Tr`.'), 'model_state_t1': ('T1', 'native SBML value', 'T1. Maps to SBML symbol `T1`.'), 'pm9_t1_m3': ('pM9_T1_M3', 'native SBML value', 'PM9 T1 M3. Maps to SBML symbol `pM9_T1_M3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL7888000034.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
