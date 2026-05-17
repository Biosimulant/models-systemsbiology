# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nikolov2020 - p53-miR34 model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nikolov2020P53Mir34ModelBiomd0000001057Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nikolov2020 - p53-miR34 model."""

    _SBML_ID = 'BIOMD0000001057'
    _TITLE = 'Nikolov2020 - p53-miR34 model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TFp53', 'miR34a']
    _SPECIES_LABELS = {'TFp53': 'TFp53', 'miR34a': 'miR34a'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mi_r34a': ('miR34a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR34a`.'), 'initial_t_fp53': ('TFp53', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TFp53`.')}
    _HEADLINE_OUTPUTS = {'mi_r34a': ('miR34a', 'native SBML value', 'miR34a. Maps to SBML symbol `miR34a`.'), 't_fp53': ('TFp53', 'native SBML value', 'TFp53. Maps to SBML symbol `TFp53`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001057.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
