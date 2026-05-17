# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Gilbert2008_ElectrochemicalBiosensor."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gilbert2008ElectrochemicalbiosensorModel1173105855Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Gilbert2008_ElectrochemicalBiosensor."""

    _SBML_ID = 'MODEL1173105855'
    _TITLE = 'Gilbert2008_ElectrochemicalBiosensor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['TF', 'TFS', 'PhzMS', 'PYO']
    _SPECIES_LABELS = {'TF': 'TF', 'TFS': 'TFS', 'PhzMS': 'PhzMS', 'PYO': 'PYO'}
    _PARAMETER_INPUTS = {'feedback_on': ('feedbackOn', 1.0, 'dimensionless', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `feedbackOn`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'tfs': ('TFS', 'native SBML value', 'TFS. Maps to SBML symbol `TFS`.'), 'model_state_tf': ('TF', 'native SBML value', 'TF. Maps to SBML symbol `TF`.'), 'phz_ms': ('PhzMS', 'native SBML value', 'PhzMS. Maps to SBML symbol `PhzMS`.'), 'pyo': ('PYO', 'native SBML value', 'PYO. Maps to SBML symbol `PYO`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1173105855.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
