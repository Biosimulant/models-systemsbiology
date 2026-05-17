# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Warren2009_CalciumWavePropagation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Warren2009CalciumwavepropagationModel1006230018Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Warren2009_CalciumWavePropagation."""

    _SBML_ID = 'MODEL1006230018'
    _TITLE = 'Warren2009_CalciumWavePropagation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['volumeCa_i', 'volumeCa_er', 'volume_iIP3', 'PIP2', 'ATP_e', 'O', 'I1', 'I2']
    _SPECIES_LABELS = {'volumeCa_i': 'VolumeCa I', 'volumeCa_er': 'VolumeCa Er', 'volume_iIP3': 'Volume IIP3', 'PIP2': 'PIP2', 'ATP_e': 'ATP E', 'O': 'O', 'I1': 'I1', 'I2': 'I2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_volume_ca_i': ('volumeCa_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `volumeCa_i`.'), 'initial_volume_ca_er': ('volumeCa_er', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `volumeCa_er`.'), 'initial_volume_iip3': ('volume_iIP3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `volume_iIP3`.'), 'initial_pip2': ('PIP2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP2`.'), 'initial_model_state_i2': ('I2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I2`.'), 'initial_model_state_i1': ('I1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I1`.')}
    _HEADLINE_OUTPUTS = {'volume_ca_i': ('volumeCa_i', 'native SBML value', 'VolumeCa I. Maps to SBML symbol `volumeCa_i`.'), 'volume_ca_er': ('volumeCa_er', 'native SBML value', 'VolumeCa Er. Maps to SBML symbol `volumeCa_er`.'), 'volume_iip3': ('volume_iIP3', 'native SBML value', 'Volume IIP3. Maps to SBML symbol `volume_iIP3`.'), 'pip2': ('PIP2', 'native SBML value', 'PIP2. Maps to SBML symbol `PIP2`.'), 'model_state_i2': ('I2', 'native SBML value', 'I2. Maps to SBML symbol `I2`.'), 'model_state_i1': ('I1', 'native SBML value', 'I1. Maps to SBML symbol `I1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230018.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
