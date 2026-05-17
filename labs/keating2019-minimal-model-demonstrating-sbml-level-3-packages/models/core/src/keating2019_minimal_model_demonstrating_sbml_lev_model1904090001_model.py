# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Keating2019 - Minimal model demonstrating SBML Level 3 packages.."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Keating2019MinimalModelDemonstratingSbmlLevModel1904090001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Keating2019 - Minimal model demonstrating SBML Level 3 packages.."""

    _SBML_ID = 'MODEL1904090001'
    _TITLE = 'Keating2019 - Minimal model demonstrating SBML Level 3 packages.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['glc', 'g6p', 'atp', 'adp', 'phos', 'hydron', 'h2o']
    _SPECIES_LABELS = {'glc': 'glucose', 'g6p': 'glucose-6-phosphate', 'atp': 'ATP', 'adp': 'ADP', 'phos': 'P', 'hydron': 'H+', 'h2o': 'H2O'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('glc', 5.0, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glc`.'), 'initial_glucose_6_phosphate': ('g6p', 0.1, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `g6p`.'), 'initial_model_state_atp': ('atp', 3.0, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`.'), 'initial_model_state_adp': ('adp', 0.8, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `adp`.'), 'initial_model_state_p': ('phos', 0.0, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `phos`.'), 'initial_model_state_h': ('hydron', 0.0, 'mmole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hydron`.')}
    _HEADLINE_OUTPUTS = {'glucose': ('glc', 'mmole', 'glucose. Maps to SBML symbol `glc`.'), 'glucose_6_phosphate': ('g6p', 'mmole', 'glucose-6-phosphate. Maps to SBML symbol `g6p`.'), 'atp': ('atp', 'mmole', 'ATP. Maps to SBML symbol `atp`.'), 'adp': ('adp', 'mmole', 'ADP. Maps to SBML symbol `adp`.'), 'model_state_p': ('phos', 'mmole', 'P. Maps to SBML symbol `phos`.'), 'model_state_h': ('hydron', 'mmole', 'H+. Maps to SBML symbol `hydron`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1904090001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
