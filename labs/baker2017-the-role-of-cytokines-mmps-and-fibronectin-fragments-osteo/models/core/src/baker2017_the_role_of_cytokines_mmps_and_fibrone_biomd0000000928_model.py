# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Baker2017 - The role of cytokines, MMPs and fibronectin fragments osteoarthritis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Baker2017TheRoleOfCytokinesMmpsAndFibroneBiomd0000000928Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Baker2017 - The role of cytokines, MMPs and fibronectin fragments osteoarthritis."""

    _SBML_ID = 'BIOMD0000000928'
    _TITLE = 'Baker2017 - The role of cytokines, MMPs and fibronectin fragments osteoarthritis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['solution0', 'solution1', 'solution2', 'solution3']
    _SPECIES_LABELS = {'solution0': 'p-Cytokines', 'solution1': 'a-Cytokines', 'solution2': 'MMP', 'solution3': 'Fragments'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_a_cytokines': ('solution1', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `solution1`.'), 'initial_fragments': ('solution3', 0.75, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `solution3`.'), 'initial_model_state_mmp': ('solution2', 0.55, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `solution2`.'), 'initial_p_cytokines': ('solution0', 0.18, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `solution0`.')}
    _HEADLINE_OUTPUTS = {'a_cytokines': ('solution1', 'native SBML value', 'a-Cytokines. Maps to SBML symbol `solution1`.'), 'fragments': ('solution3', 'native SBML value', 'Fragments. Maps to SBML symbol `solution3`.'), 'mmp': ('solution2', 'native SBML value', 'MMP. Maps to SBML symbol `solution2`.'), 'p_cytokines': ('solution0', 'native SBML value', 'p-Cytokines. Maps to SBML symbol `solution0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000928.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
