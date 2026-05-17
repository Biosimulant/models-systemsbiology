# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DellOrco2009_phototransduction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dellorco2009PhototransductionBiomd0000000326Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DellOrco2009_phototransduction."""

    _SBML_ID = 'BIOMD0000000326'
    _TITLE = 'DellOrco2009_phototransduction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Arr', 'Ca2_buff', 'Ca2_free', 'G_GTP', 'Ga_GDP', 'Ga_GTP', 'Ga_GTP_PDE_a_Ga_GTP', 'Ga_GTP_a_PDE_a_Ga_GTP', 'Gbg', 'Gt', 'Ops', 'Ops_G', 'Ops_G_GTP', 'Ops_Gt', 'PDE', 'PDE_Ga_GTP', 'PDE_a_Ga_GTP', 'R', 'R0', 'R0_G', 'R0_G_GTP', 'R0_Gt', 'R0_RKpre', 'R1', 'R1_Arr', 'R1_G', 'R1_G_GTP', 'R1_Gt', 'R1_RKpost', 'R1_RKpre', 'R2', 'R2_Arr', 'R2_G', 'R2_G_GTP', 'R2_Gt', 'R2_RKpost', 'R2_RKpre', 'R3', 'R3_Arr', 'R3_G', 'R3_G_GTP', 'R3_Gt', 'R3_RKpost', 'R3_RKpre', 'R4', 'R4_Arr', 'R4_G', 'R4_G_GTP', 'R4_Gt', 'R4_RKpost', 'R4_RKpre', 'R5', 'R5_Arr', 'R5_G', 'R5_G_GTP', 'R5_Gt', 'R5_RKpost', 'R5_RKpre', 'R6', 'R6_Arr', 'R6_G', 'R6_G_GTP', 'R6_Gt', 'R6_RKpost', 'R6_RKpre', 'RGS', 'RGS_Ga_GTP_a_PDE_a_Ga_GTP', 'RGS_PDE_a_Ga_GTP', 'RK', 'Rec_wCa2_RK', 'cGMP']
    _SPECIES_LABELS = {'Arr': 'Arr', 'Ca2_buff': 'Ca2_buff', 'Ca2_free': 'Ca2_free', 'G_GTP': 'G_GTP', 'Ga_GDP': 'Ga_GDP', 'Ga_GTP': 'Ga_GTP', 'Ga_GTP_PDE_a_Ga_GTP': 'Ga_GTP_PDE_a_Ga_GTP', 'Ga_GTP_a_PDE_a_Ga_GTP': 'Ga_GTP_a_PDE_a_Ga_GTP', 'Gbg': 'Gbg', 'Gt': 'Gt', 'Ops': 'Ops', 'Ops_G': 'Ops_G', 'Ops_G_GTP': 'Ops_G_GTP', 'Ops_Gt': 'Ops_Gt', 'PDE': 'PDE', 'PDE_Ga_GTP': 'PDE_Ga_GTP', 'PDE_a_Ga_GTP': 'PDE_a_Ga_GTP', 'R': 'R', 'R0': 'R0', 'R0_G': 'R0_G', 'R0_G_GTP': 'R0_G_GTP', 'R0_Gt': 'R0_Gt', 'R0_RKpre': 'R0_RKpre', 'R1': 'R1', 'R1_Arr': 'R1_Arr', 'R1_G': 'R1_G', 'R1_G_GTP': 'R1_G_GTP', 'R1_Gt': 'R1_Gt', 'R1_RKpost': 'R1_RKpost', 'R1_RKpre': 'R1_RKpre', 'R2': 'R2', 'R2_Arr': 'R2_Arr', 'R2_G': 'R2_G', 'R2_G_GTP': 'R2_G_GTP', 'R2_Gt': 'R2_Gt', 'R2_RKpost': 'R2_RKpost', 'R2_RKpre': 'R2_RKpre', 'R3': 'R3', 'R3_Arr': 'R3_Arr', 'R3_G': 'R3_G', 'R3_G_GTP': 'R3_G_GTP', 'R3_Gt': 'R3_Gt', 'R3_RKpost': 'R3_RKpost', 'R3_RKpre': 'R3_RKpre', 'R4': 'R4', 'R4_Arr': 'R4_Arr', 'R4_G': 'R4_G', 'R4_G_GTP': 'R4_G_GTP', 'R4_Gt': 'R4_Gt', 'R4_RKpost': 'R4_RKpost', 'R4_RKpre': 'R4_RKpre', 'R5': 'R5', 'R5_Arr': 'R5_Arr', 'R5_G': 'R5_G', 'R5_G_GTP': 'R5_G_GTP', 'R5_Gt': 'R5_Gt', 'R5_RKpost': 'R5_RKpost', 'R5_RKpre': 'R5_RKpre', 'R6': 'R6', 'R6_Arr': 'R6_Arr', 'R6_G': 'R6_G', 'R6_G_GTP': 'R6_G_GTP', 'R6_Gt': 'R6_Gt', 'R6_RKpost': 'R6_RKpost', 'R6_RKpre': 'R6_RKpre', 'RGS': 'RGS', 'RGS_Ga_GTP_a_PDE_a_Ga_GTP': 'RGS_Ga_GTP_a_PDE_a_Ga_GTP', 'RGS_PDE_a_Ga_GTP': 'RGS_PDE_a_Ga_GTP', 'RK': 'RK', 'Rec_wCa2_RK': 'Rec_wCa2_RK', 'cGMP': 'cGMP'}
    _PARAMETER_INPUTS = {'otherstimulus': ('otherstimulus', 0.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `otherstimulus`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'rec_w_ca2_rk': ('Rec_wCa2_RK', 'native SBML value', 'Rec_wCa2_RK. Maps to SBML symbol `Rec_wCa2_RK`.'), 'ca2_buff': ('Ca2_buff', 'native SBML value', 'Ca2_buff. Maps to SBML symbol `Ca2_buff`.'), 'c_gmp': ('cGMP', 'native SBML value', 'cGMP. Maps to SBML symbol `cGMP`.'), 'ca2_free': ('Ca2_free', 'native SBML value', 'Ca2_free. Maps to SBML symbol `Ca2_free`.'), 'rgs_pde_a_ga_gtp': ('RGS_PDE_a_Ga_GTP', 'native SBML value', 'RGS_PDE_a_Ga_GTP. Maps to SBML symbol `RGS_PDE_a_Ga_GTP`.'), 'r6_r_kpre': ('R6_RKpre', 'native SBML value', 'R6_RKpre. Maps to SBML symbol `R6_RKpre`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000326.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
