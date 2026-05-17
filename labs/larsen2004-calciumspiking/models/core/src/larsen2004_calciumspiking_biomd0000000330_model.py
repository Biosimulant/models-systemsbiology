# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Larsen2004_CalciumSpiking."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Larsen2004CalciumspikingBiomd0000000330Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Larsen2004_CalciumSpiking."""

    _SBML_ID = 'BIOMD0000000330'
    _TITLE = 'Larsen2004_CalciumSpiking'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G_alpha', 'PLC', 'Ca_cyt', 'Ca_ER', 'Ca_mit']
    _SPECIES_LABELS = {'G_alpha': 'G-alpha', 'PLC': 'PLC', 'Ca_cyt': 'Calcium-Cyt', 'Ca_ER': 'Calcium-ER', 'Ca_mit': 'Calcium-mit'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_er': ('Ca_ER', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_ER`.'), 'initial_g_alpha': ('G_alpha', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_alpha`.'), 'initial_calcium_cyt': ('Ca_cyt', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_cyt`.'), 'initial_calcium_mit': ('Ca_mit', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_mit`.'), 'initial_model_state_plc': ('PLC', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PLC`.')}
    _HEADLINE_OUTPUTS = {'calcium_er': ('Ca_ER', 'native SBML value', 'Calcium-ER. Maps to SBML symbol `Ca_ER`.'), 'g_alpha': ('G_alpha', 'native SBML value', 'G-alpha. Maps to SBML symbol `G_alpha`.'), 'calcium_cyt': ('Ca_cyt', 'native SBML value', 'Calcium-Cyt. Maps to SBML symbol `Ca_cyt`.'), 'calcium_mit': ('Ca_mit', 'native SBML value', 'Calcium-mit. Maps to SBML symbol `Ca_mit`.'), 'plc': ('PLC', 'native SBML value', 'PLC. Maps to SBML symbol `PLC`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000330.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
