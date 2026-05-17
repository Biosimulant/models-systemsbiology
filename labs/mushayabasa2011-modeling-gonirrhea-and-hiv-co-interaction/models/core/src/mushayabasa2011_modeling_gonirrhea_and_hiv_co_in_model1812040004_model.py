# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mushayabasa2011- Modeling gonirrhea and HIV co-interaction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mushayabasa2011ModelingGonirrheaAndHivCoInModel1812040004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mushayabasa2011- Modeling gonirrhea and HIV co-interaction."""

    _SBML_ID = 'MODEL1812040004'
    _TITLE = 'Mushayabasa2011- Modeling gonirrhea and HIV co-interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'I_G', 'I_H', 'I_GH', 'A_H', 'A_GH', 'A_HT', 'A_GHT']
    _SPECIES_LABELS = {'S': 'S', 'I_G': 'I_G', 'I_H': 'I_H', 'I_GH': 'I_GH', 'A_H': 'A_H', 'A_GH': 'A_GH', 'A_HT': 'A_HT', 'A_GHT': 'A_GHT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_i_g': ('I_G', 50000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_G`.'), 'initial_model_state_i_h': ('I_H', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_H`.'), 'initial_i_gh': ('I_GH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I_GH`.'), 'initial_a_ht': ('A_HT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_HT`.'), 'initial_model_state_a_h': ('A_H', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_H`.'), 'initial_a_ght': ('A_GHT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_GHT`.')}
    _HEADLINE_OUTPUTS = {'i_g': ('I_G', 'native SBML value', 'I_G. Maps to SBML symbol `I_G`.'), 'i_h': ('I_H', 'native SBML value', 'I_H. Maps to SBML symbol `I_H`.'), 'i_gh': ('I_GH', 'native SBML value', 'I_GH. Maps to SBML symbol `I_GH`.'), 'a_ht': ('A_HT', 'native SBML value', 'A_HT. Maps to SBML symbol `A_HT`.'), 'a_h': ('A_H', 'native SBML value', 'A_H. Maps to SBML symbol `A_H`.'), 'a_ght': ('A_GHT', 'native SBML value', 'A_GHT. Maps to SBML symbol `A_GHT`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812040004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
