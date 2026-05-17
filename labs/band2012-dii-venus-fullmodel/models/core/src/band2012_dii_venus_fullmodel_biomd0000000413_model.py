# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Band2012_DII-Venus_FullModel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Band2012DiiVenusFullmodelBiomd0000000413Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Band2012_DII-Venus_FullModel."""

    _SBML_ID = 'BIOMD0000000413'
    _TITLE = 'Band2012_DII-Venus_FullModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['auxin', 'TIR1', 'auxinTIR1', 'auxinTIR1VENUS', 'VENUS']
    _SPECIES_LABELS = {'auxin': 'Auxin', 'TIR1': 'TIR1', 'auxinTIR1': 'AuxinTIR1', 'auxinTIR1VENUS': 'AuxinTIR1VENUS', 'VENUS': 'VENUS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_venus': ('VENUS', 40.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VENUS`.'), 'initial_tir1': ('TIR1', 15.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TIR1`.'), 'initial_auxin': ('auxin', 7.38, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `auxin`.'), 'initial_auxin_tir1_venus': ('auxinTIR1VENUS', 2.78, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `auxinTIR1VENUS`.'), 'initial_auxin_tir1': ('auxinTIR1', 0.28, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `auxinTIR1`.')}
    _HEADLINE_OUTPUTS = {'venus': ('VENUS', 'native SBML value', 'VENUS. Maps to SBML symbol `VENUS`.'), 'tir1': ('TIR1', 'native SBML value', 'TIR1. Maps to SBML symbol `TIR1`.'), 'auxin': ('auxin', 'native SBML value', 'Auxin. Maps to SBML symbol `auxin`.'), 'auxin_tir1_venus': ('auxinTIR1VENUS', 'native SBML value', 'AuxinTIR1VENUS. Maps to SBML symbol `auxinTIR1VENUS`.'), 'auxin_tir1': ('auxinTIR1', 'native SBML value', 'AuxinTIR1. Maps to SBML symbol `auxinTIR1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000413.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
