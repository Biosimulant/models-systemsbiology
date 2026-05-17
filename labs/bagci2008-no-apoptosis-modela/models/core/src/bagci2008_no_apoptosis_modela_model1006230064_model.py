# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bagci2008_NO_Apoptosis_modelA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bagci2008NoApoptosisModelaModel1006230064Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bagci2008_NO_Apoptosis_modelA."""

    _SBML_ID = 'MODEL1006230064'
    _TITLE = 'Bagci2008_NO_Apoptosis_modelA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['NO', 'CcOX', 'NO_2', 'O_2m', 'ONOO_m', 'GSH', 'GSNO', 'N2O3', 'FeLn']
    _SPECIES_LABELS = {'NO': 'NO', 'CcOX': 'CcOX', 'NO_2': 'NO 2', 'O_2m': 'O 2M', 'ONOO_m': 'ONOO M', 'GSH': 'GSH', 'GSNO': 'GSNO', 'N2O3': 'N2O3', 'FeLn': 'FeLn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_onoo_m': ('ONOO_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ONOO_m`.'), 'initial_o_2_m': ('O_2m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O_2m`.'), 'initial_no_2': ('NO_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NO_2`.'), 'initial_model_state_no': ('NO', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NO`.'), 'initial_n2_o3': ('N2O3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N2O3`.'), 'initial_gsno': ('GSNO', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GSNO`.')}
    _HEADLINE_OUTPUTS = {'onoo_m': ('ONOO_m', 'native SBML value', 'ONOO M. Maps to SBML symbol `ONOO_m`.'), 'o_2_m': ('O_2m', 'native SBML value', 'O 2M. Maps to SBML symbol `O_2m`.'), 'no_2': ('NO_2', 'native SBML value', 'NO 2. Maps to SBML symbol `NO_2`.'), 'model_state_no': ('NO', 'native SBML value', 'NO. Maps to SBML symbol `NO`.'), 'n2_o3': ('N2O3', 'native SBML value', 'N2O3. Maps to SBML symbol `N2O3`.'), 'gsno': ('GSNO', 'native SBML value', 'GSNO. Maps to SBML symbol `GSNO`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230064.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
