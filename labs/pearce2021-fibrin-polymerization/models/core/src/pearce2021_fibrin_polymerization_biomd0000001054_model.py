# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Pearce2021 - Fibrin Polymerization."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pearce2021FibrinPolymerizationBiomd0000001054Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Pearce2021 - Fibrin Polymerization."""

    _SBML_ID = 'BIOMD0000001054'
    _TITLE = 'Pearce2021 - Fibrin Polymerization'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Fbna', 'FM', 'Thb', 'Fbni', 'C0', 'C1', 'C2']
    _SPECIES_LABELS = {'Fbna': 'Fbna', 'FM': 'FM', 'Thb': 'Thb', 'Fbni': 'Fbni', 'C0': 'C0', 'C1': 'C1', 'C2': 'C2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fbni': ('Fbni', 2.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fbni`.'), 'initial_model_state_thb': ('Thb', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Thb`.'), 'initial_model_state_fm': ('FM', 0.15, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FM`.'), 'initial_fbna': ('Fbna', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fbna`.'), 'initial_model_state_c2': ('C2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C2`.'), 'initial_model_state_c1': ('C1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C1`.')}
    _HEADLINE_OUTPUTS = {'fbni': ('Fbni', 'native SBML value', 'Fbni. Maps to SBML symbol `Fbni`.'), 'thb': ('Thb', 'native SBML value', 'Thb. Maps to SBML symbol `Thb`.'), 'model_state_fm': ('FM', 'native SBML value', 'FM. Maps to SBML symbol `FM`.'), 'fbna': ('Fbna', 'native SBML value', 'Fbna. Maps to SBML symbol `Fbna`.'), 'model_state_c2': ('C2', 'native SBML value', 'C2. Maps to SBML symbol `C2`.'), 'model_state_c1': ('C1', 'native SBML value', 'C1. Maps to SBML symbol `C1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001054.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
