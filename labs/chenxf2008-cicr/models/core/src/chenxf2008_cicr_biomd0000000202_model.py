# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for ChenXF2008_CICR."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chenxf2008CicrBiomd0000000202Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for ChenXF2008_CICR."""

    _SBML_ID = 'BIOMD0000000202'
    _TITLE = 'ChenXF2008_CICR'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ca_Cyt', 'IP3_Cyt', 'Ca_ER', 'S2', 'S2a', 'S4', 'Oc', 'O_o', 'Orai1']
    _SPECIES_LABELS = {'Ca_Cyt': 'Ca Cyt', 'IP3_Cyt': 'IP3 Cyt', 'Ca_ER': 'Ca ER', 'S2': 'S2', 'S2a': 'S2A', 'S4': 'S4', 'Oc': 'Oc', 'O_o': 'O O', 'Orai1': 'Orai1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_s2': ('S2', 0.54, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S2`.'), 'initial_s2_a': ('S2a', 0.06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S2a`.'), 'initial_orai1': ('Orai1', 0.001, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Orai1`.'), 'initial_model_state_s4': ('S4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S4`.'), 'initial_model_state_oc': ('Oc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Oc`.'), 'initial_model_state_o_o': ('O_o', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O_o`.')}
    _HEADLINE_OUTPUTS = {'model_state_s2': ('S2', 'native SBML value', 'S2. Maps to SBML symbol `S2`.'), 's2_a': ('S2a', 'native SBML value', 'S2A. Maps to SBML symbol `S2a`.'), 'orai1': ('Orai1', 'native SBML value', 'Orai1. Maps to SBML symbol `Orai1`.'), 'model_state_s4': ('S4', 'native SBML value', 'S4. Maps to SBML symbol `S4`.'), 'model_state_oc': ('Oc', 'native SBML value', 'Oc. Maps to SBML symbol `Oc`.'), 'o_o': ('O_o', 'native SBML value', 'O O. Maps to SBML symbol `O_o`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000202.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
