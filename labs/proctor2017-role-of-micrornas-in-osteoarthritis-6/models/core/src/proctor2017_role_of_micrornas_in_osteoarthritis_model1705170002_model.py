# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 incoherent feed forward)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 incoherent feed forward)."""

    _SBML_ID = 'MODEL1705170002'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (miR140-IL1 incoherent feed forward)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IL1', 'miR140', 'miR140_gene', 'miR140_gene_NFkB', 'MMP13_mRNA', 'MMP13_mRNA_miR140', 'NFkB', 'Sink']
    _SPECIES_LABELS = {'IL1': 'IL1', 'miR140': 'MiR140', 'miR140_gene': 'MiR140 Gene', 'miR140_gene_NFkB': 'MiR140 Gene NFkB', 'MMP13_mRNA': 'MMP13 MRNA', 'MMP13_mRNA_miR140': 'MMP13 MRNA MiR140', 'NFkB': 'NFkB', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_n_fk_b': ('NFkB', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFkB`.'), 'initial_mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene_NFkB`.'), 'initial_model_state_il1': ('IL1', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL1`.'), 'initial_mmp13_mrna': ('MMP13_mRNA', 25.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MMP13_mRNA`.'), 'initial_mi_r140': ('miR140', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`.'), 'initial_mi_r140_gene': ('miR140_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene`.')}
    _HEADLINE_OUTPUTS = {'n_fk_b': ('NFkB', 'native SBML value', 'NFkB. Maps to SBML symbol `NFkB`.'), 'mi_r140_gene_n_fk_b': ('miR140_gene_NFkB', 'native SBML value', 'MiR140 Gene NFkB. Maps to SBML symbol `miR140_gene_NFkB`.'), 'il1': ('IL1', 'native SBML value', 'IL1. Maps to SBML symbol `IL1`.'), 'mmp13_mrna': ('MMP13_mRNA', 'native SBML value', 'MMP13 MRNA. Maps to SBML symbol `MMP13_mRNA`.'), 'mi_r140': ('miR140', 'native SBML value', 'MiR140. Maps to SBML symbol `miR140`.'), 'mi_r140_gene': ('miR140_gene', 'native SBML value', 'MiR140 Gene. Maps to SBML symbol `miR140_gene`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
