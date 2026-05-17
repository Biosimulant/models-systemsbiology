# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Hatakeyama2003_MAPK."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hatakeyama2003MapkBiomd0000000146Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Hatakeyama2003_MAPK."""

    _SBML_ID = 'BIOMD0000000146'
    _TITLE = 'Hatakeyama2003_MAPK'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Akt', 'AktPIP3', 'AktPIP', 'AktPIPP', 'ERK', 'ERKP', 'ERKPP', 'GS', 'HRG', 'MEK', 'MEKP', 'MEKPP', 'PI3K', 'PI3Kstar', 'PIP3', 'R', 'RP', 'RHRG', 'RHRG2', 'RPI3K', 'RPI3Kstar', 'RShGS', 'RShP', 'RShc', 'Raf', 'Rafstar', 'RasGDP', 'RasGTP', 'ShGS', 'ShP', 'Shc', 'P_I', 'internalization', 'E', 'MKP3', 'PP2A']
    _SPECIES_LABELS = {'Akt': 'Akt', 'AktPIP3': 'AktPIP3', 'AktPIP': 'AktPIP', 'AktPIPP': 'AktPIPP', 'ERK': 'ERK', 'ERKP': 'ERKP', 'ERKPP': 'ERKPP', 'GS': 'GS', 'HRG': 'HRG', 'MEK': 'MEK', 'MEKP': 'MEKP', 'MEKPP': 'MEKPP', 'PI3K': 'PI3K', 'PI3Kstar': 'PI3Kstar', 'PIP3': 'PIP3', 'R': 'R', 'RP': 'RP', 'RHRG': 'RHRG', 'RHRG2': 'RHRG2', 'RPI3K': 'RPI3K', 'RPI3Kstar': 'RPI3Kstar', 'RShGS': 'RShGS', 'RShP': 'RShP', 'RShc': 'RShc', 'Raf': 'RAF', 'Rafstar': 'Rafstar', 'RasGDP': 'RasGDP', 'RasGTP': 'RasGTP', 'ShGS': 'ShGS', 'ShP': 'ShP', 'Shc': 'Shc', 'P_I': 'P I', 'internalization': 'Internalization', 'E': 'E', 'MKP3': 'MKP3', 'PP2A': 'PP2A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_internalization': ('internalization', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `internalization`.'), 'initial_model_state_shc': ('Shc', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Shc`.'), 'initial_model_state_erk': ('ERK', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ERK`.'), 'initial_model_state_p_i': ('P_I', 800.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_I`.'), 'initial_model_state_hrg': ('HRG', 330.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HRG`.'), 'initial_ras_gdp': ('RasGDP', 120.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RasGDP`.')}
    _HEADLINE_OUTPUTS = {'internalization': ('internalization', 'native SBML value', 'Internalization. Maps to SBML symbol `internalization`.'), 'shc': ('Shc', 'native SBML value', 'Shc. Maps to SBML symbol `Shc`.'), 'erk': ('ERK', 'native SBML value', 'ERK. Maps to SBML symbol `ERK`.'), 'p_i': ('P_I', 'native SBML value', 'P I. Maps to SBML symbol `P_I`.'), 'hrg': ('HRG', 'native SBML value', 'HRG. Maps to SBML symbol `HRG`.'), 'ras_gdp': ('RasGDP', 'native SBML value', 'RasGDP. Maps to SBML symbol `RasGDP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000146.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
