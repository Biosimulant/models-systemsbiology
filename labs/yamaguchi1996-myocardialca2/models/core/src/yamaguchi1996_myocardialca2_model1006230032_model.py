# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Yamaguchi1996_MyocardialCa2."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yamaguchi1996Myocardialca2Model1006230032Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Yamaguchi1996_MyocardialCa2."""

    _SBML_ID = 'MODEL1006230032'
    _TITLE = 'Yamaguchi1996_MyocardialCa2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['TnCa', 'CB_on', 'CumCB_on', 'CumCB_off', 'FTI']
    _SPECIES_LABELS = {'TnCa': 'TnCa', 'CB_on': 'CB On', 'CumCB_on': 'CumCB On', 'CumCB_off': 'CumCB Off', 'FTI': 'FTI'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tn_ca': ('TnCa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TnCa`.'), 'initial_model_state_fti': ('FTI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FTI`.'), 'initial_cum_cb_on': ('CumCB_on', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CumCB_on`.'), 'initial_cum_cb_off': ('CumCB_off', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CumCB_off`.'), 'initial_cb_on': ('CB_on', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CB_on`.')}
    _HEADLINE_OUTPUTS = {'tn_ca': ('TnCa', 'native SBML value', 'TnCa. Maps to SBML symbol `TnCa`.'), 'fti': ('FTI', 'native SBML value', 'FTI. Maps to SBML symbol `FTI`.'), 'cum_cb_on': ('CumCB_on', 'native SBML value', 'CumCB On. Maps to SBML symbol `CumCB_on`.'), 'cum_cb_off': ('CumCB_off', 'native SBML value', 'CumCB Off. Maps to SBML symbol `CumCB_off`.'), 'cb_on': ('CB_on', 'native SBML value', 'CB On. Maps to SBML symbol `CB_on`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230032.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
