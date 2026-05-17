# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Abu-Soud1999_HomoArginine."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AbuSoud1999HomoarginineModel9087988095Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Abu-Soud1999_HomoArginine."""

    _SBML_ID = 'MODEL9087988095'
    _TITLE = 'Abu-Soud1999_HomoArginine'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Im_minus_nNOS', 'Imidazole', 'Homoarginine', 'Im_minus_nNOS_minus_Homoarginine', 'nNOS_minus_Homoarginine']
    _SPECIES_LABELS = {'Im_minus_nNOS': 'Im Minus NNOS', 'Imidazole': 'Imidazole', 'Homoarginine': 'Homoarginine', 'Im_minus_nNOS_minus_Homoarginine': 'Im Minus NNOS Minus Homoarginine', 'nNOS_minus_Homoarginine': 'NNOS Minus Homoarginine'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_homoarginine': ('Homoarginine', 6000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Homoarginine`.'), 'initial_im_minus_nnos': ('Im_minus_nNOS', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Im_minus_nNOS`.'), 'initial_nnos_minus_homoarginine': ('nNOS_minus_Homoarginine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nNOS_minus_Homoarginine`.'), 'initial_imidazole': ('Imidazole', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Imidazole`.'), 'initial_im_minus_nnos_minus_homoarginine': ('Im_minus_nNOS_minus_Homoarginine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Im_minus_nNOS_minus_Homoarginine`.')}
    _HEADLINE_OUTPUTS = {'homoarginine': ('Homoarginine', 'native SBML value', 'Homoarginine. Maps to SBML symbol `Homoarginine`.'), 'im_minus_nnos': ('Im_minus_nNOS', 'native SBML value', 'Im Minus NNOS. Maps to SBML symbol `Im_minus_nNOS`.'), 'nnos_minus_homoarginine': ('nNOS_minus_Homoarginine', 'native SBML value', 'NNOS Minus Homoarginine. Maps to SBML symbol `nNOS_minus_Homoarginine`.'), 'imidazole': ('Imidazole', 'native SBML value', 'Imidazole. Maps to SBML symbol `Imidazole`.'), 'im_minus_nnos_minus_homoarginine': ('Im_minus_nNOS_minus_Homoarginine', 'native SBML value', 'Im Minus NNOS Minus Homoarginine. Maps to SBML symbol `Im_minus_nNOS_minus_Homoarginine`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL9087988095.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
