# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ciliberto2005 - Steady states and oscillations in the p53/Mdm2 network."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ciliberto2005SteadyStatesAndOscillationsInBiomd0000001006Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ciliberto2005 - Steady states and oscillations in the p53/Mdm2 network."""

    _SBML_ID = 'BIOMD0000001006'
    _TITLE = 'Ciliberto2005 - Steady states and oscillations in the p53/Mdm2 network'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['DNA_damage', 'IR', 'p53_total', 'p53_ub', 'p53_ub_ub', 'Mdm2_cyt', 'Mdm2_p_cyt', 'Mdm2_p_nuc', 'p53', 'MDM2_total']
    _SPECIES_LABELS = {'DNA_damage': 'DNA_damage', 'IR': 'IR', 'p53_total': 'p53_total', 'p53_ub': 'p53_ub', 'p53_ub_ub': 'p53_ub_ub', 'Mdm2_cyt': 'Mdm2_cyt', 'Mdm2_p_cyt': 'Mdm2_p_cyt', 'Mdm2_p_nuc': 'Mdm2_p_nuc', 'p53': 'p53', 'MDM2_total': 'MDM2_total'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mdm2_p_nuc': ('Mdm2_p_nuc', 0.331800000000002, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_p_nuc`.'), 'initial_mdm2_total': ('MDM2_total', 0.150090000000001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MDM2_total`.'), 'initial_mdm2_cyt': ('Mdm2_cyt', 0.1161, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_cyt`.'), 'initial_p53_total': ('p53_total', 0.07118, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_total`.'), 'initial_model_state_p53': ('p53', 0.039794, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`.'), 'initial_p53_ub': ('p53_ub', 0.02456, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_ub`.')}
    _HEADLINE_OUTPUTS = {'mdm2_p_nuc': ('Mdm2_p_nuc', 'native SBML value', 'Mdm2_p_nuc. Maps to SBML symbol `Mdm2_p_nuc`.'), 'mdm2_total': ('MDM2_total', 'native SBML value', 'MDM2_total. Maps to SBML symbol `MDM2_total`.'), 'mdm2_cyt': ('Mdm2_cyt', 'native SBML value', 'Mdm2_cyt. Maps to SBML symbol `Mdm2_cyt`.'), 'p53_total': ('p53_total', 'native SBML value', 'p53_total. Maps to SBML symbol `p53_total`.'), 'p53': ('p53', 'native SBML value', 'p53. Maps to SBML symbol `p53`.'), 'p53_ub': ('p53_ub', 'native SBML value', 'p53_ub. Maps to SBML symbol `p53_ub`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001006.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
