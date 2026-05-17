# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Munz2009 - Zombie SIZRQ."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Munz2009ZombieSizrqModel1008060002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Munz2009 - Zombie SIZRQ."""

    _SBML_ID = 'MODEL1008060002'
    _TITLE = 'Munz2009 - Zombie SIZRQ'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'I', 'Z', 'R', 'Q']
    _SPECIES_LABELS = {'S': 'Susceptible', 'I': 'Infected', 'Z': 'Zombie', 'R': 'Removed', 'Q': 'Quarantined'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_zombie': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.'), 'initial_susceptible': ('S', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_removed': ('R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.'), 'initial_quarantined': ('Q', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Q`.'), 'initial_infected': ('I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'zombie': ('Z', 'native SBML value', 'Zombie. Maps to SBML symbol `Z`.'), 'susceptible': ('S', 'native SBML value', 'Susceptible. Maps to SBML symbol `S`.'), 'removed': ('R', 'native SBML value', 'Removed. Maps to SBML symbol `R`.'), 'quarantined': ('Q', 'native SBML value', 'Quarantined. Maps to SBML symbol `Q`.'), 'infected': ('I', 'native SBML value', 'Infected. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1008060002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
