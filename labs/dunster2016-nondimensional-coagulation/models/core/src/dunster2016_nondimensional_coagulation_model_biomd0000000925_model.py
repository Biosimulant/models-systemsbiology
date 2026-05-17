# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Dunster2016 - Nondimensional Coagulation Model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dunster2016NondimensionalCoagulationModelBiomd0000000925Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Dunster2016 - Nondimensional Coagulation Model."""

    _SBML_ID = 'BIOMD0000000925'
    _TITLE = 'Dunster2016 - Nondimensional Coagulation Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Factor_Xa', 'Thrombin__IIa', 'Factor_V', 'Factor_Va', 'APC', 'VInactive', 'Prothrombinase__Va_Xa', 'Prothrombin__II', 'Xa_L', 'Va_Xa_L', 'Protein_C', 'Inactive_protein_C', 'Fibrin', 'Fibrinogen', 'Inactive_Thrombin', 'Factor_Xi']
    _SPECIES_LABELS = {'Factor_Xa': 'Factor Xa', 'Thrombin__IIa': 'Thrombin (IIa)', 'Factor_V': 'Factor V', 'Factor_Va': 'Factor Va', 'APC': 'APC', 'VInactive': 'VInactive', 'Prothrombinase__Va_Xa': 'Prothrombinase (Va:Xa)', 'Prothrombin__II': 'Prothrombin (II)', 'Xa_L': 'Xa:L', 'Va_Xa_L': 'Va:Xa:L', 'Protein_C': 'Protein C', 'Inactive_protein_C': 'Inactive protein C', 'Fibrin': 'Fibrin', 'Fibrinogen': 'Fibrinogen', 'Inactive_Thrombin': 'Inactive Thrombin', 'Factor_Xi': 'Factor Xi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_prothrombin_ii': ('Prothrombin__II', 17.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Prothrombin__II`.'), 'initial_xa_l': ('Xa_L', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_L`.'), 'initial_va_xa_l': ('Va_Xa_L', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_Xa_L`.'), 'initial_thrombin_i_ia': ('Thrombin__IIa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Thrombin__IIa`.'), 'initial_prothrombinase_va_xa': ('Prothrombinase__Va_Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Prothrombinase__Va_Xa`.'), 'initial_inactive_protein_c': ('Inactive_protein_C', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Inactive_protein_C`.')}
    _HEADLINE_OUTPUTS = {'prothrombin_ii': ('Prothrombin__II', 'native SBML value', 'Prothrombin (II). Maps to SBML symbol `Prothrombin__II`.'), 'xa_l': ('Xa_L', 'native SBML value', 'Xa:L. Maps to SBML symbol `Xa_L`.'), 'va_xa_l': ('Va_Xa_L', 'native SBML value', 'Va:Xa:L. Maps to SBML symbol `Va_Xa_L`.'), 'thrombin_i_ia': ('Thrombin__IIa', 'native SBML value', 'Thrombin (IIa). Maps to SBML symbol `Thrombin__IIa`.'), 'prothrombinase_va_xa': ('Prothrombinase__Va_Xa', 'native SBML value', 'Prothrombinase (Va:Xa). Maps to SBML symbol `Prothrombinase__Va_Xa`.'), 'inactive_protein_c': ('Inactive_protein_C', 'native SBML value', 'Inactive protein C. Maps to SBML symbol `Inactive_protein_C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000925.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
