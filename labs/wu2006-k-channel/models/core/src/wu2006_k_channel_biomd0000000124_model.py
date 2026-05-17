# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wu2006_K+Channel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wu2006KChannelBiomd0000000124Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wu2006_K+Channel."""

    _SBML_ID = 'BIOMD0000000124'
    _TITLE = 'Wu2006_K+Channel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['c', 'cer']
    _SPECIES_LABELS = {'c': 'cytosolic free ca concentration', 'cer': 'ER ca concentration'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_er_ca_concentration': ('cer', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cer`.'), 'initial_cytosolic_free_ca_concentration': ('c', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.')}
    _HEADLINE_OUTPUTS = {'er_ca_concentration': ('cer', 'native SBML value', 'ER ca concentration. Maps to SBML symbol `cer`.'), 'cytosolic_free_ca_concentration': ('c', 'native SBML value', 'cytosolic free ca concentration. Maps to SBML symbol `c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000124.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
