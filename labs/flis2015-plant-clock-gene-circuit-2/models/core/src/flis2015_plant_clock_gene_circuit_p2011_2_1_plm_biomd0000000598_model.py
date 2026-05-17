# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Flis2015 - Plant clock gene circuit (P2011.2.1 PLM_71 ver 2)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Flis2015PlantClockGeneCircuitP201121PlmBiomd0000000598Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Flis2015 - Plant clock gene circuit (P2011.2.1 PLM_71 ver 2)."""

    _SBML_ID = 'BIOMD0000000598'
    _TITLE = 'Flis2015 - Plant clock gene circuit (P2011.2.1 PLM_71 ver 2)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cCOP1c', 'cCOP1d', 'cCOP1n', 'cE3', 'cE3_m', 'cE3n', 'cE4', 'cE4_m', 'cEC', 'cEG', 'cG', 'cG_m', 'cL', 'cLUX', 'cLUX_m', 'cL_m', 'cLm', 'cNI', 'cNI_m', 'cP', 'cP7', 'cP7_m', 'cP9', 'cP9_m', 'cT', 'cT_m', 'cZG', 'cZTL']
    _SPECIES_LABELS = {'cCOP1c': 'cCOP1c', 'cCOP1d': 'cCOP1d', 'cCOP1n': 'cCOP1n', 'cE3': 'cE3', 'cE3_m': 'cE3_m', 'cE3n': 'cE3n', 'cE4': 'cE4', 'cE4_m': 'cE4_m', 'cEC': 'cEC', 'cEG': 'cEG', 'cG': 'cG', 'cG_m': 'cG_m', 'cL': 'cL', 'cLUX': 'cLUX', 'cLUX_m': 'cLUX_m', 'cL_m': 'cL_m', 'cLm': 'cLm', 'cNI': 'cNI', 'cNI_m': 'cNI_m', 'cP': 'cP', 'cP7': 'cP7', 'cP7_m': 'cP7_m', 'cP9': 'cP9', 'cP9_m': 'cP9_m', 'cT': 'cT', 'cT_m': 'cT_m', 'cZG': 'cZG', 'cZTL': 'cZTL'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c_l_m': ('cL_m', 1.0151, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cL_m`.'), 'initial_model_state_c_p': ('cP', 0.956, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cP`.'), 'initial_c_cop1n': ('cCOP1n', 0.65, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cCOP1n`.'), 'initial_c_lux': ('cLUX', 0.576, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cLUX`.'), 'initial_model_state_c_l': ('cL', 0.506, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cL`.'), 'initial_c_p7_m': ('cP7_m', 0.4016, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cP7_m`.')}
    _HEADLINE_OUTPUTS = {'c_l_m': ('cL_m', 'native SBML value', 'cL_m. Maps to SBML symbol `cL_m`.'), 'c_p': ('cP', 'native SBML value', 'cP. Maps to SBML symbol `cP`.'), 'c_cop1n': ('cCOP1n', 'native SBML value', 'cCOP1n. Maps to SBML symbol `cCOP1n`.'), 'c_lux': ('cLUX', 'native SBML value', 'cLUX. Maps to SBML symbol `cLUX`.'), 'c_l': ('cL', 'native SBML value', 'cL. Maps to SBML symbol `cL`.'), 'c_p7_m': ('cP7_m', 'native SBML value', 'cP7_m. Maps to SBML symbol `cP7_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000598.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
