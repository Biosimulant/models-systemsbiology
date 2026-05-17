# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup2003_CircClock_LD_REV-ERBalpha."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup2003CircclockLdRevErbalphaBiomd0000000083Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup2003_CircClock_LD_REV-ERBalpha."""

    _SBML_ID = 'BIOMD0000000083'
    _TITLE = 'Leloup2003_CircClock_LD_REV-ERBalpha'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mb', 'Bc', 'Bcp', 'Bn', 'Cc', 'Mc', 'Ccp', 'Mp', 'Pc', 'Pcp', 'PCc', 'PCcp', 'PCn', 'Bnp', 'PCnp', 'In', 'Mr', 'Rc', 'Rn']
    _SPECIES_LABELS = {'Mb': 'Mb', 'Bc': 'Bc', 'Bcp': 'Bcp', 'Bn': 'Bn', 'Cc': 'Cc', 'Mc': 'Mc', 'Ccp': 'Ccp', 'Mp': 'Mp', 'Pc': 'Pc', 'Pcp': 'Pcp', 'PCc': 'PCc', 'PCcp': 'PCcp', 'PCn': 'PCn', 'Bnp': 'Bnp', 'PCnp': 'PCnp', 'In': 'In', 'Mr': 'Mr', 'Rc': 'Rc', 'Rn': 'Rn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_rn': ('Rn', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rn`.'), 'initial_model_state_rc': ('Rc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rc`.'), 'initial_model_state_pcp': ('Pcp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pcp`.'), 'initial_model_state_pc': ('Pc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pc`.'), 'initial_p_cnp': ('PCnp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCnp`.'), 'initial_p_cn': ('PCn', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCn`.')}
    _HEADLINE_OUTPUTS = {'model_state_rn': ('Rn', 'native SBML value', 'Rn. Maps to SBML symbol `Rn`.'), 'model_state_rc': ('Rc', 'native SBML value', 'Rc. Maps to SBML symbol `Rc`.'), 'pcp': ('Pcp', 'native SBML value', 'Pcp. Maps to SBML symbol `Pcp`.'), 'model_state_pc': ('Pc', 'native SBML value', 'Pc. Maps to SBML symbol `Pc`.'), 'p_cnp': ('PCnp', 'native SBML value', 'PCnp. Maps to SBML symbol `PCnp`.'), 'p_cn': ('PCn', 'native SBML value', 'PCn. Maps to SBML symbol `PCn`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000083.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
