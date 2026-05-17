# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Schmierer2010_FIH_Ankyrins."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schmierer2010FihAnkyrinsBiomd0000000300Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Schmierer2010_FIH_Ankyrins."""

    _SBML_ID = 'BIOMD0000000300'
    _TITLE = 'Schmierer2010_FIH_Ankyrins'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16']
    _SPECIES_LABELS = {'species_1': 'Htot', 'species_2': 'H', 'species_3': 'A', 'species_4': 'HOH', 'species_5': 'Atot', 'species_6': 'AOH', 'species_7': 'Ftot', 'species_8': 'Ptot', 'species_9': 'HF', 'species_10': 'HP', 'species_11': 'O2', 'species_12': 'FIHfree', 'species_13': 'CAD', 'species_14': 'NAD', 'species_15': 'CADOH', 'species_16': 'A for plotting'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atot': ('species_5', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_5`.'), 'initial_model_state_a': ('species_3', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_ftot': ('species_7', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_a_for_plotting': ('species_16', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_16`.'), 'initial_ptot': ('species_8', 0.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_fi_hfree': ('species_12', 0.0099009900990099, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`.')}
    _HEADLINE_OUTPUTS = {'atot': ('species_5', 'native SBML value', 'Atot. Maps to SBML symbol `species_5`.'), 'model_state_a': ('species_3', 'native SBML value', 'A. Maps to SBML symbol `species_3`.'), 'ftot': ('species_7', 'native SBML value', 'Ftot. Maps to SBML symbol `species_7`.'), 'a_for_plotting': ('species_16', 'native SBML value', 'A for plotting. Maps to SBML symbol `species_16`.'), 'ptot': ('species_8', 'native SBML value', 'Ptot. Maps to SBML symbol `species_8`.'), 'fi_hfree': ('species_12', 'native SBML value', 'FIHfree. Maps to SBML symbol `species_12`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000300.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
