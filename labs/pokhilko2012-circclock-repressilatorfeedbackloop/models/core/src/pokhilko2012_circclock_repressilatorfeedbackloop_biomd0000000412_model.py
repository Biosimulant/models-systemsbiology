# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Pokhilko2012_CircClock_RepressilatorFeedbackloop."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pokhilko2012CircclockRepressilatorfeedbackloopBiomd0000000412Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Pokhilko2012_CircClock_RepressilatorFeedbackloop."""

    _SBML_ID = 'BIOMD0000000412'
    _TITLE = 'Pokhilko2012_CircClock_RepressilatorFeedbackloop'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cCOP1c', 'cCOP1d', 'cCOP1n', 'cE3', 'cE3_m', 'cE3n', 'cE4', 'cE4_m', 'cEC', 'cEG', 'cG', 'cG_m', 'cL', 'cLUX', 'cLUX_m', 'cL_m', 'cLm', 'cNI', 'cNI_m', 'cP', 'cP7', 'cP7_m', 'cP9', 'cP9_m', 'cT', 'cT_m', 'cZG', 'cZTL']
    _SPECIES_LABELS = {'cCOP1c': 'cCOP1c', 'cCOP1d': 'cCOP1d', 'cCOP1n': 'cCOP1n', 'cE3': 'cE3', 'cE3_m': 'cE3_m', 'cE3n': 'cE3n', 'cE4': 'cE4', 'cE4_m': 'cE4_m', 'cEC': 'cEC', 'cEG': 'cEG', 'cG': 'cG', 'cG_m': 'cG_m', 'cL': 'cL', 'cLUX': 'cLUX', 'cLUX_m': 'cLUX_m', 'cL_m': 'cL_m', 'cLm': 'cLm', 'cNI': 'cNI', 'cNI_m': 'cNI_m', 'cP': 'cP', 'cP7': 'cP7', 'cP7_m': 'cP7_m', 'cP9': 'cP9', 'cP9_m': 'cP9_m', 'cT': 'cT', 'cT_m': 'cT_m', 'cZG': 'cZG', 'cZTL': 'cZTL'}
    _PARAMETER_INPUTS = {'light_amplitude': ('lightAmplitude', 1.0, 'time', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightAmplitude`.'), 'light_offset': ('lightOffset', 0.0, 'time', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightOffset`.'), 'twilight_period': ('twilightPeriod', 0.05, 'time', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `twilightPeriod`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'c_l_m': ('cL_m', 'native SBML value', 'cL_m. Maps to SBML symbol `cL_m`.'), 'c_p': ('cP', 'native SBML value', 'cP. Maps to SBML symbol `cP`.'), 'c_cop1n': ('cCOP1n', 'native SBML value', 'cCOP1n. Maps to SBML symbol `cCOP1n`.'), 'c_lux': ('cLUX', 'native SBML value', 'cLUX. Maps to SBML symbol `cLUX`.'), 'c_l': ('cL', 'native SBML value', 'cL. Maps to SBML symbol `cL`.'), 'c_p7_m': ('cP7_m', 'native SBML value', 'cP7_m. Maps to SBML symbol `cP7_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000412.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
