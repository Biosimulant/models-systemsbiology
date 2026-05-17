# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Simon2019 - NIK-dependent p100 processing into p52 and IkBd degradation, Michaelis-Menten, SBML 2v4."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Simon2019NikDependentP100ProcessingIntoP52Biomd0000000869Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Simon2019 - NIK-dependent p100 processing into p52 and IkBd degradation, Michaelis-Menten, SBML 2v4."""

    _SBML_ID = 'BIOMD0000000869'
    _TITLE = 'Simon2019 - NIK-dependent p100 processing into p52 and IkBd degradation, Michaelis-Menten, SBML 2v4'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p100t', 'p100', 'p52', 'NIK', 'IkBd']
    _SPECIES_LABELS = {'p100t': 'p100t', 'p100': 'p100', 'p52': 'p52', 'NIK': 'NIK', 'IkBd': 'IkBd'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p100t': ('p100t', 2.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p100t`.'), 'initial_model_state_p52': ('p52', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p52`.'), 'initial_p100': ('p100', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p100`.'), 'initial_model_state_nik': ('NIK', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NIK`.'), 'initial_ik_bd': ('IkBd', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkBd`.')}
    _HEADLINE_OUTPUTS = {'p100t': ('p100t', 'native SBML value', 'p100t. Maps to SBML symbol `p100t`.'), 'p52': ('p52', 'native SBML value', 'p52. Maps to SBML symbol `p52`.'), 'p100': ('p100', 'native SBML value', 'p100. Maps to SBML symbol `p100`.'), 'nik': ('NIK', 'native SBML value', 'NIK. Maps to SBML symbol `NIK`.'), 'ik_bd': ('IkBd', 'native SBML value', 'IkBd. Maps to SBML symbol `IkBd`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000869.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
