# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Aston2018 - Dynamics of Hepatitis C Infection."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aston2018DynamicsOfHepatitisCInfectionBiomd0000000713Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Aston2018 - Dynamics of Hepatitis C Infection."""

    _SBML_ID = 'BIOMD0000000713'
    _TITLE = 'Aston2018 - Dynamics of Hepatitis C Infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'V']
    _SPECIES_LABELS = {'T': 'Healthy Hepatocytes (T)', 'I': 'Infected Hepatocytes (I)', 'V': 'Viral Load (V)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_viral_load_v': ('V', 4450000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_infected_hepatocytes_i': ('I', 417520.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_healthy_hepatocytes_t': ('T', 3.3246, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'viral_load_v': ('V', 'native SBML value', 'Viral Load (V). Maps to SBML symbol `V`.'), 'infected_hepatocytes_i': ('I', 'native SBML value', 'Infected Hepatocytes (I). Maps to SBML symbol `I`.'), 'healthy_hepatocytes_t': ('T', 'native SBML value', 'Healthy Hepatocytes (T). Maps to SBML symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000713.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
