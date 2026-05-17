# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Golomb2006_SomaticBursting."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Golomb2006SomaticburstingBiomd0000000118Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Golomb2006_SomaticBursting."""

    _SBML_ID = 'BIOMD0000000118'
    _TITLE = 'Golomb2006_SomaticBursting'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['zzs', 'bbs', 'hhs', 'V', 'nns']
    _SPECIES_LABELS = {'zzs': 'Zzs', 'bbs': 'Bbs', 'hhs': 'Hhs', 'V': 'V', 'nns': 'Nns'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_zzs': ('zzs', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zzs`.'), 'initial_model_state_nns': ('nns', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nns`.'), 'initial_model_state_hhs': ('hhs', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hhs`.'), 'initial_model_state_bbs': ('bbs', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bbs`.'), 'initial_model_state_v': ('V', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'zzs': ('zzs', 'native SBML value', 'Zzs. Maps to SBML symbol `zzs`.'), 'nns': ('nns', 'native SBML value', 'Nns. Maps to SBML symbol `nns`.'), 'hhs': ('hhs', 'native SBML value', 'Hhs. Maps to SBML symbol `hhs`.'), 'bbs': ('bbs', 'native SBML value', 'Bbs. Maps to SBML symbol `bbs`.'), 'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000118.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
