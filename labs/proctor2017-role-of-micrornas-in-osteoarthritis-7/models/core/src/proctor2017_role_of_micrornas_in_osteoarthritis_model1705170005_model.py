# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140 in osteoarthritis)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170005Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140 in osteoarthritis)."""

    _SBML_ID = 'MODEL1705170005'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (miR140 in osteoarthritis)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR140', 'miR140_SMAD3_mRNA', 'miR140_gene', 'miR140_gene_SMAD3_P', 'SMAD3', 'SMAD3_mRNA', 'SMAD3_P', 'SMAD7', 'TGFb_A', 'TGFb_I', 'Sink', 'Source', 'IL1', 'ADAMTS5_mRNA', 'ADAMTS5_mRNA_miR140', 'miR140_gene_NFkB', 'MMP13_mRNA', 'MMP13_mRNA_miR140', 'NFkB', 'HDAC4', 'HDAC4_mRNA', 'HDAC4_mRNA_miR140', 'HDAC4_RUNX2', 'HDAC4_RUNX2_gene', 'miR140_gene_SOX9', 'RUNX2', 'RUNX2_gene', 'SOX9', 'ACAN', 'AKT', 'AKT_P', 'IGF1', 'IGF1_IGFBP5', 'IGFBP5', 'IGFBP5_mRNA', 'IGFBP5_mRNA_miR140', 'IkB', 'IkB_NFkB', 'JNK', 'JNK_P', 'TNFa', 'ADAMTS5', 'COL2A1', 'anti_miR140', 'miR140_anti_miR140', 'MMP13', 'SOX9_A', 'AggFrag', 'Aggrecan', 'Aggrecan_Collagen2', 'ColFrag', 'Collagen2']
    _SPECIES_LABELS = {'miR140': 'MiR140', 'miR140_SMAD3_mRNA': 'MiR140 SMAD3 MRNA', 'miR140_gene': 'MiR140 Gene', 'miR140_gene_SMAD3_P': 'MiR140 Gene SMAD3 P', 'SMAD3': 'SMAD3', 'SMAD3_mRNA': 'SMAD3 MRNA', 'SMAD3_P': 'SMAD3 P', 'SMAD7': 'SMAD7', 'TGFb_A': 'TGFb A', 'TGFb_I': 'TGFb I', 'Sink': 'Sink', 'Source': 'Source', 'IL1': 'IL1', 'ADAMTS5_mRNA': 'ADAMTS5 MRNA', 'ADAMTS5_mRNA_miR140': 'ADAMTS5 MRNA MiR140', 'miR140_gene_NFkB': 'MiR140 Gene NFkB', 'MMP13_mRNA': 'MMP13 MRNA', 'MMP13_mRNA_miR140': 'MMP13 MRNA MiR140', 'NFkB': 'NFkB', 'HDAC4': 'HDAC4', 'HDAC4_mRNA': 'HDAC4 MRNA', 'HDAC4_mRNA_miR140': 'HDAC4 MRNA MiR140', 'HDAC4_RUNX2': 'HDAC4 RUNX2', 'HDAC4_RUNX2_gene': 'HDAC4 RUNX2 Gene', 'miR140_gene_SOX9': 'MiR140 Gene SOX9', 'RUNX2': 'RUNX2', 'RUNX2_gene': 'RUNX2 Gene', 'SOX9': 'SOX9', 'ACAN': 'ACAN', 'AKT': 'AKT', 'AKT_P': 'AKT P', 'IGF1': 'IGF1', 'IGF1_IGFBP5': 'IGF1 IGFBP5', 'IGFBP5': 'IGFBP5', 'IGFBP5_mRNA': 'IGFBP5 MRNA', 'IGFBP5_mRNA_miR140': 'IGFBP5 MRNA MiR140', 'IkB': 'IkB', 'IkB_NFkB': 'IkB NFkB', 'JNK': 'JNK', 'JNK_P': 'JNK P', 'TNFa': 'TNFa', 'ADAMTS5': 'ADAMTS5', 'COL2A1': 'COL2A1', 'anti_miR140': 'Anti MiR140', 'miR140_anti_miR140': 'MiR140 Anti MiR140', 'MMP13': 'MMP13', 'SOX9_A': 'SOX9 A', 'AggFrag': 'AggFrag', 'Aggrecan': 'Aggrecan', 'Aggrecan_Collagen2': 'Aggrecan Collagen2', 'ColFrag': 'ColFrag', 'Collagen2': 'Collagen2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tn_fa': ('TNFa', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNFa`.'), 'initial_tg_fb_a': ('TGFb_A', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_A`.'), 'initial_ik_b_n_fk_b': ('IkB_NFkB', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkB_NFkB`.'), 'initial_n_fk_b': ('NFkB', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFkB`.'), 'initial_tg_fb_i': ('TGFb_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_I`.'), 'initial_mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene_NFkB`.')}
    _HEADLINE_OUTPUTS = {'tn_fa': ('TNFa', 'native SBML value', 'TNFa. Maps to SBML symbol `TNFa`.'), 'tg_fb_a': ('TGFb_A', 'native SBML value', 'TGFb A. Maps to SBML symbol `TGFb_A`.'), 'ik_b_n_fk_b': ('IkB_NFkB', 'native SBML value', 'IkB NFkB. Maps to SBML symbol `IkB_NFkB`.'), 'n_fk_b': ('NFkB', 'native SBML value', 'NFkB. Maps to SBML symbol `NFkB`.'), 'tg_fb_i': ('TGFb_I', 'native SBML value', 'TGFb I. Maps to SBML symbol `TGFb_I`.'), 'mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 'native SBML value', 'MiR140 Gene NFkB. Maps to SBML symbol `miR140_gene_NFkB`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
