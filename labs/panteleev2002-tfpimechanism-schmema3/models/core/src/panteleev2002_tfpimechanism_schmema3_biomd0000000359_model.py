# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Panteleev2002_TFPImechanism_schmema3."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Panteleev2002TfpimechanismSchmema3Biomd0000000359Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Panteleev2002_TFPImechanism_schmema3."""

    _SBML_ID = 'BIOMD0000000359'
    _TITLE = 'Panteleev2002_TFPImechanism_schmema3'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VIIa_TF', 'X', 'VIIa_TF_X', 'VIIa_TF_Xa', 'Xa', 'TFPI', 'Xa_TFPI', 'Xa_TFPI_VIIa_TF', 'VIIa_TF_Xa_TFPI']
    _SPECIES_LABELS = {'VIIa_TF': 'VIIa_TF', 'X': 'X', 'VIIa_TF_X': 'VIIa_TF_X', 'VIIa_TF_Xa': 'VIIa_TF_Xa', 'Xa': 'Xa', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa_TFPI', 'Xa_TFPI_VIIa_TF': 'Xa_TFPI_VIIa_TF', 'VIIa_TF_Xa_TFPI': 'VIIa_TF_Xa_TFPI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vi_ia_tf': ('VIIa_TF', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_TF`.'), 'initial_xa_tfpi_vi_ia_tf': ('Xa_TFPI_VIIa_TF', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI_VIIa_TF`.'), 'initial_xa_tfpi': ('Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`.'), 'initial_vi_ia_tf_xa_tfpi': ('VIIa_TF_Xa_TFPI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_TF_Xa_TFPI`.'), 'initial_vi_ia_tf_xa': ('VIIa_TF_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_TF_Xa`.'), 'initial_vi_ia_tf_x': ('VIIa_TF_X', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa_TF_X`.')}
    _HEADLINE_OUTPUTS = {'vi_ia_tf': ('VIIa_TF', 'native SBML value', 'VIIa_TF. Maps to SBML symbol `VIIa_TF`.'), 'xa_tfpi_vi_ia_tf': ('Xa_TFPI_VIIa_TF', 'native SBML value', 'Xa_TFPI_VIIa_TF. Maps to SBML symbol `Xa_TFPI_VIIa_TF`.'), 'xa_tfpi': ('Xa_TFPI', 'native SBML value', 'Xa_TFPI. Maps to SBML symbol `Xa_TFPI`.'), 'vi_ia_tf_xa_tfpi': ('VIIa_TF_Xa_TFPI', 'native SBML value', 'VIIa_TF_Xa_TFPI. Maps to SBML symbol `VIIa_TF_Xa_TFPI`.'), 'vi_ia_tf_xa': ('VIIa_TF_Xa', 'native SBML value', 'VIIa_TF_Xa. Maps to SBML symbol `VIIa_TF_Xa`.'), 'vi_ia_tf_x': ('VIIa_TF_X', 'native SBML value', 'VIIa_TF_X. Maps to SBML symbol `VIIa_TF_X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000359.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
