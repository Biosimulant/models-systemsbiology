# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Willems1991 - Simulating thrombin generation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Willems1991SimulatingThrombinGenerationModel1807240002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Willems1991 - Simulating thrombin generation."""

    _SBML_ID = 'MODEL1807240002'
    _TITLE = 'Willems1991 - Simulating thrombin generation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Xa', 'ATIII', 'Xa_ATIII', 'IIa', 'V', 'Va', 'APC', 'Va_inactive', 'Va_Xa', 'II', 'IIa_ATIII', 'C', 'APC_inactive', 'Fibrin', 'Fibrinogen', 'Hirudin', 'IIa_Hirudin']
    _SPECIES_LABELS = {'Xa': 'Xa', 'ATIII': 'ATIII', 'Xa_ATIII': 'Xa-ATIII', 'IIa': 'IIa', 'V': 'V', 'Va': 'Va', 'APC': 'APC', 'Va_inactive': 'Va_inactive', 'Va_Xa': 'Va-Xa', 'II': 'II', 'IIa_ATIII': 'IIa-ATIII', 'C': 'C', 'APC_inactive': 'APC_inactive', 'Fibrin': 'Fibrin', 'Fibrinogen': 'Fibrinogen', 'Hirudin': 'Hirudin', 'IIa_Hirudin': 'IIa-Hirudin'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_xa_atiii': ('Xa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`.'), 'initial_va_inactive': ('Va_inactive', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_inactive`.'), 'initial_va_xa': ('Va_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_Xa`.'), 'initial_i_ia_hirudin': ('IIa_Hirudin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_Hirudin`.'), 'initial_i_ia_atiii': ('IIa_ATIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_ATIII`.'), 'initial_apc_inactive': ('APC_inactive', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `APC_inactive`.')}
    _HEADLINE_OUTPUTS = {'xa_atiii': ('Xa_ATIII', 'native SBML value', 'Xa-ATIII. Maps to SBML symbol `Xa_ATIII`.'), 'va_inactive': ('Va_inactive', 'native SBML value', 'Va_inactive. Maps to SBML symbol `Va_inactive`.'), 'va_xa': ('Va_Xa', 'native SBML value', 'Va-Xa. Maps to SBML symbol `Va_Xa`.'), 'i_ia_hirudin': ('IIa_Hirudin', 'native SBML value', 'IIa-Hirudin. Maps to SBML symbol `IIa_Hirudin`.'), 'i_ia_atiii': ('IIa_ATIII', 'native SBML value', 'IIa-ATIII. Maps to SBML symbol `IIa_ATIII`.'), 'apc_inactive': ('APC_inactive', 'native SBML value', 'APC_inactive. Maps to SBML symbol `APC_inactive`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1807240002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
