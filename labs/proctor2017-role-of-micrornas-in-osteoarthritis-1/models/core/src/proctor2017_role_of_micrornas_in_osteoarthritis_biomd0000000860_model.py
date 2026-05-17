# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Incoherent By MicroRNA)_1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisBiomd0000000860Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Incoherent By MicroRNA)_1."""

    _SBML_ID = 'BIOMD0000000860'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Incoherent By MicroRNA)_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'TF1', 'TF1target_mRNA', 'Sink']
    _SPECIES_LABELS = {'miR': 'miR', 'TF1': 'TF1', 'TF1target_mRNA': 'TF1target_mRNA', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mi_r': ('miR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR`.'), 'initial_tf1target_mrna': ('TF1target_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1target_mRNA`.'), 'initial_model_state_tf1': ('TF1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1`.'), 'initial_sink': ('Sink', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sink`.')}
    _HEADLINE_OUTPUTS = {'mi_r': ('miR', 'native SBML value', 'miR. Maps to SBML symbol `miR`.'), 'tf1target_mrna': ('TF1target_mRNA', 'native SBML value', 'TF1target_mRNA. Maps to SBML symbol `TF1target_mRNA`.'), 'tf1': ('TF1', 'native SBML value', 'TF1. Maps to SBML symbol `TF1`.'), 'sink': ('Sink', 'native SBML value', 'Sink. Maps to SBML symbol `Sink`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000860.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
