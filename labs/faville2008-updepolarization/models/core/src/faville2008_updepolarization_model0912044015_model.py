# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Faville2008_UPdepolarization."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Faville2008UpdepolarizationModel0912044015Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Faville2008_UPdepolarization."""

    _SBML_ID = 'MODEL0912044015'
    _TITLE = 'Faville2008_UPdepolarization'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Vm', 'H', 'phi3', 'CS1', 'CS2', 'CER', 'CMT', 'NS1']
    _SPECIES_LABELS = {'Vm': 'Vm', 'H': 'H', 'phi3': 'Phi3', 'CS1': 'CS1', 'CS2': 'CS2', 'CER': 'CER', 'CMT': 'CMT', 'NS1': 'NS1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_vm': ('Vm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm`.'), 'initial_phi3': ('phi3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `phi3`.'), 'initial_model_state_ns1': ('NS1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NS1`.'), 'initial_model_state_cs2': ('CS2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CS2`.'), 'initial_model_state_cs1': ('CS1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CS1`.'), 'initial_model_state_cmt': ('CMT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CMT`.')}
    _HEADLINE_OUTPUTS = {'model_state_vm': ('Vm', 'native SBML value', 'Vm. Maps to SBML symbol `Vm`.'), 'phi3': ('phi3', 'native SBML value', 'Phi3. Maps to SBML symbol `phi3`.'), 'ns1': ('NS1', 'native SBML value', 'NS1. Maps to SBML symbol `NS1`.'), 'cs2': ('CS2', 'native SBML value', 'CS2. Maps to SBML symbol `CS2`.'), 'cs1': ('CS1', 'native SBML value', 'CS1. Maps to SBML symbol `CS1`.'), 'cmt': ('CMT', 'native SBML value', 'CMT. Maps to SBML symbol `CMT`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912044015.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
