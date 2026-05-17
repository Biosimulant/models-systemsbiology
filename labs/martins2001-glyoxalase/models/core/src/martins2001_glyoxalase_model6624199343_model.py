# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Martins2001_glyoxalase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Martins2001GlyoxalaseModel6624199343Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Martins2001_glyoxalase."""

    _SBML_ID = 'MODEL6624199343'
    _TITLE = 'Martins2001_glyoxalase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GSH', 'HTA', 'SLG', 'Lac', 'MG']
    _SPECIES_LABELS = {'GSH': 'GSH', 'HTA': 'HTA', 'SLG': 'SLG', 'Lac': 'Lac', 'MG': 'MG'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_gsh': ('GSH', 8.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GSH`.'), 'initial_model_state_mg': ('MG', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MG`.'), 'initial_model_state_slg': ('SLG', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SLG`.'), 'initial_model_state_lac': ('Lac', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lac`.'), 'initial_model_state_hta': ('HTA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HTA`.')}
    _HEADLINE_OUTPUTS = {'gsh': ('GSH', 'native SBML value', 'GSH. Maps to SBML symbol `GSH`.'), 'model_state_mg': ('MG', 'native SBML value', 'MG. Maps to SBML symbol `MG`.'), 'slg': ('SLG', 'native SBML value', 'SLG. Maps to SBML symbol `SLG`.'), 'lac': ('Lac', 'native SBML value', 'Lac. Maps to SBML symbol `Lac`.'), 'hta': ('HTA', 'native SBML value', 'HTA. Maps to SBML symbol `HTA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6624199343.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
