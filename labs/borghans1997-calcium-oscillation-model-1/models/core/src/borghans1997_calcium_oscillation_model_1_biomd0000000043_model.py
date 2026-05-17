# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Borghans1997 - Calcium Oscillation - Model 1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Borghans1997CalciumOscillationModel1Biomd0000000043Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Borghans1997 - Calcium Oscillation - Model 1."""

    _SBML_ID = 'BIOMD0000000043'
    _TITLE = 'Borghans1997 - Calcium Oscillation - Model 1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EC', 'Z', 'Rho', 'Y', 'Fraction_Inactive_Channels']
    _SPECIES_LABELS = {'EC': 'EC', 'Z': 'Z', 'Rho': 'Rho', 'Y': 'Y', 'Fraction_Inactive_Channels': 'Fraction Inactive Channels'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_rho': ('Rho', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rho`.'), 'initial_model_state_ec': ('EC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`.'), 'initial_model_state_y': ('Y', 0.36, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_model_state_z': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.'), 'initial_fraction_inactive_channels': ('Fraction_Inactive_Channels', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fraction_Inactive_Channels`.')}
    _HEADLINE_OUTPUTS = {'rho': ('Rho', 'native SBML value', 'Rho. Maps to SBML symbol `Rho`.'), 'model_state_ec': ('EC', 'native SBML value', 'EC. Maps to SBML symbol `EC`.'), 'model_state_y': ('Y', 'native SBML value', 'Y. Maps to SBML symbol `Y`.'), 'model_state_z': ('Z', 'native SBML value', 'Z. Maps to SBML symbol `Z`.'), 'fraction_inactive_channels': ('Fraction_Inactive_Channels', 'native SBML value', 'Fraction Inactive Channels. Maps to SBML symbol `Fraction_Inactive_Channels`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000043.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
