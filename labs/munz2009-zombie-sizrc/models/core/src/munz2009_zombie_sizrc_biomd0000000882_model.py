# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Munz2009 - Zombie SIZRC."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Munz2009ZombieSizrcBiomd0000000882Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Munz2009 - Zombie SIZRC."""

    _SBML_ID = 'BIOMD0000000882'
    _TITLE = 'Munz2009 - Zombie SIZRC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Susceptible', 'Zombie', 'Removal']
    _SPECIES_LABELS = {'Susceptible': 'Susceptible', 'Zombie': 'Zombie', 'Removal': 'Removal'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_susceptible': ('Susceptible', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Susceptible`.'), 'initial_zombie': ('Zombie', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Zombie`.'), 'initial_removal': ('Removal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Removal`.')}
    _HEADLINE_OUTPUTS = {'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'zombie': ('Zombie', 'native SBML value', 'Zombie. Maps to SBML symbol `Zombie`.'), 'removal': ('Removal', 'native SBML value', 'Removal. Maps to SBML symbol `Removal`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000882.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
