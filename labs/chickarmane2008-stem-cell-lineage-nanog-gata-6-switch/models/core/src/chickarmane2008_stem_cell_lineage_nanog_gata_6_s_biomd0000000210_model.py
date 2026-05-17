# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Chickarmane2008 - Stem cell lineage - NANOG GATA-6 switch."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chickarmane2008StemCellLineageNanogGata6SBiomd0000000210Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Chickarmane2008 - Stem cell lineage - NANOG GATA-6 switch."""

    _SBML_ID = 'BIOMD0000000210'
    _TITLE = 'Chickarmane2008 - Stem cell lineage - NANOG GATA-6 switch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['OCT4_Gene', 'NANOG_Gene', 'SOX2_Gene', 'GATA6_Gene', 'CDX2_Gene', 'GCNF_Gene', 'targetGene', 'degradation', 'p53', 'A', 'OCT4', 'SOX2', 'NANOG', 'GATA6', 'CDX2', 'GCNF', 'OCT4_SOX2', 'Protein']
    _SPECIES_LABELS = {'OCT4_Gene': 'OCT4 Gene', 'NANOG_Gene': 'NANOG Gene', 'SOX2_Gene': 'SOX2 Gene', 'GATA6_Gene': 'GATA6 Gene', 'CDX2_Gene': 'CDX2 Gene', 'GCNF_Gene': 'GCNF Gene', 'targetGene': 'TargetGene', 'degradation': 'Degradation', 'p53': 'P53', 'A': 'A', 'OCT4': 'OCT4', 'SOX2': 'SOX2', 'NANOG': 'NANOG', 'GATA6': 'GATA6', 'CDX2': 'CDX2', 'GCNF': 'GCNF', 'OCT4_SOX2': 'OCT4 SOX2', 'Protein': 'Protein'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_target_gene': ('targetGene', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `targetGene`.'), 'initial_sox2_gene': ('SOX2_Gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SOX2_Gene`.'), 'initial_protein': ('Protein', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Protein`.'), 'initial_oct4_gene': ('OCT4_Gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `OCT4_Gene`.'), 'initial_nanog_gene': ('NANOG_Gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NANOG_Gene`.'), 'initial_gcnf_gene': ('GCNF_Gene', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GCNF_Gene`.')}
    _HEADLINE_OUTPUTS = {'target_gene': ('targetGene', 'native SBML value', 'TargetGene. Maps to SBML symbol `targetGene`.'), 'sox2_gene': ('SOX2_Gene', 'native SBML value', 'SOX2 Gene. Maps to SBML symbol `SOX2_Gene`.'), 'protein': ('Protein', 'native SBML value', 'Protein. Maps to SBML symbol `Protein`.'), 'oct4_gene': ('OCT4_Gene', 'native SBML value', 'OCT4 Gene. Maps to SBML symbol `OCT4_Gene`.'), 'nanog_gene': ('NANOG_Gene', 'native SBML value', 'NANOG Gene. Maps to SBML symbol `NANOG_Gene`.'), 'gcnf_gene': ('GCNF_Gene', 'native SBML value', 'GCNF Gene. Maps to SBML symbol `GCNF_Gene`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000210.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
