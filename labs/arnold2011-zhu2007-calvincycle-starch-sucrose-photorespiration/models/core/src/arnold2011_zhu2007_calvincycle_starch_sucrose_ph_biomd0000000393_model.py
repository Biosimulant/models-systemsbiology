# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Zhu2007_CalvinCycle_Starch_Sucrose_Photorespiration."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Zhu2007CalvincycleStarchSucrosePhBiomd0000000393Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Zhu2007_CalvinCycle_Starch_Sucrose_Photorespiration."""

    _SBML_ID = 'BIOMD0000000393'
    _TITLE = 'Arnold2011_Zhu2007_CalvinCycle_Starch_Sucrose_Photorespiration'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PGA', 'DPGA', 'GAP', 'DHAP', 'TP', 'FBP', 'F6P', 'G6P', 'G1P', 'HeP', 'E4P', 'SBP', 'S7P', 'X5P', 'R5P', 'Ru5P', 'PeP', 'RuBP', 'ATP', 'ADP', 'NADPH', 'Pi', 'PGCA', 'GCA', 'GCEA', 'CO2', 'O2', 'NADP', 'HPRc', 'GCAc', 'GOAc', 'GLYc', 'SERc', 'GCEAc', 'PGAc', 'GAPc', 'DHAPc', 'TPc', 'FBPc', 'F6Pc', 'G6Pc', 'G1Pc', 'HePc', 'F26BPc', 'UDPGc', 'SucPc', 'Succ', 'UTPc', 'UDPc', 'NAD', 'NADH', 'GLUc', 'KGc', 'Pic', 'PiTc', 'ATPc', 'ADPc', 'PiPic']
    _SPECIES_LABELS = {'PGA': 'PGA', 'DPGA': 'DPGA', 'GAP': 'GAP', 'DHAP': 'DHAP', 'TP': 'TP', 'FBP': 'FBP', 'F6P': 'F6P', 'G6P': 'G6P', 'G1P': 'G1P', 'HeP': 'HeP', 'E4P': 'E4P', 'SBP': 'SBP', 'S7P': 'S7P', 'X5P': 'X5P', 'R5P': 'R5P', 'Ru5P': 'Ru5P', 'PeP': 'PeP', 'RuBP': 'RuBP', 'ATP': 'ATP', 'ADP': 'ADP', 'NADPH': 'NADPH', 'Pi': 'Pi', 'PGCA': 'PGCA', 'GCA': 'GCA', 'GCEA': 'GCEA', 'CO2': 'CO2', 'O2': 'O2', 'NADP': 'NADP', 'HPRc': 'HPRc', 'GCAc': 'GCAc', 'GOAc': 'GOAc', 'GLYc': 'GLYc', 'SERc': 'SERc', 'GCEAc': 'GCEAc', 'PGAc': 'PGAc', 'GAPc': 'GAPc', 'DHAPc': 'DHAPc', 'TPc': 'TPc', 'FBPc': 'FBPc', 'F6Pc': 'F6Pc', 'G6Pc': 'G6Pc', 'G1Pc': 'G1Pc', 'HePc': 'HePc', 'F26BPc': 'F26BPc', 'UDPGc': 'UDPGc', 'SucPc': 'SucPc', 'Succ': 'Succ', 'UTPc': 'UTPc', 'UDPc': 'UDPc', 'NAD': 'NAD', 'NADH': 'NADH', 'GLUc': 'GLUc', 'KGc': 'KGc', 'Pic': 'Pic', 'PiTc': 'PiTc', 'ATPc': 'ATPc', 'ADPc': 'ADPc', 'PiPic': 'PiPic'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_gl_uc': ('GLUc', 24.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GLUc`.'), 'initial_se_rc': ('SERc', 7.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SERc`.'), 'initial_he_pc': ('HePc', 5.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HePc`.'), 'initial_pi_tc': ('PiTc', 4.0999844, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PiTc`.'), 'initial_model_state_pic': ('Pic', 4.09998299977232, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pic`.'), 'initial_g6_pc': ('G6Pc', 3.88432062242307, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6Pc`.')}
    _HEADLINE_OUTPUTS = {'gl_uc': ('GLUc', 'native SBML value', 'GLUc. Maps to SBML symbol `GLUc`.'), 'se_rc': ('SERc', 'native SBML value', 'SERc. Maps to SBML symbol `SERc`.'), 'he_pc': ('HePc', 'native SBML value', 'HePc. Maps to SBML symbol `HePc`.'), 'pi_tc': ('PiTc', 'native SBML value', 'PiTc. Maps to SBML symbol `PiTc`.'), 'pic': ('Pic', 'native SBML value', 'Pic. Maps to SBML symbol `Pic`.'), 'g6_pc': ('G6Pc', 'native SBML value', 'G6Pc. Maps to SBML symbol `G6Pc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000393.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
