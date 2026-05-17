# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lee2010_ThrombinActivation_OneForm_minimal."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2010ThrombinactivationOneformMinimalBiomd0000000363Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lee2010_ThrombinActivation_OneForm_minimal."""

    _SBML_ID = 'BIOMD0000000363'
    _TITLE = 'Lee2010_ThrombinActivation_OneForm_minimal'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['II', 'M', 'IIa', 'P2']
    _SPECIES_LABELS = {'II': 'II', 'M': 'M', 'IIa': 'IIa', 'P2': 'P2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ii': ('II', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II`.'), 'initial_model_state_p2': ('P2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`.'), 'initial_i_ia': ('IIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa`.'), 'initial_model_state_m': ('M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_ii': ('II', 'native SBML value', 'II. Maps to SBML symbol `II`.'), 'model_state_p2': ('P2', 'native SBML value', 'P2. Maps to SBML symbol `P2`.'), 'i_ia': ('IIa', 'native SBML value', 'IIa. Maps to SBML symbol `IIa`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000363.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
