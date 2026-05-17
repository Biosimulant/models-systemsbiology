# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nagashima2002 - Simulating blood coagulation inhibitory effects."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nagashima2002SimulatingBloodCoagulationInhibBiomd0000000747Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nagashima2002 - Simulating blood coagulation inhibitory effects."""

    _SBML_ID = 'BIOMD0000000747'
    _TITLE = 'Nagashima2002 - Simulating blood coagulation inhibitory effects'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IX', 'TF_VIIa_IX', 'TF_VIIa', 'IXa', 'TF_VIIa_X', 'X', 'Xa', 'VIII', 'Xa_VIII', 'VIIIa', 'IIa', 'IIa_VIII', 'VIIIa_IXa', 'VIIIa_IXa_X', 'V', 'Xa_V', 'Va', 'IIa_V', 'Va_Xa', 'II', 'Va_Xa_II', 'Fibrinogen', 'Fibrinogen_IIa', 'Fibrin', 'VIIIa_inact', 'IXa_inact', 'Xa_inact', 'IIa_inact', 'Xa_Xa_Inhibitor', 'Xa_Inhibitor', 'Va_Xa_Xa_Inhibitor', 'IIa_IIa_Inhibitor', 'IIa_Inhibitor']
    _SPECIES_LABELS = {'IX': 'IX', 'TF_VIIa_IX': 'TF:VIIa:IX', 'TF_VIIa': 'TF:VIIa', 'IXa': 'IXa', 'TF_VIIa_X': 'TF:VIIa:X', 'X': 'X', 'Xa': 'Xa', 'VIII': 'VIII', 'Xa_VIII': 'Xa:VIII', 'VIIIa': 'VIIIa', 'IIa': 'IIa', 'IIa_VIII': 'IIa:VIII', 'VIIIa_IXa': 'VIIIa:IXa', 'VIIIa_IXa_X': 'VIIIa:IXa:X', 'V': 'V', 'Xa_V': 'Xa:V', 'Va': 'Va', 'IIa_V': 'IIa:V', 'Va_Xa': 'Va:Xa', 'II': 'II', 'Va_Xa_II': 'Va:Xa:II', 'Fibrinogen': 'Fibrinogen', 'Fibrinogen_IIa': 'Fibrinogen:IIa', 'Fibrin': 'Fibrin', 'VIIIa_inact': 'VIIIa_inact', 'IXa_inact': 'IXa_inact', 'Xa_inact': 'Xa_inact', 'IIa_inact': 'IIa_inact', 'Xa_Xa_Inhibitor': 'Xa:Xa_Inhibitor', 'Xa_Inhibitor': 'Xa_Inhibitor', 'Va_Xa_Xa_Inhibitor': 'Va:Xa:Xa_Inhibitor', 'IIa_IIa_Inhibitor': 'IIa:IIa_Inhibitor', 'IIa_Inhibitor': 'IIa_Inhibitor'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tf_vi_ia': ('TF_VIIa', 0.005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF_VIIa`.'), 'initial_xa_inact': ('Xa_inact', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_inact`.'), 'initial_xa_inhibitor': ('Xa_Inhibitor', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Inhibitor`.'), 'initial_xa_xa_inhibitor': ('Xa_Xa_Inhibitor', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Xa_Inhibitor`.'), 'initial_xa_viii': ('Xa_VIII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_VIII`.'), 'initial_xa_v': ('Xa_V', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_V`.')}
    _HEADLINE_OUTPUTS = {'tf_vi_ia': ('TF_VIIa', 'native SBML value', 'TF:VIIa. Maps to SBML symbol `TF_VIIa`.'), 'xa_inact': ('Xa_inact', 'native SBML value', 'Xa_inact. Maps to SBML symbol `Xa_inact`.'), 'xa_inhibitor': ('Xa_Inhibitor', 'native SBML value', 'Xa_Inhibitor. Maps to SBML symbol `Xa_Inhibitor`.'), 'xa_xa_inhibitor': ('Xa_Xa_Inhibitor', 'native SBML value', 'Xa:Xa_Inhibitor. Maps to SBML symbol `Xa_Xa_Inhibitor`.'), 'xa_viii': ('Xa_VIII', 'native SBML value', 'Xa:VIII. Maps to SBML symbol `Xa_VIII`.'), 'xa_v': ('Xa_V', 'native SBML value', 'Xa:V. Maps to SBML symbol `Xa_V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000747.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
