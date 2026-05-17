# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ueda2001_typeBtrichothecenes."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ueda2001TypebtrichothecenesModel1006230044Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ueda2001_typeBtrichothecenes."""

    _SBML_ID = 'MODEL1006230044'
    _TITLE = 'Ueda2001_typeBtrichothecenes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Per_m', 'Per_c', 'Tim_m', 'Tim_c', 'PT_c', 'PT_n', 'Clk_m', 'Clk_c', 'CC_c', 'CC_n']
    _SPECIES_LABELS = {'Per_m': 'Per M', 'Per_c': 'Per C', 'Tim_m': 'Tim M', 'Tim_c': 'Tim C', 'PT_c': 'PT C', 'PT_n': 'PT N', 'Clk_m': 'Clk M', 'Clk_c': 'Clk C', 'CC_c': 'CC C', 'CC_n': 'CC N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tim_m': ('Tim_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tim_m`.'), 'initial_tim_c': ('Tim_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tim_c`.'), 'initial_per_m': ('Per_m', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Per_m`.'), 'initial_per_c': ('Per_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Per_c`.'), 'initial_pt_n': ('PT_n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PT_n`.'), 'initial_pt_c': ('PT_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PT_c`.')}
    _HEADLINE_OUTPUTS = {'tim_m': ('Tim_m', 'native SBML value', 'Tim M. Maps to SBML symbol `Tim_m`.'), 'tim_c': ('Tim_c', 'native SBML value', 'Tim C. Maps to SBML symbol `Tim_c`.'), 'per_m': ('Per_m', 'native SBML value', 'Per M. Maps to SBML symbol `Per_m`.'), 'per_c': ('Per_c', 'native SBML value', 'Per C. Maps to SBML symbol `Per_c`.'), 'pt_n': ('PT_n', 'native SBML value', 'PT N. Maps to SBML symbol `PT_n`.'), 'pt_c': ('PT_c', 'native SBML value', 'PT C. Maps to SBML symbol `PT_c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230044.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
