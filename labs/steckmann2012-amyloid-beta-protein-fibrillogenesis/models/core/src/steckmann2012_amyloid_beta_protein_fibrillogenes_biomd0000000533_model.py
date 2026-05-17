# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Steckmann2012 - Amyloid beta-protein fibrillogenesis (kinetics of secondary structure conversion)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Steckmann2012AmyloidBetaProteinFibrillogenesBiomd0000000533Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Steckmann2012 - Amyloid beta-protein fibrillogenesis (kinetics of secondary structure conversion)."""

    _SBML_ID = 'BIOMD0000000533'
    _TITLE = 'Steckmann2012 - Amyloid beta-protein fibrillogenesis (kinetics of secondary structure conversion)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RCT0', 'alpha', 'BN1', 'BN2', 'BN3', 'BN4', 'BTX', 'BM', 'RCT1', 'RC', 'beta']
    _SPECIES_LABELS = {'RCT0': 'RCT0', 'alpha': 'alpha', 'BN1': 'BN1', 'BN2': 'BN2', 'BN3': 'BN3', 'BN4': 'BN4', 'BTX': 'BTX', 'BM': 'BM', 'RCT1': 'RCT1', 'RC': 'RC', 'beta': 'beta'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_beta': ('beta', 11.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `beta`.'), 'initial_alpha': ('alpha', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha`.'), 'initial_rct0': ('RCT0', 88.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RCT0`.'), 'initial_model_state_rc': ('RC', 88.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RC`.'), 'initial_model_state_bn1': ('BN1', 11.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `BN1`.'), 'initial_rct1': ('RCT1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RCT1`.')}
    _HEADLINE_OUTPUTS = {'beta': ('beta', 'native SBML value', 'beta. Maps to SBML symbol `beta`.'), 'alpha': ('alpha', 'native SBML value', 'alpha. Maps to SBML symbol `alpha`.'), 'rct0': ('RCT0', 'native SBML value', 'RCT0. Maps to SBML symbol `RCT0`.'), 'model_state_rc': ('RC', 'native SBML value', 'RC. Maps to SBML symbol `RC`.'), 'bn1': ('BN1', 'native SBML value', 'BN1. Maps to SBML symbol `BN1`.'), 'rct1': ('RCT1', 'native SBML value', 'RCT1. Maps to SBML symbol `RCT1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000533.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
