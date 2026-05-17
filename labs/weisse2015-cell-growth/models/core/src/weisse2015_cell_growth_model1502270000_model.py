# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Weisse2015 - Cell Growth."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Weisse2015CellGrowthModel1502270000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Weisse2015 - Cell Growth."""

    _SBML_ID = 'MODEL1502270000'
    _TITLE = 'Weisse2015 - Cell Growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['rmr', 'em', 'rmp', 'rmq', 'rmt', 'et', 'rmm', 'zmm', 'zmr', 'zmp', 'zmq', 'zmt', 'mt', 'mm', 'q', 'p', 'si', 'mq', 'mp', 'mr', 'r', 'a']
    _SPECIES_LABELS = {'rmr': 'Rmr', 'em': 'Em', 'rmp': 'Rmp', 'rmq': 'Rmq', 'rmt': 'Rmt', 'et': 'Et', 'rmm': 'Rmm', 'zmm': 'Zmm', 'zmr': 'Zmr', 'zmp': 'Zmp', 'zmq': 'Zmq', 'zmt': 'Zmt', 'mt': 'Mt', 'mm': 'Mm', 'q': 'Q', 'p': 'P', 'si': 'Si', 'mq': 'Mq', 'mp': 'Mp', 'mr': 'Mr', 'r': 'R', 'a': 'A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_zmt': ('zmt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zmt`.'), 'initial_model_state_zmr': ('zmr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zmr`.'), 'initial_model_state_zmq': ('zmq', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zmq`.'), 'initial_model_state_zmp': ('zmp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zmp`.'), 'initial_model_state_zmm': ('zmm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zmm`.'), 'initial_model_state_si': ('si', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `si`.')}
    _HEADLINE_OUTPUTS = {'zmt': ('zmt', 'native SBML value', 'Zmt. Maps to SBML symbol `zmt`.'), 'zmr': ('zmr', 'native SBML value', 'Zmr. Maps to SBML symbol `zmr`.'), 'zmq': ('zmq', 'native SBML value', 'Zmq. Maps to SBML symbol `zmq`.'), 'zmp': ('zmp', 'native SBML value', 'Zmp. Maps to SBML symbol `zmp`.'), 'zmm': ('zmm', 'native SBML value', 'Zmm. Maps to SBML symbol `zmm`.'), 'model_state_si': ('si', 'native SBML value', 'Si. Maps to SBML symbol `si`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1502270000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
