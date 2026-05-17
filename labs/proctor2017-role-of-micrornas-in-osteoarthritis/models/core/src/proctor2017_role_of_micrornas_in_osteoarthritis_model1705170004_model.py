# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Mir140-IGFBP5 incoherent feed forward)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (Mir140-IGFBP5 incoherent feed forward)."""

    _SBML_ID = 'MODEL1705170004'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (Mir140-IGFBP5 incoherent feed forward)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ACAN', 'AKT', 'AKT_P', 'IGF1', 'IGF1_IGFBP5', 'IGFBP5', 'IGFBP5_mRNA', 'IGFBP5_mRNA_miR140', 'IkB', 'IkB_NFkB', 'JNK', 'JNK_P', 'miR140', 'miR140_gene', 'miR140_gene_NFkB', 'NFkB', 'TNFa', 'Sink', 'Source']
    _SPECIES_LABELS = {'ACAN': 'ACAN', 'AKT': 'AKT', 'AKT_P': 'AKT P', 'IGF1': 'IGF1', 'IGF1_IGFBP5': 'IGF1 IGFBP5', 'IGFBP5': 'IGFBP5', 'IGFBP5_mRNA': 'IGFBP5 MRNA', 'IGFBP5_mRNA_miR140': 'IGFBP5 MRNA MiR140', 'IkB': 'IkB', 'IkB_NFkB': 'IkB NFkB', 'JNK': 'JNK', 'JNK_P': 'JNK P', 'miR140': 'MiR140', 'miR140_gene': 'MiR140 Gene', 'miR140_gene_NFkB': 'MiR140 Gene NFkB', 'NFkB': 'NFkB', 'TNFa': 'TNFa', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tn_fa': ('TNFa', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNFa`.'), 'initial_ik_b_n_fk_b': ('IkB_NFkB', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkB_NFkB`.'), 'initial_n_fk_b': ('NFkB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFkB`.'), 'initial_mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene_NFkB`.'), 'initial_igf1': ('IGF1', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IGF1`.'), 'initial_mi_r140': ('miR140', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`.')}
    _HEADLINE_OUTPUTS = {'tn_fa': ('TNFa', 'native SBML value', 'TNFa. Maps to SBML symbol `TNFa`.'), 'ik_b_n_fk_b': ('IkB_NFkB', 'native SBML value', 'IkB NFkB. Maps to SBML symbol `IkB_NFkB`.'), 'n_fk_b': ('NFkB', 'native SBML value', 'NFkB. Maps to SBML symbol `NFkB`.'), 'mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 'native SBML value', 'MiR140 Gene NFkB. Maps to SBML symbol `miR140_gene_NFkB`.'), 'igf1': ('IGF1', 'native SBML value', 'IGF1. Maps to SBML symbol `IGF1`.'), 'mi_r140': ('miR140', 'native SBML value', 'MiR140. Maps to SBML symbol `miR140`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
