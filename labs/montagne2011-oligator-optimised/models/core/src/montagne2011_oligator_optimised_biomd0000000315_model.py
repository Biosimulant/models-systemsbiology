# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Montagne2011_Oligator_optimised."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Montagne2011OligatorOptimisedBiomd0000000315Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Montagne2011_Oligator_optimised."""

    _SBML_ID = 'BIOMD0000000315'
    _TITLE = 'Montagne2011_Oligator_optimised'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T1', 'alpha', 'alpha_T1', 'alpha_T1_alpha', 'T1_alpha', 'alpha_alpha_T1', 'T2', 'alpha_T2', 'alpha_T2_beta', 'beta', 'T2_beta', 'alpha_beta_T2', 'T3', 'beta_T3', 'beta_T3_Inh', 'Inh', 'T3_Inh', 'beta_Inh_T3', 'Inh_T1']
    _SPECIES_LABELS = {'T1': 'T1', 'alpha': 'alpha', 'alpha_T1': 'alpha_T1', 'alpha_T1_alpha': 'alpha_T1_alpha', 'T1_alpha': 'T1_alpha', 'alpha_alpha_T1': 'alpha_alpha_T1', 'T2': 'T2', 'alpha_T2': 'alpha_T2', 'alpha_T2_beta': 'alpha_T2_beta', 'beta': 'beta', 'T2_beta': 'T2_beta', 'alpha_beta_T2': 'alpha_beta_T2', 'T3': 'T3', 'beta_T3': 'beta_T3', 'beta_T3_Inh': 'beta_T3_Inh', 'Inh': 'Inh', 'T3_Inh': 'T3_Inh', 'beta_Inh_T3': 'beta_Inh_T3', 'Inh_T1': 'Inh_T1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha': ('alpha', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha`.'), 'initial_beta_t3_inh': ('beta_T3_Inh', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta_T3_Inh`.'), 'initial_beta_t3': ('beta_T3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta_T3`.'), 'initial_beta_inh_t3': ('beta_Inh_T3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta_Inh_T3`.'), 'initial_beta': ('beta', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta`.'), 'initial_alpha_beta_t2': ('alpha_beta_T2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha_beta_T2`.')}
    _HEADLINE_OUTPUTS = {'alpha': ('alpha', 'native SBML value', 'alpha. Maps to SBML symbol `alpha`.'), 'beta_t3_inh': ('beta_T3_Inh', 'native SBML value', 'beta_T3_Inh. Maps to SBML symbol `beta_T3_Inh`.'), 'beta_t3': ('beta_T3', 'native SBML value', 'beta_T3. Maps to SBML symbol `beta_T3`.'), 'beta_inh_t3': ('beta_Inh_T3', 'native SBML value', 'beta_Inh_T3. Maps to SBML symbol `beta_Inh_T3`.'), 'beta': ('beta', 'native SBML value', 'beta. Maps to SBML symbol `beta`.'), 'alpha_beta_t2': ('alpha_beta_T2', 'native SBML value', 'alpha_beta_T2. Maps to SBML symbol `alpha_beta_T2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000315.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
