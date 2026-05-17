# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Zhu2009_CalvinCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Zhu2009CalvincycleBiomd0000000388Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Zhu2009_CalvinCycle."""

    _SBML_ID = 'BIOMD0000000388'
    _TITLE = 'Arnold2011_Zhu2009_CalvinCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'PGA', 'DPGA', 'GAP', 'Ru5P', 'ADP', 'ATP', 'Pi']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'PGA': 'PGA', 'DPGA': 'DPGA', 'GAP': 'GAP', 'Ru5P': 'Ru5P', 'ADP': 'ADP', 'ATP': 'ATP', 'Pi': 'Pi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pi': ('Pi', 6.3477, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`.'), 'initial_model_state_pga': ('PGA', 2.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`.'), 'initial_ru_bp': ('RuBP', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`.'), 'initial_model_state_adp': ('ADP', 0.82, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_atp': ('ATP', 0.68, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_ru5_p': ('Ru5P', 0.0501, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ru5P`.')}
    _HEADLINE_OUTPUTS = {'model_state_pi': ('Pi', 'native SBML value', 'Pi. Maps to SBML symbol `Pi`.'), 'pga': ('PGA', 'native SBML value', 'PGA. Maps to SBML symbol `PGA`.'), 'ru_bp': ('RuBP', 'native SBML value', 'RuBP. Maps to SBML symbol `RuBP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'ru5_p': ('Ru5P', 'native SBML value', 'Ru5P. Maps to SBML symbol `Ru5P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000388.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
