# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Salazar2009_PhotoperiodicRegulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Salazar2009PhotoperiodicregulationModel1005050000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Salazar2009_PhotoperiodicRegulation."""

    _SBML_ID = 'MODEL1005050000'
    _TITLE = 'Salazar2009_PhotoperiodicRegulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cCOp', 'cFTm', 'cLc', 'cLm', 'cLn', 'cPn', 'cTc', 'cTm', 'cTn', 'cXc', 'cXm', 'cXn', 'cYc', 'cYm', 'cYn']
    _SPECIES_LABELS = {'cCOp': 'cCOp', 'cFTm': 'cFTm', 'cLc': 'cLc', 'cLm': 'cLm', 'cLn': 'cLn', 'cPn': 'cPn', 'cTc': 'cTc', 'cTm': 'cTm', 'cTn': 'cTn', 'cXc': 'cXc', 'cXm': 'cXm', 'cXn': 'cXn', 'cYc': 'cYc', 'cYm': 'cYm', 'cYn': 'cYn'}
    _PARAMETER_INPUTS = {'light_amplitude': ('lightAmplitude', 1.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightAmplitude`.'), 'light_offset': ('lightOffset', 0.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `lightOffset`.'), 'twilight_period': ('twilightPeriod', 0.0416666667, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `twilightPeriod`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'c_tc': ('cTc', 'native SBML value', 'cTc. Maps to SBML symbol `cTc`.'), 'c_xc': ('cXc', 'native SBML value', 'cXc. Maps to SBML symbol `cXc`.'), 'c_pn': ('cPn', 'native SBML value', 'cPn. Maps to SBML symbol `cPn`.'), 'c_lm': ('cLm', 'native SBML value', 'cLm. Maps to SBML symbol `cLm`.'), 'c_tm': ('cTm', 'native SBML value', 'cTm. Maps to SBML symbol `cTm`.'), 'c_xn': ('cXn', 'native SBML value', 'cXn. Maps to SBML symbol `cXn`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1005050000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
