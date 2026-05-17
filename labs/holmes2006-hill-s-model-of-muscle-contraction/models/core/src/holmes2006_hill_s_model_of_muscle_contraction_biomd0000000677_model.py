# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Holmes2006 - Hill's model of muscle contraction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Holmes2006HillSModelOfMuscleContractionBiomd0000000677Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Holmes2006 - Hill's model of muscle contraction."""

    _SBML_ID = 'BIOMD0000000677'
    _TITLE = "Holmes2006 - Hill's model of muscle contraction"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['L_ce']
    _SPECIES_LABELS = {'L_ce': 'L Ce'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_l_ce': ('L_ce', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L_ce`.')}
    _HEADLINE_OUTPUTS = {'l_ce': ('L_ce', 'native SBML value', 'L Ce. Maps to SBML symbol `L_ce`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000677.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
