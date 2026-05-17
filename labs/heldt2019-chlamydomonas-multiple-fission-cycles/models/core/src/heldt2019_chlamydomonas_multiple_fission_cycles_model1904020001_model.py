# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Heldt2019 - Chlamydomonas multiple-fission cycles."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heldt2019ChlamydomonasMultipleFissionCyclesModel1904020001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Heldt2019 - Chlamydomonas multiple-fission cycles."""

    _SBML_ID = 'MODEL1904020001'
    _TITLE = 'Heldt2019 - Chlamydomonas multiple-fission cycles'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['SK', 'TF', 'IN', 'INTF', 'IP', 'S', 'M', 'A', 'FK', 'TFt', 'INt']
    _SPECIES_LABELS = {'SK': 'SK', 'TF': 'TF', 'IN': 'IN', 'INTF': 'INTF', 'IP': 'IP', 'S': 'S', 'M': 'M', 'A': 'A', 'FK': 'FK', 'TFt': 'TFt', 'INt': 'INt'}
    _PARAMETER_INPUTS = {'light': ('Light', 1.0, 'unit_0', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Light`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'i_nt': ('INt', 'native SBML value', 'INt. Maps to SBML symbol `INt`.'), 'model_state_ip': ('IP', 'native SBML value', 'IP. Maps to SBML symbol `IP`.'), 'in_value': ('IN', 'native SBML value', 'IN. Maps to SBML symbol `IN`.'), 't_ft': ('TFt', 'native SBML value', 'TFt. Maps to SBML symbol `TFt`.'), 'model_state_sk': ('SK', 'native SBML value', 'SK. Maps to SBML symbol `SK`.'), 'intf': ('INTF', 'native SBML value', 'INTF. Maps to SBML symbol `INTF`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1904020001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
