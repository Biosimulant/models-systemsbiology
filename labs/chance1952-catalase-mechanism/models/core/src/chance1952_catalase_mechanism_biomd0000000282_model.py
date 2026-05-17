# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Chance1952_Catalase_Mechanism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chance1952CatalaseMechanismBiomd0000000282Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Chance1952_Catalase_Mechanism."""

    _SBML_ID = 'BIOMD0000000282'
    _TITLE = 'Chance1952_Catalase_Mechanism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['e', 'x', 'p', 'p1', 'a', 'p2']
    _SPECIES_LABELS = {'e': 'enzyme E (catalase)', 'x': 'substrate S (hydrogen peroxide)', 'p': 'enzyme-substrate complex ES (catalase - hydrogen peroxide)', 'p1': 'product 1', 'a': 'donor AH2', 'p2': 'product 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_product_2': ('p2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p2`.'), 'initial_product_1': ('p1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p1`.'), 'initial_substrate_s_hydrogen_peroxide': ('x', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.'), 'initial_enzyme_e_catalase': ('e', 1.36, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `e`.'), 'initial_enzyme_substrate_complex_es_catalase_hydrogen_peroxide': ('p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p`.'), 'initial_donor_ah2': ('a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `a`.')}
    _HEADLINE_OUTPUTS = {'product_2': ('p2', 'native SBML value', 'product 2. Maps to SBML symbol `p2`.'), 'product_1': ('p1', 'native SBML value', 'product 1. Maps to SBML symbol `p1`.'), 'substrate_s_hydrogen_peroxide': ('x', 'native SBML value', 'substrate S (hydrogen peroxide). Maps to SBML symbol `x`.'), 'enzyme_e_catalase': ('e', 'native SBML value', 'enzyme E (catalase). Maps to SBML symbol `e`.'), 'enzyme_substrate_complex_es_catalase_hydrogen_peroxide': ('p', 'native SBML value', 'enzyme-substrate complex ES (catalase - hydrogen peroxide). Maps to SBML symbol `p`.'), 'donor_ah2': ('a', 'native SBML value', 'donor AH2. Maps to SBML symbol `a`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000282.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
