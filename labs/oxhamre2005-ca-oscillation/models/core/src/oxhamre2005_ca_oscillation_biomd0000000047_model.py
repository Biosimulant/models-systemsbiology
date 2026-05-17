# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Oxhamre2005_Ca_oscillation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Oxhamre2005CaOscillationBiomd0000000047Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Oxhamre2005_Ca_oscillation."""

    _SBML_ID = 'BIOMD0000000047'
    _TITLE = 'Oxhamre2005_Ca_oscillation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CaER', 'Ca_Cyt']
    _SPECIES_LABELS = {'CaER': 'CaER', 'Ca_Cyt': 'Ca Cyt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_er': ('CaER', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaER`.'), 'initial_ca_cyt': ('Ca_Cyt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_Cyt`.')}
    _HEADLINE_OUTPUTS = {'ca_er': ('CaER', 'native SBML value', 'CaER. Maps to SBML symbol `CaER`.'), 'ca_cyt': ('Ca_Cyt', 'native SBML value', 'Ca Cyt. Maps to SBML symbol `Ca_Cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000047.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
