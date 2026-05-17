# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup2003_CircClock_LD."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup2003CircclockLdBiomd0000000078Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup2003_CircClock_LD."""

    _SBML_ID = 'BIOMD0000000078'
    _TITLE = 'Leloup2003_CircClock_LD'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15']
    _SPECIES_LABELS = {'species_0': 'Mb', 'species_1': 'Bc', 'species_2': 'Bcp', 'species_3': 'Bn', 'species_4': 'Cc', 'species_5': 'Mc', 'species_6': 'Ccp', 'species_7': 'Mp', 'species_8': 'Pc', 'species_9': 'Pcp', 'species_10': 'PCc', 'species_11': 'PCcp', 'species_12': 'PCn', 'species_13': 'Bnp', 'species_14': 'PCnp', 'species_15': 'In'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_mb': ('species_0', 9.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0`.'), 'initial_model_state_mp': ('species_7', 2.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_model_state_bc': ('species_1', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_model_state_bn': ('species_3', 1.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`.'), 'initial_model_state_mc': ('species_5', 1.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_5`.'), 'initial_p_cn': ('species_12', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`.')}
    _HEADLINE_OUTPUTS = {'model_state_mb': ('species_0', 'native SBML value', 'Mb. Maps to SBML symbol `species_0`.'), 'model_state_mp': ('species_7', 'native SBML value', 'Mp. Maps to SBML symbol `species_7`.'), 'model_state_bc': ('species_1', 'native SBML value', 'Bc. Maps to SBML symbol `species_1`.'), 'model_state_bn': ('species_3', 'native SBML value', 'Bn. Maps to SBML symbol `species_3`.'), 'model_state_mc': ('species_5', 'native SBML value', 'Mc. Maps to SBML symbol `species_5`.'), 'p_cn': ('species_12', 'native SBML value', 'PCn. Maps to SBML symbol `species_12`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000078.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
