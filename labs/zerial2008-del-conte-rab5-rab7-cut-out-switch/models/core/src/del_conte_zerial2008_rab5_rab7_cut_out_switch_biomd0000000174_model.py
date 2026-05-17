# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Del_Conte_Zerial2008_Rab5_Rab7_cut_out_switch."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class DelConteZerial2008Rab5Rab7CutOutSwitchBiomd0000000174Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Del_Conte_Zerial2008_Rab5_Rab7_cut_out_switch."""

    _SBML_ID = 'BIOMD0000000174'
    _TITLE = 'Del_Conte_Zerial2008_Rab5_Rab7_cut_out_switch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['r5', 'R5', 'r7', 'R7']
    _SPECIES_LABELS = {'r5': 'Rab5-GDP', 'R5': 'Rab5-GTP', 'r7': 'Rab7-GDP', 'R7': 'Rab7-GTP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rab7_gdp': ('r7', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r7`.'), 'initial_rab5_gdp': ('r5', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r5`.'), 'initial_rab7_gtp': ('R7', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R7`.'), 'initial_rab5_gtp': ('R5', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R5`.')}
    _HEADLINE_OUTPUTS = {'rab7_gdp': ('r7', 'native SBML value', 'Rab7-GDP. Maps to SBML symbol `r7`.'), 'rab5_gdp': ('r5', 'native SBML value', 'Rab5-GDP. Maps to SBML symbol `r5`.'), 'rab7_gtp': ('R7', 'native SBML value', 'Rab7-GTP. Maps to SBML symbol `R7`.'), 'rab5_gtp': ('R5', 'native SBML value', 'Rab5-GTP. Maps to SBML symbol `R5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000174.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
