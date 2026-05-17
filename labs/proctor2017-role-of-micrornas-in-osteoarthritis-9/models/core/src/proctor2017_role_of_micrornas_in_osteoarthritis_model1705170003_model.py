# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-SOX9 incoherent feed forward)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-SOX9 incoherent feed forward)."""

    _SBML_ID = 'MODEL1705170003'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (miR140-SOX9 incoherent feed forward)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['HDAC4', 'HDAC4_mRNA', 'HDAC4_mRNA_miR140', 'HDAC4_RUNX2', 'HDAC4_RUNX2_gene', 'miR140', 'miR140_gene', 'miR140_gene_SOX9', 'MMP13_mRNA', 'RUNX2', 'RUNX2_gene', 'SOX9', 'Sink', 'Source']
    _SPECIES_LABELS = {'HDAC4': 'HDAC4', 'HDAC4_mRNA': 'HDAC4 MRNA', 'HDAC4_mRNA_miR140': 'HDAC4 MRNA MiR140', 'HDAC4_RUNX2': 'HDAC4 RUNX2', 'HDAC4_RUNX2_gene': 'HDAC4 RUNX2 Gene', 'miR140': 'MiR140', 'miR140_gene': 'MiR140 Gene', 'miR140_gene_SOX9': 'MiR140 Gene SOX9', 'MMP13_mRNA': 'MMP13 MRNA', 'RUNX2': 'RUNX2', 'RUNX2_gene': 'RUNX2 Gene', 'SOX9': 'SOX9', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_sox9': ('SOX9', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SOX9`.'), 'initial_runx2': ('RUNX2', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RUNX2`.'), 'initial_hdac4': ('HDAC4', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HDAC4`.'), 'initial_mi_r140': ('miR140', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`.'), 'initial_hdac4_mrna': ('HDAC4_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HDAC4_mRNA`.'), 'initial_runx2_gene': ('RUNX2_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RUNX2_gene`.')}
    _HEADLINE_OUTPUTS = {'sox9': ('SOX9', 'native SBML value', 'SOX9. Maps to SBML symbol `SOX9`.'), 'runx2': ('RUNX2', 'native SBML value', 'RUNX2. Maps to SBML symbol `RUNX2`.'), 'hdac4': ('HDAC4', 'native SBML value', 'HDAC4. Maps to SBML symbol `HDAC4`.'), 'mi_r140': ('miR140', 'native SBML value', 'MiR140. Maps to SBML symbol `miR140`.'), 'hdac4_mrna': ('HDAC4_mRNA', 'native SBML value', 'HDAC4 MRNA. Maps to SBML symbol `HDAC4_mRNA`.'), 'runx2_gene': ('RUNX2_gene', 'native SBML value', 'RUNX2 Gene. Maps to SBML symbol `RUNX2_gene`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
