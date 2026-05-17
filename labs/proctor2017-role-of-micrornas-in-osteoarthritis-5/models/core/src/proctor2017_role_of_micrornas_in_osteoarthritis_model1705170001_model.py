# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 coherent feed forward)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 coherent feed forward)."""

    _SBML_ID = 'MODEL1705170001'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 coherent feed forward)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IL1', 'miR140', 'miR140_gene', 'ADAMTS5_mRNA', 'ADAMTS5_mRNA_miR140', 'Sink']
    _SPECIES_LABELS = {'IL1': 'IL1', 'miR140': 'MiR140', 'miR140_gene': 'MiR140 Gene', 'ADAMTS5_mRNA': 'ADAMTS5 MRNA', 'ADAMTS5_mRNA_miR140': 'ADAMTS5 MRNA MiR140', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mi_r140': ('miR140', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`.'), 'initial_model_state_il1': ('IL1', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL1`.'), 'initial_mi_r140_gene': ('miR140_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene`.'), 'initial_sink': ('Sink', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sink`.'), 'initial_adamts5_mrna_mi_r140': ('ADAMTS5_mRNA_miR140', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADAMTS5_mRNA_miR140`.'), 'initial_adamts5_mrna': ('ADAMTS5_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADAMTS5_mRNA`.')}
    _HEADLINE_OUTPUTS = {'mi_r140': ('miR140', 'native SBML value', 'MiR140. Maps to SBML symbol `miR140`.'), 'il1': ('IL1', 'native SBML value', 'IL1. Maps to SBML symbol `IL1`.'), 'mi_r140_gene': ('miR140_gene', 'native SBML value', 'MiR140 Gene. Maps to SBML symbol `miR140_gene`.'), 'sink': ('Sink', 'native SBML value', 'Sink. Maps to SBML symbol `Sink`.'), 'adamts5_mrna_mi_r140': ('ADAMTS5_mRNA_miR140', 'native SBML value', 'ADAMTS5 MRNA MiR140. Maps to SBML symbol `ADAMTS5_mRNA_miR140`.'), 'adamts5_mrna': ('ADAMTS5_mRNA', 'native SBML value', 'ADAMTS5 MRNA. Maps to SBML symbol `ADAMTS5_mRNA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
