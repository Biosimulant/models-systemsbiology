# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for LeBeau1999 - IP3-dependent intracellular calcium oscillations due to agonist stimulation from Cholecytokinin."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lebeau1999Ip3DependentIntracellularCalciumOBiomd0000000965Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for LeBeau1999 - IP3-dependent intracellular calcium oscillations due to agonist stimulation from Cholecytokinin."""

    _SBML_ID = 'BIOMD0000000965'
    _TITLE = 'LeBeau1999 - IP3-dependent intracellular calcium oscillations due to agonist stimulation from Cholecytokinin'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'O', 'I1', 'I2', 'c']
    _SPECIES_LABELS = {'S': 'S', 'O': 'O', 'I1': 'I1', 'I2': 'I2', 'c': 'Ca2+'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ca2': ('c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c`.'), 'initial_model_state_i2': ('I2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I2`.'), 'initial_model_state_i1': ('I1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I1`.'), 'initial_model_state_s': ('S', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`.'), 'initial_model_state_o': ('O', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O`.')}
    _HEADLINE_OUTPUTS = {'ca2': ('c', 'native SBML value', 'Ca2+. Maps to SBML symbol `c`.'), 'model_state_i2': ('I2', 'native SBML value', 'I2. Maps to SBML symbol `I2`.'), 'model_state_i1': ('I1', 'native SBML value', 'I1. Maps to SBML symbol `I1`.'), 'model_state_s': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'model_state_o': ('O', 'native SBML value', 'O. Maps to SBML symbol `O`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000965.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
