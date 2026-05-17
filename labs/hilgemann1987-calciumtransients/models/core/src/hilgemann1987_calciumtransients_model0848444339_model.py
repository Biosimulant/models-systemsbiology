# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Hilgemann1987_CalciumTransients."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hilgemann1987CalciumtransientsModel0848444339Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Hilgemann1987_CalciumTransients."""

    _SBML_ID = 'MODEL0848444339'
    _TITLE = 'Hilgemann1987_CalciumTransients'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['V_membrane', 'm', 'h', 'd', 'f_Ca', 'ActFrac', 'ProdFrac', 'Na_i', 'Ca_o', 'K_i', 'Ca_i_intracellular_calcium_concentration', 'Ca_up', 'Ca_rel', 'Ca_Calmod', 'Ca_Trop']
    _SPECIES_LABELS = {'V_membrane': 'V Membrane', 'm': 'M', 'h': 'H', 'd': 'D', 'f_Ca': 'F Ca', 'ActFrac': 'ActFrac', 'ProdFrac': 'ProdFrac', 'Na_i': 'Na I', 'Ca_o': 'Ca O', 'K_i': 'K I', 'Ca_i_intracellular_calcium_concentration': 'Ca I Intracellular Calcium Concentration', 'Ca_up': 'Ca Up', 'Ca_rel': 'Ca Rel', 'Ca_Calmod': 'Ca Calmod', 'Ca_Trop': 'Ca Trop'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`.'), 'initial_prod_frac': ('ProdFrac', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ProdFrac`.'), 'initial_na_i': ('Na_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Na_i`.'), 'initial_model_state_k_i': ('K_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `K_i`.'), 'initial_f_ca': ('f_Ca', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `f_Ca`.'), 'initial_ca_up': ('Ca_up', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_up`.')}
    _HEADLINE_OUTPUTS = {'v_membrane': ('V_membrane', 'native SBML value', 'V Membrane. Maps to SBML symbol `V_membrane`.'), 'prod_frac': ('ProdFrac', 'native SBML value', 'ProdFrac. Maps to SBML symbol `ProdFrac`.'), 'na_i': ('Na_i', 'native SBML value', 'Na I. Maps to SBML symbol `Na_i`.'), 'k_i': ('K_i', 'native SBML value', 'K I. Maps to SBML symbol `K_i`.'), 'f_ca': ('f_Ca', 'native SBML value', 'F Ca. Maps to SBML symbol `f_Ca`.'), 'ca_up': ('Ca_up', 'native SBML value', 'Ca Up. Maps to SBML symbol `Ca_up`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0848444339.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
