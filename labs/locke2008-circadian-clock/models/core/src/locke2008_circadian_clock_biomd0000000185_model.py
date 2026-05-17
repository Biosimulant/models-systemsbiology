# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Locke2008_Circadian_Clock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Locke2008CircadianClockBiomd0000000185Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Locke2008_Circadian_Clock."""

    _SBML_ID = 'BIOMD0000000185'
    _TITLE = 'Locke2008_Circadian_Clock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X1', 'Y1', 'Z1', 'V1', 'X2', 'Y2', 'Z2', 'V2']
    _SPECIES_LABELS = {'X1': 'clock gene mRNA', 'Y1': 'clock protein', 'Z1': 'Transcriptional repressor', 'V1': 'Neuropeptide', 'X2': 'clock gene mRNA', 'Y2': 'clock protein', 'Z2': 'Transcriptional repressor', 'V2': 'Neuropeptide'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_clock_gene_mrna': ('X1', 4.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X1`.'), 'initial_clock_protein': ('Y1', 3.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y1`.'), 'initial_transcriptional_repressor': ('Z1', 2.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z1`.'), 'initial_clock_protein_2': ('Y2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y2`.'), 'initial_clock_gene_mrna_2': ('X2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X2`.'), 'initial_transcriptional_repressor_2': ('Z2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z2`.')}
    _HEADLINE_OUTPUTS = {'clock_gene_mrna': ('X1', 'native SBML value', 'clock gene mRNA. Maps to SBML symbol `X1`.'), 'clock_protein': ('Y1', 'native SBML value', 'clock protein. Maps to SBML symbol `Y1`.'), 'transcriptional_repressor': ('Z1', 'native SBML value', 'Transcriptional repressor. Maps to SBML symbol `Z1`.'), 'clock_protein_2': ('Y2', 'native SBML value', 'clock protein. Maps to SBML symbol `Y2`.'), 'clock_gene_mrna_2': ('X2', 'native SBML value', 'clock gene mRNA. Maps to SBML symbol `X2`.'), 'transcriptional_repressor_2': ('Z2', 'native SBML value', 'Transcriptional repressor. Maps to SBML symbol `Z2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000185.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
