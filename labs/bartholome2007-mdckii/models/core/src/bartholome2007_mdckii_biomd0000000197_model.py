# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bartholome2007_MDCKII."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bartholome2007MdckiiBiomd0000000197Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bartholome2007_MDCKII."""

    _SBML_ID = 'BIOMD0000000197'
    _TITLE = 'Bartholome2007_MDCKII'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x3', 'x4', 'x5', 'BSP_tot', 'BSP_cell']
    _SPECIES_LABELS = {'x1': 'free basolateral BSP', 'x2': 'basolateral bound BSP', 'x3': 'free intracellular BSP', 'x4': 'bound intracellular BSP', 'x5': 'apical BSP', 'BSP_tot': 'total BSP', 'BSP_cell': 'intracellular BSP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_bsp': ('BSP_cell', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BSP_cell`.'), 'initial_free_intracellular_bsp': ('x3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x3`.'), 'initial_bound_intracellular_bsp': ('x4', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x4`.'), 'initial_apical_bsp': ('x5', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x5`.'), 'initial_free_basolateral_bsp': ('x1', 88.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x1`.'), 'initial_total_bsp': ('BSP_tot', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BSP_tot`.')}
    _HEADLINE_OUTPUTS = {'intracellular_bsp': ('BSP_cell', 'native SBML value', 'intracellular BSP. Maps to SBML symbol `BSP_cell`.'), 'free_intracellular_bsp': ('x3', 'native SBML value', 'free intracellular BSP. Maps to SBML symbol `x3`.'), 'bound_intracellular_bsp': ('x4', 'native SBML value', 'bound intracellular BSP. Maps to SBML symbol `x4`.'), 'apical_bsp': ('x5', 'native SBML value', 'apical BSP. Maps to SBML symbol `x5`.'), 'free_basolateral_bsp': ('x1', 'native SBML value', 'free basolateral BSP. Maps to SBML symbol `x1`.'), 'total_bsp': ('BSP_tot', 'native SBML value', 'total BSP. Maps to SBML symbol `BSP_tot`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000197.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
