# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Westermark2003_Pancreatic_GlycOsc_extended."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Westermark2003PancreaticGlycoscExtendedBiomd0000000236Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Westermark2003_Pancreatic_GlycOsc_extended."""

    _SBML_ID = 'BIOMD0000000236'
    _TITLE = 'Westermark2003_Pancreatic_GlycOsc_extended'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLC', 'G6P_F6P', 'F6P', 'FBP', 'G3P', 'DHAP', 'DHAP_G3P']
    _SPECIES_LABELS = {'GLC': 'intracellular glucose', 'G6P_F6P': 'G6P_F6P', 'F6P': 'fructose-6-phosphate', 'FBP': 'fructose-1,6-biphosphate', 'G3P': 'glyceraldehyde--phosphate', 'DHAP': 'dihydroxyacetone-phosphate', 'DHAP_G3P': 'DHAP-G3P pool'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_glucose': ('GLC', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GLC`.'), 'initial_g6_p_f6_p': ('G6P_F6P', 3.71728, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6P_F6P`.'), 'initial_dhap_g3_p_pool': ('DHAP_G3P', 0.00262966, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DHAP_G3P`.'), 'initial_fructose_1_6_biphosphate': ('FBP', 0.00063612, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FBP`.'), 'initial_glyceraldehyde_phosphate': ('G3P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3P`.'), 'initial_fructose_6_phosphate': ('F6P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `F6P`.')}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('GLC', 'native SBML value', 'intracellular glucose. Maps to SBML symbol `GLC`.'), 'g6_p_f6_p': ('G6P_F6P', 'native SBML value', 'G6P_F6P. Maps to SBML symbol `G6P_F6P`.'), 'dhap_g3_p_pool': ('DHAP_G3P', 'native SBML value', 'DHAP-G3P pool. Maps to SBML symbol `DHAP_G3P`.'), 'fructose_1_6_biphosphate': ('FBP', 'native SBML value', 'fructose-1,6-biphosphate. Maps to SBML symbol `FBP`.'), 'glyceraldehyde_phosphate': ('G3P', 'native SBML value', 'glyceraldehyde--phosphate. Maps to SBML symbol `G3P`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'fructose-6-phosphate. Maps to SBML symbol `F6P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000236.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
