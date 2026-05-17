# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Poolman2000_CalvinCycle_Starch."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Poolman2000CalvincycleStarchBiomd0000000391Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Poolman2000_CalvinCycle_Starch."""

    _SBML_ID = 'BIOMD0000000391'
    _TITLE = 'Arnold2011_Poolman2000_CalvinCycle_Starch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'PGA', 'DPGA', 'GAP', 'DHAP', 'FBP', 'F6P', 'E4P', 'SBP', 'S7P', 'X5P', 'R5P', 'Ru5P', 'G6P', 'G1P', 'ATP', 'ADP', 'NADPH', 'NADP', 'H', 'Pi', 'Pext']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'PGA': 'PGA', 'DPGA': 'DPGA', 'GAP': 'GAP', 'DHAP': 'DHAP', 'FBP': 'FBP', 'F6P': 'F6P', 'E4P': 'E4P', 'SBP': 'SBP', 'S7P': 'S7P', 'X5P': 'X5P', 'R5P': 'R5P', 'Ru5P': 'Ru5P', 'G6P': 'G6P', 'G1P': 'G1P', 'ATP': 'ATP', 'ADP': 'ADP', 'NADPH': 'NADPH', 'NADP': 'NADP', 'H': 'H', 'Pi': 'Pi', 'Pext': 'Pext'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pga': ('PGA', 2.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`.'), 'initial_s7_p': ('S7P', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S7P`.'), 'initial_ru_bp': ('RuBP', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`.'), 'initial_g6_p': ('G6P', 1.47375779111085, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6P`.'), 'initial_model_state_pi': ('Pi', 0.977800000000002, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`.'), 'initial_model_state_adp': ('ADP', 0.82, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.')}
    _HEADLINE_OUTPUTS = {'pga': ('PGA', 'native SBML value', 'PGA. Maps to SBML symbol `PGA`.'), 's7_p': ('S7P', 'native SBML value', 'S7P. Maps to SBML symbol `S7P`.'), 'ru_bp': ('RuBP', 'native SBML value', 'RuBP. Maps to SBML symbol `RuBP`.'), 'g6_p': ('G6P', 'native SBML value', 'G6P. Maps to SBML symbol `G6P`.'), 'model_state_pi': ('Pi', 'native SBML value', 'Pi. Maps to SBML symbol `Pi`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000391.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
