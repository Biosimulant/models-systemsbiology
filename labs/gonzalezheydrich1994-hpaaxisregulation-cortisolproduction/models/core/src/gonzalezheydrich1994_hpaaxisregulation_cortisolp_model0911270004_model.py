# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for GonzalezHeydrich1994_HPAaxisRegulation_CortisolProduction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gonzalezheydrich1994HpaaxisregulationCortisolpModel0911270004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for GonzalezHeydrich1994_HPAaxisRegulation_CortisolProduction."""

    _SBML_ID = 'MODEL0911270004'
    _TITLE = 'GonzalezHeydrich1994_HPAaxisRegulation_CortisolProduction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['cortisol', 'ACTH', 'CRH']
    _SPECIES_LABELS = {'cortisol': 'Cortisol', 'ACTH': 'ACTH', 'CRH': 'CRH'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cortisol': ('cortisol', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cortisol`.'), 'initial_model_state_crh': ('CRH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CRH`.'), 'initial_acth': ('ACTH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ACTH`.')}
    _HEADLINE_OUTPUTS = {'cortisol': ('cortisol', 'native SBML value', 'Cortisol. Maps to SBML symbol `cortisol`.'), 'crh': ('CRH', 'native SBML value', 'CRH. Maps to SBML symbol `CRH`.'), 'acth': ('ACTH', 'native SBML value', 'ACTH. Maps to SBML symbol `ACTH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0911270004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
