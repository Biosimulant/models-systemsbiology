# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Szymanska2009 - Mathematical modeling of heat shock protein synthesis in response to temperature change."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Szymanska2009MathematicalModelingOfHeatShocBiomd0000000896Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Szymanska2009 - Mathematical modeling of heat shock protein synthesis in response to temperature change."""

    _SBML_ID = 'BIOMD0000000896'
    _TITLE = 'Szymanska2009 - Mathematical modeling of heat shock protein synthesis in response to temperature change'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Hsp70', 'HSF', 'S', 'Hsp70_HSF', 'Hsp70_S', 'HSF_3', 'HSE', 'HSF_3_HSE', 'mRNA']
    _SPECIES_LABELS = {'Hsp70': 'Hsp70', 'HSF': 'HSF', 'S': 'S', 'Hsp70_HSF': 'Hsp70_HSF', 'Hsp70_S': 'Hsp70_S', 'HSF_3': 'HSF_3', 'HSE': 'HSE', 'HSF_3_HSE': 'HSF_3_HSE', 'mRNA': 'mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_hsp70_hsf': ('Hsp70_HSF', 76.4593, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Hsp70_HSF`.'), 'initial_mrna': ('mRNA', 1.01603, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mRNA`.'), 'initial_hsf_3_hse': ('HSF_3_HSE', 1.01603, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HSF_3_HSE`.'), 'initial_hsf_3': ('HSF_3', 0.0535203, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HSF_3`.'), 'initial_hsp70_s': ('Hsp70_S', 1.74782e-14, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Hsp70_S`.'), 'initial_model_state_hse': ('HSE', 18.984, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HSE`.')}
    _HEADLINE_OUTPUTS = {'hsp70_hsf': ('Hsp70_HSF', 'native SBML value', 'Hsp70_HSF. Maps to SBML symbol `Hsp70_HSF`.'), 'mrna': ('mRNA', 'native SBML value', 'mRNA. Maps to SBML symbol `mRNA`.'), 'hsf_3_hse': ('HSF_3_HSE', 'native SBML value', 'HSF_3_HSE. Maps to SBML symbol `HSF_3_HSE`.'), 'hsf_3': ('HSF_3', 'native SBML value', 'HSF_3. Maps to SBML symbol `HSF_3`.'), 'hsp70_s': ('Hsp70_S', 'native SBML value', 'Hsp70_S. Maps to SBML symbol `Hsp70_S`.'), 'hse': ('HSE', 'native SBML value', 'HSE. Maps to SBML symbol `HSE`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000896.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
