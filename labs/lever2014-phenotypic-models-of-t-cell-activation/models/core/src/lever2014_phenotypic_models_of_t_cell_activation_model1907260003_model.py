# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lever2014 - Phenotypic models of T cell activation.."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lever2014PhenotypicModelsOfTCellActivationModel1907260003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lever2014 - Phenotypic models of T cell activation.."""

    _SBML_ID = 'MODEL1907260003'
    _TITLE = 'Lever2014 - Phenotypic models of T cell activation.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'P', 'T']
    _SPECIES_LABELS = {'C0': 'C0', 'C1': 'C1', 'C2': 'C2', 'C3': 'C3', 'C4': 'C4', 'C5': 'C5', 'C6': 'C6', 'C7': 'C7', 'C8': 'C8', 'C9': 'C9', 'C10': 'C10', 'P': 'P', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_c0': ('C0', 30000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C0`.'), 'initial_model_state_c9': ('C9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C9`.'), 'initial_model_state_c8': ('C8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C8`.'), 'initial_model_state_c7': ('C7', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C7`.'), 'initial_model_state_c6': ('C6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C6`.'), 'initial_model_state_c5': ('C5', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C5`.')}
    _HEADLINE_OUTPUTS = {'model_state_c0': ('C0', 'native SBML value', 'C0. Maps to SBML symbol `C0`.'), 'model_state_c9': ('C9', 'native SBML value', 'C9. Maps to SBML symbol `C9`.'), 'model_state_c8': ('C8', 'native SBML value', 'C8. Maps to SBML symbol `C8`.'), 'model_state_c7': ('C7', 'native SBML value', 'C7. Maps to SBML symbol `C7`.'), 'model_state_c6': ('C6', 'native SBML value', 'C6. Maps to SBML symbol `C6`.'), 'model_state_c5': ('C5', 'native SBML value', 'C5. Maps to SBML symbol `C5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1907260003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
