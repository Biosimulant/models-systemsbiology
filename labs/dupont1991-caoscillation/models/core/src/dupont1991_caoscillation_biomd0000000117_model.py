# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Dupont1991_CaOscillation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dupont1991CaoscillationBiomd0000000117Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Dupont1991_CaOscillation."""

    _SBML_ID = 'BIOMD0000000117'
    _TITLE = 'Dupont1991_CaOscillation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['z', 'y']
    _SPECIES_LABELS = {'z': 'Ca in the cytosol', 'y': 'Ca in the InsP3-insensitive pool'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_in_the_ins_p3_insensitive_pool': ('y', 1.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`.'), 'initial_ca_in_the_cytosol': ('z', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.')}
    _HEADLINE_OUTPUTS = {'ca_in_the_ins_p3_insensitive_pool': ('y', 'native SBML value', 'Ca in the InsP3-insensitive pool. Maps to SBML symbol `y`.'), 'ca_in_the_cytosol': ('z', 'native SBML value', 'Ca in the cytosol. Maps to SBML symbol `z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000117.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
