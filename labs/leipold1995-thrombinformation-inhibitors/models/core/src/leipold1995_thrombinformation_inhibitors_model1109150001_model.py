# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leipold1995_ThrombinFormation-inhibitors."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leipold1995ThrombinformationInhibitorsModel1109150001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leipold1995_ThrombinFormation-inhibitors."""

    _SBML_ID = 'MODEL1109150001'
    _TITLE = 'Leipold1995_ThrombinFormation-inhibitors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33']
    _SPECIES_LABELS = {'species_1': 'IX', 'species_2': 'TF_VIIa', 'species_3': 'TF_VIIa_IX', 'species_4': 'IXa', 'species_5': 'TF_VIIa_X', 'species_6': 'X', 'species_7': 'Xa', 'species_8': 'VIII', 'species_9': 'VIII_IXa', 'species_10': 'VIIIa(Xa)', 'species_11': 'VIIIa(Xa)_IXa', 'species_12': 'VIIIa(IIa)', 'species_13': 'VIIIa(IIa)_IXa', 'species_14': 'VIIIa(Xa)_IXa_X', 'species_15': 'VIIIa(IIa)_IXa_X', 'species_16': 'VIII*', 'species_17': 'VIIIa(Xa)*', 'species_18': 'VIIIa(IIa)*', 'species_19': 'V', 'species_20': 'Xa_V', 'species_21': 'Va', 'species_22': 'Xa_VIII', 'species_23': 'Va_Xa', 'species_24': 'II', 'species_25': 'Va_Xa_II', 'species_26': 'Va_Xa_mIIa', 'species_27': 'mIIa', 'species_28': 'IIa', 'species_29': 'mIIa_V', 'species_30': 'Va(IIa)', 'species_31': 'mIIa_VIII', 'species_32': 'IIa_V', 'species_33': 'IIa_VIII'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ii': ('species_24', 1400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_24`.'), 'initial_model_state_x': ('species_6', 170.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.'), 'initial_model_state_ix': ('species_1', 90.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_model_state_v': ('species_19', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`.'), 'initial_viii': ('species_8', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_tf_vi_ia': ('species_2', 0.0043, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.')}
    _HEADLINE_OUTPUTS = {'model_state_ii': ('species_24', 'native SBML value', 'II. Maps to SBML symbol `species_24`.'), 'model_state_x': ('species_6', 'native SBML value', 'X. Maps to SBML symbol `species_6`.'), 'model_state_ix': ('species_1', 'native SBML value', 'IX. Maps to SBML symbol `species_1`.'), 'model_state_v': ('species_19', 'native SBML value', 'V. Maps to SBML symbol `species_19`.'), 'viii': ('species_8', 'native SBML value', 'VIII. Maps to SBML symbol `species_8`.'), 'tf_vi_ia': ('species_2', 'native SBML value', 'TF_VIIa. Maps to SBML symbol `species_2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1109150001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
