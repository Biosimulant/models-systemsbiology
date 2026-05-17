# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Laisk2006_CalvinCycle_Starch_Sucrose."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Laisk2006CalvincycleStarchSucroseBiomd0000000392Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Laisk2006_CalvinCycle_Starch_Sucrose."""

    _SBML_ID = 'BIOMD0000000392'
    _TITLE = 'Arnold2011_Laisk2006_CalvinCycle_Starch_Sucrose'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'E', 'ER', 'EPP', 'EPG', 'EP', 'EOP', 'PGA', 'TP', 'GAP', 'DHAP', 'FBP', 'HeP', 'F6P', 'G6P', 'G1P', 'E4P', 'SBP', 'S7P', 'PeP', 'X5P', 'R5P', 'Ru5P', 'ADPG', 'ATP', 'ADP', 'Pi', 'PiPi', 'H', 'CO2', 'O2', 'NADPH', 'NADP', 'PGAc', 'TPc', 'GAPc', 'DHAPc', 'FBPc', 'F26BPc', 'HePc', 'F6Pc', 'G6Pc', 'G1Pc', 'UDPGc', 'UTPc', 'UDPc', 'ATPc', 'ADPc', 'SucPc', 'Succ', 'Pic', 'PiPic', 'Hc']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'E': 'E', 'ER': 'ER', 'EPP': 'EPP', 'EPG': 'EPG', 'EP': 'EP', 'EOP': 'EOP', 'PGA': 'PGA', 'TP': 'TP', 'GAP': 'GAP', 'DHAP': 'DHAP', 'FBP': 'FBP', 'HeP': 'HeP', 'F6P': 'F6P', 'G6P': 'G6P', 'G1P': 'G1P', 'E4P': 'E4P', 'SBP': 'SBP', 'S7P': 'S7P', 'PeP': 'PeP', 'X5P': 'X5P', 'R5P': 'R5P', 'Ru5P': 'Ru5P', 'ADPG': 'ADPG', 'ATP': 'ATP', 'ADP': 'ADP', 'Pi': 'Pi', 'PiPi': 'PiPi', 'H': 'H', 'CO2': 'CO2', 'O2': 'O2', 'NADPH': 'NADPH', 'NADP': 'NADP', 'PGAc': 'PGAc', 'TPc': 'TPc', 'GAPc': 'GAPc', 'DHAPc': 'DHAPc', 'FBPc': 'FBPc', 'F26BPc': 'F26BPc', 'HePc': 'HePc', 'F6Pc': 'F6Pc', 'G6Pc': 'G6Pc', 'G1Pc': 'G1Pc', 'UDPGc': 'UDPGc', 'UTPc': 'UTPc', 'UDPc': 'UDPc', 'ATPc': 'ATPc', 'ADPc': 'ADPc', 'SucPc': 'SucPc', 'Succ': 'Succ', 'Pic': 'Pic', 'PiPic': 'PiPic', 'Hc': 'Hc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_hc': ('Hc', 0.158489318357816, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Hc`.'), 'initial_model_state_pi': ('Pi', 0.0109928959090909, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`.'), 'initial_he_pc': ('HePc', 0.0058, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HePc`.'), 'initial_model_state_pga': ('PGA', 0.0024, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`.'), 'initial_t_pc': ('TPc', 0.0023, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TPc`.'), 'initial_he_p': ('HeP', 0.0022, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HeP`.')}
    _HEADLINE_OUTPUTS = {'model_state_hc': ('Hc', 'native SBML value', 'Hc. Maps to SBML symbol `Hc`.'), 'model_state_pi': ('Pi', 'native SBML value', 'Pi. Maps to SBML symbol `Pi`.'), 'he_pc': ('HePc', 'native SBML value', 'HePc. Maps to SBML symbol `HePc`.'), 'pga': ('PGA', 'native SBML value', 'PGA. Maps to SBML symbol `PGA`.'), 't_pc': ('TPc', 'native SBML value', 'TPc. Maps to SBML symbol `TPc`.'), 'he_p': ('HeP', 'native SBML value', 'HeP. Maps to SBML symbol `HeP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000392.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
