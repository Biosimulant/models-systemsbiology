# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sorokina2011_StarchMetabolism_Ostreococcus."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sorokina2011StarchmetabolismOstreococcusModel1204240000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sorokina2011_StarchMetabolism_Ostreococcus."""

    _SBML_ID = 'MODEL1204240000'
    _TITLE = 'Sorokina2011_StarchMetabolism_Ostreococcus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33', 'species_34', 'species_35', 'species_37', 'species_39', 'species_40']
    _SPECIES_LABELS = {'species_1': 'CO2', 'species_2': 'GAP', 'species_3': 'NADPH', 'species_4': 'NADP', 'species_5': 'ADP', 'species_6': 'ATP', 'species_7': 'P', 'species_8': 'GP', 'species_9': 'F16BP', 'species_10': 'F6P', 'species_11': 'G6P', 'species_12': 'G1P', 'species_13': 'PPi', 'species_14': 'ADPG', 'species_15': '20LG', 'species_16': 'maltotriose', 'species_17': '40LG', 'species_18': '40BG', 'species_19': '60BG', 'species_20': '60LG', 'species_21': '80LG', 'species_22': '80BG', 'species_23': '100LG', 'species_24': '100BG', 'species_25': '120BG', 'species_26': '100LG_s', 'species_27': '100LG_g', 'species_28': '100BG_s', 'species_29': '100BG_g', 'species_30': '120BG_s', 'species_31': '120BG_g', 'species_32': '100LG-s', 'species_33': '100LG_s_P', 'species_34': '100BG_s_P', 'species_35': '120BG_s_P', 'species_37': 'maltose', 'species_39': 'glu', 'species_40': '20ADPG'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_maltotriose': ('species_16', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_16`.'), 'initial_maltose': ('species_37', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_37`.'), 'initial_model_state_glu': ('species_39', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_39`.'), 'initial_p_pi': ('species_13', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`.'), 'initial_model_state_p': ('species_7', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_nadph': ('species_3', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.')}
    _HEADLINE_OUTPUTS = {'maltotriose': ('species_16', 'native SBML value', 'maltotriose. Maps to SBML symbol `species_16`.'), 'maltose': ('species_37', 'native SBML value', 'maltose. Maps to SBML symbol `species_37`.'), 'glu': ('species_39', 'native SBML value', 'glu. Maps to SBML symbol `species_39`.'), 'p_pi': ('species_13', 'native SBML value', 'PPi. Maps to SBML symbol `species_13`.'), 'model_state_p': ('species_7', 'native SBML value', 'P. Maps to SBML symbol `species_7`.'), 'nadph': ('species_3', 'native SBML value', 'NADPH. Maps to SBML symbol `species_3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1204240000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
