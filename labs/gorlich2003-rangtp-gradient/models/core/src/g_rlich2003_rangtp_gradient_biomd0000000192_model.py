# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Görlich2003_RanGTP_gradient."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GRlich2003RangtpGradientBiomd0000000192Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Görlich2003_RanGTP_gradient."""

    _SBML_ID = 'BIOMD0000000192'
    _TITLE = 'Görlich2003_RanGTP_gradient'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RanGDP_nuc', 'RCC1_RanGDP', 'GDP', 'RCC1', 'RCC1_RanGTP', 'RCC1_Ran', 'GTP', 'RanGTP_nuc', 'RanGAP', 'RanBP1', 'RanGTP_cy', 'RanGTP_RanBP1', 'RanGDP_cy']
    _SPECIES_LABELS = {'RanGDP_nuc': 'RanGDP Nuc', 'RCC1_RanGDP': 'RCC1 RanGDP', 'GDP': 'GDP', 'RCC1': 'RCC1', 'RCC1_RanGTP': 'RCC1 RanGTP', 'RCC1_Ran': 'RCC1 Ran', 'GTP': 'GTP', 'RanGTP_nuc': 'RanGTP Nuc', 'RanGAP': 'RanGAP', 'RanBP1': 'RanBP1', 'RanGTP_cy': 'RanGTP Cy', 'RanGTP_RanBP1': 'RanGTP RanBP1', 'RanGDP_cy': 'RanGDP Cy'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_gtp': ('GTP', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GTP`.'), 'initial_ran_gdp_cy': ('RanGDP_cy', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RanGDP_cy`.'), 'initial_ran_bp1': ('RanBP1', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RanBP1`.'), 'initial_model_state_gdp': ('GDP', 1.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GDP`.'), 'initial_ran_gap': ('RanGAP', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RanGAP`.'), 'initial_rcc1': ('RCC1', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RCC1`.')}
    _HEADLINE_OUTPUTS = {'gtp': ('GTP', 'native SBML value', 'GTP. Maps to SBML symbol `GTP`.'), 'ran_gdp_cy': ('RanGDP_cy', 'native SBML value', 'RanGDP Cy. Maps to SBML symbol `RanGDP_cy`.'), 'ran_bp1': ('RanBP1', 'native SBML value', 'RanBP1. Maps to SBML symbol `RanBP1`.'), 'gdp': ('GDP', 'native SBML value', 'GDP. Maps to SBML symbol `GDP`.'), 'ran_gap': ('RanGAP', 'native SBML value', 'RanGAP. Maps to SBML symbol `RanGAP`.'), 'rcc1': ('RCC1', 'native SBML value', 'RCC1. Maps to SBML symbol `RCC1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000192.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
