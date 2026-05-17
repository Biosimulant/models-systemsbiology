# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup2003_CircClock_DD_REV-ERBalpha."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup2003CircclockDdRevErbalphaBiomd0000000074Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup2003_CircClock_DD_REV-ERBalpha."""

    _SBML_ID = 'BIOMD0000000074'
    _TITLE = 'Leloup2003_CircClock_DD_REV-ERBalpha'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18']
    _SPECIES_LABELS = {'species_0': 'Mb', 'species_1': 'Bc', 'species_2': 'Bcp', 'species_3': 'Bn', 'species_4': 'Cc', 'species_5': 'Mc', 'species_6': 'Ccp', 'species_7': 'Mp', 'species_8': 'Pc', 'species_9': 'Pcp', 'species_10': 'PCc', 'species_11': 'PCcp', 'species_12': 'PCn', 'species_13': 'Bnp', 'species_14': 'PCnp', 'species_15': 'In', 'species_16': 'Mr', 'species_17': 'Rc', 'species_18': 'Rn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_rn': ('species_18', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_18`.'), 'initial_model_state_rc': ('species_17', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_17`.'), 'initial_model_state_pcp': ('species_9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_9`.'), 'initial_model_state_pc': ('species_8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_p_cnp': ('species_14', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`.'), 'initial_p_cn': ('species_12', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`.')}
    _HEADLINE_OUTPUTS = {'model_state_rn': ('species_18', 'native SBML value', 'Rn. Maps to SBML symbol `species_18`.'), 'model_state_rc': ('species_17', 'native SBML value', 'Rc. Maps to SBML symbol `species_17`.'), 'pcp': ('species_9', 'native SBML value', 'Pcp. Maps to SBML symbol `species_9`.'), 'model_state_pc': ('species_8', 'native SBML value', 'Pc. Maps to SBML symbol `species_8`.'), 'p_cnp': ('species_14', 'native SBML value', 'PCnp. Maps to SBML symbol `species_14`.'), 'p_cn': ('species_12', 'native SBML value', 'PCn. Maps to SBML symbol `species_12`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000074.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
