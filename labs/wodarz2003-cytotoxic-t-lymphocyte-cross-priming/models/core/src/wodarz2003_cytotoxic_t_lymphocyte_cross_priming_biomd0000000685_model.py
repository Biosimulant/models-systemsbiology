# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wodarz2003 - Cytotoxic T lymphocyte cross-priming."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2003CytotoxicTLymphocyteCrossPrimingBiomd0000000685Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wodarz2003 - Cytotoxic T lymphocyte cross-priming."""

    _SBML_ID = 'BIOMD0000000685'
    _TITLE = 'Wodarz2003 - Cytotoxic T lymphocyte cross-priming'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['T', 'A', 'A_star', 'C']
    _SPECIES_LABELS = {'T': 'T', 'A': 'A', 'A_star': 'A Star', 'C': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_a_star': ('A_star', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A_star`.'), 'initial_model_state_t': ('T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_c': ('C', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`.'), 'initial_model_state_a': ('A', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.')}
    _HEADLINE_OUTPUTS = {'a_star': ('A_star', 'native SBML value', 'A Star. Maps to SBML symbol `A_star`.'), 'model_state_t': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'model_state_c': ('C', 'native SBML value', 'C. Maps to SBML symbol `C`.'), 'model_state_a': ('A', 'native SBML value', 'A. Maps to SBML symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000685.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
