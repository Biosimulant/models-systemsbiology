# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Burghaus2014 - Simulating blood coagulation factor Xa inhibitors."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Burghaus2014SimulatingBloodCoagulationFactorModel1807180005Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Burghaus2014 - Simulating blood coagulation factor Xa inhibitors."""

    _SBML_ID = 'MODEL1807180005'
    _TITLE = 'Burghaus2014 - Simulating blood coagulation factor Xa inhibitors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['fII', 'fIX', 'fVII', 'R_warfarin', 'S_warfarin', 'fX', 'Protein_C', 'Protein_S']
    _SPECIES_LABELS = {'fII': 'fII', 'fIX': 'fIX', 'fVII': 'fVII', 'R_warfarin': 'R-warfarin', 'S_warfarin': 'S-warfarin', 'fX': 'fX', 'Protein_C': 'Protein-C', 'Protein_S': 'Protein-S'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_s_warfarin': ('S_warfarin', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S_warfarin`.'), 'initial_r_warfarin': ('R_warfarin', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_warfarin`.'), 'initial_f_ii': ('fII', 1.4e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fII`.'), 'initial_model_state_f_x': ('fX', 1.6e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fX`.'), 'initial_protein_s': ('Protein_S', 1.4e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Protein_S`.'), 'initial_f_ix': ('fIX', 9e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fIX`.')}
    _HEADLINE_OUTPUTS = {'s_warfarin': ('S_warfarin', 'native SBML value', 'S-warfarin. Maps to SBML symbol `S_warfarin`.'), 'r_warfarin': ('R_warfarin', 'native SBML value', 'R-warfarin. Maps to SBML symbol `R_warfarin`.'), 'f_ii': ('fII', 'native SBML value', 'fII. Maps to SBML symbol `fII`.'), 'f_x': ('fX', 'native SBML value', 'fX. Maps to SBML symbol `fX`.'), 'protein_s': ('Protein_S', 'native SBML value', 'Protein-S. Maps to SBML symbol `Protein_S`.'), 'f_ix': ('fIX', 'native SBML value', 'fIX. Maps to SBML symbol `fIX`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1807180005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
