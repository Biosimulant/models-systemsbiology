# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Reynolds2006 - Reduced model of the acute inflammatory response."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reynolds2006ReducedModelOfTheAcuteInflammaBiomd0000000714Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Reynolds2006 - Reduced model of the acute inflammatory response."""

    _SBML_ID = 'BIOMD0000000714'
    _TITLE = 'Reynolds2006 - Reduced model of the acute inflammatory response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P', 'Nstar', 'D', 'C_A']
    _SPECIES_LABELS = {'P': 'Pathogen (P)', 'Nstar': 'Activated Phagocytes (Nstar)', 'D': 'Tissue Damage (D)', 'C_A': 'Anti-inflammatory mediators (C_A)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_anti_inflammatory_mediators_c_a': ('C_A', 0.125, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C_A`.'), 'initial_activated_phagocytes_nstar': ('Nstar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nstar`.'), 'initial_pathogen_p': ('P', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_tissue_damage_d': ('D', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'anti_inflammatory_mediators_c_a': ('C_A', 'native SBML value', 'Anti-inflammatory mediators (C_A). Maps to SBML symbol `C_A`.'), 'activated_phagocytes_nstar': ('Nstar', 'native SBML value', 'Activated Phagocytes (Nstar). Maps to SBML symbol `Nstar`.'), 'pathogen_p': ('P', 'native SBML value', 'Pathogen (P). Maps to SBML symbol `P`.'), 'tissue_damage_d': ('D', 'native SBML value', 'Tissue Damage (D). Maps to SBML symbol `D`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000714.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
