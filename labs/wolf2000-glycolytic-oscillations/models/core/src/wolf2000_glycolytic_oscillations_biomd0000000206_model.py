# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wolf2000_Glycolytic_Oscillations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wolf2000GlycolyticOscillationsBiomd0000000206Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wolf2000_Glycolytic_Oscillations."""

    _SBML_ID = 'BIOMD0000000206'
    _TITLE = 'Wolf2000_Glycolytic_Oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 'at', 's2', 's3', 'na', 's4', 's5', 's6', 's6o']
    _SPECIES_LABELS = {'s1': 'Glucose', 'at': 'ATP', 's2': 'F16P', 's3': 'Triose_Gly3Phos_DHAP', 'na': 'NAD', 's4': '3PG', 's5': 'Pyruvate', 's6': 'Acetaldehyde', 's6o': 'extracellular acetaldehyde'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pyruvate': ('s5', 8.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s5`.'), 'initial_f16_p': ('s2', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s2`.'), 'initial_model_state_atp': ('at', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `at`.'), 'initial_glucose': ('s1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_model_state_3_pg': ('s4', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s4`.'), 'initial_triose_gly3_phos_dhap': ('s3', 0.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s3`.')}
    _HEADLINE_OUTPUTS = {'pyruvate': ('s5', 'native SBML value', 'Pyruvate. Maps to SBML symbol `s5`.'), 'f16_p': ('s2', 'native SBML value', 'F16P. Maps to SBML symbol `s2`.'), 'atp': ('at', 'native SBML value', 'ATP. Maps to SBML symbol `at`.'), 'glucose': ('s1', 'native SBML value', 'Glucose. Maps to SBML symbol `s1`.'), 'model_state_3_pg': ('s4', 'native SBML value', '3PG. Maps to SBML symbol `s4`.'), 'triose_gly3_phos_dhap': ('s3', 'native SBML value', 'Triose_Gly3Phos_DHAP. Maps to SBML symbol `s3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000206.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
