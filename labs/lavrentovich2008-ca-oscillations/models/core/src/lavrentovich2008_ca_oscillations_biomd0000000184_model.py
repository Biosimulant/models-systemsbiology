# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lavrentovich2008_Ca_Oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lavrentovich2008CaOscillationsBiomd0000000184Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lavrentovich2008_Ca_Oscillations."""

    _SBML_ID = 'BIOMD0000000184'
    _TITLE = 'Lavrentovich2008_Ca_Oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'Y', 'Z']
    _SPECIES_LABELS = {'X': 'Cytoplasmic Calcium', 'Y': 'Calcium in ER', 'Z': 'IP3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_in_er': ('Y', 1.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_ip3': ('Z', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.'), 'initial_cytoplasmic_calcium': ('X', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.')}
    _HEADLINE_OUTPUTS = {'calcium_in_er': ('Y', 'native SBML value', 'Calcium in ER. Maps to SBML symbol `Y`.'), 'ip3': ('Z', 'native SBML value', 'IP3. Maps to SBML symbol `Z`.'), 'cytoplasmic_calcium': ('X', 'native SBML value', 'Cytoplasmic Calcium. Maps to SBML symbol `X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000184.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
