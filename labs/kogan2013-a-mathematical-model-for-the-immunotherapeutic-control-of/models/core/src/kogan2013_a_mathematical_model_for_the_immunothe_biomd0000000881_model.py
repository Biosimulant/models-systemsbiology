# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kogan2013 - A mathematical model for the immunotherapeutic control of the TH1 TH2 imbalance in melanoma."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kogan2013AMathematicalModelForTheImmunotheBiomd0000000881Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kogan2013 - A mathematical model for the immunotherapeutic control of the TH1 TH2 imbalance in melanoma."""

    _SBML_ID = 'BIOMD0000000881'
    _TITLE = 'Kogan2013 - A mathematical model for the immunotherapeutic control of the TH1 TH2 imbalance in melanoma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T_1', 'T_2', 'G', 'I']
    _SPECIES_LABELS = {'T_1': 'T_1', 'T_2': 'T_2', 'G': 'G', 'I': 'I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_t_2': ('T_2', 1000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_2`.'), 'initial_model_state_t_1': ('T_1', 500000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T_1`.'), 'initial_model_state_i': ('I', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.'), 'initial_model_state_g': ('G', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G`.')}
    _HEADLINE_OUTPUTS = {'t_2': ('T_2', 'native SBML value', 'T_2. Maps to SBML symbol `T_2`.'), 't_1': ('T_1', 'native SBML value', 'T_1. Maps to SBML symbol `T_1`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'model_state_g': ('G', 'native SBML value', 'G. Maps to SBML symbol `G`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000881.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
