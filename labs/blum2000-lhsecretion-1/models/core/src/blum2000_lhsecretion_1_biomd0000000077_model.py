# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Blum2000_LHsecretion_1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Blum2000Lhsecretion1Biomd0000000077Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Blum2000_LHsecretion_1."""

    _SBML_ID = 'BIOMD0000000077'
    _TITLE = 'Blum2000_LHsecretion_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['H', 'HR', 'R', 'HRRH', 'E', 'GQ', 'IP3', 'CHO']
    _SPECIES_LABELS = {'H': 'H', 'HR': 'HR', 'R': 'R', 'HRRH': 'HRRH', 'E': 'E', 'GQ': 'GQ', 'IP3': 'IP3', 'CHO': 'CHO'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_gq': ('GQ', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GQ`.'), 'initial_model_state_ip3': ('IP3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IP3`.'), 'initial_hrrh': ('HRRH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HRRH`.'), 'initial_model_state_hr': ('HR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HR`.'), 'initial_model_state_cho': ('CHO', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CHO`.'), 'initial_model_state_h': ('H', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`.')}
    _HEADLINE_OUTPUTS = {'model_state_gq': ('GQ', 'native SBML value', 'GQ. Maps to SBML symbol `GQ`.'), 'ip3': ('IP3', 'native SBML value', 'IP3. Maps to SBML symbol `IP3`.'), 'hrrh': ('HRRH', 'native SBML value', 'HRRH. Maps to SBML symbol `HRRH`.'), 'model_state_hr': ('HR', 'native SBML value', 'HR. Maps to SBML symbol `HR`.'), 'cho': ('CHO', 'native SBML value', 'CHO. Maps to SBML symbol `CHO`.'), 'model_state_h': ('H', 'native SBML value', 'H. Maps to SBML symbol `H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000077.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
