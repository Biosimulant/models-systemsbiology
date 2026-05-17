# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mazemondet2012 - beta-catenin dynamics in human neural progenitor cells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mazemondet2012BetaCateninDynamicsInHumanNeModel1303140000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mazemondet2012 - beta-catenin dynamics in human neural progenitor cells."""

    _SBML_ID = 'MODEL1303140000'
    _TITLE = 'Mazemondet2012 - beta-catenin dynamics in human neural progenitor cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_6']
    _SPECIES_LABELS = {'species_1': 'BetaCyt', 'species_2': 'Axin', 'species_3': 'AxinP', 'species_4': 'Wnt', 'species_6': 'BetaNuc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_beta_cyt': ('species_1', 16365.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_beta_nuc': ('species_6', 6655.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.'), 'initial_model_state_wnt': ('species_4', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_axin': ('species_2', 4.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.'), 'initial_axin_p': ('species_3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.')}
    _HEADLINE_OUTPUTS = {'beta_cyt': ('species_1', 'native SBML value', 'BetaCyt. Maps to SBML symbol `species_1`.'), 'beta_nuc': ('species_6', 'native SBML value', 'BetaNuc. Maps to SBML symbol `species_6`.'), 'wnt': ('species_4', 'native SBML value', 'Wnt. Maps to SBML symbol `species_4`.'), 'axin': ('species_2', 'native SBML value', 'Axin. Maps to SBML symbol `species_2`.'), 'axin_p': ('species_3', 'native SBML value', 'AxinP. Maps to SBML symbol `species_3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1303140000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
