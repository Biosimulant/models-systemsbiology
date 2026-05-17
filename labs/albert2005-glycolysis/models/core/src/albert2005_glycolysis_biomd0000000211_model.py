# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Albert2005_Glycolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Albert2005GlycolysisBiomd0000000211Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Albert2005_Glycolysis."""

    _SBML_ID = 'BIOMD0000000211'
    _TITLE = 'Albert2005_Glycolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27']
    _SPECIES_LABELS = {'species_1': 'pyruvate', 'species_2': 'adpc', 'species_3': 'atpc', 'species_4': 'phosphoenolpyruvate', 'species_5': '2phosphoglycerate', 'species_6': 'ampc', 'species_7': '3phosphoglycerate cytosol', 'species_8': 'dihydroxyacetonephosphate cytosol', 'species_9': 'glycerol3phosphate cytosol', 'species_10': 'glucose', 'species_11': 'atpg', 'species_12': 'adpg', 'species_13': 'ampg', 'species_14': 'glucose6phosphate', 'species_15': 'fructose6phosphate', 'species_16': 'fructose16bisphosphate', 'species_17': 'dihydroxyacetonephosphate', 'species_18': 'glyceraldehyde3phosphate', 'species_19': 'nad', 'species_20': 'nadh', 'species_21': 'bisphosphoglycerate', 'species_22': 'glycerol3phosphate', 'species_23': '3phosphoglycerate', 'species_24': 'glycerol', 'species_25': 'glucose external', 'species_26': 'pyruvate external', 'species_27': 'glycerol external'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_external': ('species_25', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_25`.'), 'initial_pyruvate_external': ('species_26', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_26`.'), 'initial_glycerol_external': ('species_27', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_27`.'), 'initial_glycerol3phosphate': ('species_22', 10.5208853981, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_22`.'), 'initial_pyruvate': ('species_1', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_fructose16bisphosphate': ('species_16', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_16`.')}
    _HEADLINE_OUTPUTS = {'glucose_external': ('species_25', 'native SBML value', 'glucose external. Maps to SBML symbol `species_25`.'), 'pyruvate_external': ('species_26', 'native SBML value', 'pyruvate external. Maps to SBML symbol `species_26`.'), 'glycerol_external': ('species_27', 'native SBML value', 'glycerol external. Maps to SBML symbol `species_27`.'), 'glycerol3phosphate': ('species_22', 'native SBML value', 'glycerol3phosphate. Maps to SBML symbol `species_22`.'), 'pyruvate': ('species_1', 'native SBML value', 'pyruvate. Maps to SBML symbol `species_1`.'), 'fructose16bisphosphate': ('species_16', 'native SBML value', 'fructose16bisphosphate. Maps to SBML symbol `species_16`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000211.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
