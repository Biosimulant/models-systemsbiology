# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mayya2005_STATmodule."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mayya2005StatmoduleBiomd0000000167Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mayya2005_STATmodule."""

    _SBML_ID = 'BIOMD0000000167'
    _TITLE = 'Mayya2005_STATmodule'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['stat_sol', 'Pstat_sol', 'statKinase_sol', 'PstatDimer_sol', 'PstatDimer_nuc', 'stat_nuc', 'Pstat_nuc', 'statPhosphatase_nuc', 'species_test']
    _SPECIES_LABELS = {'stat_sol': 'stat_sol', 'Pstat_sol': 'Pstat_sol', 'statKinase_sol': 'statKinase_sol', 'PstatDimer_sol': 'PstatDimer_sol', 'PstatDimer_nuc': 'PstatDimer_nuc', 'stat_nuc': 'stat_nuc', 'Pstat_nuc': 'Pstat_nuc', 'statPhosphatase_nuc': 'statPhosphatase_nuc', 'species_test': 'species_test'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stat_phosphatase_nuc': ('statPhosphatase_nuc', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `statPhosphatase_nuc`.'), 'initial_stat_sol': ('stat_sol', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `stat_sol`.'), 'initial_stat_nuc': ('stat_nuc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `stat_nuc`.'), 'initial_stat_kinase_sol': ('statKinase_sol', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `statKinase_sol`.'), 'initial_species_test': ('species_test', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_test`.'), 'initial_pstat_sol': ('Pstat_sol', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pstat_sol`.')}
    _HEADLINE_OUTPUTS = {'stat_phosphatase_nuc': ('statPhosphatase_nuc', 'native SBML value', 'statPhosphatase_nuc. Maps to SBML symbol `statPhosphatase_nuc`.'), 'stat_sol': ('stat_sol', 'native SBML value', 'stat_sol. Maps to SBML symbol `stat_sol`.'), 'stat_nuc': ('stat_nuc', 'native SBML value', 'stat_nuc. Maps to SBML symbol `stat_nuc`.'), 'stat_kinase_sol': ('statKinase_sol', 'native SBML value', 'statKinase_sol. Maps to SBML symbol `statKinase_sol`.'), 'species_test': ('species_test', 'native SBML value', 'species_test. Maps to SBML symbol `species_test`.'), 'pstat_sol': ('Pstat_sol', 'native SBML value', 'Pstat_sol. Maps to SBML symbol `Pstat_sol`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000167.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
