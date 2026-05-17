# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Baugh1998 - Regulation of coagulation factor Xa by TFPI."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Baugh1998RegulationOfCoagulationFactorXaByModel1807180001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Baugh1998 - Regulation of coagulation factor Xa by TFPI."""

    _SBML_ID = 'MODEL1807180001'
    _TITLE = 'Baugh1998 - Regulation of coagulation factor Xa by TFPI'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'E', 'ES', 'P', 'I', 'P_I', 'EP_I']
    _SPECIES_LABELS = {'S': 'S', 'E': 'E', 'ES': 'ES', 'P': 'P', 'I': 'I', 'P_I': 'P:I', 'EP_I': 'EP:I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p_i': ('P_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_I`.'), 'initial_ep_i': ('EP_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EP_I`.'), 'initial_model_state_es': ('ES', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ES`.'), 'initial_model_state_s': ('S', 0.17, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_i': ('I', 0.0024, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_model_state_e': ('E', 0.000128, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E`.')}
    _HEADLINE_OUTPUTS = {'p_i': ('P_I', 'native SBML value', 'P:I. Maps to SBML symbol `P_I`.'), 'ep_i': ('EP_I', 'native SBML value', 'EP:I. Maps to SBML symbol `EP_I`.'), 'model_state_es': ('ES', 'native SBML value', 'ES. Maps to SBML symbol `ES`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'model_state_e': ('E', 'native SBML value', 'E. Maps to SBML symbol `E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1807180001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
