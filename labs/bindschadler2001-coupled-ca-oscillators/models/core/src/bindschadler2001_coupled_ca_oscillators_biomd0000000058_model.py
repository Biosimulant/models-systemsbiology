# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bindschadler2001_coupled_Ca_oscillators."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bindschadler2001CoupledCaOscillatorsBiomd0000000058Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bindschadler2001_coupled_Ca_oscillators."""

    _SBML_ID = 'BIOMD0000000058'
    _TITLE = 'Bindschadler2001_coupled_Ca_oscillators'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['c1', 'h1', 'c2', 'h2']
    _SPECIES_LABELS = {'c1': 'Calcium ion Cell1', 'h1': 'Receptor fraction Cell1', 'c2': 'Calcium ion Cell2', 'h2': 'Receptor fraction Cell2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_receptor_fraction_cell1': ('h1', 0.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h1`.'), 'initial_calcium_ion_cell1': ('c1', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c1`.'), 'initial_receptor_fraction_cell2': ('h2', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `h2`.'), 'initial_calcium_ion_cell2': ('c2', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c2`.')}
    _HEADLINE_OUTPUTS = {'receptor_fraction_cell1': ('h1', 'native SBML value', 'Receptor fraction Cell1. Maps to SBML symbol `h1`.'), 'calcium_ion_cell1': ('c1', 'native SBML value', 'Calcium ion Cell1. Maps to SBML symbol `c1`.'), 'receptor_fraction_cell2': ('h2', 'native SBML value', 'Receptor fraction Cell2. Maps to SBML symbol `h2`.'), 'calcium_ion_cell2': ('c2', 'native SBML value', 'Calcium ion Cell2. Maps to SBML symbol `c2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000058.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
