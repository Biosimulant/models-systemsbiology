# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Coherent By MicroRNA)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1610100003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Coherent By MicroRNA)."""

    _SBML_ID = 'MODEL1610100003'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Coherent By MicroRNA)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'TF1', 'TF1_TF2target_gene', 'TF2', 'TF2target_mRNA', 'TF2target_gene', 'TF2_TF2target_gene', 'Sink']
    _SPECIES_LABELS = {'miR': 'MiR', 'TF1': 'TF1', 'TF1_TF2target_gene': 'TF1 TF2target Gene', 'TF2': 'TF2', 'TF2target_mRNA': 'TF2target MRNA', 'TF2target_gene': 'TF2target Gene', 'TF2_TF2target_gene': 'TF2 TF2target Gene', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tf2target_mrna': ('TF2target_mRNA', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF2target_mRNA`.'), 'initial_model_state_tf2': ('TF2', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF2`.'), 'initial_tf2target_gene': ('TF2target_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF2target_gene`.'), 'initial_tf2_tf2target_gene': ('TF2_TF2target_gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF2_TF2target_gene`.'), 'initial_tf1_tf2target_gene': ('TF1_TF2target_gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_TF2target_gene`.'), 'initial_model_state_tf1': ('TF1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1`.')}
    _HEADLINE_OUTPUTS = {'tf2target_mrna': ('TF2target_mRNA', 'native SBML value', 'TF2target MRNA. Maps to SBML symbol `TF2target_mRNA`.'), 'tf2': ('TF2', 'native SBML value', 'TF2. Maps to SBML symbol `TF2`.'), 'tf2target_gene': ('TF2target_gene', 'native SBML value', 'TF2target Gene. Maps to SBML symbol `TF2target_gene`.'), 'tf2_tf2target_gene': ('TF2_TF2target_gene', 'native SBML value', 'TF2 TF2target Gene. Maps to SBML symbol `TF2_TF2target_gene`.'), 'tf1_tf2target_gene': ('TF1_TF2target_gene', 'native SBML value', 'TF1 TF2target Gene. Maps to SBML symbol `TF1_TF2target_gene`.'), 'tf1': ('TF1', 'native SBML value', 'TF1. Maps to SBML symbol `TF1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1610100003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
