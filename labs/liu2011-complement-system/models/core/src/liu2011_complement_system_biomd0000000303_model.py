# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Liu2011_Complement_System."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Liu2011ComplementSystemBiomd0000000303Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Liu2011_Complement_System."""

    _SBML_ID = 'BIOMD0000000303'
    _TITLE = 'Liu2011_Complement_System'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CRP', 'PC', 'PC_CRP', 'C4', 'C4a', 'C4b', 'C2', 'C1', 'PC_CRP_C1', 'C2a', 'C2b', 'C4b_C2a', 'C3', 'C3a', 'C3b', 'dC3b', 'MASP', 'dC4b_C2a', 'GlcNac', 'GlcNac_LF', 'LF', 'GlcNac_LF_MASP', 'PC_CRP_LF', 'PC_CRP_LF_MASP', 'GlcNac_LF_CRP', 'GlcNac_LF_CRP_C1', 'C4BP', 'C4BP_PC_CRP', 'C4BP_GlcNac_LF_CRP', 'iC4b_C2a', 'C4BP_C4b', 'C4b_C2a_C4BP', 'dC4b_C2a_C4BP', 'PC_CRP_LF_C1', 'C4BP_PC_CRP_LF', 'GlcNac_LF_CRP_MASP', 'PC_CRP_LF_C1_MASP', 'GlcNac_LF_C1_MASP', 'GlcNac_HF', 'HF', 'GlcNac_HF_MASP', 'X']
    _SPECIES_LABELS = {'CRP': 'CRP', 'PC': 'PC', 'PC_CRP': 'PC/CRP', 'C4': 'C4', 'C4a': 'C4a', 'C4b': 'C4b', 'C2': 'C2', 'C1': 'C1', 'PC_CRP_C1': 'PC/CRP/C1', 'C2a': 'C2a', 'C2b': 'C2b', 'C4b_C2a': 'C4b/C2a', 'C3': 'C3', 'C3a': 'C3a', 'C3b': 'C3b', 'dC3b': 'dC3b', 'MASP': 'MASP', 'dC4b_C2a': 'dC4b/C2a', 'GlcNac': 'GlcNac', 'GlcNac_LF': 'GlcNac/LF', 'LF': 'LF', 'GlcNac_LF_MASP': 'GlcNac/LF/MASP', 'PC_CRP_LF': 'PC/CRP/LF', 'PC_CRP_LF_MASP': 'PC/CRP/LF/MASP', 'GlcNac_LF_CRP': 'GlcNac/LF/CRP', 'GlcNac_LF_CRP_C1': 'GlcNac/LF/CRP/C1', 'C4BP': 'C4BP', 'C4BP_PC_CRP': 'C4BP/PC/CRP', 'C4BP_GlcNac_LF_CRP': 'C4BP/GlcNac/LF/CRP', 'iC4b_C2a': 'iC4b/C2a', 'C4BP_C4b': 'C4BP/C4b', 'C4b_C2a_C4BP': 'C4b/C2a/C4BP', 'dC4b_C2a_C4BP': 'dC4b/C2a/C4BP', 'PC_CRP_LF_C1': 'PC/CRP/LF/C1', 'C4BP_PC_CRP_LF': 'C4BP/PC/CRP/LF', 'GlcNac_LF_CRP_MASP': 'GlcNac/LF/CRP/MASP', 'PC_CRP_LF_C1_MASP': 'PC/CRP/LF/C1/MASP', 'GlcNac_LF_C1_MASP': 'GlcNac/LF/C1/MASP', 'GlcNac_HF': 'GlcNac/HF', 'HF': 'HF', 'GlcNac_HF_MASP': 'GlcNac/HF/MASP', 'X': 'X'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_i_c4b_c2a': ('iC4b_C2a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `iC4b_C2a`.'), 'initial_d_c4b_c2a_c4_bp': ('dC4b_C2a_C4BP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dC4b_C2a_C4BP`.'), 'initial_d_c4b_c2a': ('dC4b_C2a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dC4b_C2a`.'), 'initial_d_c3b': ('dC3b', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dC3b`.'), 'initial_pc_crp_lf_masp': ('PC_CRP_LF_MASP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PC_CRP_LF_MASP`.'), 'initial_pc_crp_lf_c1_masp': ('PC_CRP_LF_C1_MASP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PC_CRP_LF_C1_MASP`.')}
    _HEADLINE_OUTPUTS = {'i_c4b_c2a': ('iC4b_C2a', 'native SBML value', 'iC4b/C2a. Maps to SBML symbol `iC4b_C2a`.'), 'd_c4b_c2a_c4_bp': ('dC4b_C2a_C4BP', 'native SBML value', 'dC4b/C2a/C4BP. Maps to SBML symbol `dC4b_C2a_C4BP`.'), 'd_c4b_c2a': ('dC4b_C2a', 'native SBML value', 'dC4b/C2a. Maps to SBML symbol `dC4b_C2a`.'), 'd_c3b': ('dC3b', 'native SBML value', 'dC3b. Maps to SBML symbol `dC3b`.'), 'pc_crp_lf_masp': ('PC_CRP_LF_MASP', 'native SBML value', 'PC/CRP/LF/MASP. Maps to SBML symbol `PC_CRP_LF_MASP`.'), 'pc_crp_lf_c1_masp': ('PC_CRP_LF_C1_MASP', 'native SBML value', 'PC/CRP/LF/C1/MASP. Maps to SBML symbol `PC_CRP_LF_C1_MASP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000303.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
