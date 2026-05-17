# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kogan2001_aPTT_coagulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kogan2001ApttCoagulationModel1109160001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kogan2001_aPTT_coagulation."""

    _SBML_ID = 'MODEL1109160001'
    _TITLE = 'Kogan2001_aPTT_coagulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33', 'species_34', 'species_35', 'species_36', 'species_37', 'species_38', 'species_39', 'species_40']
    _SPECIES_LABELS = {'species_1': 'XIIa', 'species_2': 'Va', 'species_3': 'Va_Xa', 'species_4': 'Xa', 'species_5': 'IXa', 'species_6': 'VIIIa', 'species_7': 'VIIIa_IXa', 'species_8': 'ATIII', 'species_9': 'IIa', 'species_10': 'IIa_ATIII', 'species_11': 'IIa_alpha1AT', 'species_12': 'alpha1AT', 'species_13': 'IIa_alpha2M', 'species_14': 'alpha2M', 'species_15': 'Xa_ATIII', 'species_16': 'Xa_alpha1AT', 'species_17': 'TFPI', 'species_18': 'Xa_TFPI', 'species_19': 'IXa_ATIII', 'species_20': 'C1inh', 'species_21': 'XIa', 'species_22': 'XIa_C1inh', 'species_23': 'XIa_alpha1AT', 'species_24': 'XIa_alpha2AP', 'species_25': 'alpha2AP', 'species_26': 'PAI1', 'species_27': 'XIa_PAI1', 'species_28': 'XIa_ATIII', 'species_29': 'XI', 'species_30': 'IX', 'species_31': 'X', 'species_32': 'II', 'species_33': 'V', 'species_34': 'VIII', 'species_35': 'I', 'species_36': 'Ia', 'species_37': 'Xa_Va', 'species_38': 'Va_Xa_ATIII', 'species_39': 'Va_Xa_alpha1AT', 'species_40': 'IXa_VIIIa_ATIII'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha1_at': ('species_12', 24.4999988201872, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`.'), 'initial_model_state_i': ('species_35', 8.29999960030832, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_35`.'), 'initial_atiii': ('species_8', 3.39999983627088, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_alpha2_m': ('species_14', 3.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.'), 'initial_model_state_ii': ('species_32', 1.39999993258213, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_32`.'), 'initial_c1inh': ('species_20', 1.27, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`.')}
    _HEADLINE_OUTPUTS = {'alpha1_at': ('species_12', 'native SBML value', 'alpha1AT. Maps to SBML symbol `species_12`.'), 'model_state_i': ('species_35', 'native SBML value', 'I. Maps to SBML symbol `species_35`.'), 'atiii': ('species_8', 'native SBML value', 'ATIII. Maps to SBML symbol `species_8`.'), 'alpha2_m': ('species_14', 'native SBML value', 'alpha2M. Maps to SBML symbol `species_14`.'), 'model_state_ii': ('species_32', 'native SBML value', 'II. Maps to SBML symbol `species_32`.'), 'c1inh': ('species_20', 'native SBML value', 'C1inh. Maps to SBML symbol `species_20`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1109160001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
