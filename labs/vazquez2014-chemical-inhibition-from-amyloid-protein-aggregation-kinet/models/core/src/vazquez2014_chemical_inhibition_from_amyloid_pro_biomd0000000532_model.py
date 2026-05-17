# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Vazquez2014 - Chemical inhibition from amyloid protein aggregation kinetics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vazquez2014ChemicalInhibitionFromAmyloidProBiomd0000000532Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Vazquez2014 - Chemical inhibition from amyloid protein aggregation kinetics."""

    _SBML_ID = 'BIOMD0000000532'
    _TITLE = 'Vazquez2014 - Chemical inhibition from amyloid protein aggregation kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'Xm', 'Vm', 'Lambda']
    _SPECIES_LABELS = {'X': 'X', 'Xm': 'Xm', 'Vm': 'Vm', 'Lambda': 'Lambda'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lambda_value': ('Lambda', 3.47731075423886, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lambda`.'), 'initial_model_state_xm': ('Xm', 0.972654947412286, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xm`.'), 'initial_model_state_vm': ('Vm', 0.239400820174643, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm`.'), 'initial_model_state_x': ('X', 0.00427219370168501, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.')}
    _HEADLINE_OUTPUTS = {'lambda_value': ('Lambda', 'native SBML value', 'Lambda. Maps to SBML symbol `Lambda`.'), 'model_state_xm': ('Xm', 'native SBML value', 'Xm. Maps to SBML symbol `Xm`.'), 'model_state_vm': ('Vm', 'native SBML value', 'Vm. Maps to SBML symbol `Vm`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000532.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
