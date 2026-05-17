# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Troein2011_ClockCircuit_OstreococcusTauri."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Troein2011ClockcircuitOstreococcustauriBiomd0000000350Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Troein2011_ClockCircuit_OstreococcusTauri."""

    _SBML_ID = 'BIOMD0000000350'
    _TITLE = 'Troein2011_ClockCircuit_OstreococcusTauri'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['acc', 'toc1_mrna', 'toc1_1', 'toc1_2', 'cca1_mrna', 'cca1_c', 'cca1_n', 'toc1luc_mrna', 'toc1luc_1', 'toc1luc_2', 'cca1luc_mrna', 'cca1luc', 'luc_mrna', 'luc']
    _SPECIES_LABELS = {'acc': 'acc', 'toc1_mrna': 'toc1_mrna', 'toc1_1': 'toc1_1', 'toc1_2': 'toc1_2', 'cca1_mrna': 'cca1_mrna', 'cca1_c': 'cca1_c', 'cca1_n': 'cca1_n', 'toc1luc_mrna': 'toc1luc_mrna', 'toc1luc_1': 'toc1luc_1', 'toc1luc_2': 'toc1luc_2', 'cca1luc_mrna': 'cca1luc_mrna', 'cca1luc': 'cca1luc', 'luc_mrna': 'luc_mrna', 'luc': 'luc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cca1_mrna': ('cca1_mrna', 0.104555645465821, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cca1_mrna`.'), 'initial_toc1_mrna': ('toc1_mrna', 0.0385665277682963, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `toc1_mrna`.'), 'initial_toc1luc_mrna': ('toc1luc_mrna', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `toc1luc_mrna`.'), 'initial_luc_mrna': ('luc_mrna', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `luc_mrna`.'), 'initial_cca1luc_mrna': ('cca1luc_mrna', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cca1luc_mrna`.'), 'initial_cca1_n': ('cca1_n', 3.07283764226433, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cca1_n`.')}
    _HEADLINE_OUTPUTS = {'cca1_mrna': ('cca1_mrna', 'native SBML value', 'cca1_mrna. Maps to SBML symbol `cca1_mrna`.'), 'toc1_mrna': ('toc1_mrna', 'native SBML value', 'toc1_mrna. Maps to SBML symbol `toc1_mrna`.'), 'toc1luc_mrna': ('toc1luc_mrna', 'native SBML value', 'toc1luc_mrna. Maps to SBML symbol `toc1luc_mrna`.'), 'luc_mrna': ('luc_mrna', 'native SBML value', 'luc_mrna. Maps to SBML symbol `luc_mrna`.'), 'cca1luc_mrna': ('cca1luc_mrna', 'native SBML value', 'cca1luc_mrna. Maps to SBML symbol `cca1luc_mrna`.'), 'cca1_n': ('cca1_n', 'native SBML value', 'cca1_n. Maps to SBML symbol `cca1_n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000350.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
