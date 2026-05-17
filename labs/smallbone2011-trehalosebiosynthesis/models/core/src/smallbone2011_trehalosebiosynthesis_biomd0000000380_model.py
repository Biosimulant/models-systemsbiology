# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Smallbone2011_TrehaloseBiosynthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2011TrehalosebiosynthesisBiomd0000000380Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Smallbone2011_TrehaloseBiosynthesis."""

    _SBML_ID = 'BIOMD0000000380'
    _TITLE = 'Smallbone2011_TrehaloseBiosynthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['glc', 'g1p', 'g6p', 'trh', 't6p', 'udg', 'adp', 'atp', 'ppi', 'f6p', 'h', 'pho', 'udp', 'utp', 'h2o', 'glx']
    _SPECIES_LABELS = {'glc': 'glucose', 'g1p': 'glucose 1-phosphate', 'g6p': 'glucose 6-phosphate', 'trh': 'trehalose', 't6p': 'trehalose 6-phosphate', 'udg': 'UDP glucose', 'adp': 'ADP', 'atp': 'ATP', 'ppi': 'diphosphate', 'f6p': 'fructose 6-phosphate', 'h': 'H+', 'pho': 'phosphate', 'udp': 'UDP', 'utp': 'UTP', 'h2o': 'water', 'glx': 'glucose'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('glx', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glx`.'), 'initial_glucose_6_phosphate': ('g6p', 2.675, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `g6p`.'), 'initial_udp_glucose': ('udg', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `udg`.'), 'initial_glucose_1_phosphate': ('g1p', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `g1p`.'), 'initial_glucose_2': ('glc', 0.09675, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glc`.'), 'initial_model_state_atp': ('atp', 2.525, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`.')}
    _HEADLINE_OUTPUTS = {'glucose': ('glx', 'native SBML value', 'glucose. Maps to SBML symbol `glx`.'), 'glucose_6_phosphate': ('g6p', 'native SBML value', 'glucose 6-phosphate. Maps to SBML symbol `g6p`.'), 'udp_glucose': ('udg', 'native SBML value', 'UDP glucose. Maps to SBML symbol `udg`.'), 'glucose_1_phosphate': ('g1p', 'native SBML value', 'glucose 1-phosphate. Maps to SBML symbol `g1p`.'), 'glucose_2': ('glc', 'native SBML value', 'glucose. Maps to SBML symbol `glc`.'), 'atp': ('atp', 'native SBML value', 'ATP. Maps to SBML symbol `atp`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000380.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
