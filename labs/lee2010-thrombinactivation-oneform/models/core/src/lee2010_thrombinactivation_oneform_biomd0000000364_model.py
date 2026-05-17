# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lee2010_ThrombinActivation_OneForm."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2010ThrombinactivationOneformBiomd0000000364Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lee2010_ThrombinActivation_OneForm."""

    _SBML_ID = 'BIOMD0000000364'
    _TITLE = 'Lee2010_ThrombinActivation_OneForm'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'E_P_1', 'P', 'M', 'M1', 'E_M1', 'E_M', 'T', 'E_P_2', 'P2', 'P21', 'E_P21', 'E_P2', 'E_P1']
    _SPECIES_LABELS = {'E': 'E', 'E_P_1': 'E_P_1', 'P': 'P', 'M': 'M', 'M1': 'M1', 'E_M1': 'E_M1', 'E_M': 'E_M', 'T': 'T', 'E_P_2': 'E_P_2', 'P2': 'P2', 'P21': 'P21', 'E_P21': 'E_P21', 'E_P2': 'E_P2', 'E_P1': 'E_P1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_e_p_2': ('E_P_2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P_2`.'), 'initial_e_p_1': ('E_P_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P_1`.'), 'initial_e_p21': ('E_P21', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P21`.'), 'initial_e_p2': ('E_P2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P2`.'), 'initial_e_p1': ('E_P1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_P1`.'), 'initial_e_m1': ('E_M1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_M1`.')}
    _HEADLINE_OUTPUTS = {'e_p_2': ('E_P_2', 'native SBML value', 'E_P_2. Maps to SBML symbol `E_P_2`.'), 'e_p_1': ('E_P_1', 'native SBML value', 'E_P_1. Maps to SBML symbol `E_P_1`.'), 'e_p21': ('E_P21', 'native SBML value', 'E_P21. Maps to SBML symbol `E_P21`.'), 'e_p2': ('E_P2', 'native SBML value', 'E_P2. Maps to SBML symbol `E_P2`.'), 'e_p1': ('E_P1', 'native SBML value', 'E_P1. Maps to SBML symbol `E_P1`.'), 'e_m1': ('E_M1', 'native SBML value', 'E_M1. Maps to SBML symbol `E_M1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000364.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
