# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rovers1995_Photsynthetic_Oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rovers1995PhotsyntheticOscillationsBiomd0000000292Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rovers1995_Photsynthetic_Oscillations."""

    _SBML_ID = 'BIOMD0000000292'
    _TITLE = 'Rovers1995_Photsynthetic_Oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NADPH', 'ADP', 'ATP', 'X', 'Y', 'NADP']
    _SPECIES_LABELS = {'NADPH': 'NADPH', 'ADP': 'ADP', 'ATP': 'ATP', 'X': 'X', 'Y': 'Y', 'NADP': 'NADP_super_+'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nadp_super': ('NADP', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`.'), 'initial_model_state_adp': ('ADP', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_nadph': ('NADPH', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`.'), 'initial_model_state_atp': ('ATP', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_x': ('X', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_model_state_y': ('Y', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.')}
    _HEADLINE_OUTPUTS = {'nadp_super': ('NADP', 'native SBML value', 'NADP_super_+. Maps to SBML symbol `NADP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'nadph': ('NADPH', 'native SBML value', 'NADPH. Maps to SBML symbol `NADPH`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.'), 'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000292.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
