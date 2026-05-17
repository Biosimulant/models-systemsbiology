# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Hong2009_CircadianClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hong2009CircadianclockBiomd0000000216Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Hong2009_CircadianClock."""

    _SBML_ID = 'BIOMD0000000216'
    _TITLE = 'Hong2009_CircadianClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'TF', 'CP', 'CP2', 'IC', 'CPtot']
    _SPECIES_LABELS = {'M': 'M', 'TF': 'TF', 'CP': 'CP', 'CP2': 'CP2', 'IC': 'IC', 'CPtot': 'CPtot'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ic': ('IC', 0.37, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IC`.'), 'initial_model_state_tf': ('TF', 0.13, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF`.'), 'initial_model_state_cp2': ('CP2', 0.046, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CP2`.'), 'initial_model_state_cp': ('CP', 0.037, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CP`.'), 'initial_c_ptot': ('CPtot', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CPtot`.'), 'initial_model_state_m': ('M', 1.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'model_state_ic': ('IC', 'native SBML value', 'IC. Maps to SBML symbol `IC`.'), 'model_state_tf': ('TF', 'native SBML value', 'TF. Maps to SBML symbol `TF`.'), 'cp2': ('CP2', 'native SBML value', 'CP2. Maps to SBML symbol `CP2`.'), 'model_state_cp': ('CP', 'native SBML value', 'CP. Maps to SBML symbol `CP`.'), 'c_ptot': ('CPtot', 'native SBML value', 'CPtot. Maps to SBML symbol `CPtot`.'), 'model_state_m': ('M', 'native SBML value', 'M. Maps to SBML symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000216.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
