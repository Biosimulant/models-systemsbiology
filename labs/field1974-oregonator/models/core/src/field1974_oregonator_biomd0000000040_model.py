# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Field1974_Oregonator."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Field1974OregonatorBiomd0000000040Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Field1974_Oregonator."""

    _SBML_ID = 'BIOMD0000000040'
    _TITLE = 'Field1974_Oregonator'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Br', 'BrO3', 'Ce', 'HBrO2', 'HOBr']
    _SPECIES_LABELS = {'Br': 'Br-', 'BrO3': 'BrO3-', 'Ce': 'Ce4+', 'HBrO2': 'HBrO2', 'HOBr': 'HOBr'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_br_o3': ('BrO3', 0.06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BrO3`.'), 'initial_model_state_ce4': ('Ce', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ce`.'), 'initial_model_state_br': ('Br', 1e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Br`.'), 'initial_h_br_o2': ('HBrO2', 5e-11, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HBrO2`.'), 'initial_ho_br': ('HOBr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HOBr`.')}
    _HEADLINE_OUTPUTS = {'br_o3': ('BrO3', 'native SBML value', 'BrO3-. Maps to SBML symbol `BrO3`.'), 'ce4': ('Ce', 'native SBML value', 'Ce4+. Maps to SBML symbol `Ce`.'), 'model_state_br': ('Br', 'native SBML value', 'Br-. Maps to SBML symbol `Br`.'), 'h_br_o2': ('HBrO2', 'native SBML value', 'HBrO2. Maps to SBML symbol `HBrO2`.'), 'ho_br': ('HOBr', 'native SBML value', 'HOBr. Maps to SBML symbol `HOBr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000040.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
