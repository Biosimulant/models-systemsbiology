# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Giersch1990_CalvinCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Giersch1990CalvincycleBiomd0000000390Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Giersch1990_CalvinCycle."""

    _SBML_ID = 'BIOMD0000000390'
    _TITLE = 'Arnold2011_Giersch1990_CalvinCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'PGA', 'TP', 'Ru5P', 'Pi', 'ATP', 'ADP', 'E_RuBisCO', 'totRuBP', 'TPc', 'Pic']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'PGA': 'PGA', 'TP': 'TP', 'Ru5P': 'Ru5P', 'Pi': 'Pi', 'ATP': 'ATP', 'ADP': 'ADP', 'E_RuBisCO': 'RuBisCo', 'totRuBP': 'totRuBP', 'TPc': 'TPc', 'Pic': 'Pic'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tot_ru_bp': ('totRuBP', 3.68496263079223, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `totRuBP`.'), 'initial_ru_bis_co': ('E_RuBisCO', 3.56, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_RuBisCO`.'), 'initial_model_state_pi': ('Pi', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`.'), 'initial_model_state_pga': ('PGA', 2.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`.'), 'initial_ru_bp': ('RuBP', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`.'), 'initial_model_state_pic': ('Pic', 1.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pic`.')}
    _HEADLINE_OUTPUTS = {'tot_ru_bp': ('totRuBP', 'native SBML value', 'totRuBP. Maps to SBML symbol `totRuBP`.'), 'ru_bis_co': ('E_RuBisCO', 'native SBML value', 'RuBisCo. Maps to SBML symbol `E_RuBisCO`.'), 'model_state_pi': ('Pi', 'native SBML value', 'Pi. Maps to SBML symbol `Pi`.'), 'pga': ('PGA', 'native SBML value', 'PGA. Maps to SBML symbol `PGA`.'), 'ru_bp': ('RuBP', 'native SBML value', 'RuBP. Maps to SBML symbol `RuBP`.'), 'pic': ('Pic', 'native SBML value', 'Pic. Maps to SBML symbol `Pic`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000390.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
