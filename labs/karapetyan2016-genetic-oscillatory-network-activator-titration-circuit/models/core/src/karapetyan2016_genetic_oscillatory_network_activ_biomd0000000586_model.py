# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Karapetyan2016 - Genetic oscillatory network - Activator Titration Circuit (ATC)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Karapetyan2016GeneticOscillatoryNetworkActivBiomd0000000586Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Karapetyan2016 - Genetic oscillatory network - Activator Titration Circuit (ATC)."""

    _SBML_ID = 'BIOMD0000000586'
    _TITLE = 'Karapetyan2016 - Genetic oscillatory network - Activator Titration Circuit (ATC)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G0', 'G1', 'rA', 'I', 'rI', 'A', 'AI', 'A2', 'G2', 'G3']
    _SPECIES_LABELS = {'G0': 'G0', 'G1': 'G1', 'rA': 'rA', 'I': 'I', 'rI': 'rI', 'A': 'A', 'AI': 'AI', 'A2': 'A2', 'G2': 'G2', 'G3': 'G3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_r_i': ('rI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rI`.'), 'initial_model_state_r_a': ('rA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rA`.'), 'initial_model_state_g0': ('G0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G0`.'), 'initial_model_state_g3': ('G3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3`.'), 'initial_model_state_g2': ('G2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G2`.'), 'initial_model_state_g1': ('G1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G1`.')}
    _HEADLINE_OUTPUTS = {'r_i': ('rI', 'native SBML value', 'rI. Maps to SBML symbol `rI`.'), 'r_a': ('rA', 'native SBML value', 'rA. Maps to SBML symbol `rA`.'), 'model_state_g0': ('G0', 'native SBML value', 'G0. Maps to SBML symbol `G0`.'), 'model_state_g3': ('G3', 'native SBML value', 'G3. Maps to SBML symbol `G3`.'), 'model_state_g2': ('G2', 'native SBML value', 'G2. Maps to SBML symbol `G2`.'), 'model_state_g1': ('G1', 'native SBML value', 'G1. Maps to SBML symbol `G1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000586.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
