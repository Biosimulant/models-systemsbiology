# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Musante2017 - Switching behaviour of PP2A inhibition by ARPP-16 - mutual inhibitions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Musante2017SwitchingBehaviourOfPp2aInhibitiBiomd0000000643Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Musante2017 - Switching behaviour of PP2A inhibition by ARPP-16 - mutual inhibitions."""

    _SBML_ID = 'BIOMD0000000643'
    _TITLE = 'Musante2017 - Switching behaviour of PP2A inhibition by ARPP-16 - mutual inhibitions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A46', 'A88', 'M', 'PKA', 'BB', 'Complex']
    _SPECIES_LABELS = {'A46': 'A46', 'A88': 'A88', 'M': 'M', 'PKA': 'PKA', 'BB': 'BB', 'Complex': 'Complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_bb': ('BB', 11.8161515151515, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BB`.'), 'initial_model_state_a46': ('A46', 9.80000000000001, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A46`.'), 'initial_complex': ('Complex', 1.9958693267679, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Complex`.'), 'initial_model_state_a88': ('A88', 0.199999999999994, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A88`.'), 'initial_model_state_pka': ('PKA', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PKA`.'), 'initial_model_state_m': ('M', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_bb': ('BB', 'substance', 'BB. Maps to SBML symbol `BB`.'), 'a46': ('A46', 'substance', 'A46. Maps to SBML symbol `A46`.'), 'complex': ('Complex', 'substance', 'Complex. Maps to SBML symbol `Complex`.'), 'a88': ('A88', 'substance', 'A88. Maps to SBML symbol `A88`.'), 'pka': ('PKA', 'substance', 'PKA. Maps to SBML symbol `PKA`.'), 'model_state_m': ('M', 'substance', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000643.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
