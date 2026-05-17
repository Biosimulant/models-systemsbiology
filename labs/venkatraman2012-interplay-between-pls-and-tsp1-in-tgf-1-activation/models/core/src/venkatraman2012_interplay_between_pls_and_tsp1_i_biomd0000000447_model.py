# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Venkatraman2012 - Interplay between PLS and TSP1 in TGF-β1 activation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Venkatraman2012InterplayBetweenPlsAndTsp1IBiomd0000000447Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Venkatraman2012 - Interplay between PLS and TSP1 in TGF-β1 activation."""

    _SBML_ID = 'BIOMD0000000447'
    _TITLE = 'Venkatraman2012 - Interplay between PLS and TSP1 in TGF-β1 activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13']
    _SPECIES_LABELS = {'species_1': 'PLG', 'species_2': 'PLS', 'species_3': 'scUPA', 'species_4': 'tcUPA', 'species_5': 'LTGFb1', 'species_6': 'TGFb1', 'species_7': 'TSP1', 'species_8': 'PAI1', 'species_9': 'TSP1:PLS', 'species_10': 'A2M', 'species_11': 'A2M:PLS', 'species_12': 'PAI1:tcUPA', 'species_13': 'PAI1:scUPA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ltg_fb1': ('species_5', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_5`.'), 'initial_tg_fb1': ('species_6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.'), 'initial_a2_m': ('species_10', 0.005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_10`.'), 'initial_model_state_plg': ('species_1', 0.003, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_sc_upa': ('species_3', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_tc_upa': ('species_4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.')}
    _HEADLINE_OUTPUTS = {'ltg_fb1': ('species_5', 'native SBML value', 'LTGFb1. Maps to SBML symbol `species_5`.'), 'tg_fb1': ('species_6', 'native SBML value', 'TGFb1. Maps to SBML symbol `species_6`.'), 'a2_m': ('species_10', 'native SBML value', 'A2M. Maps to SBML symbol `species_10`.'), 'plg': ('species_1', 'native SBML value', 'PLG. Maps to SBML symbol `species_1`.'), 'sc_upa': ('species_3', 'native SBML value', 'scUPA. Maps to SBML symbol `species_3`.'), 'tc_upa': ('species_4', 'native SBML value', 'tcUPA. Maps to SBML symbol `species_4`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000447.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
