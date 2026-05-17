# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Haut1974_Pentose_Cycle_Rat."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Haut1974PentoseCycleRatModel1004070000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Haut1974_Pentose_Cycle_Rat."""

    _SBML_ID = 'MODEL1004070000'
    _TITLE = 'Haut1974_Pentose_Cycle_Rat'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['glucose_inside_cell', 'glucose_outside_cell', 'lactose', 'glucose_hexokinase', 'hexokinase', 'glucose_6_phosphate', 'hexokinase_inhibited', 'fructose_6_phosphate', 'fructose_16_diphosphate', 'dihydroxyacetone_3_phosphate', 'glyceraldehyde_3_phosphate', 'glycerol', 'pyruvate', '_6_phosphogluconolactone', 'NADP', 'NADPH', '_6_phosphogluconate', 'CO2A', 'ribulose_5_phosphate', 'ribose_5_phosphate', 'xylulose_5_phosphate', 'sedoheptulose_7_phosphate', 'erythrose_4_phosphate', 'lactate', 'acetyl_CoA', 'CO2B', 'CIT0C', 'CO2C', 'CO2D', 'fatty_acids', 'CIT2C', 'CIT1C']
    _SPECIES_LABELS = {'glucose_inside_cell': 'glucose (inside cell)', 'glucose_outside_cell': 'glucose (outside cell)', 'lactose': 'lactose', 'glucose_hexokinase': 'glucose-hexokinase', 'hexokinase': 'hexokinase', 'glucose_6_phosphate': 'glucose 6-phosphate', 'hexokinase_inhibited': 'hexokinase (inhibited)', 'fructose_6_phosphate': 'fructose 6-phosphate', 'fructose_16_diphosphate': 'fructose 1,6 diphosphate', 'dihydroxyacetone_3_phosphate': 'dihydroxyacetone 3-phosphate', 'glyceraldehyde_3_phosphate': 'glyceraldehyde 3-phosphate', 'glycerol': 'glycerol', 'pyruvate': 'pyruvate', '_6_phosphogluconolactone': '6-phosphogluconolactone', 'NADP': 'NADP+', 'NADPH': 'NADPH', '_6_phosphogluconate': '6-phosphogluconate', 'CO2A': 'CO2A', 'ribulose_5_phosphate': 'ribulose 5-phosphate', 'ribose_5_phosphate': 'ribose 5-phosphate', 'xylulose_5_phosphate': 'xylulose 5-phosphate', 'sedoheptulose_7_phosphate': 'sedoheptulose 7-phosphate', 'erythrose_4_phosphate': 'erythrose 4-phosphate', 'lactate': 'lactate', 'acetyl_CoA': 'acetyl-CoA', 'CO2B': 'CO2B', 'CIT0C': 'CIT0C: all C4 compounds in the tricarboxylic acid cycle', 'CO2C': 'CO2C', 'CO2D': 'CO2D', 'fatty_acids': 'fatty acids', 'CIT2C': 'CIT2C: all C6 compounds in the tricarboxylic acid cycle', 'CIT1C': 'CIT1C: alpha-oxoglutarate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_outside_cell': ('glucose_outside_cell', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glucose_outside_cell`.'), 'initial_glucose_6_phosphate': ('glucose_6_phosphate', 0.058, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glucose_6_phosphate`.'), 'initial_nadp': ('NADP', 0.019, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`.'), 'initial_glucose_hexokinase': ('glucose_hexokinase', 1e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glucose_hexokinase`.'), 'initial_glucose_inside_cell': ('glucose_inside_cell', 1e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glucose_inside_cell`.'), 'initial_nadph': ('NADPH', 3.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`.')}
    _HEADLINE_OUTPUTS = {'glucose_outside_cell': ('glucose_outside_cell', 'native SBML value', 'glucose (outside cell). Maps to SBML symbol `glucose_outside_cell`.'), 'glucose_6_phosphate': ('glucose_6_phosphate', 'native SBML value', 'glucose 6-phosphate. Maps to SBML symbol `glucose_6_phosphate`.'), 'nadp': ('NADP', 'native SBML value', 'NADP+. Maps to SBML symbol `NADP`.'), 'glucose_hexokinase': ('glucose_hexokinase', 'native SBML value', 'glucose-hexokinase. Maps to SBML symbol `glucose_hexokinase`.'), 'glucose_inside_cell': ('glucose_inside_cell', 'native SBML value', 'glucose (inside cell). Maps to SBML symbol `glucose_inside_cell`.'), 'nadph': ('NADPH', 'native SBML value', 'NADPH. Maps to SBML symbol `NADPH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1004070000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
