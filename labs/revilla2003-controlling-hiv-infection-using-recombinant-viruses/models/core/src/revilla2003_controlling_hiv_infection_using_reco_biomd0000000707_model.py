# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Revilla2003 - Controlling HIV infection using recombinant viruses."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Revilla2003ControllingHivInfectionUsingRecoBiomd0000000707Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Revilla2003 - Controlling HIV infection using recombinant viruses."""

    _SBML_ID = 'BIOMD0000000707'
    _TITLE = 'Revilla2003 - Controlling HIV infection using recombinant viruses'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Normal_Th_cells', 'Pathogen_Virus', 'Single_Infected_Th_Cells', 'Recombinant_Virus', 'Double_Infected_Th_Cells']
    _SPECIES_LABELS = {'Normal_Th_cells': 'Normal Th cells', 'Pathogen_Virus': 'Pathogen Virus', 'Single_Infected_Th_Cells': 'Single Infected Th Cells', 'Recombinant_Virus': 'Recombinant Virus', 'Double_Infected_Th_Cells': 'Double Infected Th Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_normal_th_cells': ('Normal_Th_cells', 3.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Normal_Th_cells`.'), 'initial_pathogen_virus': ('Pathogen_Virus', 149.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pathogen_Virus`.'), 'initial_single_infected_th_cells': ('Single_Infected_Th_Cells', 6.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Single_Infected_Th_Cells`.'), 'initial_recombinant_virus': ('Recombinant_Virus', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Recombinant_Virus`.'), 'initial_double_infected_th_cells': ('Double_Infected_Th_Cells', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Double_Infected_Th_Cells`.')}
    _HEADLINE_OUTPUTS = {'normal_th_cells': ('Normal_Th_cells', 'native SBML value', 'Normal Th cells. Maps to SBML symbol `Normal_Th_cells`.'), 'pathogen_virus': ('Pathogen_Virus', 'native SBML value', 'Pathogen Virus. Maps to SBML symbol `Pathogen_Virus`.'), 'single_infected_th_cells': ('Single_Infected_Th_Cells', 'native SBML value', 'Single Infected Th Cells. Maps to SBML symbol `Single_Infected_Th_Cells`.'), 'recombinant_virus': ('Recombinant_Virus', 'native SBML value', 'Recombinant Virus. Maps to SBML symbol `Recombinant_Virus`.'), 'double_infected_th_cells': ('Double_Infected_Th_Cells', 'native SBML value', 'Double Infected Th Cells. Maps to SBML symbol `Double_Infected_Th_Cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000707.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
