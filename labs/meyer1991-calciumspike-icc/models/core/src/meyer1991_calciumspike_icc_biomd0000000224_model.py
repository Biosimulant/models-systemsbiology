# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Meyer1991_CalciumSpike_ICC."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Meyer1991CalciumspikeIccBiomd0000000224Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Meyer1991_CalciumSpike_ICC."""

    _SBML_ID = 'BIOMD0000000224'
    _TITLE = 'Meyer1991_CalciumSpike_ICC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CaI', 'IP3', 'CaS', 'g']
    _SPECIES_LABELS = {'CaI': 'CaI', 'IP3': 'IP3', 'CaS': 'CaS', 'g': 'G'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_s': ('CaS', 1100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaS`.'), 'initial_ca_i': ('CaI', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CaI`.'), 'initial_model_state_ip3': ('IP3', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IP3`.'), 'initial_model_state_g': ('g', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `g`.')}
    _HEADLINE_OUTPUTS = {'ca_s': ('CaS', 'native SBML value', 'CaS. Maps to SBML symbol `CaS`.'), 'ca_i': ('CaI', 'native SBML value', 'CaI. Maps to SBML symbol `CaI`.'), 'ip3': ('IP3', 'native SBML value', 'IP3. Maps to SBML symbol `IP3`.'), 'model_state_g': ('g', 'native SBML value', 'G. Maps to SBML symbol `g`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000224.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
