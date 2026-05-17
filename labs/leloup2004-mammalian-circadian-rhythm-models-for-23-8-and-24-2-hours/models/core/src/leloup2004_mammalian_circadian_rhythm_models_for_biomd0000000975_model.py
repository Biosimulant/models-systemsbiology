# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup2004 - Mammalian Circadian Rhythm models for 23.8 and 24.2 hours timeperiod."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup2004MammalianCircadianRhythmModelsForBiomd0000000975Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup2004 - Mammalian Circadian Rhythm models for 23.8 and 24.2 hours timeperiod."""

    _SBML_ID = 'BIOMD0000000975'
    _TITLE = 'Leloup2004 - Mammalian Circadian Rhythm models for 23.8 and 24.2 hours timeperiod'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['MP_0', 'MC_0', 'MB_0', 'PC_0', 'CC_0', 'PCP_0', 'CCP_0', 'PCC_0', 'PCN_0', 'PCNP_0', 'PCCP_0', 'BC_0', 'BCP_0', 'BN_0', 'BNP_0', 'IN_0', 'BTot', 'CTot', 'PTot']
    _SPECIES_LABELS = {'MP_0': 'MP', 'MC_0': 'MC', 'MB_0': 'MB', 'PC_0': 'PC', 'CC_0': 'CC', 'PCP_0': 'PCP', 'CCP_0': 'CCP', 'PCC_0': 'PCC', 'PCN_0': 'PCN', 'PCNP_0': 'PCNP', 'PCCP_0': 'PCCP', 'BC_0': 'BC', 'BCP_0': 'BCP', 'BN_0': 'BN', 'BNP_0': 'BNP', 'IN_0': 'IN', 'BTot': 'BTot', 'CTot': 'CTot', 'PTot': 'PTot'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_mb': ('MB_0', 8.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MB_0`.'), 'initial_model_state_pcp': ('PCP_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCP_0`.'), 'initial_pcnp': ('PCNP_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCNP_0`.'), 'initial_model_state_pcn': ('PCN_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCN_0`.'), 'initial_pccp': ('PCCP_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCCP_0`.'), 'initial_model_state_pcc': ('PCC_0', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCC_0`.')}
    _HEADLINE_OUTPUTS = {'model_state_mb': ('MB_0', 'native SBML value', 'MB. Maps to SBML symbol `MB_0`.'), 'pcp': ('PCP_0', 'native SBML value', 'PCP. Maps to SBML symbol `PCP_0`.'), 'pcnp': ('PCNP_0', 'native SBML value', 'PCNP. Maps to SBML symbol `PCNP_0`.'), 'pcn': ('PCN_0', 'native SBML value', 'PCN. Maps to SBML symbol `PCN_0`.'), 'pccp': ('PCCP_0', 'native SBML value', 'PCCP. Maps to SBML symbol `PCCP_0`.'), 'pcc': ('PCC_0', 'native SBML value', 'PCC. Maps to SBML symbol `PCC_0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000975.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
