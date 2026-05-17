# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Legewie2006_apoptosis_NC."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Legewie2006ApoptosisNcBiomd0000000103Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Legewie2006_apoptosis_NC."""

    _SBML_ID = 'BIOMD0000000103'
    _TITLE = 'Legewie2006_apoptosis_NC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'C9', 'C9X', 'X', 'AC9X', 'AC9', 'C3', 'C3_star', 'C3_starX', 'C9_starX', 'C9_star', 'AC9_star', 'AC9_starX', 'C9X_C3_star', 'AC9X_C3_star', 'C9_starX_C3_star', 'AC9_starX_C3_star']
    _SPECIES_LABELS = {'A': 'APAF-1', 'C9': 'Caspase 9', 'C9X': 'Caspase 9-XIAP complex', 'X': 'XIAP', 'AC9X': 'APAF-1-Caspase 9-XIAP complex', 'AC9': 'APAF-1-Caspase 9 complex', 'C3': 'Caspase 3', 'C3_star': 'Caspase 3 cleaved', 'C3_starX': 'Caspase 3 cleaved - XIAP complex', 'C9_starX': 'Caspase 9 cleaved-XIAP complex', 'C9_star': 'Caspase 9 cleaved', 'AC9_star': 'APAF-1-Caspase 9 cleaved complex', 'AC9_starX': 'Apaf-1-Caspase 9 cleaved -XIAP complex', 'C9X_C3_star': 'Apaf-1-Caspase 9 cleaved -XIAP complex', 'AC9X_C3_star': 'Apaf-1-Caspase 9 cleaved -XIAP complex', 'C9_starX_C3_star': 'Apaf-1-Caspase 9 cleaved -XIAP complex', 'AC9_starX_C3_star': 'Apaf-1-Caspase 9 cleaved -XIAP complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_caspase_3': ('C3', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C3`.'), 'initial_caspase_9': ('C9', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C9`.'), 'initial_caspase_9_xiap_complex': ('C9X', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C9X`.'), 'initial_caspase_9_cleaved_xiap_complex': ('C9_starX', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C9_starX`.'), 'initial_caspase_9_cleaved': ('C9_star', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C9_star`.'), 'initial_caspase_3_cleaved_xiap_complex': ('C3_starX', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C3_starX`.')}
    _HEADLINE_OUTPUTS = {'caspase_3': ('C3', 'native SBML value', 'Caspase 3. Maps to SBML symbol `C3`.'), 'caspase_9': ('C9', 'native SBML value', 'Caspase 9. Maps to SBML symbol `C9`.'), 'caspase_9_xiap_complex': ('C9X', 'native SBML value', 'Caspase 9-XIAP complex. Maps to SBML symbol `C9X`.'), 'caspase_9_cleaved_xiap_complex': ('C9_starX', 'native SBML value', 'Caspase 9 cleaved-XIAP complex. Maps to SBML symbol `C9_starX`.'), 'caspase_9_cleaved': ('C9_star', 'native SBML value', 'Caspase 9 cleaved. Maps to SBML symbol `C9_star`.'), 'caspase_3_cleaved_xiap_complex': ('C3_starX', 'native SBML value', 'Caspase 3 cleaved - XIAP complex. Maps to SBML symbol `C3_starX`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000103.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
