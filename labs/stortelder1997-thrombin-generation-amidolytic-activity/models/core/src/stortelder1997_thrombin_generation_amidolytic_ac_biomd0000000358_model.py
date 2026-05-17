# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Stortelder1997 - Thrombin Generation Amidolytic Activity."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Stortelder1997ThrombinGenerationAmidolyticAcBiomd0000000358Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Stortelder1997 - Thrombin Generation Amidolytic Activity."""

    _SBML_ID = 'BIOMD0000000358'
    _TITLE = 'Stortelder1997 - Thrombin Generation Amidolytic Activity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'Xa', 'Xa_ATIII', 'PL', 'PT', 'Va', 'IIa', 'V', 'II', 'IIa_alpha2M', 'IIa_ATIII', 'RVV']
    _SPECIES_LABELS = {'X': 'X', 'Xa': 'Xa', 'Xa_ATIII': 'Xa_ATIII', 'PL': 'PL', 'PT': 'PT', 'Va': 'Va', 'IIa': 'IIa', 'V': 'V', 'II': 'II', 'IIa_alpha2M': 'IIa_alpha2M', 'IIa_ATIII': 'IIa_ATIII', 'RVV': 'RVV'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_xa_atiii': ('Xa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`.'), 'initial_i_ia_alpha2_m': ('IIa_alpha2M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_alpha2M`.'), 'initial_i_ia_atiii': ('IIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_ATIII`.'), 'initial_model_state_ii': ('II', 509.2998, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II`.'), 'initial_model_state_pl': ('PL', 9.999997, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PL`.'), 'initial_model_state_rvv': ('RVV', 0.3349999, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RVV`.')}
    _HEADLINE_OUTPUTS = {'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa_ATIII. Maps to SBML symbol `Xa_ATIII`.'), 'i_ia_alpha2_m': ('IIa_alpha2M', 'native SBML value', 'IIa_alpha2M. Maps to SBML symbol `IIa_alpha2M`.'), 'i_ia_atiii': ('IIa_ATIII', 'native SBML value', 'IIa_ATIII. Maps to SBML symbol `IIa_ATIII`.'), 'model_state_ii': ('II', 'native SBML value', 'II. Maps to SBML symbol `II`.'), 'model_state_pl': ('PL', 'native SBML value', 'PL. Maps to SBML symbol `PL`.'), 'rvv': ('RVV', 'native SBML value', 'RVV. Maps to SBML symbol `RVV`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000358.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
