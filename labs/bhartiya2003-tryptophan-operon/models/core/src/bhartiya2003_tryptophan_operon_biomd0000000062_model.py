# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bhartiya2003_Tryptophan_operon."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhartiya2003TryptophanOperonBiomd0000000062Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bhartiya2003_Tryptophan_operon."""

    _SBML_ID = 'BIOMD0000000062'
    _TITLE = 'Bhartiya2003_Tryptophan_operon'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Enz', 'Ts', 'Tt', 'To']
    _SPECIES_LABELS = {'Enz': 'Anthranilate synthase', 'Ts': 'Synthesized tryptophan', 'Tt': 'Total tryptophan', 'To': 'exog. Trp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_exog_trp': ('To', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `To`.'), 'initial_total_tryptophan': ('Tt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tt`.'), 'initial_synthesized_tryptophan': ('Ts', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ts`.'), 'initial_anthranilate_synthase': ('Enz', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Enz`.')}
    _HEADLINE_OUTPUTS = {'exog_trp': ('To', 'native SBML value', 'exog. Trp. Maps to SBML symbol `To`.'), 'total_tryptophan': ('Tt', 'native SBML value', 'Total tryptophan. Maps to SBML symbol `Tt`.'), 'synthesized_tryptophan': ('Ts', 'native SBML value', 'Synthesized tryptophan. Maps to SBML symbol `Ts`.'), 'anthranilate_synthase': ('Enz', 'native SBML value', 'Anthranilate synthase. Maps to SBML symbol `Enz`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000062.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
