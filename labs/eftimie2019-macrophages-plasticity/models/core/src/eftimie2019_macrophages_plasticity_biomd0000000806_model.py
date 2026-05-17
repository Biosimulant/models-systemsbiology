# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Eftimie2019-Macrophages Plasticity."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Eftimie2019MacrophagesPlasticityBiomd0000000806Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Eftimie2019-Macrophages Plasticity."""

    _SBML_ID = 'BIOMD0000000806'
    _TITLE = 'Eftimie2019-Macrophages Plasticity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['UnInfected_Tumour_Cells_Xu', 'Infected_Tumour_Cells_Xi', 'Virus_Xv', 'Effector_Cytotoxic_CD8_TCells__Xe', 'M1_Macrophage_Xm1', 'M2_Macrophage_Xm2']
    _SPECIES_LABELS = {'UnInfected_Tumour_Cells_Xu': 'UnInfected_Tumour_Cells(Xu)', 'Infected_Tumour_Cells_Xi': 'Infected_Tumour_Cells(Xi)', 'Virus_Xv': 'Virus(Xv)', 'Effector_Cytotoxic_CD8_TCells__Xe': 'Effector_Cytotoxic_CD8_TCells (Xe)', 'M1_Macrophage_Xm1': 'M1_Macrophage(Xm1)', 'M2_Macrophage_Xm2': 'M2_Macrophage(Xm2)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_virus_xv': ('Virus_Xv', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Virus_Xv`.'), 'initial_m2_macrophage_xm2': ('M2_Macrophage_Xm2', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M2_Macrophage_Xm2`.'), 'initial_m1_macrophage_xm1': ('M1_Macrophage_Xm1', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M1_Macrophage_Xm1`.'), 'initial_infected_tumour_cells_xi': ('Infected_Tumour_Cells_Xi', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Infected_Tumour_Cells_Xi`.'), 'initial_un_infected_tumour_cells_xu': ('UnInfected_Tumour_Cells_Xu', 500000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `UnInfected_Tumour_Cells_Xu`.'), 'initial_effector_cytotoxic_cd8_t_cells_xe': ('Effector_Cytotoxic_CD8_TCells__Xe', 0.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Effector_Cytotoxic_CD8_TCells__Xe`.')}
    _HEADLINE_OUTPUTS = {'virus_xv': ('Virus_Xv', 'substance', 'Virus(Xv). Maps to SBML symbol `Virus_Xv`.'), 'm2_macrophage_xm2': ('M2_Macrophage_Xm2', 'substance', 'M2_Macrophage(Xm2). Maps to SBML symbol `M2_Macrophage_Xm2`.'), 'm1_macrophage_xm1': ('M1_Macrophage_Xm1', 'substance', 'M1_Macrophage(Xm1). Maps to SBML symbol `M1_Macrophage_Xm1`.'), 'infected_tumour_cells_xi': ('Infected_Tumour_Cells_Xi', 'substance', 'Infected_Tumour_Cells(Xi). Maps to SBML symbol `Infected_Tumour_Cells_Xi`.'), 'un_infected_tumour_cells_xu': ('UnInfected_Tumour_Cells_Xu', 'substance', 'UnInfected_Tumour_Cells(Xu). Maps to SBML symbol `UnInfected_Tumour_Cells_Xu`.'), 'effector_cytotoxic_cd8_t_cells_xe': ('Effector_Cytotoxic_CD8_TCells__Xe', 'substance', 'Effector_Cytotoxic_CD8_TCells (Xe). Maps to SBML symbol `Effector_Cytotoxic_CD8_TCells__Xe`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000806.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
