# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Stephanou2019 - pH as a potential therapeutic target to improve temozolomide antitumor efficacy."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Stephanou2019PhAsAPotentialTherapeuticTargModel1909300003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Stephanou2019 - pH as a potential therapeutic target to improve temozolomide antitumor efficacy."""

    _SBML_ID = 'MODEL1909300003'
    _TITLE = 'Stephanou2019 - pH as a potential therapeutic target to improve temozolomide antitumor efficacy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TMZ_intracellular_dynamics_T_i', 'TMZ_extracellular_concentration_T_o', 'MTIC_M_i', 'Cation_C_i', 'DNA_adducts']
    _SPECIES_LABELS = {'TMZ_intracellular_dynamics_T_i': 'TMZ intracellular dynamics T_i', 'TMZ_extracellular_concentration_T_o': 'TMZ extracellular concentration T_o', 'MTIC_M_i': 'MTIC M_i', 'Cation_C_i': 'Cation C_i', 'DNA_adducts': 'DNA adducts'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mtic_m_i': ('MTIC_M_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MTIC_M_i`.'), 'initial_dna_adducts': ('DNA_adducts', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DNA_adducts`.'), 'initial_cation_c_i': ('Cation_C_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cation_C_i`.'), 'initial_tmz_intracellular_dynamics_t_i': ('TMZ_intracellular_dynamics_T_i', 62.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TMZ_intracellular_dynamics_T_i`.'), 'initial_tmz_extracellular_concentration_t_o': ('TMZ_extracellular_concentration_T_o', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TMZ_extracellular_concentration_T_o`.')}
    _HEADLINE_OUTPUTS = {'mtic_m_i': ('MTIC_M_i', 'native SBML value', 'MTIC M_i. Maps to SBML symbol `MTIC_M_i`.'), 'dna_adducts': ('DNA_adducts', 'native SBML value', 'DNA adducts. Maps to SBML symbol `DNA_adducts`.'), 'cation_c_i': ('Cation_C_i', 'native SBML value', 'Cation C_i. Maps to SBML symbol `Cation_C_i`.'), 'tmz_intracellular_dynamics_t_i': ('TMZ_intracellular_dynamics_T_i', 'native SBML value', 'TMZ intracellular dynamics T_i. Maps to SBML symbol `TMZ_intracellular_dynamics_T_i`.'), 'tmz_extracellular_concentration_t_o': ('TMZ_extracellular_concentration_T_o', 'native SBML value', 'TMZ extracellular concentration T_o. Maps to SBML symbol `TMZ_extracellular_concentration_T_o`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909300003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
