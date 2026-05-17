# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Martins2004_Yeast_Glycolysis_GlycerolSynthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Martins2004YeastGlycolysisGlycerolsynthesisModel1009220000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Martins2004_Yeast_Glycolysis_GlycerolSynthesis."""

    _SBML_ID = 'MODEL1009220000'
    _TITLE = 'Martins2004_Yeast_Glycolysis_GlycerolSynthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLCx', 'GLC', 'ATP', 'G6P', 'ADP', 'F6P', 'F16bP', 'AMP', 'F26bP', 'DHAP', 'GAP', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AcAld', 'CO2', 'EtOH', 'GLY', 'glycogen', 'trehalose', 'succinate', 'G3P', 'iP', 'GLYx']
    _SPECIES_LABELS = {'GLCx': 'glucose', 'GLC': 'glucose', 'ATP': 'ATP', 'G6P': 'glucose 6-phosphate', 'ADP': 'ADP', 'F6P': 'fructose 6-phosphate', 'F16bP': 'fructose 1,6-bisphosphate', 'AMP': 'AMP', 'F26bP': 'fructose 2,6-bisphosphate', 'DHAP': 'dihydroxyacetone phosphate', 'GAP': 'glyceraldehyde 3-phosphate', 'NAD': 'NAD', 'BPG': '1,3-bisphosphoglycerate', 'NADH': 'NADH', 'P3G': '3-phosphoglycerate', 'P2G': '2-phosphoglycerate', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'AcAld': 'acetaldehyde', 'CO2': 'CO2', 'EtOH': 'ethanol', 'GLY': 'glycerol', 'glycogen': 'glycogen', 'trehalose': 'trehalose', 'succinate': 'succinate', 'G3P': 'glycerol 3-phosphate', 'iP': 'phosphate', 'GLYx': 'glycerol'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('GLCx', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GLCx`.'), 'initial_ethanol': ('EtOH', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EtOH`.'), 'initial_glycerol': ('GLY', 20.45195687551, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GLY`.'), 'initial_fructose_1_6_bisphosphate': ('F16bP', 20.1291037756343, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `F16bP`.'), 'initial_glucose_6_phosphate': ('G6P', 3.26087372504791, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6P`.'), 'initial_dihydroxyacetone_phosphate': ('DHAP', 2.5253634682754, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DHAP`.')}
    _HEADLINE_OUTPUTS = {'glucose': ('GLCx', 'native SBML value', 'glucose. Maps to SBML symbol `GLCx`.'), 'ethanol': ('EtOH', 'native SBML value', 'ethanol. Maps to SBML symbol `EtOH`.'), 'glycerol': ('GLY', 'native SBML value', 'glycerol. Maps to SBML symbol `GLY`.'), 'fructose_1_6_bisphosphate': ('F16bP', 'native SBML value', 'fructose 1,6-bisphosphate. Maps to SBML symbol `F16bP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'glucose 6-phosphate. Maps to SBML symbol `G6P`.'), 'dihydroxyacetone_phosphate': ('DHAP', 'native SBML value', 'dihydroxyacetone phosphate. Maps to SBML symbol `DHAP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1009220000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
