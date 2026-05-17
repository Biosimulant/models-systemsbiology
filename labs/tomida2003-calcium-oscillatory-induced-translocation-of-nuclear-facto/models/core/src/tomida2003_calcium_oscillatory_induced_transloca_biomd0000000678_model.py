# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tomida2003 - Calcium Oscillatory-induced translocation of nuclear factor of activated T cells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tomida2003CalciumOscillatoryInducedTranslocaBiomd0000000678Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tomida2003 - Calcium Oscillatory-induced translocation of nuclear factor of activated T cells."""

    _SBML_ID = 'BIOMD0000000678'
    _TITLE = 'Tomida2003 - Calcium Oscillatory-induced translocation of nuclear factor of activated T cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NFAT_phosphorylated', 'NFAT_dephosphorylated', 'NFAT_transported', 'stimulus']
    _SPECIES_LABELS = {'NFAT_phosphorylated': 'NFAT_phosphorylated', 'NFAT_dephosphorylated': 'NFAT_dephosphorylated', 'NFAT_transported': 'NFAT_transported', 'stimulus': 'stimulus'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stimulus': ('stimulus', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `stimulus`.'), 'initial_nfat_phosphorylated': ('NFAT_phosphorylated', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFAT_phosphorylated`.'), 'initial_nfat_transported': ('NFAT_transported', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFAT_transported`.'), 'initial_nfat_dephosphorylated': ('NFAT_dephosphorylated', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFAT_dephosphorylated`.')}
    _HEADLINE_OUTPUTS = {'stimulus': ('stimulus', 'native SBML value', 'stimulus. Maps to SBML symbol `stimulus`.'), 'nfat_phosphorylated': ('NFAT_phosphorylated', 'native SBML value', 'NFAT_phosphorylated. Maps to SBML symbol `NFAT_phosphorylated`.'), 'nfat_transported': ('NFAT_transported', 'native SBML value', 'NFAT_transported. Maps to SBML symbol `NFAT_transported`.'), 'nfat_dephosphorylated': ('NFAT_dephosphorylated', 'native SBML value', 'NFAT_dephosphorylated. Maps to SBML symbol `NFAT_dephosphorylated`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000678.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
