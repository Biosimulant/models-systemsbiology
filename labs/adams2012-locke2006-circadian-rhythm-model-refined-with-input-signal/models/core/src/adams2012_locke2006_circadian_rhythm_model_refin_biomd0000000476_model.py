# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Adams2012 - Locke2006 Circadian Rhythm model refined with Input Signal Light Function."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Adams2012Locke2006CircadianRhythmModelRefinBiomd0000000476Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Adams2012 - Locke2006 Circadian Rhythm model refined with Input Signal Light Function."""

    _SBML_ID = 'BIOMD0000000476'
    _TITLE = 'Adams2012 - Locke2006 Circadian Rhythm model refined with Input Signal Light Function'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cLm', 'cLc', 'cLn', 'cTm', 'cTc', 'cTn', 'cXm', 'cXc', 'cXn', 'cYm', 'cYc', 'cYn', 'cPn', 'cAm', 'cAc', 'cAn']
    _SPECIES_LABELS = {'cLm': 'LHY mRNA', 'cLc': 'LHY protein in cytoplasm', 'cLn': 'LHY protein in nucleus', 'cTm': 'TOC1 mRNA', 'cTc': 'TOC1 protein  in cytoplasm', 'cTn': 'TOC1 protein in nucleus', 'cXm': 'X mRNA', 'cXc': 'X protein in cytoplasm', 'cXn': 'X protein in nucleus', 'cYm': 'Y mRNA', 'cYc': 'Y protein in the cytoplasm', 'cYn': 'Y protein in nucleus', 'cPn': 'light sensitive protein P', 'cAm': 'PPR7/9 mRNA', 'cAc': 'PPR7/9 protein in cytoplasm', 'cAn': 'PPR7/9 protein in nucleus'}
    _PARAMETER_INPUTS = {'light_amplitude': ('lightAmplitude', 1.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightAmplitude`.'), 'light_offset': ('lightOffset', 0.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightOffset`.'), 'twilight_period': ('twilightPeriod', 0.0416666667, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `twilightPeriod`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'ppr7_9_mrna': ('cAm', 'native SBML value', 'PPR7/9 mRNA. Maps to SBML symbol `cAm`.'), 'toc1_protein_in_cytoplasm': ('cTc', 'native SBML value', 'TOC1 protein  in cytoplasm. Maps to SBML symbol `cTc`.'), 'x_protein_in_cytoplasm': ('cXc', 'native SBML value', 'X protein in cytoplasm. Maps to SBML symbol `cXc`.'), 'ppr7_9_protein_in_nucleus': ('cAn', 'native SBML value', 'PPR7/9 protein in nucleus. Maps to SBML symbol `cAn`.'), 'light_sensitive_protein_p': ('cPn', 'native SBML value', 'light sensitive protein P. Maps to SBML symbol `cPn`.'), 'ppr7_9_protein_in_cytoplasm': ('cAc', 'native SBML value', 'PPR7/9 protein in cytoplasm. Maps to SBML symbol `cAc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000476.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
