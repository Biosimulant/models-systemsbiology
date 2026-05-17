# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Clarke2006_Smad_signalling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Clarke2006SmadSignallingBiomd0000000112Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Clarke2006_Smad_signalling."""

    _SBML_ID = 'BIOMD0000000112'
    _TITLE = 'Clarke2006_Smad_signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['receptor', 'R_smad_cyt', 'R_smad_P_cyt', 'smad4_cyt', 'R_smad_P_smad4_cyt', 'R_smad_P_smad4_nuc', 'R_smad_nuc', 'R_smad_P_nuc', 'smad4_nuc', 'Pi']
    _SPECIES_LABELS = {'receptor': 'receptors', 'R_smad_cyt': 'R-Smad_cyt', 'R_smad_P_cyt': 'R-Smad-P_cyt', 'smad4_cyt': 'Smad4_cyt', 'R_smad_P_smad4_cyt': 'R-Smad-P-Smad4_cyt', 'R_smad_P_smad4_nuc': 'R-Smad-P-Smad4_nuc', 'R_smad_nuc': 'R-Smad_nuc', 'R_smad_P_nuc': 'R-Smad-P_nuc', 'smad4_nuc': 'Smad4_nuc', 'Pi': 'Pi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_r_smad_cyt': ('R_smad_cyt', 162000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_smad_cyt`.'), 'initial_smad4_cyt': ('smad4_cyt', 120000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `smad4_cyt`.'), 'initial_smad4_nuc': ('smad4_nuc', 30000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `smad4_nuc`.'), 'initial_r_smad_nuc': ('R_smad_nuc', 18000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_smad_nuc`.'), 'initial_receptors': ('receptor', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `receptor`.'), 'initial_r_smad_p_nuc': ('R_smad_P_nuc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_smad_P_nuc`.')}
    _HEADLINE_OUTPUTS = {'r_smad_cyt': ('R_smad_cyt', 'native SBML value', 'R-Smad_cyt. Maps to SBML symbol `R_smad_cyt`.'), 'smad4_cyt': ('smad4_cyt', 'native SBML value', 'Smad4_cyt. Maps to SBML symbol `smad4_cyt`.'), 'smad4_nuc': ('smad4_nuc', 'native SBML value', 'Smad4_nuc. Maps to SBML symbol `smad4_nuc`.'), 'r_smad_nuc': ('R_smad_nuc', 'native SBML value', 'R-Smad_nuc. Maps to SBML symbol `R_smad_nuc`.'), 'receptors': ('receptor', 'native SBML value', 'receptors. Maps to SBML symbol `receptor`.'), 'r_smad_p_nuc': ('R_smad_P_nuc', 'native SBML value', 'R-Smad-P_nuc. Maps to SBML symbol `R_smad_P_nuc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000112.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
