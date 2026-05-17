# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ataullahkhanov1996_Adenylate."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ataullahkhanov1996AdenylateBiomd0000000054Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ataullahkhanov1996_Adenylate."""

    _SBML_ID = 'BIOMD0000000054'
    _TITLE = 'Ataullahkhanov1996_Adenylate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I', 'E', 'A']
    _SPECIES_LABELS = {'I': 'Ions', 'E': 'Energy pool', 'A': 'Adenylate pool'}
    _PARAMETER_INPUTS = {'extracellular_ion_concentration': ('J', 100.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `J`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'ions': ('I', 'native SBML value', 'Ions. Maps to SBML symbol `I`.'), 'energy_pool': ('E', 'native SBML value', 'Energy pool. Maps to SBML symbol `E`.'), 'adenylate_pool': ('A', 'native SBML value', 'Adenylate pool. Maps to SBML symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000054.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
