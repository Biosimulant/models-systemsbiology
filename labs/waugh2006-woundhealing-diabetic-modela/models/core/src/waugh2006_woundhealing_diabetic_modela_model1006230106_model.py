# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Waugh2006_WoundHealing_Diabetic_ModelA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Waugh2006WoundhealingDiabeticModelaModel1006230106Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Waugh2006_WoundHealing_Diabetic_ModelA."""

    _SBML_ID = 'MODEL1006230106'
    _TITLE = 'Waugh2006_WoundHealing_Diabetic_ModelA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['phi_I', 'phi_R', 'T', 'P', 'F', 'C', 'H']
    _SPECIES_LABELS = {'phi_I': 'Phi I', 'phi_R': 'Phi R', 'T': 'T', 'P': 'P', 'F': 'F', 'C': 'C', 'H': 'H'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_phi_r': ('phi_R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `phi_R`.'), 'initial_phi_i': ('phi_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `phi_I`.'), 'initial_model_state_t': ('T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_p': ('P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_model_state_h': ('H', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`.'), 'initial_model_state_f': ('F', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `F`.')}
    _HEADLINE_OUTPUTS = {'phi_r': ('phi_R', 'native SBML value', 'Phi R. Maps to SBML symbol `phi_R`.'), 'phi_i': ('phi_I', 'native SBML value', 'Phi I. Maps to SBML symbol `phi_I`.'), 'model_state_t': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.'), 'model_state_h': ('H', 'native SBML value', 'H. Maps to SBML symbol `H`.'), 'model_state_f': ('F', 'native SBML value', 'F. Maps to SBML symbol `F`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230106.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
