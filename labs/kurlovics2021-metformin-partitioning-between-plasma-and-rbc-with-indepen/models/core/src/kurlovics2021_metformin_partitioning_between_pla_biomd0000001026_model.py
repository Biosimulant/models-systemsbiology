# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kurlovics2021 - Metformin partitioning between plasma and RBC with independent Kin and Kout coefficients."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kurlovics2021MetforminPartitioningBetweenPlaBiomd0000001026Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kurlovics2021 - Metformin partitioning between plasma and RBC with independent Kin and Kout coefficients."""

    _SBML_ID = 'BIOMD0000001026'
    _TITLE = 'Kurlovics2021 - Metformin partitioning between plasma and RBC with independent Kin and Kout coefficients'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mrbc']
    _SPECIES_LABELS = {'Mrbc': 'Mrbc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mrbc': ('Mrbc', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mrbc`.')}
    _HEADLINE_OUTPUTS = {'mrbc': ('Mrbc', 'substance', 'Mrbc. Maps to SBML symbol `Mrbc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001026.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
