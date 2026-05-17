# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zhang2007 - Mechanism of DNA damage response (Model2)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhang2007MechanismOfDnaDamageResponseModelBiomd0000001009Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zhang2007 - Mechanism of DNA damage response (Model2)."""

    _SBML_ID = 'BIOMD0000001009'
    _TITLE = 'Zhang2007 - Mechanism of DNA damage response (Model2)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p53_total', 'MDM2cyt', 'MDM2nuc', 'DNAdamage', 'p53_inact', 'p53_act']
    _SPECIES_LABELS = {'p53_total': 'p53_total', 'MDM2cyt': 'MDM2cyt', 'MDM2nuc': 'MDM2nuc', 'DNAdamage': 'DNAdamage', 'p53_inact': 'p53_inact', 'p53_act': 'p53_act'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_dn_adamage': ('DNAdamage', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DNAdamage`.'), 'initial_p53_total': ('p53_total', 0.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_total`.'), 'initial_p53_inact': ('p53_inact', 0.19, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_inact`.'), 'initial_p53_act': ('p53_act', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_act`.'), 'initial_mdm2nuc': ('MDM2nuc', 0.55, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2nuc`.'), 'initial_mdm2cyt': ('MDM2cyt', 0.21, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2cyt`.')}
    _HEADLINE_OUTPUTS = {'dn_adamage': ('DNAdamage', 'native SBML value', 'DNAdamage. Maps to SBML symbol `DNAdamage`.'), 'p53_total': ('p53_total', 'native SBML value', 'p53_total. Maps to SBML symbol `p53_total`.'), 'p53_inact': ('p53_inact', 'native SBML value', 'p53_inact. Maps to SBML symbol `p53_inact`.'), 'p53_act': ('p53_act', 'native SBML value', 'p53_act. Maps to SBML symbol `p53_act`.'), 'mdm2nuc': ('MDM2nuc', 'native SBML value', 'MDM2nuc. Maps to SBML symbol `MDM2nuc`.'), 'mdm2cyt': ('MDM2cyt', 'native SBML value', 'MDM2cyt. Maps to SBML symbol `MDM2cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001009.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
