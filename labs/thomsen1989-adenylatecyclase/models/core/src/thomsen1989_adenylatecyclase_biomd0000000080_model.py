# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Thomsen1989_AdenylateCyclase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Thomsen1989AdenylatecyclaseBiomd0000000080Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Thomsen1989_AdenylateCyclase."""

    _SBML_ID = 'BIOMD0000000080'
    _TITLE = 'Thomsen1989_AdenylateCyclase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['D', 'DR', 'DRG_GDP', 'G_GDP', 'DRG', 'GDP', 'DRG_GTP', 'GTP', 'G_GTP', 'R']
    _SPECIES_LABELS = {'D': 'D', 'DR': 'DR', 'DRG_GDP': 'DRG_GDP', 'G_GDP': 'G_GDP', 'DRG': 'DRG', 'GDP': 'GDP', 'DRG_GTP': 'DRG_GTP', 'GTP': 'GTP', 'G_GTP': 'G_GTP', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_g_gdp': ('G_GDP', 1e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_GDP`.'), 'initial_g_gtp': ('G_GTP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_GTP`.'), 'initial_drg_gtp': ('DRG_GTP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DRG_GTP`.'), 'initial_drg_gdp': ('DRG_GDP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DRG_GDP`.'), 'initial_model_state_gtp': ('GTP', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GTP`.'), 'initial_model_state_gdp': ('GDP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GDP`.')}
    _HEADLINE_OUTPUTS = {'g_gdp': ('G_GDP', 'native SBML value', 'G_GDP. Maps to SBML symbol `G_GDP`.'), 'g_gtp': ('G_GTP', 'native SBML value', 'G_GTP. Maps to SBML symbol `G_GTP`.'), 'drg_gtp': ('DRG_GTP', 'native SBML value', 'DRG_GTP. Maps to SBML symbol `DRG_GTP`.'), 'drg_gdp': ('DRG_GDP', 'native SBML value', 'DRG_GDP. Maps to SBML symbol `DRG_GDP`.'), 'gtp': ('GTP', 'native SBML value', 'GTP. Maps to SBML symbol `GTP`.'), 'gdp': ('GDP', 'native SBML value', 'GDP. Maps to SBML symbol `GDP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000080.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
