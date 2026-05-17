# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Masison2022 - Cellular ferritin iron storage."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Masison2022CellularFerritinIronStorageModel2211030001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Masison2022 - Cellular ferritin iron storage."""

    _SBML_ID = 'MODEL2211030001'
    _TITLE = 'Masison2022 - Cellular ferritin iron storage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['LIP', 'FT_cage', 'core', 'DFP']
    _SPECIES_LABELS = {'LIP': 'LIP', 'FT_cage': 'FT-cage', 'core': 'core', 'DFP': 'DFP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_core': ('core', 7.5e-06, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `core`.'), 'initial_ft_cage': ('FT_cage', 5e-09, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FT_cage`.'), 'initial_model_state_lip': ('LIP', 1e-05, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LIP`.'), 'initial_model_state_dfp': ('DFP', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DFP`.')}
    _HEADLINE_OUTPUTS = {'core': ('core', 'substance', 'core. Maps to SBML symbol `core`.'), 'ft_cage': ('FT_cage', 'substance', 'FT-cage. Maps to SBML symbol `FT_cage`.'), 'lip': ('LIP', 'substance', 'LIP. Maps to SBML symbol `LIP`.'), 'dfp': ('DFP', 'substance', 'DFP. Maps to SBML symbol `DFP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2211030001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
