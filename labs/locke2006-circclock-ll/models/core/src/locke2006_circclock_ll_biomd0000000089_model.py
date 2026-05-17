# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Locke2006_CircClock_LL."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Locke2006CircclockLlBiomd0000000089Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Locke2006_CircClock_LL."""

    _SBML_ID = 'BIOMD0000000089'
    _TITLE = 'Locke2006_CircClock_LL'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cLm', 'cLc', 'cLn', 'cTm', 'cTc', 'cTn', 'cXm', 'cXc', 'cXn', 'cYm', 'cYc', 'cYn', 'cPn', 'cAm', 'cAc', 'cAn']
    _SPECIES_LABELS = {'cLm': 'LHY mRNA', 'cLc': 'LHY protein in cytoplasm', 'cLn': 'LHY protein in nucleus', 'cTm': 'TOC1 mRNA', 'cTc': 'TOC1 protein  in cytoplasm', 'cTn': 'TOC1 protein in nucleus', 'cXm': 'X mRNA', 'cXc': 'X protein in cytoplasm', 'cXn': 'X protein in nucleus', 'cYm': 'Y mRNA', 'cYc': 'Y protein in the cytoplasm', 'cYn': 'Y protein in nucleus', 'cPn': 'light sensitive protein P', 'cAm': 'PPR7/9 mRNA', 'cAc': 'PPR7/9 protein in cytoplasm', 'cAn': 'PPR7/9 protein in nucleus'}
    _PARAMETER_INPUTS = {'light': ('light', 1.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `light`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'ppr7_9_mrna': ('cAm', 'native SBML value', 'PPR7/9 mRNA. Maps to SBML symbol `cAm`.'), 'ppr7_9_protein_in_nucleus': ('cAn', 'native SBML value', 'PPR7/9 protein in nucleus. Maps to SBML symbol `cAn`.'), 'ppr7_9_protein_in_cytoplasm': ('cAc', 'native SBML value', 'PPR7/9 protein in cytoplasm. Maps to SBML symbol `cAc`.'), 'toc1_protein_in_cytoplasm': ('cTc', 'native SBML value', 'TOC1 protein  in cytoplasm. Maps to SBML symbol `cTc`.'), 'x_protein_in_cytoplasm': ('cXc', 'native SBML value', 'X protein in cytoplasm. Maps to SBML symbol `cXc`.'), 'light_sensitive_protein_p': ('cPn', 'native SBML value', 'light sensitive protein P. Maps to SBML symbol `cPn`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000089.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
