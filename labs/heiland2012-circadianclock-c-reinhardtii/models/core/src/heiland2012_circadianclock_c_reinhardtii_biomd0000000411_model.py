# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Heiland2012_CircadianClock_C.reinhardtii."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heiland2012CircadianclockCReinhardtiiBiomd0000000411Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Heiland2012_CircadianClock_C.reinhardtii."""

    _SBML_ID = 'BIOMD0000000411'
    _TITLE = 'Heiland2012_CircadianClock_C.reinhardtii'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s2', 's9', 's10', 's11', 's13', 'species_1', 'species_2', 'species_3', 'species_4']
    _SPECIES_LABELS = {'s2': 'C3_Gene', 's9': 'C3_mRNA', 's10': 'C_3', 's11': 'C_3_P', 's13': 'C_3_pre', 'species_1': 'C1', 'species_2': 'C1_mRNA', 'species_3': 'C1_phos', 'species_4': 'c1c3complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c3_mrna': ('s9', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s9`.'), 'initial_c3_gene': ('s2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s2`.'), 'initial_c1_mrna': ('species_2', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`.'), 'initial_c1c3complex': ('species_4', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_4`.'), 'initial_c_3_pre': ('s13', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s13`.'), 'initial_c_3_p': ('s11', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s11`.')}
    _HEADLINE_OUTPUTS = {'c3_mrna': ('s9', 'native SBML value', 'C3_mRNA. Maps to SBML symbol `s9`.'), 'c3_gene': ('s2', 'native SBML value', 'C3_Gene. Maps to SBML symbol `s2`.'), 'c1_mrna': ('species_2', 'native SBML value', 'C1_mRNA. Maps to SBML symbol `species_2`.'), 'c1c3complex': ('species_4', 'native SBML value', 'c1c3complex. Maps to SBML symbol `species_4`.'), 'c_3_pre': ('s13', 'native SBML value', 'C_3_pre. Maps to SBML symbol `s13`.'), 'c_3_p': ('s11', 'native SBML value', 'C_3_P. Maps to SBML symbol `s11`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000411.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
