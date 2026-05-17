# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Koivumaki2009_SERCAATPase_Standalone."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koivumaki2009SercaatpaseStandaloneModel1006230023Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Koivumaki2009_SERCAATPase_Standalone."""

    _SBML_ID = 'MODEL1006230023'
    _TITLE = 'Koivumaki2009_SERCAATPase_Standalone'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Ca_serca']
    _SPECIES_LABELS = {'Ca_serca': 'Ca Serca'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_serca': ('Ca_serca', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_serca`.')}
    _HEADLINE_OUTPUTS = {'ca_serca': ('Ca_serca', 'native SBML value', 'Ca Serca. Maps to SBML symbol `Ca_serca`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230023.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
