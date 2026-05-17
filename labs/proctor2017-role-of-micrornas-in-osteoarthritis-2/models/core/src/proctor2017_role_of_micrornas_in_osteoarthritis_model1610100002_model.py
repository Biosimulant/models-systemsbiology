# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA with Delay)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1610100002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA with Delay)."""

    _SBML_ID = 'MODEL1610100002'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA with Delay)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'miR_gene', 'miR_gene_TF1', 'pri_miR', 'Signal', 'TF1_cyt', 'TF1_nuc', 'TF1_mRNA', 'Sink']
    _SPECIES_LABELS = {'miR': 'MiR', 'miR_gene': 'MiR Gene', 'miR_gene_TF1': 'MiR Gene TF1', 'pri_miR': 'Pri MiR', 'Signal': 'Signal', 'TF1_cyt': 'TF1 Cyt', 'TF1_nuc': 'TF1 Nuc', 'TF1_mRNA': 'TF1 MRNA', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_signal': ('Signal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Signal`.'), 'initial_mi_r_gene': ('miR_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene`.'), 'initial_tf1_nuc': ('TF1_nuc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_nuc`.'), 'initial_tf1_mrna': ('TF1_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_mRNA`.'), 'initial_tf1_cyt': ('TF1_cyt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_cyt`.'), 'initial_sink': ('Sink', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sink`.')}
    _HEADLINE_OUTPUTS = {'signal': ('Signal', 'native SBML value', 'Signal. Maps to SBML symbol `Signal`.'), 'mi_r_gene': ('miR_gene', 'native SBML value', 'MiR Gene. Maps to SBML symbol `miR_gene`.'), 'tf1_nuc': ('TF1_nuc', 'native SBML value', 'TF1 Nuc. Maps to SBML symbol `TF1_nuc`.'), 'tf1_mrna': ('TF1_mRNA', 'native SBML value', 'TF1 MRNA. Maps to SBML symbol `TF1_mRNA`.'), 'tf1_cyt': ('TF1_cyt', 'native SBML value', 'TF1 Cyt. Maps to SBML symbol `TF1_cyt`.'), 'sink': ('Sink', 'native SBML value', 'Sink. Maps to SBML symbol `Sink`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1610100002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
