# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Shibeko2012 - Model of IIa generation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shibeko2012ModelOfIiaGenerationModel1808150001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Shibeko2012 - Model of IIa generation."""

    _SBML_ID = 'MODEL1808150001'
    _TITLE = 'Shibeko2012 - Model of IIa generation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VII', 'VIIa', 'X', 'Xa', 'ATIII', 'VII_TF', 'VIIa_TF', 'TF', 'TFPI', 'Xa_TFPI', 'VIIa_TF_Xa_TFPI', 'VIIa_i_TF_Xa_TFPI', 'VIIa_i', 'VIIa_i_TF', 'V', 'Va', 'Xa_Va', 'II', 'IIa', 'PL']
    _SPECIES_LABELS = {'VII': 'VII', 'VIIa': 'VIIa', 'X': 'X', 'Xa': 'Xa', 'ATIII': 'ATIII', 'VII_TF': 'VII:TF', 'VIIa_TF': 'VIIa:TF', 'TF': 'TF', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa:TFPI', 'VIIa_TF_Xa_TFPI': 'VIIa:TF:Xa:TFPI', 'VIIa_i_TF_Xa_TFPI': 'VIIa_i:TF:Xa:TFPI', 'VIIa_i': 'VIIa_i', 'VIIa_i_TF': 'VIIa_i:TF', 'V': 'V', 'Va': 'Va', 'Xa_Va': 'Xa:Va', 'II': 'II', 'IIa': 'IIa', 'PL': 'PL'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_xa_va': ('Xa_Va', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_vi_ia_i_tf_xa_tfpi': ('VIIa_i_TF_Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_i_TF_Xa_TFPI`.'), 'initial_vi_ia_i_tf': ('VIIa_i_TF', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_i_TF`.'), 'initial_vi_ia_i': ('VIIa_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_i`.'), 'initial_vi_ia_tf_xa_tfpi': ('VIIa_TF_Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_TF_Xa_TFPI`.')}
    _HEADLINE_OUTPUTS = {'xa_va': ('Xa_Va', 'native SBML value', 'Xa:Va. Maps to SBML symbol `Xa_Va`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa:TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'vi_ia_i_tf_xa_tfpi': ('VIIa_i_TF_Xa_TFPI', 'native SBML value', 'VIIa_i:TF:Xa:TFPI. Maps to SBML symbol `VIIa_i_TF_Xa_TFPI`.'), 'vi_ia_i_tf': ('VIIa_i_TF', 'native SBML value', 'VIIa_i:TF. Maps to SBML symbol `VIIa_i_TF`.'), 'vi_ia_i': ('VIIa_i', 'native SBML value', 'VIIa_i. Maps to SBML symbol `VIIa_i`.'), 'vi_ia_tf_xa_tfpi': ('VIIa_TF_Xa_TFPI', 'native SBML value', 'VIIa:TF:Xa:TFPI. Maps to SBML symbol `VIIa_TF_Xa_TFPI`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808150001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
