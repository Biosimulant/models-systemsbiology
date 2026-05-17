# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zhang2007 - Mechanism of DNA damage response (Model3)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhang2007MechanismOfDnaDamageResponseModelBiomd0000001010Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zhang2007 - Mechanism of DNA damage response (Model3)."""

    _SBML_ID = 'BIOMD0000001010'
    _TITLE = 'Zhang2007 - Mechanism of DNA damage response (Model3)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p53', 'DNAdamage', 'MDM2']
    _SPECIES_LABELS = {'p53': 'p53', 'DNAdamage': 'DNAdamage', 'MDM2': 'MDM2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_dn_adamage': ('DNAdamage', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DNAdamage`.'), 'initial_model_state_p53': ('p53', 0.36, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`.'), 'initial_mdm2': ('MDM2', 0.71, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2`.')}
    _HEADLINE_OUTPUTS = {'dn_adamage': ('DNAdamage', 'substance', 'DNAdamage. Maps to SBML symbol `DNAdamage`.'), 'p53': ('p53', 'substance', 'p53. Maps to SBML symbol `p53`.'), 'mdm2': ('MDM2', 'substance', 'MDM2. Maps to SBML symbol `MDM2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001010.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
