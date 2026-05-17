# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Schmitz2014 - RNA triplex formation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schmitz2014RnaTriplexFormationBiomd0000000530Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Schmitz2014 - RNA triplex formation."""

    _SBML_ID = 'BIOMD0000000530'
    _TITLE = 'Schmitz2014 - RNA triplex formation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10']
    _SPECIES_LABELS = {'species_1': 'mRNA', 'species_2': 'miRNA_1', 'species_3': 'miRNA_2', 'species_4': 'duplex_1', 'species_5': 'duplex_2', 'species_6': 'triplex', 'species_7': 'TF_mRNA', 'species_8': 'TF_miRNA_1', 'species_9': 'TF_miRNA_2', 'species_10': 'protein'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_protein': ('species_10', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_10`.'), 'initial_mrna': ('species_1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`.'), 'initial_tf_mi_rna_2': ('species_9', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_9`.'), 'initial_tf_mi_rna_1': ('species_8', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`.'), 'initial_tf_mrna': ('species_7', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`.'), 'initial_triplex': ('species_6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_6`.')}
    _HEADLINE_OUTPUTS = {'protein': ('species_10', 'native SBML value', 'protein. Maps to SBML symbol `species_10`.'), 'mrna': ('species_1', 'native SBML value', 'mRNA. Maps to SBML symbol `species_1`.'), 'tf_mi_rna_2': ('species_9', 'native SBML value', 'TF_miRNA_2. Maps to SBML symbol `species_9`.'), 'tf_mi_rna_1': ('species_8', 'native SBML value', 'TF_miRNA_1. Maps to SBML symbol `species_8`.'), 'tf_mrna': ('species_7', 'native SBML value', 'TF_mRNA. Maps to SBML symbol `species_7`.'), 'triplex': ('species_6', 'native SBML value', 'triplex. Maps to SBML symbol `species_6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000530.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
