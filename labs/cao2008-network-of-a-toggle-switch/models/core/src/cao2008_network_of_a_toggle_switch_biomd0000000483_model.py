# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cao2008 - Network of a toggle switch."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2008NetworkOfAToggleSwitchBiomd0000000483Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cao2008 - Network of a toggle switch."""

    _SBML_ID = 'BIOMD0000000483'
    _TITLE = 'Cao2008 - Network of a toggle switch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pa', 'Pb', 'Da', 'Db', 'BDa', 'BDb']
    _SPECIES_LABELS = {'Pa': 'Pa', 'Pb': 'Pb', 'Da': 'Da', 'Db': 'Db', 'BDa': 'BDa', 'BDb': 'BDb'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pb': ('Pb', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pb`.'), 'initial_model_state_pa': ('Pa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pa`.'), 'initial_model_state_db': ('Db', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Db`.'), 'initial_model_state_da': ('Da', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Da`.'), 'initial_b_db': ('BDb', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BDb`.'), 'initial_b_da': ('BDa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BDa`.')}
    _HEADLINE_OUTPUTS = {'model_state_pb': ('Pb', 'native SBML value', 'Pb. Maps to SBML symbol `Pb`.'), 'model_state_pa': ('Pa', 'native SBML value', 'Pa. Maps to SBML symbol `Pa`.'), 'model_state_db': ('Db', 'native SBML value', 'Db. Maps to SBML symbol `Db`.'), 'model_state_da': ('Da', 'native SBML value', 'Da. Maps to SBML symbol `Da`.'), 'b_db': ('BDb', 'native SBML value', 'BDb. Maps to SBML symbol `BDb`.'), 'b_da': ('BDa', 'native SBML value', 'BDa. Maps to SBML symbol `BDa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000483.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
