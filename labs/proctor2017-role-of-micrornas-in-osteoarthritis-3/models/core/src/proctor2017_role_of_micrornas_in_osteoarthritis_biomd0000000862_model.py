# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedback By Micro RNA)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisBiomd0000000862Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedback By Micro RNA)."""

    _SBML_ID = 'BIOMD0000000862'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedback By Micro RNA)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'miR_gene', 'miR_gene_TF1', 'miR_gene_TF2', 'Signal', 'TF1', 'TF1_mRNA', 'TF2', 'Sink']
    _SPECIES_LABELS = {'miR': 'miR', 'miR_gene': 'miR_gene', 'miR_gene_TF1': 'miR_gene_TF1', 'miR_gene_TF2': 'miR_gene_TF2', 'Signal': 'Signal', 'TF1': 'TF1', 'TF1_mRNA': 'TF1_mRNA', 'TF2': 'TF2', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_signal': ('Signal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Signal`.'), 'initial_mi_r': ('miR', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR`.'), 'initial_mi_r_gene': ('miR_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene`.'), 'initial_mi_r_gene_tf2': ('miR_gene_TF2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene_TF2`.'), 'initial_mi_r_gene_tf1': ('miR_gene_TF1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene_TF1`.'), 'initial_tf1_mrna': ('TF1_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_mRNA`.')}
    _HEADLINE_OUTPUTS = {'signal': ('Signal', 'native SBML value', 'Signal. Maps to SBML symbol `Signal`.'), 'mi_r': ('miR', 'native SBML value', 'miR. Maps to SBML symbol `miR`.'), 'mi_r_gene': ('miR_gene', 'native SBML value', 'miR_gene. Maps to SBML symbol `miR_gene`.'), 'mi_r_gene_tf2': ('miR_gene_TF2', 'native SBML value', 'miR_gene_TF2. Maps to SBML symbol `miR_gene_TF2`.'), 'mi_r_gene_tf1': ('miR_gene_TF1', 'native SBML value', 'miR_gene_TF1. Maps to SBML symbol `miR_gene_TF1`.'), 'tf1_mrna': ('TF1_mRNA', 'native SBML value', 'TF1_mRNA. Maps to SBML symbol `TF1_mRNA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000862.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
