# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Schmierer_2008_Smad_Tgfb."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schmierer2008SmadTgfbBiomd0000000173Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Schmierer_2008_Smad_Tgfb."""

    _SBML_ID = 'BIOMD0000000173'
    _TITLE = 'Schmierer_2008_Smad_Tgfb'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PPase', 'S2_n', 'pS2_n', 'G_n', 'pG_n', 'S22_n', 'S24_n', 'S4_n', 'G2_n', 'G4_n', 'GG_n', 'S22_c', 'S24_c', 'S4_c', 'S2_c', 'pS2_c', 'G_c', 'pG_c', 'G2_c', 'G4_c', 'GG_c', 'TGFb_c', 'R_act', 'R', 'R_inact', 'SB']
    _SPECIES_LABELS = {'PPase': 'PPase', 'S2_n': 'Smad2_n', 'pS2_n': 'pSmad2_n', 'G_n': 'GFP-Smad2_n', 'pG_n': 'pGFP-Smad2_n', 'S22_n': 'pSmad2/pSmad2_n', 'S24_n': 'pSmad2/Smad4_n', 'S4_n': 'Smad4_n', 'G2_n': 'pGFP-Smad2/pSmad2_n', 'G4_n': 'pGFP-Smad2/Smad4_n', 'GG_n': 'pGFP-Smad2/pGFP_Smad2_n', 'S22_c': 'pSmad2/pSmad2_c', 'S24_c': 'pSmad2/Smad4_c', 'S4_c': 'Smad4_c', 'S2_c': 'Smad2_c', 'pS2_c': 'pSmad2_c', 'G_c': 'GFP-Smad2_c', 'pG_c': 'pGFP-Smad2_c', 'G2_c': 'pGFP-Smad2/pSmad2_c', 'G4_c': 'pGFP-Smad2/Smad4_c', 'GG_c': 'pGFP-Smad2/pGFP-Smad2_c', 'TGFb_c': 'TGFb_c', 'R_act': 'R_act', 'R': 'R', 'R_inact': 'R_inact', 'SB': 'SB-431542'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_smad2_c': ('S2_c', 60.5899176013587, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S2_c`.'), 'initial_gfp_smad2_c': ('G_c', 60.5899176013587, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_c`.'), 'initial_smad4_c': ('S4_c', 50.78103407, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S4_c`.'), 'initial_smad4_n': ('S4_n', 50.78093897, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S4_n`.'), 'initial_smad2_n': ('S2_n', 28.514773357617, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S2_n`.'), 'initial_gfp_smad2_n': ('G_n', 28.514773357617, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_n`.')}
    _HEADLINE_OUTPUTS = {'smad2_c': ('S2_c', 'native SBML value', 'Smad2_c. Maps to SBML symbol `S2_c`.'), 'gfp_smad2_c': ('G_c', 'native SBML value', 'GFP-Smad2_c. Maps to SBML symbol `G_c`.'), 'smad4_c': ('S4_c', 'native SBML value', 'Smad4_c. Maps to SBML symbol `S4_c`.'), 'smad4_n': ('S4_n', 'native SBML value', 'Smad4_n. Maps to SBML symbol `S4_n`.'), 'smad2_n': ('S2_n', 'native SBML value', 'Smad2_n. Maps to SBML symbol `S2_n`.'), 'gfp_smad2_n': ('G_n', 'native SBML value', 'GFP-Smad2_n. Maps to SBML symbol `G_n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000173.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
