# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Hahn1986_CalvinCycle_Starch_Sucrose."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Hahn1986CalvincycleStarchSucroseBiomd0000000389Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Hahn1986_CalvinCycle_Starch_Sucrose."""

    _SBML_ID = 'BIOMD0000000389'
    _TITLE = 'Arnold2011_Hahn1986_CalvinCycle_Starch_Sucrose'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'PGA', 'TP', 'HeP', 'TPGA', 'E4P', 'S7P', 'Ru5P', 'GG', 'ATP', 'ADP', 'UTP', 'UDP', 'Pi', 'CO2', 'TPc', 'HePc', 'Suc', 'Pic', 'SucV', 'E', 'Resp']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'PGA': 'PGA', 'TP': 'TP', 'HeP': 'HeP', 'TPGA': 'TPGA', 'E4P': 'E4P', 'S7P': 'S7P', 'Ru5P': 'Ru5P', 'GG': 'GG', 'ATP': 'ATP', 'ADP': 'ADP', 'UTP': 'UTP', 'UDP': 'UDP', 'Pi': 'Pi', 'CO2': 'CO2', 'TPc': 'TPc', 'HePc': 'HePc', 'Suc': 'Suc', 'Pic': 'Pic', 'SucV': 'SucV', 'E': 'E', 'Resp': 'Resp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_gg': ('GG', 99.9999999999999, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GG`.'), 'initial_suc_v': ('SucV', 77.31, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SucV`.'), 'initial_model_state_suc': ('Suc', 77.31, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Suc`.'), 'initial_model_state_co2': ('CO2', 31.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CO2`.'), 'initial_model_state_atp': ('ATP', 3.875, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_utp': ('UTP', 3.871, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `UTP`.')}
    _HEADLINE_OUTPUTS = {'model_state_gg': ('GG', 'native SBML value', 'GG. Maps to SBML symbol `GG`.'), 'suc_v': ('SucV', 'native SBML value', 'SucV. Maps to SBML symbol `SucV`.'), 'suc': ('Suc', 'native SBML value', 'Suc. Maps to SBML symbol `Suc`.'), 'co2': ('CO2', 'native SBML value', 'CO2. Maps to SBML symbol `CO2`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'utp': ('UTP', 'native SBML value', 'UTP. Maps to SBML symbol `UTP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000389.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
