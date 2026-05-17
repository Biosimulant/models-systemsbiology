# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Radosavljevic2009_BioterroristAttack_PanicProtection_1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Radosavljevic2009BioterroristattackPanicprotecBiomd0000000836Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Radosavljevic2009_BioterroristAttack_PanicProtection_1."""

    _SBML_ID = 'BIOMD0000000836'
    _TITLE = 'Radosavljevic2009_BioterroristAttack_PanicProtection_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'P']
    _SPECIES_LABELS = {'S': 'panic_intensity', 'P': 'protection+prevention_intensity'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_protection_prevention_intensity': ('P', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_panic_intensity': ('S', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.')}
    _HEADLINE_OUTPUTS = {'protection_prevention_intensity': ('P', 'native SBML value', 'protection+prevention_intensity. Maps to SBML symbol `P`.'), 'panic_intensity': ('S', 'native SBML value', 'panic_intensity. Maps to SBML symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000836.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
