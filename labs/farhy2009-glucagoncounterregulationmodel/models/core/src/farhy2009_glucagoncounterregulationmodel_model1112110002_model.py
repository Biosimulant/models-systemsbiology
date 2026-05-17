# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Farhy2009_GlucagonCounterRegulationModel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Farhy2009GlucagoncounterregulationmodelModel1112110002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Farhy2009_GlucagonCounterRegulationModel."""

    _SBML_ID = 'MODEL1112110002'
    _TITLE = 'Farhy2009_GlucagonCounterRegulationModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GL', 'INS']
    _SPECIES_LABELS = {'GL': 'GL', 'INS': 'INS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ins': ('INS', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `INS`.'), 'initial_model_state_gl': ('GL', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GL`.')}
    _HEADLINE_OUTPUTS = {'ins': ('INS', 'native SBML value', 'INS. Maps to SBML symbol `INS`.'), 'model_state_gl': ('GL', 'native SBML value', 'GL. Maps to SBML symbol `GL`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1112110002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
