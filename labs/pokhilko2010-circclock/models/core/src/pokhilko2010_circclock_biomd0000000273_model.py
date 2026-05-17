# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Pokhilko2010_CircClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pokhilko2010CircclockBiomd0000000273Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Pokhilko2010_CircClock."""

    _SBML_ID = 'BIOMD0000000273'
    _TITLE = 'Pokhilko2010_CircClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cG', 'cG_m', 'cL', 'cL_m', 'cLm', 'cNI', 'cNI_m', 'cP', 'cP7', 'cP7_m', 'cP9', 'cP9_m', 'cT', 'cT_m', 'cTm', 'cY', 'cY_m', 'cZG', 'cZTL']
    _SPECIES_LABELS = {'cG': 'cG', 'cG_m': 'cG_m', 'cL': 'cL', 'cL_m': 'cL_m', 'cLm': 'cLm', 'cNI': 'cNI', 'cNI_m': 'cNI_m', 'cP': 'cP', 'cP7': 'cP7', 'cP7_m': 'cP7_m', 'cP9': 'cP9', 'cP9_m': 'cP9_m', 'cT': 'cT', 'cT_m': 'cT_m', 'cTm': 'cTm', 'cY': 'cY', 'cY_m': 'cY_m', 'cZG': 'cZG', 'cZTL': 'cZTL'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c_l_m': ('cL_m', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cL_m`.'), 'initial_model_state_c_p': ('cP', 0.825, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cP`.'), 'initial_model_state_c_l': ('cL', 0.416, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cL`.'), 'initial_model_state_c_t': ('cT', 0.393, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cT`.'), 'initial_c_p9_m': ('cP9_m', 0.35, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cP9_m`.'), 'initial_c_ztl': ('cZTL', 0.323, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cZTL`.')}
    _HEADLINE_OUTPUTS = {'c_l_m': ('cL_m', 'native SBML value', 'cL_m. Maps to SBML symbol `cL_m`.'), 'c_p': ('cP', 'native SBML value', 'cP. Maps to SBML symbol `cP`.'), 'c_l': ('cL', 'native SBML value', 'cL. Maps to SBML symbol `cL`.'), 'c_t': ('cT', 'native SBML value', 'cT. Maps to SBML symbol `cT`.'), 'c_p9_m': ('cP9_m', 'native SBML value', 'cP9_m. Maps to SBML symbol `cP9_m`.'), 'c_ztl': ('cZTL', 'native SBML value', 'cZTL. Maps to SBML symbol `cZTL`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000273.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
