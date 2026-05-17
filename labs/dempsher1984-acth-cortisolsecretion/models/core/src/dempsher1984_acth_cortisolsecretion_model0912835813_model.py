# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Dempsher1984_ACTH_CortisolSecretion."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dempsher1984ActhCortisolsecretionModel0912835813Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Dempsher1984_ACTH_CortisolSecretion."""

    _SBML_ID = 'MODEL0912835813'
    _TITLE = 'Dempsher1984_ACTH_CortisolSecretion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['cAMP', 'V', 'W', 'CHOC', 'CHOM', 'CHOL', 'Kmtr', 'Kfor', 'CHON', 'PREG', 'PRO', 'HYPR', 'CORT']
    _SPECIES_LABELS = {'cAMP': 'CAMP', 'V': 'V', 'W': 'W', 'CHOC': 'CHOC', 'CHOM': 'CHOM', 'CHOL': 'CHOL', 'Kmtr': 'Kmtr', 'Kfor': 'Kfor', 'CHON': 'CHON', 'PREG': 'PREG', 'PRO': 'PRO', 'HYPR': 'HYPR', 'CORT': 'CORT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pro': ('PRO', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PRO`.'), 'initial_preg': ('PREG', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PREG`.'), 'initial_kmtr': ('Kmtr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Kmtr`.'), 'initial_kfor': ('Kfor', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Kfor`.'), 'initial_hypr': ('HYPR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HYPR`.'), 'initial_cort': ('CORT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CORT`.')}
    _HEADLINE_OUTPUTS = {'pro': ('PRO', 'native SBML value', 'PRO. Maps to SBML symbol `PRO`.'), 'preg': ('PREG', 'native SBML value', 'PREG. Maps to SBML symbol `PREG`.'), 'kmtr': ('Kmtr', 'native SBML value', 'Kmtr. Maps to SBML symbol `Kmtr`.'), 'kfor': ('Kfor', 'native SBML value', 'Kfor. Maps to SBML symbol `Kfor`.'), 'hypr': ('HYPR', 'native SBML value', 'HYPR. Maps to SBML symbol `HYPR`.'), 'cort': ('CORT', 'native SBML value', 'CORT. Maps to SBML symbol `CORT`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912835813.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
