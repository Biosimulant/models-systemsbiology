# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ibrahim2008_MCC_assembly_model_KDM."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ibrahim2008MccAssemblyModelKdmBiomd0000000193Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ibrahim2008_MCC_assembly_model_KDM."""

    _SBML_ID = 'BIOMD0000000193'
    _TITLE = 'Ibrahim2008_MCC_assembly_model_KDM'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mad1_CMad2', 'OMad2', 'Mad1_CMad2_OMad2', 'Cdc20', 'Cdc20_CMad2', 'Bub3_BubR1', 'MCC', 'Bub3_BubR1_Cdc20']
    _SPECIES_LABELS = {'Mad1_CMad2': 'Mad1:C-Mad2', 'OMad2': 'O-Mad2', 'Mad1_CMad2_OMad2': 'Mad1:C-Mad2:O-Mad2*', 'Cdc20': 'Cdc20', 'Cdc20_CMad2': 'Cdc20:C-Mad2', 'Bub3_BubR1': 'Bub3:BubR1', 'MCC': 'MCC', 'Bub3_BubR1_Cdc20': 'Bub3:BubR1:Cdc20'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_o_mad2': ('OMad2', 1.3e-07, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `OMad2`.'), 'initial_bub3_bub_r1': ('Bub3_BubR1', 1.3e-07, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bub3_BubR1`.'), 'initial_mad1_c_mad2': ('Mad1_CMad2', 5e-08, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mad1_CMad2`.'), 'initial_mad1_c_mad2_o_mad2': ('Mad1_CMad2_OMad2', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mad1_CMad2_OMad2`.'), 'initial_cdc20_c_mad2': ('Cdc20_CMad2', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdc20_CMad2`.'), 'initial_bub3_bub_r1_cdc20': ('Bub3_BubR1_Cdc20', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bub3_BubR1_Cdc20`.')}
    _HEADLINE_OUTPUTS = {'o_mad2': ('OMad2', 'mole', 'O-Mad2. Maps to SBML symbol `OMad2`.'), 'bub3_bub_r1': ('Bub3_BubR1', 'mole', 'Bub3:BubR1. Maps to SBML symbol `Bub3_BubR1`.'), 'mad1_c_mad2': ('Mad1_CMad2', 'mole', 'Mad1:C-Mad2. Maps to SBML symbol `Mad1_CMad2`.'), 'mad1_c_mad2_o_mad2': ('Mad1_CMad2_OMad2', 'mole', 'Mad1:C-Mad2:O-Mad2*. Maps to SBML symbol `Mad1_CMad2_OMad2`.'), 'cdc20_c_mad2': ('Cdc20_CMad2', 'mole', 'Cdc20:C-Mad2. Maps to SBML symbol `Cdc20_CMad2`.'), 'bub3_bub_r1_cdc20': ('Bub3_BubR1_Cdc20', 'mole', 'Bub3:BubR1:Cdc20. Maps to SBML symbol `Bub3_BubR1_Cdc20`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000193.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
