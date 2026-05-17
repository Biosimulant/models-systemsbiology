# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zi2007_TGFbeta_signaling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zi2007TgfbetaSignalingBiomd0000000163Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zi2007_TGFbeta_signaling."""

    _SBML_ID = 'BIOMD0000000163'
    _TITLE = 'Zi2007_TGFbeta_signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Smad2c', 'Smad2n', 'Smad4c', 'Smad4n', 'T1R_Surf', 'T1R_Cave', 'T1R_EE', 'T2R_Surf', 'T2R_Cave', 'T2R_EE', 'LRC_Surf', 'LRC_Cave', 'LRC_EE', 'Smads_Complex_c', 'Smads_Complex_n', 'TGF_beta']
    _SPECIES_LABELS = {'Smad2c': 'Smad2c', 'Smad2n': 'Smad2n', 'Smad4c': 'Smad4c', 'Smad4n': 'Smad4n', 'T1R_Surf': 'T1R_Surf', 'T1R_Cave': 'T1R_Cave', 'T1R_EE': 'T1R_EE', 'T2R_Surf': 'T2R_Surf', 'T2R_Cave': 'T2R_Cave', 'T2R_EE': 'T2R_EE', 'LRC_Surf': 'LRC_Surf', 'LRC_Cave': 'LRC_Cave', 'LRC_EE': 'LRC_EE', 'Smads_Complex_c': 'Smads_Complex_c', 'Smads_Complex_n': 'Smads_Complex_n', 'TGF_beta': 'TGF_beta'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_t1_r_cave': ('T1R_Cave', 2.092, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1R_Cave`.'), 'initial_t1_r_ee': ('T1R_EE', 2.06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1R_EE`.'), 'initial_t2_r_cave': ('T2R_Cave', 1.778, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T2R_Cave`.'), 'initial_t2_r_ee': ('T2R_EE', 1.148, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T2R_EE`.'), 'initial_t1_r_surf': ('T1R_Surf', 0.237, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1R_Surf`.'), 'initial_t2_r_surf': ('T2R_Surf', 0.202, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T2R_Surf`.')}
    _HEADLINE_OUTPUTS = {'t1_r_cave': ('T1R_Cave', 'native SBML value', 'T1R_Cave. Maps to SBML symbol `T1R_Cave`.'), 't1_r_ee': ('T1R_EE', 'native SBML value', 'T1R_EE. Maps to SBML symbol `T1R_EE`.'), 't2_r_cave': ('T2R_Cave', 'native SBML value', 'T2R_Cave. Maps to SBML symbol `T2R_Cave`.'), 't2_r_ee': ('T2R_EE', 'native SBML value', 'T2R_EE. Maps to SBML symbol `T2R_EE`.'), 't1_r_surf': ('T1R_Surf', 'native SBML value', 'T1R_Surf. Maps to SBML symbol `T1R_Surf`.'), 't2_r_surf': ('T2R_Surf', 'native SBML value', 'T2R_Surf. Maps to SBML symbol `T2R_Surf`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000163.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
