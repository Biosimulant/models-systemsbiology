# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kamihira2000 - calcitonin fibrillation kinetics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kamihira2000CalcitoninFibrillationKineticsBiomd0000000614Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kamihira2000 - calcitonin fibrillation kinetics."""

    _SBML_ID = 'BIOMD0000000614'
    _TITLE = 'Kamihira2000 - calcitonin fibrillation kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['f']
    _SPECIES_LABELS = {'f': 'fibril fraction'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fibril_fraction': ('f', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `f`.')}
    _HEADLINE_OUTPUTS = {'fibril_fraction': ('f', 'native SBML value', 'fibril fraction. Maps to SBML symbol `f`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000614.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
