# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-SMAD3 double negative feedback)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017RoleOfMicrornasInOsteoarthritisModel1705170000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017- Role of microRNAs in osteoarthritis (miR140-SMAD3 double negative feedback)."""

    _SBML_ID = 'MODEL1705170000'
    _TITLE = 'Proctor2017- Role of microRNAs in osteoarthritis (miR140-SMAD3 double negative feedback)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR140', 'miR140_gene', 'miR140_gene_SMAD3_P', 'miR140_SMAD3_mRNA', 'SMAD3', 'SMAD3_mRNA', 'SMAD3_P', 'SMAD7', 'TGFb_A', 'TGFb_I', 'Sink', 'Source']
    _SPECIES_LABELS = {'miR140': 'MiR140', 'miR140_gene': 'MiR140 Gene', 'miR140_gene_SMAD3_P': 'MiR140 Gene SMAD3 P', 'miR140_SMAD3_mRNA': 'MiR140 SMAD3 MRNA', 'SMAD3': 'SMAD3', 'SMAD3_mRNA': 'SMAD3 MRNA', 'SMAD3_P': 'SMAD3 P', 'SMAD7': 'SMAD7', 'TGFb_A': 'TGFb A', 'TGFb_I': 'TGFb I', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tg_fb_a': ('TGFb_A', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_A`.'), 'initial_tg_fb_i': ('TGFb_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_I`.'), 'initial_mi_r140': ('miR140', 450.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`.'), 'initial_smad3': ('SMAD3', 250.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SMAD3`.'), 'initial_mi_r140_smad3_mrna': ('miR140_SMAD3_mRNA', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_SMAD3_mRNA`.'), 'initial_smad3_mrna': ('SMAD3_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SMAD3_mRNA`.')}
    _HEADLINE_OUTPUTS = {'tg_fb_a': ('TGFb_A', 'native SBML value', 'TGFb A. Maps to SBML symbol `TGFb_A`.'), 'tg_fb_i': ('TGFb_I', 'native SBML value', 'TGFb I. Maps to SBML symbol `TGFb_I`.'), 'mi_r140': ('miR140', 'native SBML value', 'MiR140. Maps to SBML symbol `miR140`.'), 'smad3': ('SMAD3', 'native SBML value', 'SMAD3. Maps to SBML symbol `SMAD3`.'), 'mi_r140_smad3_mrna': ('miR140_SMAD3_mRNA', 'native SBML value', 'MiR140 SMAD3 MRNA. Maps to SBML symbol `miR140_SMAD3_mRNA`.'), 'smad3_mrna': ('SMAD3_mRNA', 'native SBML value', 'SMAD3 MRNA. Maps to SBML symbol `SMAD3_mRNA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1705170000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
