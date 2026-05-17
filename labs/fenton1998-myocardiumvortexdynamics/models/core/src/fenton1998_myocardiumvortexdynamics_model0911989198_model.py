# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fenton1998_MyocardiumVortexDynamics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fenton1998MyocardiumvortexdynamicsModel0911989198Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fenton1998_MyocardiumVortexDynamics."""

    _SBML_ID = 'MODEL0911989198'
    _TITLE = 'Fenton1998_MyocardiumVortexDynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['u_membrane', 'v', 'w']
    _SPECIES_LABELS = {'u_membrane': 'U Membrane', 'v': 'V', 'w': 'W'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_u_membrane': ('u_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `u_membrane`.'), 'initial_model_state_w': ('w', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `w`.'), 'initial_model_state_v': ('v', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `v`.')}
    _HEADLINE_OUTPUTS = {'u_membrane': ('u_membrane', 'native SBML value', 'U Membrane. Maps to SBML symbol `u_membrane`.'), 'model_state_w': ('w', 'native SBML value', 'W. Maps to SBML symbol `w`.'), 'model_state_v': ('v', 'native SBML value', 'V. Maps to SBML symbol `v`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0911989198.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
