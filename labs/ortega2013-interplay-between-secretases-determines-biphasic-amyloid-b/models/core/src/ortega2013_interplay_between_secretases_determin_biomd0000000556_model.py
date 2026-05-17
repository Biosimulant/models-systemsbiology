# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ortega2013 - Interplay between secretases determines biphasic amyloid-beta level."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ortega2013InterplayBetweenSecretasesDeterminBiomd0000000556Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ortega2013 - Interplay between secretases determines biphasic amyloid-beta level."""

    _SBML_ID = 'BIOMD0000000556'
    _TITLE = 'Ortega2013 - Interplay between secretases determines biphasic amyloid-beta level'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['APP', 'C83', 'C99', 'AB', 'X', 'p3']
    _SPECIES_LABELS = {'APP': 'APP', 'C83': 'C83', 'C99': 'C99', 'AB': 'AB', 'X': 'X', 'p3': 'p3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_p3': ('p3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p3`.'), 'initial_model_state_c99': ('C99', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C99`.'), 'initial_model_state_c83': ('C83', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C83`.'), 'initial_model_state_app': ('APP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `APP`.'), 'initial_model_state_ab': ('AB', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AB`.'), 'initial_model_state_x': ('X', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.')}
    _HEADLINE_OUTPUTS = {'model_state_p3': ('p3', 'native SBML value', 'p3. Maps to SBML symbol `p3`.'), 'c99': ('C99', 'native SBML value', 'C99. Maps to SBML symbol `C99`.'), 'c83': ('C83', 'native SBML value', 'C83. Maps to SBML symbol `C83`.'), 'app': ('APP', 'native SBML value', 'APP. Maps to SBML symbol `APP`.'), 'model_state_ab': ('AB', 'native SBML value', 'AB. Maps to SBML symbol `AB`.'), 'model_state_x': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000556.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
