# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ma2002_cAMP_oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ma2002CampOscillationsBiomd0000000229Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ma2002_cAMP_oscillations."""

    _SBML_ID = 'BIOMD0000000229'
    _TITLE = 'Ma2002_cAMP_oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ACA', 'CAR1', 'PKA', 'incAMP', 'ERK2', 'REGA', 'excAMP']
    _SPECIES_LABELS = {'ACA': 'ACA', 'CAR1': 'CAR1', 'PKA': 'PKA', 'incAMP': 'incAMP', 'ERK2': 'ERK2', 'REGA': 'REGA', 'excAMP': 'excAMP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_erk2': ('ERK2', 1.13, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ERK2`.'), 'initial_incamp': ('incAMP', 1.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `incAMP`.'), 'initial_excamp': ('excAMP', 0.48, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `excAMP`.'), 'initial_model_state_aca': ('ACA', 3.39, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ACA`.'), 'initial_car1': ('CAR1', 2.45, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CAR1`.'), 'initial_model_state_pka': ('PKA', 1.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PKA`.')}
    _HEADLINE_OUTPUTS = {'erk2': ('ERK2', 'native SBML value', 'ERK2. Maps to SBML symbol `ERK2`.'), 'incamp': ('incAMP', 'native SBML value', 'incAMP. Maps to SBML symbol `incAMP`.'), 'excamp': ('excAMP', 'native SBML value', 'excAMP. Maps to SBML symbol `excAMP`.'), 'aca': ('ACA', 'native SBML value', 'ACA. Maps to SBML symbol `ACA`.'), 'car1': ('CAR1', 'native SBML value', 'CAR1. Maps to SBML symbol `CAR1`.'), 'pka': ('PKA', 'native SBML value', 'PKA. Maps to SBML symbol `PKA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000229.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
