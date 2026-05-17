# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Crespo2012 - Kinetics of Amyloid Fibril Formation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Crespo2012KineticsOfAmyloidFibrilFormationBiomd0000000531Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Crespo2012 - Kinetics of Amyloid Fibril Formation."""

    _SBML_ID = 'BIOMD0000000531'
    _TITLE = 'Crespo2012 - Kinetics of Amyloid Fibril Formation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['alpha']
    _SPECIES_LABELS = {'alpha': 'alpha'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha': ('alpha', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha`.')}
    _HEADLINE_OUTPUTS = {'alpha': ('alpha', 'native SBML value', 'alpha. Maps to SBML symbol `alpha`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000531.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
