# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Pandey2018-reversible transition between quiescence and proliferation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pandey2018ReversibleTransitionBetweenQuiesceBiomd0000000954Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Pandey2018-reversible transition between quiescence and proliferation."""

    _SBML_ID = 'BIOMD0000000954'
    _TITLE = 'Pandey2018-reversible transition between quiescence and proliferation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Myc', 'CycDT', 'CycET', 'CycAT', 'E2FT', 'Comp1', 'Comp2', 'Rbp', 'CkiT', 'CycECki', 'CycDCki', 'CycACki', 'Cdh1dp', 'Emi1T', 'EmiC', 'Cdh1', 'UbI', 'E2F', 'Rb', 'Rbpp', 'CycE', 'CycD', 'CycA', 'Cdh1p', 'Cdh1T']
    _SPECIES_LABELS = {'Myc': 'Myc', 'CycDT': 'CycDT', 'CycET': 'CycET', 'CycAT': 'CycAT', 'E2FT': 'E2FT', 'Comp1': 'Comp1', 'Comp2': 'Comp2', 'Rbp': 'Rbp', 'CkiT': 'CkiT', 'CycECki': 'CycECki', 'CycDCki': 'CycDCki', 'CycACki': 'CycACki', 'Cdh1dp': 'Cdh1dp', 'Emi1T': 'Emi1T', 'EmiC': 'EmiC', 'Cdh1': 'Cdh1', 'UbI': 'UbI', 'E2F': 'E2F', 'Rb': 'Rb', 'Rbpp': 'Rbpp', 'CycE': 'CycE', 'CycD': 'CycD', 'CycA': 'CycA', 'Cdh1p': 'Cdh1p', 'Cdh1T': 'Cdh1T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cdh1dp': ('Cdh1dp', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdh1dp`.'), 'initial_cdh1_t': ('Cdh1T', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdh1T`.'), 'initial_cdh1': ('Cdh1', 0.998, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cdh1`.'), 'initial_model_state_rb': ('Rb', 0.894, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rb`.'), 'initial_cki_t': ('CkiT', 0.2, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CkiT`.'), 'initial_cyc_et': ('CycET', 0.119, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CycET`.')}
    _HEADLINE_OUTPUTS = {'cdh1dp': ('Cdh1dp', 'substance', 'Cdh1dp. Maps to SBML symbol `Cdh1dp`.'), 'cdh1_t': ('Cdh1T', 'substance', 'Cdh1T. Maps to SBML symbol `Cdh1T`.'), 'cdh1': ('Cdh1', 'substance', 'Cdh1. Maps to SBML symbol `Cdh1`.'), 'model_state_rb': ('Rb', 'substance', 'Rb. Maps to SBML symbol `Rb`.'), 'cki_t': ('CkiT', 'substance', 'CkiT. Maps to SBML symbol `CkiT`.'), 'cyc_et': ('CycET', 'substance', 'CycET. Maps to SBML symbol `CycET`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000954.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
