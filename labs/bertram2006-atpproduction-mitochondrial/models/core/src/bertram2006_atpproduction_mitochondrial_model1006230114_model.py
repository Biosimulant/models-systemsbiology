# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bertram2006_ATPproduction_Mitochondrial."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram2006AtpproductionMitochondrialModel1006230114Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bertram2006_ATPproduction_Mitochondrial."""

    _SBML_ID = 'MODEL1006230114'
    _TITLE = 'Bertram2006_ATPproduction_Mitochondrial'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['NADHm', 'ADPm', 'PSIm', 'Cam', 'ADPc', 'FBP', 'c']
    _SPECIES_LABELS = {'NADHm': 'NADHm', 'ADPm': 'ADPm', 'PSIm': 'PSIm', 'Cam': 'Cam', 'ADPc': 'ADPc', 'FBP': 'FBP', 'c': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_cam': ('Cam', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cam`.'), 'initial_ps_im': ('PSIm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PSIm`.'), 'initial_nad_hm': ('NADHm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADHm`.'), 'initial_model_state_fbp': ('FBP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FBP`.'), 'initial_ad_pm': ('ADPm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADPm`.'), 'initial_ad_pc': ('ADPc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADPc`.')}
    _HEADLINE_OUTPUTS = {'cam': ('Cam', 'native SBML value', 'Cam. Maps to SBML symbol `Cam`.'), 'ps_im': ('PSIm', 'native SBML value', 'PSIm. Maps to SBML symbol `PSIm`.'), 'nad_hm': ('NADHm', 'native SBML value', 'NADHm. Maps to SBML symbol `NADHm`.'), 'fbp': ('FBP', 'native SBML value', 'FBP. Maps to SBML symbol `FBP`.'), 'ad_pm': ('ADPm', 'native SBML value', 'ADPm. Maps to SBML symbol `ADPm`.'), 'ad_pc': ('ADPc', 'native SBML value', 'ADPc. Maps to SBML symbol `ADPc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230114.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
