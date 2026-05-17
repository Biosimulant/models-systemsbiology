# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Demir1999_SinoatrialNodeActivity_Heart."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Demir1999SinoatrialnodeactivityHeartModel0912940495Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Demir1999_SinoatrialNodeActivity_Heart."""

    _SBML_ID = 'MODEL0912940495'
    _TITLE = 'Demir1999_SinoatrialNodeActivity_Heart'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V_membrane', 'm', 'h1', 'h2', 'd_L', 'f_L', 'd_T', 'f_T', 'P_a', 'P_i', 'y', 'a', 'Ca_Calmod', 'Ca_Trop', 'Ca_Mg_Trop', 'Mg_Mg_Trop', 'Na_i', 'K_i', 'Ca_i', 'Na_c', 'K_c', 'Ca_c', 'Ca_Calse', 'F1', 'F2', 'F3', 'Ca_up', 'Ca_rel', 'cAMP']
    _SPECIES_LABELS = {'V_membrane': 'V Membrane', 'm': 'M', 'h1': 'H1', 'h2': 'H2', 'd_L': 'D L', 'f_L': 'F L', 'd_T': 'D T', 'f_T': 'F T', 'P_a': 'P A', 'P_i': 'P I', 'y': 'Y', 'a': 'A', 'Ca_Calmod': 'Ca Calmod', 'Ca_Trop': 'Ca Trop', 'Ca_Mg_Trop': 'Ca Mg Trop', 'Mg_Mg_Trop': 'Mg Mg Trop', 'Na_i': 'Na I', 'K_i': 'K I', 'Ca_i': 'Ca I', 'Na_c': 'Na C', 'K_c': 'K C', 'Ca_c': 'Ca C', 'Ca_Calse': 'Ca Calse', 'F1': 'F1', 'F2': 'F2', 'F3': 'F3', 'Ca_up': 'Ca Up', 'Ca_rel': 'Ca Rel', 'cAMP': 'CAMP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_model_state_p_i': ('P_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_i`.'), 'initial_model_state_p_a': ('P_a', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_a`.'), 'initial_na_i': ('Na_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Na_i`.'), 'initial_na_c': ('Na_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Na_c`.'), 'initial_mg_mg_trop': ('Mg_Mg_Trop', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mg_Mg_Trop`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 'p_i': ('P_i', 'native SBML value', 'P I. Maps to SBML symbol `P_i`.'), 'p_a': ('P_a', 'native SBML value', 'P A. Maps to SBML symbol `P_a`.'), 'na_i': ('Na_i', 'native SBML value', 'Na I. Maps to SBML symbol `Na_i`.'), 'na_c': ('Na_c', 'native SBML value', 'Na C. Maps to SBML symbol `Na_c`.'), 'mg_mg_trop': ('Mg_Mg_Trop', 'native SBML value', 'Mg Mg Trop. Maps to SBML symbol `Mg_Mg_Trop`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912940495.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
