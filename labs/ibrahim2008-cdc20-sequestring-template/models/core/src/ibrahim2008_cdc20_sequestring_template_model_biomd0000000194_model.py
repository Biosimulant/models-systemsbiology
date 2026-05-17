# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ibrahim2008_Cdc20_Sequestring_Template_Model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ibrahim2008Cdc20SequestringTemplateModelBiomd0000000194Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ibrahim2008_Cdc20_Sequestring_Template_Model."""

    _SBML_ID = 'BIOMD0000000194'
    _TITLE = 'Ibrahim2008_Cdc20_Sequestring_Template_Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mad1_CMad2', 'OMad2', 'Mad1_CMad2_OMad2', 'Cdc20', 'Cdc20_CMad2']
    _SPECIES_LABELS = {'Mad1_CMad2': 'Mad1:C-Mad2', 'OMad2': 'O-Mad2', 'Mad1_CMad2_OMad2': 'Mad1:C-Mad2:O-Mad2*', 'Cdc20': 'Cdc20', 'Cdc20_CMad2': 'Cdc20:C-Mad2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_o_mad2': ('OMad2', 1.5e-07, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `OMad2`.'), 'initial_mad1_c_mad2': ('Mad1_CMad2', 5e-08, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mad1_CMad2`.'), 'initial_mad1_c_mad2_o_mad2': ('Mad1_CMad2_OMad2', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mad1_CMad2_OMad2`.'), 'initial_cdc20_c_mad2': ('Cdc20_CMad2', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdc20_CMad2`.'), 'initial_cdc20': ('Cdc20', 2.2e-07, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdc20`.')}
    _HEADLINE_OUTPUTS = {'o_mad2': ('OMad2', 'mole', 'O-Mad2. Maps to SBML symbol `OMad2`.'), 'mad1_c_mad2': ('Mad1_CMad2', 'mole', 'Mad1:C-Mad2. Maps to SBML symbol `Mad1_CMad2`.'), 'mad1_c_mad2_o_mad2': ('Mad1_CMad2_OMad2', 'mole', 'Mad1:C-Mad2:O-Mad2*. Maps to SBML symbol `Mad1_CMad2_OMad2`.'), 'cdc20_c_mad2': ('Cdc20_CMad2', 'mole', 'Cdc20:C-Mad2. Maps to SBML symbol `Cdc20_CMad2`.'), 'cdc20': ('Cdc20', 'mole', 'Cdc20. Maps to SBML symbol `Cdc20`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000194.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
