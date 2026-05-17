# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Edelstein1996 - EPSP ACh event."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Edelstein1996EpspAchEventBiomd0000000001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Edelstein1996 - EPSP ACh event."""

    _SBML_ID = 'BIOMD0000000001'
    _TITLE = 'Edelstein1996 - EPSP ACh event'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['BLL', 'IL', 'AL', 'A', 'BL', 'B', 'DLL', 'D', 'ILL', 'DL', 'I', 'ALL']
    _SPECIES_LABELS = {'BLL': 'BasalACh2', 'IL': 'IntermediateACh', 'AL': 'ActiveACh', 'A': 'Active', 'BL': 'BasalACh', 'B': 'Basal', 'DLL': 'DesensitisedACh2', 'D': 'Desensitised', 'ILL': 'IntermediateACh2', 'DL': 'DesensitisedACh', 'I': 'Intermediate', 'ALL': 'ActiveACh2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intermediate_a_ch2': ('ILL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ILL`.'), 'initial_intermediate_a_ch': ('IL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL`.'), 'initial_desensitised_a_ch2': ('DLL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DLL`.'), 'initial_desensitised_a_ch': ('DL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DL`.'), 'initial_basal_a_ch2': ('BLL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BLL`.'), 'initial_basal_a_ch': ('BL', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BL`.')}
    _HEADLINE_OUTPUTS = {'intermediate_a_ch2': ('ILL', 'native SBML value', 'IntermediateACh2. Maps to SBML symbol `ILL`.'), 'intermediate_a_ch': ('IL', 'native SBML value', 'IntermediateACh. Maps to SBML symbol `IL`.'), 'desensitised_a_ch2': ('DLL', 'native SBML value', 'DesensitisedACh2. Maps to SBML symbol `DLL`.'), 'desensitised_a_ch': ('DL', 'native SBML value', 'DesensitisedACh. Maps to SBML symbol `DL`.'), 'basal_a_ch2': ('BLL', 'native SBML value', 'BasalACh2. Maps to SBML symbol `BLL`.'), 'basal_a_ch': ('BL', 'native SBML value', 'BasalACh. Maps to SBML symbol `BL`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
