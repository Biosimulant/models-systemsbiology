# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Marhl2000_CaOscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Marhl2000CaoscillationsBiomd0000000039Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Marhl2000_CaOscillations."""

    _SBML_ID = 'BIOMD0000000039'
    _TITLE = 'Marhl2000_CaOscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ca_cyt', 'CaER', 'CaM', 'CaPr', 'Pr']
    _SPECIES_LABELS = {'Ca_cyt': 'Ca Cyt', 'CaER': 'CaER', 'CaM': 'CaM', 'CaPr': 'CaPr', 'Pr': 'Pr'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_pr': ('CaPr', 85.45, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaPr`.'), 'initial_model_state_pr': ('Pr', 34.55, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pr`.'), 'initial_ca_er': ('CaER', 0.76, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaER`.'), 'initial_ca_cyt': ('Ca_cyt', 0.35, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_cyt`.'), 'initial_ca_m': ('CaM', 0.29, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaM`.')}
    _HEADLINE_OUTPUTS = {'ca_pr': ('CaPr', 'native SBML value', 'CaPr. Maps to SBML symbol `CaPr`.'), 'model_state_pr': ('Pr', 'native SBML value', 'Pr. Maps to SBML symbol `Pr`.'), 'ca_er': ('CaER', 'native SBML value', 'CaER. Maps to SBML symbol `CaER`.'), 'ca_cyt': ('Ca_cyt', 'native SBML value', 'Ca Cyt. Maps to SBML symbol `Ca_cyt`.'), 'ca_m': ('CaM', 'native SBML value', 'CaM. Maps to SBML symbol `CaM`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000039.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
