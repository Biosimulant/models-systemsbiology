# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Whitcomb2004_Bicarbonate_Pancreas."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Whitcomb2004BicarbonatePancreasBiomd0000000327Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Whitcomb2004_Bicarbonate_Pancreas."""

    _SBML_ID = 'BIOMD0000000327'
    _TITLE = 'Whitcomb2004_Bicarbonate_Pancreas'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['bb', 'cb', 'nb', 'bi', 'ci', 'ni', 'bl', 'cl']
    _SPECIES_LABELS = {'bb': 'HCO3-', 'cb': 'CL-', 'nb': 'Na+', 'bi': 'HCO3-', 'ci': 'CL-', 'ni': 'Na+', 'bl': 'HCO3-', 'cl': 'CL-'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_na': ('nb', 140.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nb`.'), 'initial_model_state_cl': ('cb', 130.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cb`.'), 'initial_model_state_cl_2': ('ci', 60.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ci`.'), 'initial_hco3': ('bl', 32.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bl`.'), 'initial_hco3_2': ('bb', 22.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bb`.'), 'initial_hco3_3': ('bi', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bi`.')}
    _HEADLINE_OUTPUTS = {'model_state_na': ('nb', 'native SBML value', 'Na+. Maps to SBML symbol `nb`.'), 'model_state_cl': ('cb', 'native SBML value', 'CL-. Maps to SBML symbol `cb`.'), 'model_state_cl_2': ('ci', 'native SBML value', 'CL-. Maps to SBML symbol `ci`.'), 'hco3': ('bl', 'native SBML value', 'HCO3-. Maps to SBML symbol `bl`.'), 'hco3_2': ('bb', 'native SBML value', 'HCO3-. Maps to SBML symbol `bb`.'), 'hco3_3': ('bi', 'native SBML value', 'HCO3-. Maps to SBML symbol `bi`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000327.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
