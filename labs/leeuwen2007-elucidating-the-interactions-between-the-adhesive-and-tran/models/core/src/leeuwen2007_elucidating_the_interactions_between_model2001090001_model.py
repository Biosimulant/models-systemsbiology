# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leeuwen2007 - Elucidating the interactions between the adhesive and transcriptional functions of beta-catenin in normal and cancerous cells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leeuwen2007ElucidatingTheInteractionsBetweenModel2001090001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leeuwen2007 - Elucidating the interactions between the adhesive and transcriptional functions of beta-catenin in normal and cancerous cells."""

    _SBML_ID = 'MODEL2001090001'
    _TITLE = 'Leeuwen2007 - Elucidating the interactions between the adhesive and transcriptional functions of beta-catenin in normal and cancerous cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['D', 'X', 'C0', 'A', 'Cu', 'CA', 'C0T', 'T', 'Y', 'Cc', 'CcT']
    _SPECIES_LABELS = {'D': 'D', 'X': 'X', 'C0': 'C0', 'A': 'A', 'Cu': 'Cu', 'CA': 'CA', 'C0T': 'C0T', 'T': 'T', 'Y': 'Y', 'Cc': 'Cc', 'CcT': 'CcT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ca': ('CA', 18.14, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CA`.'), 'initial_c0_t': ('C0T', 2.54, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C0T`.'), 'initial_model_state_c0': ('C0', 2.54, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C0`.'), 'initial_model_state_cu': ('Cu', 0.45, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cu`.'), 'initial_cc_t': ('CcT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CcT`.'), 'initial_model_state_cc': ('Cc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cc`.')}
    _HEADLINE_OUTPUTS = {'model_state_ca': ('CA', 'native SBML value', 'CA. Maps to SBML symbol `CA`.'), 'c0_t': ('C0T', 'native SBML value', 'C0T. Maps to SBML symbol `C0T`.'), 'model_state_c0': ('C0', 'native SBML value', 'C0. Maps to SBML symbol `C0`.'), 'model_state_cu': ('Cu', 'native SBML value', 'Cu. Maps to SBML symbol `Cu`.'), 'cc_t': ('CcT', 'native SBML value', 'CcT. Maps to SBML symbol `CcT`.'), 'model_state_cc': ('Cc', 'native SBML value', 'Cc. Maps to SBML symbol `Cc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001090001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
