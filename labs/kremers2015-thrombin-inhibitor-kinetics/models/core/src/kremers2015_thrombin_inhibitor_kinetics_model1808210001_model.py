# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kremers2015 - Thrombin Inhibitor Kinetics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kremers2015ThrombinInhibitorKineticsModel1808210001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kremers2015 - Thrombin Inhibitor Kinetics."""

    _SBML_ID = 'MODEL1808210001'
    _TITLE = 'Kremers2015 - Thrombin Inhibitor Kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T_AT', 'T_a2M', 'T_MS', 'T', 'a2M', 'AT', 'MS']
    _SPECIES_LABELS = {'T_AT': 'T:AT', 'T_a2M': 'T:a2M', 'T_MS': 'T:MS', 'T': 'T', 'a2M': 'a2M', 'AT': 'AT', 'MS': 'MS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_a2_m': ('a2M', 3.03e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a2M`.'), 'initial_t_a2_m': ('T_a2M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_a2M`.'), 'initial_t_ms': ('T_MS', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_MS`.'), 'initial_t_at': ('T_AT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_AT`.'), 'initial_model_state_at': ('AT', 1.94e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AT`.'), 'initial_model_state_ms': ('MS', 7.47e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MS`.')}
    _HEADLINE_OUTPUTS = {'a2_m': ('a2M', 'native SBML value', 'a2M. Maps to SBML symbol `a2M`.'), 't_a2_m': ('T_a2M', 'native SBML value', 'T:a2M. Maps to SBML symbol `T_a2M`.'), 't_ms': ('T_MS', 'native SBML value', 'T:MS. Maps to SBML symbol `T_MS`.'), 't_at': ('T_AT', 'native SBML value', 'T:AT. Maps to SBML symbol `T_AT`.'), 'model_state_at': ('AT', 'native SBML value', 'AT. Maps to SBML symbol `AT`.'), 'model_state_ms': ('MS', 'native SBML value', 'MS. Maps to SBML symbol `MS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808210001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
