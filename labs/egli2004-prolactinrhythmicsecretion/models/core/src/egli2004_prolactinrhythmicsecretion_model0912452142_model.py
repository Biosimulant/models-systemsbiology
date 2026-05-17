# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Egli2004_ProlactinRhythmicSecretion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Egli2004ProlactinrhythmicsecretionModel0912452142Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Egli2004_ProlactinRhythmicSecretion."""

    _SBML_ID = 'MODEL0912452142'
    _TITLE = 'Egli2004_ProlactinRhythmicSecretion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['PRL', 'DA', 'OT']
    _SPECIES_LABELS = {'PRL': 'PRL', 'DA': 'DA', 'OT': 'OT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_prl': ('PRL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PRL`.'), 'initial_model_state_ot': ('OT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `OT`.'), 'initial_model_state_da': ('DA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DA`.')}
    _HEADLINE_OUTPUTS = {'prl': ('PRL', 'native SBML value', 'PRL. Maps to SBML symbol `PRL`.'), 'model_state_ot': ('OT', 'native SBML value', 'OT. Maps to SBML symbol `OT`.'), 'model_state_da': ('DA', 'native SBML value', 'DA. Maps to SBML symbol `DA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912452142.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
