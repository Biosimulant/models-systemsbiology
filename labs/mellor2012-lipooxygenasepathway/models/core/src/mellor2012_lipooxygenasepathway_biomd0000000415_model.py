# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mellor2012_LipooxygenasePathway."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mellor2012LipooxygenasepathwayBiomd0000000415Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mellor2012_LipooxygenasePathway."""

    _SBML_ID = 'BIOMD0000000415'
    _TITLE = 'Mellor2012_LipooxygenasePathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15']
    _SPECIES_LABELS = {'species_1': 'LA', 'species_7': '13HOD-S(Z,E)', 'species_8': '13HOD-R(Z,E)', 'species_9': '13HOD-S(E,E)', 'species_10': '13HOD-R(E,E)', 'species_11': '9HOD-S(Z,E)', 'species_12': '9HOD-R(Z,E)', 'species_13': '9HOD-S(E,E)', 'species_14': '9HOD-R(E,E)', 'species_15': 'nHexanal'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_la': ('species_1', 6.69999967735732e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_n_hexanal': ('species_15', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_15`.'), 'initial_model_state_9_hod_s_z_e': ('species_11', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_11`.'), 'initial_model_state_9_hod_s_e_e': ('species_13', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`.'), 'initial_model_state_9_hod_r_z_e': ('species_12', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`.'), 'initial_model_state_9_hod_r_e_e': ('species_14', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.')}
    _HEADLINE_OUTPUTS = {'model_state_la': ('species_1', 'native SBML value', 'LA. Maps to SBML symbol `species_1`.'), 'n_hexanal': ('species_15', 'native SBML value', 'nHexanal. Maps to SBML symbol `species_15`.'), 'model_state_9_hod_s_z_e': ('species_11', 'native SBML value', '9HOD-S(Z,E). Maps to SBML symbol `species_11`.'), 'model_state_9_hod_s_e_e': ('species_13', 'native SBML value', '9HOD-S(E,E). Maps to SBML symbol `species_13`.'), 'model_state_9_hod_r_z_e': ('species_12', 'native SBML value', '9HOD-R(Z,E). Maps to SBML symbol `species_12`.'), 'model_state_9_hod_r_e_e': ('species_14', 'native SBML value', '9HOD-R(E,E). Maps to SBML symbol `species_14`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000415.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
