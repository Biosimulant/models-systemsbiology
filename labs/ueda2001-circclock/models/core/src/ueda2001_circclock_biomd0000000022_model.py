# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ueda2001_CircClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ueda2001CircclockBiomd0000000022Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ueda2001_CircClock."""

    _SBML_ID = 'BIOMD0000000022'
    _TITLE = 'Ueda2001_CircClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EmptySet', 'CCc', 'CCn', 'Clkc', 'Clkm', 'Perc', 'Perm', 'PTc', 'PTn', 'Timc', 'Timm', 'species_0000012', 'species_0000013']
    _SPECIES_LABELS = {'EmptySet': 'EmptySet', 'CCc': 'Clk-Cyc_cyt', 'CCn': 'Clk-Cyc_nuc', 'Clkc': 'Clk_cyt', 'Clkm': 'Clk_mRNA', 'Perc': 'Per_cyt', 'Perm': 'Per_mRNA', 'PTc': 'Per-Tim_cyt', 'PTn': 'Per-Tim_nuc', 'Timc': 'Tim_cyt', 'Timm': 'Tim_mRNA', 'species_0000012': 'Cyc_cyt', 'species_0000013': 'Dbt_cyt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_per_tim_nuc': ('PTn', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PTn`.'), 'initial_dbt_cyt': ('species_0000013', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000013`.'), 'initial_cyc_cyt': ('species_0000012', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000012`.'), 'initial_per_tim_cyt': ('PTc', 0.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PTc`.'), 'initial_tim_cyt': ('Timc', 0.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Timc`.'), 'initial_tim_mrna': ('Timm', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Timm`.')}
    _HEADLINE_OUTPUTS = {'per_tim_nuc': ('PTn', 'native SBML value', 'Per-Tim_nuc. Maps to SBML symbol `PTn`.'), 'dbt_cyt': ('species_0000013', 'native SBML value', 'Dbt_cyt. Maps to SBML symbol `species_0000013`.'), 'cyc_cyt': ('species_0000012', 'native SBML value', 'Cyc_cyt. Maps to SBML symbol `species_0000012`.'), 'per_tim_cyt': ('PTc', 'native SBML value', 'Per-Tim_cyt. Maps to SBML symbol `PTc`.'), 'tim_cyt': ('Timc', 'native SBML value', 'Tim_cyt. Maps to SBML symbol `Timc`.'), 'tim_mrna': ('Timm', 'native SBML value', 'Tim_mRNA. Maps to SBML symbol `Timm`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000022.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
