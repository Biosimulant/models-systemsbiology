# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Karapetyan2016 - Genetic oscillatory network - Repressor Titration Circuit (RTC)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Karapetyan2016GeneticOscillatoryNetworkRepreBiomd0000000587Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Karapetyan2016 - Genetic oscillatory network - Repressor Titration Circuit (RTC)."""

    _SBML_ID = 'BIOMD0000000587'
    _TITLE = 'Karapetyan2016 - Genetic oscillatory network - Repressor Titration Circuit (RTC)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G0', 'G1', 'rR', 'I', 'rI', 'R', 'RI', 'R2', 'G2', 'G3']
    _SPECIES_LABELS = {'G0': 'G0', 'G1': 'G1', 'rR': 'rR', 'I': 'I', 'rI': 'rI', 'R': 'R', 'RI': 'RI', 'R2': 'R2', 'G2': 'G2', 'G3': 'G3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_r_r': ('rR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rR`.'), 'initial_model_state_r_i': ('rI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rI`.'), 'initial_model_state_g0': ('G0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G0`.'), 'initial_model_state_ri': ('RI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI`.'), 'initial_model_state_r2': ('R2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R2`.'), 'initial_model_state_g3': ('G3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3`.')}
    _HEADLINE_OUTPUTS = {'r_r': ('rR', 'native SBML value', 'rR. Maps to SBML symbol `rR`.'), 'r_i': ('rI', 'native SBML value', 'rI. Maps to SBML symbol `rI`.'), 'model_state_g0': ('G0', 'native SBML value', 'G0. Maps to SBML symbol `G0`.'), 'model_state_ri': ('RI', 'native SBML value', 'RI. Maps to SBML symbol `RI`.'), 'model_state_r2': ('R2', 'native SBML value', 'R2. Maps to SBML symbol `R2`.'), 'model_state_g3': ('G3', 'native SBML value', 'G3. Maps to SBML symbol `G3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000587.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
