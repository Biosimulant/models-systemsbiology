# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Locke2005 - Circadian Clock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Locke2005CircadianClockBiomd0000000055Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Locke2005 - Circadian Clock."""

    _SBML_ID = 'BIOMD0000000055'
    _TITLE = 'Locke2005 - Circadian Clock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cLm', 'cLc', 'cLn', 'cTm', 'cTc', 'cTn', 'cXm', 'cXc', 'cXn', 'cYm', 'cYc', 'cYn', 'cPn']
    _SPECIES_LABELS = {'cLm': 'LHY mRNA', 'cLc': 'LHY protein in cytoplasm', 'cLn': 'LHY protein in nucleus', 'cTm': 'TOC1 mRNA', 'cTc': 'TOC1 protein in cytoplasm', 'cTn': 'TOC1 protein in nucleus', 'cXm': 'X mRNA', 'cXc': 'X protein in cytoplasm', 'cXn': 'X protein in nucleus', 'cYm': 'Y mRNA', 'cYc': 'Y protein in cytoplasm', 'cYn': 'Y protein in nucleus', 'cPn': 'light sensitive protein P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_toc1_protein_in_cytoplasm': ('cTc', 8.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTc`.'), 'initial_x_protein_in_cytoplasm': ('cXc', 1.34, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXc`.'), 'initial_light_sensitive_protein_p': ('cPn', 0.835, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cPn`.'), 'initial_lhy_mrna': ('cLm', 0.539, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cLm`.'), 'initial_toc1_mrna': ('cTm', 0.456, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTm`.'), 'initial_x_protein_in_nucleus': ('cXn', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXn`.')}
    _HEADLINE_OUTPUTS = {'toc1_protein_in_cytoplasm': ('cTc', 'native SBML value', 'TOC1 protein in cytoplasm. Maps to SBML symbol `cTc`.'), 'x_protein_in_cytoplasm': ('cXc', 'native SBML value', 'X protein in cytoplasm. Maps to SBML symbol `cXc`.'), 'light_sensitive_protein_p': ('cPn', 'native SBML value', 'light sensitive protein P. Maps to SBML symbol `cPn`.'), 'lhy_mrna': ('cLm', 'native SBML value', 'LHY mRNA. Maps to SBML symbol `cLm`.'), 'toc1_mrna': ('cTm', 'native SBML value', 'TOC1 mRNA. Maps to SBML symbol `cTm`.'), 'x_protein_in_nucleus': ('cXn', 'native SBML value', 'X protein in nucleus. Maps to SBML symbol `cXn`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000055.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
