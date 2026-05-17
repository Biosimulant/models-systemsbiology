# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kim2007_CellularMemory_AsymmetricModel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2007CellularmemoryAsymmetricmodelBiomd0000000179Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kim2007_CellularMemory_AsymmetricModel."""

    _SBML_ID = 'BIOMD0000000179'
    _TITLE = 'Kim2007_CellularMemory_AsymmetricModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R1', 'P1', 'P1_prime', 'R2', 'P2', 'P2_prime', 'P3_prime']
    _SPECIES_LABELS = {'R1': 'R1', 'P1': 'P1', 'P1_prime': 'P1 Prime', 'R2': 'R2', 'P2': 'P2', 'P2_prime': 'P2 Prime', 'P3_prime': 'P3 Prime'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p2_prime': ('P2_prime', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2_prime`.'), 'initial_model_state_p2': ('P2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`.'), 'initial_model_state_r2': ('R2', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R2`.'), 'initial_p3_prime': ('P3_prime', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P3_prime`.'), 'initial_p1_prime': ('P1_prime', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1_prime`.'), 'initial_model_state_p1': ('P1', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1`.')}
    _HEADLINE_OUTPUTS = {'p2_prime': ('P2_prime', 'native SBML value', 'P2 Prime. Maps to SBML symbol `P2_prime`.'), 'model_state_p2': ('P2', 'native SBML value', 'P2. Maps to SBML symbol `P2`.'), 'model_state_r2': ('R2', 'native SBML value', 'R2. Maps to SBML symbol `R2`.'), 'p3_prime': ('P3_prime', 'native SBML value', 'P3 Prime. Maps to SBML symbol `P3_prime`.'), 'p1_prime': ('P1_prime', 'native SBML value', 'P1 Prime. Maps to SBML symbol `P1_prime`.'), 'model_state_p1': ('P1', 'native SBML value', 'P1. Maps to SBML symbol `P1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000179.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
