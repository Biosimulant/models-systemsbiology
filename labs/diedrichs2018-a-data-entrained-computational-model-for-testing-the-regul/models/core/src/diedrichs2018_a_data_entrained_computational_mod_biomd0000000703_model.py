# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Diedrichs2018 - A data-entrained computational model for testing the regulatory logic of the vertebrate unfolded protein response."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Diedrichs2018ADataEntrainedComputationalModBiomd0000000703Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Diedrichs2018 - A data-entrained computational model for testing the regulatory logic of the vertebrate unfolded protein response."""

    _SBML_ID = 'BIOMD0000000703'
    _TITLE = 'Diedrichs2018 - A data-entrained computational model for testing the regulatory logic of the vertebrate unfolded protein response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'A6', 'b', 'Btot', 'A4', 'c', 'C', 'g', 'G', 'Ep', 'x']
    _SPECIES_LABELS = {'U': 'U', 'A6': 'A6', 'b': 'b', 'Btot': 'Btot', 'A4': 'A4', 'c': 'c', 'C': 'C', 'g': 'g', 'G': 'G', 'Ep': 'Ep', 'x': 'x'}
    _PARAMETER_INPUTS = {'stress': ('Stress', 2.0, 'unit_1', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Stress`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_x': ('x', 'native SBML value', 'x. Maps to SBML symbol `x`.'), 'model_state_g': ('g', 'native SBML value', 'g. Maps to SBML symbol `g`.'), 'model_state_c': ('c', 'native SBML value', 'c. Maps to SBML symbol `c`.'), 'model_state_b': ('b', 'native SBML value', 'b. Maps to SBML symbol `b`.'), 'model_state_ep': ('Ep', 'native SBML value', 'Ep. Maps to SBML symbol `Ep`.'), 'btot': ('Btot', 'native SBML value', 'Btot. Maps to SBML symbol `Btot`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000703.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
