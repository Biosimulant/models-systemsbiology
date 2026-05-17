# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Boehm2014 - isoform-specific dimerization of pSTAT5A and pSTAT5B."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Boehm2014IsoformSpecificDimerizationOfPstatBiomd0000000591Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Boehm2014 - isoform-specific dimerization of pSTAT5A and pSTAT5B."""

    _SBML_ID = 'BIOMD0000000591'
    _TITLE = 'Boehm2014 - isoform-specific dimerization of pSTAT5A and pSTAT5B'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['STAT5A', 'STAT5B', 'pApB', 'pApA', 'pBpB', 'nucpApA', 'nucpApB', 'nucpBpB']
    _SPECIES_LABELS = {'STAT5A': 'STAT5A', 'STAT5B': 'STAT5B', 'pApB': 'PApB', 'pApA': 'PApA', 'pBpB': 'PBpB', 'nucpApA': 'NucpApA', 'nucpApB': 'NucpApB', 'nucpBpB': 'NucpBpB'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stat5_b': ('STAT5B', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `STAT5B`.'), 'initial_stat5_a': ('STAT5A', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `STAT5A`.'), 'initial_p_bp_b': ('pBpB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pBpB`.'), 'initial_p_ap_b': ('pApB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pApB`.'), 'initial_p_ap_a': ('pApA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pApA`.'), 'initial_nucp_bp_b': ('nucpBpB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nucpBpB`.')}
    _HEADLINE_OUTPUTS = {'stat5_b': ('STAT5B', 'native SBML value', 'STAT5B. Maps to SBML symbol `STAT5B`.'), 'stat5_a': ('STAT5A', 'native SBML value', 'STAT5A. Maps to SBML symbol `STAT5A`.'), 'p_bp_b': ('pBpB', 'native SBML value', 'PBpB. Maps to SBML symbol `pBpB`.'), 'p_ap_b': ('pApB', 'native SBML value', 'PApB. Maps to SBML symbol `pApB`.'), 'p_ap_a': ('pApA', 'native SBML value', 'PApA. Maps to SBML symbol `pApA`.'), 'nucp_bp_b': ('nucpBpB', 'native SBML value', 'NucpBpB. Maps to SBML symbol `nucpBpB`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000591.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
