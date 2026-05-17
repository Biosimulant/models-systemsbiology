# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Karagiannis2004_CollagenIproteolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Karagiannis2004CollageniproteolysisModel0911270007Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Karagiannis2004_CollagenIproteolysis."""

    _SBML_ID = 'MODEL0911270007'
    _TITLE = 'Karagiannis2004_CollagenIproteolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['MT1', 'MT1cat', 'MT1t', 'T2', 'MT1_T2', 'M2p', 'MT1_T2_M2p', 'MT1_T2_M2p_MT1', 'MT1_T2_star', 'M2', 'M2_T2', 'M2_T2_star', 'M2_C1', 'C1', 'C1D']
    _SPECIES_LABELS = {'MT1': 'MT1', 'MT1cat': 'MT1cat', 'MT1t': 'MT1t', 'T2': 'T2', 'MT1_T2': 'MT1 T2', 'M2p': 'M2P', 'MT1_T2_M2p': 'MT1 T2 M2P', 'MT1_T2_M2p_MT1': 'MT1 T2 M2P MT1', 'MT1_T2_star': 'MT1 T2 Star', 'M2': 'M2', 'M2_T2': 'M2 T2', 'M2_T2_star': 'M2 T2 Star', 'M2_C1': 'M2 C1', 'C1': 'C1', 'C1D': 'C1D'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_t2': ('T2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T2`.'), 'initial_mt1t': ('MT1t', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MT1t`.'), 'initial_mt1cat': ('MT1cat', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MT1cat`.'), 'initial_mt1_t2_star': ('MT1_T2_star', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MT1_T2_star`.'), 'initial_mt1_t2_m2_p_mt1': ('MT1_T2_M2p_MT1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MT1_T2_M2p_MT1`.'), 'initial_mt1_t2_m2_p': ('MT1_T2_M2p', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MT1_T2_M2p`.')}
    _HEADLINE_OUTPUTS = {'model_state_t2': ('T2', 'native SBML value', 'T2. Maps to SBML symbol `T2`.'), 'mt1t': ('MT1t', 'native SBML value', 'MT1t. Maps to SBML symbol `MT1t`.'), 'mt1cat': ('MT1cat', 'native SBML value', 'MT1cat. Maps to SBML symbol `MT1cat`.'), 'mt1_t2_star': ('MT1_T2_star', 'native SBML value', 'MT1 T2 Star. Maps to SBML symbol `MT1_T2_star`.'), 'mt1_t2_m2_p_mt1': ('MT1_T2_M2p_MT1', 'native SBML value', 'MT1 T2 M2P MT1. Maps to SBML symbol `MT1_T2_M2p_MT1`.'), 'mt1_t2_m2_p': ('MT1_T2_M2p', 'native SBML value', 'MT1 T2 M2P. Maps to SBML symbol `MT1_T2_M2p`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0911270007.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
