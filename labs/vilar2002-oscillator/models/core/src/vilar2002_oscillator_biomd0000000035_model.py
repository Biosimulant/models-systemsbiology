# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Vilar2002_Oscillator."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vilar2002OscillatorBiomd0000000035Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Vilar2002_Oscillator."""

    _SBML_ID = 'BIOMD0000000035'
    _TITLE = 'Vilar2002_Oscillator'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EmptySet', 'A', 'C', 'DA', 'DAp', 'DR', 'DRp', 'MA', 'MR', 'R']
    _SPECIES_LABELS = {'EmptySet': 'EmptySet', 'A': 'A', 'C': 'C', 'DA': 'DA', 'DAp': 'DAp', 'DR': 'DR', 'DRp': 'DRp', 'MA': 'MA', 'MR': 'MR', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_dr': ('DR', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DR`.'), 'initial_model_state_da': ('DA', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DA`.'), 'initial_model_state_mr': ('MR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MR`.'), 'initial_model_state_ma': ('MA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MA`.'), 'initial_empty_set': ('EmptySet', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EmptySet`.'), 'initial_d_rp': ('DRp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DRp`.')}
    _HEADLINE_OUTPUTS = {'model_state_dr': ('DR', 'native SBML value', 'DR. Maps to SBML symbol `DR`.'), 'model_state_da': ('DA', 'native SBML value', 'DA. Maps to SBML symbol `DA`.'), 'model_state_mr': ('MR', 'native SBML value', 'MR. Maps to SBML symbol `MR`.'), 'model_state_ma': ('MA', 'native SBML value', 'MA. Maps to SBML symbol `MA`.'), 'empty_set': ('EmptySet', 'native SBML value', 'EmptySet. Maps to SBML symbol `EmptySet`.'), 'd_rp': ('DRp', 'native SBML value', 'DRp. Maps to SBML symbol `DRp`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000035.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
