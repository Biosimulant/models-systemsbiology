# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisBiomd0000000864Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA)."""

    _SBML_ID = 'BIOMD0000000864'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'miR_gene', 'miR_gene_TF1', 'Signal', 'TF1', 'TF1_mRNA', 'Sink']
    _SPECIES_LABELS = {'miR': 'miR', 'miR_gene': 'miR_gene', 'miR_gene_TF1': 'miR_gene_TF1', 'Signal': 'Signal', 'TF1': 'TF1', 'TF1_mRNA': 'TF1_mRNA', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_signal': ('Signal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Signal`.'), 'initial_mi_r_gene': ('miR_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene`.'), 'initial_mi_r_gene_tf1': ('miR_gene_TF1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene_TF1`.'), 'initial_mi_r': ('miR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR`.'), 'initial_tf1_mrna': ('TF1_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_mRNA`.'), 'initial_model_state_tf1': ('TF1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1`.')}
    _HEADLINE_OUTPUTS = {'signal': ('Signal', 'native SBML value', 'Signal. Maps to SBML symbol `Signal`.'), 'mi_r_gene': ('miR_gene', 'native SBML value', 'miR_gene. Maps to SBML symbol `miR_gene`.'), 'mi_r_gene_tf1': ('miR_gene_TF1', 'native SBML value', 'miR_gene_TF1. Maps to SBML symbol `miR_gene_TF1`.'), 'mi_r': ('miR', 'native SBML value', 'miR. Maps to SBML symbol `miR`.'), 'tf1_mrna': ('TF1_mRNA', 'native SBML value', 'TF1_mRNA. Maps to SBML symbol `TF1_mRNA`.'), 'tf1': ('TF1', 'native SBML value', 'TF1. Maps to SBML symbol `TF1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000864.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
