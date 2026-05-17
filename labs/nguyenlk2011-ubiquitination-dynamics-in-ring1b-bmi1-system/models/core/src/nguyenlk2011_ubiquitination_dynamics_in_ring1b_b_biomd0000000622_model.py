# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for NguyenLK2011 - Ubiquitination dynamics in Ring1B/Bmi1 system."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nguyenlk2011UbiquitinationDynamicsInRing1bBBiomd0000000622Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for NguyenLK2011 - Ubiquitination dynamics in Ring1B/Bmi1 system."""

    _SBML_ID = 'BIOMD0000000622'
    _TITLE = 'NguyenLK2011 - Ubiquitination dynamics in Ring1B/Bmi1 system'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Bmi1', 'Bmi1ubd', 'R1B', 'R1Bubd', 'USP7tot', 'Z', 'Zub', 'R1Buba', 'R1Bub', 'H2A', 'H2Auba']
    _SPECIES_LABELS = {'Bmi1': 'Bmi1', 'Bmi1ubd': 'Bmi1ubd', 'R1B': 'R1B', 'R1Bubd': 'R1Bubd', 'USP7tot': 'USP7tot', 'Z': 'Z', 'Zub': 'Zub', 'R1Buba': 'R1Buba', 'R1Bub': 'R1Bub', 'H2A': 'H2A', 'H2Auba': 'H2Auba'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_bmi1': ('Bmi1', 1.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bmi1`.'), 'initial_bmi1ubd': ('Bmi1ubd', 1.08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bmi1ubd`.'), 'initial_usp7tot': ('USP7tot', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `USP7tot`.'), 'initial_r1_buba': ('R1Buba', 0.44, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R1Buba`.'), 'initial_model_state_zub': ('Zub', 0.12, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Zub`.'), 'initial_r1_bubd': ('R1Bubd', 0.12, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R1Bubd`.')}
    _HEADLINE_OUTPUTS = {'bmi1': ('Bmi1', 'native SBML value', 'Bmi1. Maps to SBML symbol `Bmi1`.'), 'bmi1ubd': ('Bmi1ubd', 'native SBML value', 'Bmi1ubd. Maps to SBML symbol `Bmi1ubd`.'), 'usp7tot': ('USP7tot', 'native SBML value', 'USP7tot. Maps to SBML symbol `USP7tot`.'), 'r1_buba': ('R1Buba', 'native SBML value', 'R1Buba. Maps to SBML symbol `R1Buba`.'), 'zub': ('Zub', 'native SBML value', 'Zub. Maps to SBML symbol `Zub`.'), 'r1_bubd': ('R1Bubd', 'native SBML value', 'R1Bubd. Maps to SBML symbol `R1Bubd`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000622.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
