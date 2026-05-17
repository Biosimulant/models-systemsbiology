# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zager2007_Genistein_Biliary_Excretion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zager2007GenisteinBiliaryExcretionModel6963432821Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zager2007_Genistein_Biliary_Excretion."""

    _SBML_ID = 'MODEL6963432821'
    _TITLE = 'Zager2007_Genistein_Biliary_Excretion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Cgen_pp', 'Cgen_rp', 'Cgen_l', 'Cgen_GI', 'Ccon_l', 'Ccon_ROB', 'Acon_b']
    _SPECIES_LABELS = {'Cgen_pp': 'Cgen Pp', 'Cgen_rp': 'Cgen Rp', 'Cgen_l': 'Cgen L', 'Cgen_GI': 'Cgen GI', 'Ccon_l': 'Ccon L', 'Ccon_ROB': 'Ccon ROB', 'Acon_b': 'Acon B'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cgen_rp': ('Cgen_rp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cgen_rp`.'), 'initial_cgen_pp': ('Cgen_pp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cgen_pp`.'), 'initial_cgen_l': ('Cgen_l', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cgen_l`.'), 'initial_cgen_gi': ('Cgen_GI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cgen_GI`.'), 'initial_ccon_rob': ('Ccon_ROB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ccon_ROB`.'), 'initial_ccon_l': ('Ccon_l', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ccon_l`.')}
    _HEADLINE_OUTPUTS = {'cgen_rp': ('Cgen_rp', 'native SBML value', 'Cgen Rp. Maps to SBML symbol `Cgen_rp`.'), 'cgen_pp': ('Cgen_pp', 'native SBML value', 'Cgen Pp. Maps to SBML symbol `Cgen_pp`.'), 'cgen_l': ('Cgen_l', 'native SBML value', 'Cgen L. Maps to SBML symbol `Cgen_l`.'), 'cgen_gi': ('Cgen_GI', 'native SBML value', 'Cgen GI. Maps to SBML symbol `Cgen_GI`.'), 'ccon_rob': ('Ccon_ROB', 'native SBML value', 'Ccon ROB. Maps to SBML symbol `Ccon_ROB`.'), 'ccon_l': ('Ccon_l', 'native SBML value', 'Ccon L. Maps to SBML symbol `Ccon_l`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6963432821.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
