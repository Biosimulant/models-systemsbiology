# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lockwood2006 - Alzheimer's Disease PBPK model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lockwood2006AlzheimerSDiseasePbpkModelBiomd0000000673Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lockwood2006 - Alzheimer's Disease PBPK model."""

    _SBML_ID = 'BIOMD0000000673'
    _TITLE = "Lockwood2006 - Alzheimer's Disease PBPK model"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'assignment_rules'
    _OBSERVABLES = ['Keq_P', 'Kel_P', 'Emax', 'n', 'CeA_U', 'ICea_U', 'Model_Inactive', 'Model_active_Linear', 'Model_active_Hyperbolic', 'Model_active_Sigmoidal', 'Model_active_U_Shaped', 'PD_CeA', 'ADAS_COG_P', 'PD_CeP', 'S']
    _SPECIES_LABELS = {'Keq_P': 'Keq P', 'Kel_P': 'Kel P', 'Emax': 'Emax', 'n': 'N', 'CeA_U': 'CeA U', 'ICea_U': 'ICea U', 'Model_Inactive': 'Model Inactive', 'Model_active_Linear': 'Model Active Linear', 'Model_active_Hyperbolic': 'Model Active Hyperbolic', 'Model_active_Sigmoidal': 'Model Active Sigmoidal', 'Model_active_U_Shaped': 'Model Active U Shaped', 'PD_CeA': 'PD CeA', 'ADAS_COG_P': 'ADAS COG P', 'PD_CeP': 'PD CeP', 'S': 'S'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'pd_ce_p': ('PD_CeP', 'native SBML value', 'PD CeP. Maps to SBML symbol `PD_CeP`.'), 'pd_ce_a': ('PD_CeA', 'native SBML value', 'PD CeA. Maps to SBML symbol `PD_CeA`.'), 'model_inactive': ('Model_Inactive', 'native SBML value', 'Model Inactive. Maps to SBML symbol `Model_Inactive`.'), 'model_active_u_shaped': ('Model_active_U_Shaped', 'native SBML value', 'Model Active U Shaped. Maps to SBML symbol `Model_active_U_Shaped`.'), 'model_active_sigmoidal': ('Model_active_Sigmoidal', 'native SBML value', 'Model Active Sigmoidal. Maps to SBML symbol `Model_active_Sigmoidal`.'), 'model_active_linear': ('Model_active_Linear', 'native SBML value', 'Model Active Linear. Maps to SBML symbol `Model_active_Linear`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000673.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
