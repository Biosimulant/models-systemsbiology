# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sachse2008_FibroblastInteractingMyocytes."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sachse2008FibroblastinteractingmyocytesModel7914759868Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sachse2008_FibroblastInteractingMyocytes."""

    _SBML_ID = 'MODEL7914759868'
    _TITLE = 'Sachse2008_FibroblastInteractingMyocytes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V_membrane', 'm_sodium_current_m_gate', 'h', 'j', 'd', 'f_11', 'f_12', 'Ca_inact', 'r', 's', 's_slow', 'r_ss', 's_ss', 'y', 'P_C1', 'P_O1', 'P_O2', 'P_C2', 'Ca_i', 'Na_i', 'K_i', 'Ca_ss_intracellular_ion_concentrations', 'Ca_JSR', 'Ca_NSR', 'VmReal', 'C0ShkrReal', 'C1ShkrReal', 'C2ShkrReal', 'C3ShkrReal', 'C4ShkrReal', 'OShkrReal']
    _SPECIES_LABELS = {'V_membrane': 'V Membrane', 'm_sodium_current_m_gate': 'M Sodium Current M Gate', 'h': 'H', 'j': 'J', 'd': 'D', 'f_11': 'F 11', 'f_12': 'F 12', 'Ca_inact': 'Ca Inact', 'r': 'R', 's': 'S', 's_slow': 'S Slow', 'r_ss': 'R Ss', 's_ss': 'S Ss', 'y': 'Y', 'P_C1': 'P C1', 'P_O1': 'P O1', 'P_O2': 'P O2', 'P_C2': 'P C2', 'Ca_i': 'Ca I', 'Na_i': 'Na I', 'K_i': 'K I', 'Ca_ss_intracellular_ion_concentrations': 'Ca Ss Intracellular Ion Concentrations', 'Ca_JSR': 'Ca JSR', 'Ca_NSR': 'Ca NSR', 'VmReal': 'VmReal', 'C0ShkrReal': 'C0ShkrReal', 'C1ShkrReal': 'C1ShkrReal', 'C2ShkrReal': 'C2ShkrReal', 'C3ShkrReal': 'C3ShkrReal', 'C4ShkrReal': 'C4ShkrReal', 'OShkrReal': 'OShkrReal'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vm_real': ('VmReal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VmReal`.'), 'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_s_ss': ('s_ss', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s_ss`.'), 'initial_s_slow': ('s_slow', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s_slow`.'), 'initial_r_ss': ('r_ss', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `r_ss`.'), 'initial_p_o2': ('P_O2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_O2`.')}
    _HEADLINE_OUTPUTS = {'vm_real': ('VmReal', 'native SBML value', 'VmReal. Maps to SBML symbol `VmReal`.'), 'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 's_ss': ('s_ss', 'native SBML value', 'S Ss. Maps to SBML symbol `s_ss`.'), 's_slow': ('s_slow', 'native SBML value', 'S Slow. Maps to SBML symbol `s_slow`.'), 'r_ss': ('r_ss', 'native SBML value', 'R Ss. Maps to SBML symbol `r_ss`.'), 'p_o2': ('P_O2', 'native SBML value', 'P O2. Maps to SBML symbol `P_O2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL7914759868.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
