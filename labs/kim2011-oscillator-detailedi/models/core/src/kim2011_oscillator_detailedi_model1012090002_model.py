# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kim2011_Oscillator_DetailedI."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2011OscillatorDetailediModel1012090002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kim2011_Oscillator_DetailedI."""

    _SBML_ID = 'MODEL1012090002'
    _TITLE = 'Kim2011_Oscillator_DetailedI'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20']
    _SPECIES_LABELS = {'species_1': 'T12', 'species_2': 'A2', 'species_3': 'T21', 'species_4': 'A1', 'species_5': 'dI1', 'species_6': 'rA1', 'species_7': 'rI2', 'species_8': 'T12A2', 'species_9': 'T21A1', 'species_10': 'A1dI1', 'species_11': 'rA1dI1', 'species_12': 'A2rI2', 'species_13': 'RNAP', 'species_14': 'RNaseH', 'species_15': 'RNAPT12A2', 'species_16': 'RNAPT12', 'species_17': 'RNAPT21A1', 'species_18': 'RNAPT21', 'species_19': 'RNaseHrA1dI1', 'species_20': 'RNaseHA2rI2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rnap': ('species_13', 1.25e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`.'), 'initial_r_nase_h': ('species_14', 1.5e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.'), 'initial_r_nase_hr_a1d_i1': ('species_19', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`.'), 'initial_r_nase_ha2r_i2': ('species_20', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`.'), 'initial_rnapt21_a1': ('species_17', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_17`.'), 'initial_rnapt21': ('species_18', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_18`.')}
    _HEADLINE_OUTPUTS = {'rnap': ('species_13', 'native SBML value', 'RNAP. Maps to SBML symbol `species_13`.'), 'r_nase_h': ('species_14', 'native SBML value', 'RNaseH. Maps to SBML symbol `species_14`.'), 'r_nase_hr_a1d_i1': ('species_19', 'native SBML value', 'RNaseHrA1dI1. Maps to SBML symbol `species_19`.'), 'r_nase_ha2r_i2': ('species_20', 'native SBML value', 'RNaseHA2rI2. Maps to SBML symbol `species_20`.'), 'rnapt21_a1': ('species_17', 'native SBML value', 'RNAPT21A1. Maps to SBML symbol `species_17`.'), 'rnapt21': ('species_18', 'native SBML value', 'RNAPT21. Maps to SBML symbol `species_18`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1012090002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
