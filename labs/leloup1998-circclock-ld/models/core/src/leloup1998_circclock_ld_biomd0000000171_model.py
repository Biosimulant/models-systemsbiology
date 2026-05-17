# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup1998_CircClock_LD."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup1998CircclockLdBiomd0000000171Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup1998_CircClock_LD."""

    _SBML_ID = 'BIOMD0000000171'
    _TITLE = 'Leloup1998_CircClock_LD'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M_T', 'M_P', 'T0', 'T1', 'T2', 'P0', 'P1', 'P2', 'C', 'CN', 'Tt', 'Pt']
    _SPECIES_LABELS = {'M_T': 'tim mRNA', 'M_P': 'per mRNA', 'T0': 'TIM', 'T1': 'TIM-p', 'T2': 'TIM-pp', 'P0': 'PER', 'P1': 'PER-p', 'P2': 'PER-pp', 'C': 'PER_TIM complex cytoplasm', 'CN': 'PER_TIM complex nuclear', 'Tt': 'total TIM', 'Pt': 'total PER'}
    _PARAMETER_INPUTS = {'light_dark_period': ('l_d', 12.0, 'time', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `l_d`.'), 'v_d_t_fold_incr_during_light': ('v_dT_fac', 2.0, 'dimensionless', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `v_dT_fac`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'tim_mrna': ('M_T', 'native SBML value', 'tim mRNA. Maps to SBML symbol `M_T`.'), 'per_mrna': ('M_P', 'native SBML value', 'per mRNA. Maps to SBML symbol `M_P`.'), 'tim_pp': ('T2', 'native SBML value', 'TIM-pp. Maps to SBML symbol `T2`.'), 'per_tim_complex_nuclear': ('CN', 'native SBML value', 'PER_TIM complex nuclear. Maps to SBML symbol `CN`.'), 'tim_p': ('T1', 'native SBML value', 'TIM-p. Maps to SBML symbol `T1`.'), 'tim': ('T0', 'native SBML value', 'TIM. Maps to SBML symbol `T0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000171.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
