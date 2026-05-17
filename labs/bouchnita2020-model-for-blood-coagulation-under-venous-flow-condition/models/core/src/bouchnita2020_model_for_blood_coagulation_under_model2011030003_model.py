# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bouchnita2020 - Model for blood coagulation under venous flow condition."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bouchnita2020ModelForBloodCoagulationUnderModel2011030003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bouchnita2020 - Model for blood coagulation under venous flow condition."""

    _SBML_ID = 'MODEL2011030003'
    _TITLE = 'Bouchnita2020 - Model for blood coagulation under venous flow condition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Xa', 'II', 'IIa', 'ATIII', 'TF', 'VIIa']
    _SPECIES_LABELS = {'Xa': 'Xa', 'II': 'II', 'IIa': 'IIa', 'ATIII': 'ATIII', 'TF': 'TF', 'VIIa': 'VIIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atiii': ('ATIII', 3000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATIII`.'), 'initial_model_state_ii': ('II', 950.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II`.'), 'initial_vi_ia': ('VIIa', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIa`.'), 'initial_model_state_tf': ('TF', 0.0005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF`.'), 'initial_model_state_xa': ('Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa`.'), 'initial_i_ia': ('IIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa`.')}
    _HEADLINE_OUTPUTS = {'atiii': ('ATIII', 'native SBML value', 'ATIII. Maps to SBML symbol `ATIII`.'), 'model_state_ii': ('II', 'native SBML value', 'II. Maps to SBML symbol `II`.'), 'vi_ia': ('VIIa', 'native SBML value', 'VIIa. Maps to SBML symbol `VIIa`.'), 'model_state_tf': ('TF', 'native SBML value', 'TF. Maps to SBML symbol `TF`.'), 'model_state_xa': ('Xa', 'native SBML value', 'Xa. Maps to SBML symbol `Xa`.'), 'i_ia': ('IIa', 'native SBML value', 'IIa. Maps to SBML symbol `IIa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2011030003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
