# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Qiao2004_ThrombinGeneration."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Qiao2004ThrombingenerationModel1108260015Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Qiao2004_ThrombinGeneration."""

    _SBML_ID = 'MODEL1108260015'
    _TITLE = 'Qiao2004_ThrombinGeneration'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IXa', 'VIIIa', 'Xa', 'Va', 'APC', 'IIa']
    _SPECIES_LABELS = {'IXa': 'IXa', 'VIIIa': 'VIIIa', 'Xa': 'Xa', 'Va': 'Va', 'APC': 'APC', 'IIa': 'IIa'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_xa': ('Xa', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa`.'), 'initial_model_state_va': ('Va', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va`.'), 'initial_vii_ia': ('VIIIa', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VIIIa`.'), 'initial_i_xa': ('IXa', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IXa`.'), 'initial_i_ia': ('IIa', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa`.'), 'initial_model_state_apc': ('APC', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `APC`.')}
    _HEADLINE_OUTPUTS = {'model_state_xa': ('Xa', 'native SBML value', 'Xa. Maps to SBML symbol `Xa`.'), 'model_state_va': ('Va', 'native SBML value', 'Va. Maps to SBML symbol `Va`.'), 'vii_ia': ('VIIIa', 'native SBML value', 'VIIIa. Maps to SBML symbol `VIIIa`.'), 'i_xa': ('IXa', 'native SBML value', 'IXa. Maps to SBML symbol `IXa`.'), 'i_ia': ('IIa', 'native SBML value', 'IIa. Maps to SBML symbol `IIa`.'), 'apc': ('APC', 'native SBML value', 'APC. Maps to SBML symbol `APC`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1108260015.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
