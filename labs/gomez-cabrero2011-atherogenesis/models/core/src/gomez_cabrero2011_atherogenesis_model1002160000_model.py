# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Gomez-Cabrero2011_Atherogenesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GomezCabrero2011AtherogenesisModel1002160000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Gomez-Cabrero2011_Atherogenesis."""

    _SBML_ID = 'MODEL1002160000'
    _TITLE = 'Gomez-Cabrero2011_Atherogenesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19']
    _SPECIES_LABELS = {'species_1': 'LDL', 'species_2': 'oxLDL', 'species_3': 'HDL', 'species_4': 'MP', 'species_5': 'PLAQUE', 'species_6': 'TINF', 'species_7': 'TAINF', 'species_8': 'Bcells', 'species_9': 'ACT_END', 'species_10': 'SUMoxidLDL', 'species_11': 'SUMForFoam', 'species_12': 'SUMRecTINF', 'species_13': 'SUMRecTAINF', 'species_14': 'SUMRecBcells', 'species_15': 'HDL_blood', 'species_16': 'LDL_blood', 'species_17': 'SUMACT_END', 'species_18': 'SIGMOID_ACTENDstim', 'species_19': 'SIGMOID_ACTENDinh'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_sum_rec_bcells': ('species_14', 2.67523886569906e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.'), 'initial_bcells': ('species_8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_ldl_blood': ('species_16', 2.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_16`.'), 'initial_hdl_blood': ('species_15', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_15`.'), 'initial_sigmoid_acten_dinh': ('species_19', 0.000423556497672639, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`.'), 'initial_sigmoid_acten_dstim': ('species_18', 7.69164659200097e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_18`.')}
    _HEADLINE_OUTPUTS = {'sum_rec_bcells': ('species_14', 'native SBML value', 'SUMRecBcells. Maps to SBML symbol `species_14`.'), 'bcells': ('species_8', 'native SBML value', 'Bcells. Maps to SBML symbol `species_8`.'), 'ldl_blood': ('species_16', 'native SBML value', 'LDL_blood. Maps to SBML symbol `species_16`.'), 'hdl_blood': ('species_15', 'native SBML value', 'HDL_blood. Maps to SBML symbol `species_15`.'), 'sigmoid_acten_dinh': ('species_19', 'native SBML value', 'SIGMOID_ACTENDinh. Maps to SBML symbol `species_19`.'), 'sigmoid_acten_dstim': ('species_18', 'native SBML value', 'SIGMOID_ACTENDstim. Maps to SBML symbol `species_18`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1002160000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
