# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tiemann2011_PhenotypeTransitions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tiemann2011PhenotypetransitionsModel1112150000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tiemann2011_PhenotypeTransitions."""

    _SBML_ID = 'MODEL1112150000'
    _TITLE = 'Tiemann2011_PhenotypeTransitions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9']
    _SPECIES_LABELS = {'species_1': 'FC', 'species_2': 'CE_cyt', 'species_3': 'CE_ER', 'species_4': 'TG_cyt', 'species_5': 'TG_ER', 'species_6': 'TG_plasma', 'species_7': 'CE_plasma', 'species_8': 'CE_HDL', 'species_9': 'FFA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tg_cyt': ('species_4', 3.1832, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_model_state_fc': ('species_1', 1.9366, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_ce_hdl': ('species_8', 1.35, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_ce_cyt': ('species_2', 0.6624, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.'), 'initial_ce_plasma': ('species_7', 0.61, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_tg_plasma': ('species_6', 0.46, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.')}
    _HEADLINE_OUTPUTS = {'tg_cyt': ('species_4', 'native SBML value', 'TG_cyt. Maps to SBML symbol `species_4`.'), 'model_state_fc': ('species_1', 'native SBML value', 'FC. Maps to SBML symbol `species_1`.'), 'ce_hdl': ('species_8', 'native SBML value', 'CE_HDL. Maps to SBML symbol `species_8`.'), 'ce_cyt': ('species_2', 'native SBML value', 'CE_cyt. Maps to SBML symbol `species_2`.'), 'ce_plasma': ('species_7', 'native SBML value', 'CE_plasma. Maps to SBML symbol `species_7`.'), 'tg_plasma': ('species_6', 'native SBML value', 'TG_plasma. Maps to SBML symbol `species_6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1112150000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
