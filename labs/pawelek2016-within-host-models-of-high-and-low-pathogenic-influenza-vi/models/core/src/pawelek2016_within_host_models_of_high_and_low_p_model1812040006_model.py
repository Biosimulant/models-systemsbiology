# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Pawelek2016 - Within-Host Models of High and Low Pathogenic Influenza Virus Infections."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pawelek2016WithinHostModelsOfHighAndLowPModel1812040006Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Pawelek2016 - Within-Host Models of High and Low Pathogenic Influenza Virus Infections."""

    _SBML_ID = 'MODEL1812040006'
    _TITLE = 'Pawelek2016 - Within-Host Models of High and Low Pathogenic Influenza Virus Infections'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'V', 'M_R', 'M_A', 'M_I', 'A']
    _SPECIES_LABELS = {'T': 'T', 'I': 'I', 'V': 'V', 'M_R': 'M_R', 'M_A': 'M_A', 'M_I': 'M_I', 'A': 'A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_m_r': ('M_R', 12718130.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_R`.'), 'initial_model_state_m_i': ('M_I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_I`.'), 'initial_model_state_m_a': ('M_A', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_A`.'), 'initial_model_state_t': ('T', 7000000000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`.'), 'initial_model_state_v': ('V', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`.'), 'initial_model_state_i': ('I', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'m_r': ('M_R', 'native SBML value', 'M_R. Maps to SBML symbol `M_R`.'), 'm_i': ('M_I', 'native SBML value', 'M_I. Maps to SBML symbol `M_I`.'), 'm_a': ('M_A', 'native SBML value', 'M_A. Maps to SBML symbol `M_A`.'), 'model_state_t': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'model_state_v': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.'), 'model_state_i': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812040006.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
