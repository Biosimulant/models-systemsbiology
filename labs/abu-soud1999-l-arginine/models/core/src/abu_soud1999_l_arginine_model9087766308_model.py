# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Abu-Soud1999_L-Arginine."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AbuSoud1999LArginineModel9087766308Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Abu-Soud1999_L-Arginine."""

    _SBML_ID = 'MODEL9087766308'
    _TITLE = 'Abu-Soud1999_L-Arginine'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Im_minus_nNOS', 'L_minus_Arginine', 'Im_minus_nNOS_minus_L_minus_Arginine', 'nNOS_minus_L_minus_Arginine', 'Imidazole']
    _SPECIES_LABELS = {'Im_minus_nNOS': 'Im Minus NNOS', 'L_minus_Arginine': 'L Minus Arginine', 'Im_minus_nNOS_minus_L_minus_Arginine': 'Im Minus NNOS Minus L Minus Arginine', 'nNOS_minus_L_minus_Arginine': 'NNOS Minus L Minus Arginine', 'Imidazole': 'Imidazole'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_l_minus_arginine': ('L_minus_Arginine', 6000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L_minus_Arginine`.'), 'initial_im_minus_nnos': ('Im_minus_nNOS', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Im_minus_nNOS`.'), 'initial_imidazole': ('Imidazole', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Imidazole`.'), 'initial_nnos_minus_l_minus_arginine': ('nNOS_minus_L_minus_Arginine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nNOS_minus_L_minus_Arginine`.'), 'initial_im_minus_nnos_minus_l_minus_arginine': ('Im_minus_nNOS_minus_L_minus_Arginine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Im_minus_nNOS_minus_L_minus_Arginine`.')}
    _HEADLINE_OUTPUTS = {'l_minus_arginine': ('L_minus_Arginine', 'native SBML value', 'L Minus Arginine. Maps to SBML symbol `L_minus_Arginine`.'), 'im_minus_nnos': ('Im_minus_nNOS', 'native SBML value', 'Im Minus NNOS. Maps to SBML symbol `Im_minus_nNOS`.'), 'imidazole': ('Imidazole', 'native SBML value', 'Imidazole. Maps to SBML symbol `Imidazole`.'), 'nnos_minus_l_minus_arginine': ('nNOS_minus_L_minus_Arginine', 'native SBML value', 'NNOS Minus L Minus Arginine. Maps to SBML symbol `nNOS_minus_L_minus_Arginine`.'), 'im_minus_nnos_minus_l_minus_arginine': ('Im_minus_nNOS_minus_L_minus_Arginine', 'native SBML value', 'Im Minus NNOS Minus L Minus Arginine. Maps to SBML symbol `Im_minus_nNOS_minus_L_minus_Arginine`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL9087766308.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
