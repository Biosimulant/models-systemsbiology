# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Montañez2008_Arginine_catabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class MontaEz2008ArginineCatabolismBiomd0000000191Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Montañez2008_Arginine_catabolism."""

    _SBML_ID = 'BIOMD0000000191'
    _TITLE = 'Montañez2008_Arginine_catabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ARGex', 'ORN', 'ARGin']
    _SPECIES_LABELS = {'ARGex': 'Arginine ex', 'ORN': 'Ornithine', 'ARGin': 'Arginine in'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_arginine_ex': ('ARGex', 330.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ARGex`.'), 'initial_ornithine': ('ORN', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ORN`.'), 'initial_arginine_in': ('ARGin', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ARGin`.')}
    _HEADLINE_OUTPUTS = {'arginine_ex': ('ARGex', 'native SBML value', 'Arginine ex. Maps to SBML symbol `ARGex`.'), 'ornithine': ('ORN', 'native SBML value', 'Ornithine. Maps to SBML symbol `ORN`.'), 'arginine_in': ('ARGin', 'native SBML value', 'Arginine in. Maps to SBML symbol `ARGin`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000191.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
