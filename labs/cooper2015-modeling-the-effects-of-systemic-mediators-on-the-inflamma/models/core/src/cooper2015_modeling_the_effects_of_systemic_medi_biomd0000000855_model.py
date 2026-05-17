# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cooper2015 - Modeling the effects of systemic mediators on the inflammatory phase of wound healing."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cooper2015ModelingTheEffectsOfSystemicMediBiomd0000000855Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cooper2015 - Modeling the effects of systemic mediators on the inflammatory phase of wound healing."""

    _SBML_ID = 'BIOMD0000000855'
    _TITLE = 'Cooper2015 - Modeling the effects of systemic mediators on the inflammatory phase of wound healing'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P', 'Pt', 'M', 'N']
    _SPECIES_LABELS = {'P': 'P', 'Pt': 'Pt', 'M': 'M', 'N': 'N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pt': ('Pt', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pt`.'), 'initial_model_state_p': ('P', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.'), 'initial_model_state_n': ('N', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N`.'), 'initial_model_state_m': ('M', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_pt': ('Pt', 'native SBML value', 'Pt. Maps to SBML symbol `Pt`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.'), 'model_state_n': ('N', 'native SBML value', 'N. Maps to SBML symbol `N`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000855.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
