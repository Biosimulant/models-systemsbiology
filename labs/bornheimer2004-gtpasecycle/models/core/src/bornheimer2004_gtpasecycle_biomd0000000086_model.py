# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bornheimer2004_GTPaseCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bornheimer2004GtpasecycleBiomd0000000086Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bornheimer2004_GTPaseCycle."""

    _SBML_ID = 'BIOMD0000000086'
    _TITLE = 'Bornheimer2004_GTPaseCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16']
    _SPECIES_LABELS = {'species_0': 'A', 'species_1': 'G', 'species_2': 'GA', 'species_3': 'T', 'species_4': 'R', 'species_5': 'G*T', 'species_6': 'GD', 'species_7': 'Pi', 'species_8': 'D', 'species_9': 'RG', 'species_10': 'RG*T', 'species_11': 'G*AT', 'species_12': 'GAD', 'species_13': 'RGD', 'species_14': 'RGA', 'species_15': 'RG*AT', 'species_16': 'RGAD'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pi': ('species_7', 0.0044, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_model_state_t': ('species_3', 0.000468, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_model_state_d': ('species_8', 0.000149, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_model_state_r': ('species_4', 1e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_model_state_g': ('species_1', 1e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_model_state_rgd': ('species_13', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`.')}
    _HEADLINE_OUTPUTS = {'model_state_pi': ('species_7', 'native SBML value', 'Pi. Maps to SBML symbol `species_7`.'), 'model_state_t': ('species_3', 'native SBML value', 'T. Maps to SBML symbol `species_3`.'), 'model_state_d': ('species_8', 'native SBML value', 'D. Maps to SBML symbol `species_8`.'), 'model_state_r': ('species_4', 'native SBML value', 'R. Maps to SBML symbol `species_4`.'), 'model_state_g': ('species_1', 'native SBML value', 'G. Maps to SBML symbol `species_1`.'), 'rgd': ('species_13', 'native SBML value', 'RGD. Maps to SBML symbol `species_13`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000086.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
