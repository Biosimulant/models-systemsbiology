# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zhang2007 - Mechanism of DNA damage response (Model1)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhang2007MechanismOfDnaDamageResponseModelBiomd0000001007Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zhang2007 - Mechanism of DNA damage response (Model1)."""

    _SBML_ID = 'BIOMD0000001007'
    _TITLE = 'Zhang2007 - Mechanism of DNA damage response (Model1)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p53', 'MDM2cyt', 'MDM2nuc', 'DNAdamage']
    _SPECIES_LABELS = {'p53': 'p53', 'MDM2cyt': 'MDM2cyt', 'MDM2nuc': 'MDM2nuc', 'DNAdamage': 'DNAdamage'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_dn_adamage': ('DNAdamage', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DNAdamage`.'), 'initial_model_state_p53': ('p53', 0.186, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`.'), 'initial_mdm2nuc': ('MDM2nuc', 0.647000000000002, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2nuc`.'), 'initial_mdm2cyt': ('MDM2cyt', 0.158, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2cyt`.')}
    _HEADLINE_OUTPUTS = {'dn_adamage': ('DNAdamage', 'native SBML value', 'DNAdamage. Maps to SBML symbol `DNAdamage`.'), 'p53': ('p53', 'native SBML value', 'p53. Maps to SBML symbol `p53`.'), 'mdm2nuc': ('MDM2nuc', 'native SBML value', 'MDM2nuc. Maps to SBML symbol `MDM2nuc`.'), 'mdm2cyt': ('MDM2cyt', 'native SBML value', 'MDM2cyt. Maps to SBML symbol `MDM2cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001007.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
