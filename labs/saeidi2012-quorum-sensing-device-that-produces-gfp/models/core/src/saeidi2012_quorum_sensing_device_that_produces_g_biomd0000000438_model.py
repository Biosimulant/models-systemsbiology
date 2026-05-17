# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Saeidi2012 - Quorum sensing device that produces GFP."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Saeidi2012QuorumSensingDeviceThatProducesGBiomd0000000438Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Saeidi2012 - Quorum sensing device that produces GFP."""

    _SBML_ID = 'BIOMD0000000438'
    _TITLE = 'Saeidi2012 - Quorum sensing device that produces GFP'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's19', 's3', 's4', 's16', 's17', 's5', 's42', 's2', 's45']
    _SPECIES_LABELS = {'s1': 'Ptet-LasR', 's19': 'LasR', 's3': 'sa3_degraded', 's4': '3OC12HSL', 's16': 'pLuxR', 's17': 'A pLux', 's5': 'sa6_degraded', 's42': 'LasR/AHL', 's2': 'mRNA(LasR)', 's45': 'GFP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p_lux_r': ('s16', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s16`.'), 'initial_ptet_las_r': ('s1', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_model_state_3_oc12_hsl': ('s4', 5e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s4`.'), 'initial_las_r': ('s19', 1e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s19`.'), 'initial_sa6_degraded': ('s5', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s5`.'), 'initial_sa3_degraded': ('s3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s3`.')}
    _HEADLINE_OUTPUTS = {'p_lux_r': ('s16', 'native SBML value', 'pLuxR. Maps to SBML symbol `s16`.'), 'ptet_las_r': ('s1', 'native SBML value', 'Ptet-LasR. Maps to SBML symbol `s1`.'), 'model_state_3_oc12_hsl': ('s4', 'native SBML value', '3OC12HSL. Maps to SBML symbol `s4`.'), 'las_r': ('s19', 'native SBML value', 'LasR. Maps to SBML symbol `s19`.'), 'sa6_degraded': ('s5', 'native SBML value', 'sa6_degraded. Maps to SBML symbol `s5`.'), 'sa3_degraded': ('s3', 'native SBML value', 'sa3_degraded. Maps to SBML symbol `s3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000438.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
