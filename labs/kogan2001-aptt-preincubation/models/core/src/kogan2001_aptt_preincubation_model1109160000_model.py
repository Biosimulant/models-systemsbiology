# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kogan2001_aPTT_preincubation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kogan2001ApttPreincubationModel1109160000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kogan2001_aPTT_preincubation."""

    _SBML_ID = 'MODEL1109160000'
    _TITLE = 'Kogan2001_aPTT_preincubation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30']
    _SPECIES_LABELS = {'species_1': 'XII', 'species_2': 'XIIa', 'species_3': 'ATIII', 'species_4': 'alpha1AT', 'species_5': 'alpha2M', 'species_6': 'C1inh', 'species_7': 'XIa', 'species_8': 'XIa_C1inh', 'species_9': 'XIa_alpha1AT', 'species_10': 'XIa_alpha2AP', 'species_11': 'alpha2AP', 'species_12': 'PAI1', 'species_13': 'XIa_PAI1', 'species_14': 'XIa_ATIII', 'species_15': 'XIIa_C1inh', 'species_16': 'XIIa_alpha2AP', 'species_17': 'XIIa_alpha2M', 'species_18': 'XIIa_ATIII', 'species_19': 'XIIa_PAI1', 'species_20': 'XIIf', 'species_21': 'XIIf_C1inh', 'species_22': 'XIIf_alpha2AP', 'species_23': 'XIIf_ATIII', 'species_24': 'K', 'species_25': 'K_C1inh', 'species_26': 'K_alpha2M', 'species_27': 'K_PAI1', 'species_28': 'K_ATIII', 'species_29': 'PK', 'species_30': 'XI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha1_at': ('species_4', 24.4999988201872, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_alpha2_m': ('species_5', 3.49999983145531, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_5`.'), 'initial_atiii': ('species_3', 3.39999983627088, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_c1inh': ('species_6', 1.69999991813544, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.'), 'initial_alpha2_ap': ('species_11', 0.899999956659938, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_11`.'), 'initial_model_state_pk': ('species_29', 0.579999972069738, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_29`.')}
    _HEADLINE_OUTPUTS = {'alpha1_at': ('species_4', 'native SBML value', 'alpha1AT. Maps to SBML symbol `species_4`.'), 'alpha2_m': ('species_5', 'native SBML value', 'alpha2M. Maps to SBML symbol `species_5`.'), 'atiii': ('species_3', 'native SBML value', 'ATIII. Maps to SBML symbol `species_3`.'), 'c1inh': ('species_6', 'native SBML value', 'C1inh. Maps to SBML symbol `species_6`.'), 'alpha2_ap': ('species_11', 'native SBML value', 'alpha2AP. Maps to SBML symbol `species_11`.'), 'model_state_pk': ('species_29', 'native SBML value', 'PK. Maps to SBML symbol `species_29`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1109160000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
