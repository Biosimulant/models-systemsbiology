# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for ChowHall2008 Dynamics of Human Weight Change_ODE_1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chowhall2008DynamicsOfHumanWeightChangeOdeBiomd0000000901Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for ChowHall2008 Dynamics of Human Weight Change_ODE_1."""

    _SBML_ID = 'BIOMD0000000901'
    _TITLE = 'ChowHall2008 Dynamics of Human Weight Change_ODE_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Fat_Mass', 'Lean_Mass', 'Body_Mass']
    _SPECIES_LABELS = {'Fat_Mass': 'Fat Mass', 'Lean_Mass': 'Lean Mass', 'Body_Mass': 'Body Mass'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_body_mass': ('Body_Mass', 100.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Body_Mass`.'), 'initial_lean_mass': ('Lean_Mass', 50.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lean_Mass`.'), 'initial_fat_mass': ('Fat_Mass', 50.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fat_Mass`.')}
    _HEADLINE_OUTPUTS = {'body_mass': ('Body_Mass', 'substance', 'Body Mass. Maps to SBML symbol `Body_Mass`.'), 'lean_mass': ('Lean_Mass', 'substance', 'Lean Mass. Maps to SBML symbol `Lean_Mass`.'), 'fat_mass': ('Fat_Mass', 'substance', 'Fat Mass. Maps to SBML symbol `Fat_Mass`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000901.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
