# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Yi2003_GproteinCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yi2003GproteincycleBiomd0000000072Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Yi2003_GproteinCycle."""

    _SBML_ID = 'BIOMD0000000072'
    _TITLE = 'Yi2003_GproteinCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'R', 'G', 'Gbg', 'Gd', 'Ga', 'RL']
    _SPECIES_LABELS = {'L': 'Ligand', 'R': 'Receptor', 'G': 'Inactive heterotrimeric G-protein', 'Gbg': 'Free levels of G-beta-gamma', 'Gd': 'G-alpha-GDP', 'Ga': 'G-alpha-GTP', 'RL': 'Receptor-Ligand'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_g_alpha_gdp': ('Gd', 3000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gd`.'), 'initial_free_levels_of_g_beta_gamma': ('Gbg', 3000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gbg`.'), 'initial_receptor_ligand': ('RL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RL`.'), 'initial_g_alpha_gtp': ('Ga', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ga`.'), 'initial_ligand': ('L', 6.02e+17, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.'), 'initial_receptor': ('R', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.')}
    _HEADLINE_OUTPUTS = {'g_alpha_gdp': ('Gd', 'native SBML value', 'G-alpha-GDP. Maps to SBML symbol `Gd`.'), 'free_levels_of_g_beta_gamma': ('Gbg', 'native SBML value', 'Free levels of G-beta-gamma. Maps to SBML symbol `Gbg`.'), 'receptor_ligand': ('RL', 'native SBML value', 'Receptor-Ligand. Maps to SBML symbol `RL`.'), 'g_alpha_gtp': ('Ga', 'native SBML value', 'G-alpha-GTP. Maps to SBML symbol `Ga`.'), 'ligand': ('L', 'native SBML value', 'Ligand. Maps to SBML symbol `L`.'), 'receptor': ('R', 'native SBML value', 'Receptor. Maps to SBML symbol `R`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000072.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
