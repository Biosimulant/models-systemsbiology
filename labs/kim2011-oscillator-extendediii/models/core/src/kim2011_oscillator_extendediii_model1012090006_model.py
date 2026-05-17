# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kim2011_Oscillator_ExtendedIII."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2011OscillatorExtendediiiModel1012090006Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kim2011_Oscillator_ExtendedIII."""

    _SBML_ID = 'MODEL1012090006'
    _TITLE = 'Kim2011_Oscillator_ExtendedIII'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33', 'species_34', 'species_35', 'species_36', 'species_37', 'species_38']
    _SPECIES_LABELS = {'species_1': 'T12', 'species_2': 'A2', 'species_3': 'T31', 'species_4': 'A1', 'species_5': 'rI3', 'species_6': 'rI1', 'species_7': 'rI2', 'species_8': 'T12A2', 'species_9': 'T31A1', 'species_10': 'A1rI1', 'species_11': 'A3', 'species_12': 'A2rI2', 'species_13': 'RNAP', 'species_14': 'RNaseH', 'species_15': 'RNAPT12A2', 'species_16': 'RNAPT12', 'species_17': 'RNAPT23A3', 'species_18': 'RNAPT23', 'species_19': 'RNaseHA1rI1', 'species_20': 'RNaseHA2rI2', 'species_21': 'T23', 'species_22': 'T23A3', 'species_23': 'RNAPT31A1', 'species_24': 'RNAPT31', 'species_25': 'sI2', 'species_26': 'A2sI2', 'species_27': 'T12A2sI2', 'species_28': 'RNAPT12A2sI2', 'species_29': 'A1sI1', 'species_30': 'A3sI3', 'species_31': 'A3rI3', 'species_32': 'RNaseHA3rI3', 'species_33': 'T23A3sI3', 'species_34': 'T31A1sI1', 'species_35': 'sI1', 'species_36': 'sI3', 'species_37': 'RNAPT23A3sI3', 'species_38': 'RNAPT31A1sI1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rnap': ('species_13', 8.34e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`.'), 'initial_r_nase_h': ('species_14', 1.04e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.'), 'initial_r_nase_ha3r_i3': ('species_32', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_32`.'), 'initial_r_nase_ha2r_i2': ('species_20', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`.'), 'initial_r_nase_ha1r_i1': ('species_19', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`.'), 'initial_rnapt31_a1s_i1': ('species_38', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_38`.')}
    _HEADLINE_OUTPUTS = {'rnap': ('species_13', 'native SBML value', 'RNAP. Maps to SBML symbol `species_13`.'), 'r_nase_h': ('species_14', 'native SBML value', 'RNaseH. Maps to SBML symbol `species_14`.'), 'r_nase_ha3r_i3': ('species_32', 'native SBML value', 'RNaseHA3rI3. Maps to SBML symbol `species_32`.'), 'r_nase_ha2r_i2': ('species_20', 'native SBML value', 'RNaseHA2rI2. Maps to SBML symbol `species_20`.'), 'r_nase_ha1r_i1': ('species_19', 'native SBML value', 'RNaseHA1rI1. Maps to SBML symbol `species_19`.'), 'rnapt31_a1s_i1': ('species_38', 'native SBML value', 'RNAPT31A1sI1. Maps to SBML symbol `species_38`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1012090006.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
