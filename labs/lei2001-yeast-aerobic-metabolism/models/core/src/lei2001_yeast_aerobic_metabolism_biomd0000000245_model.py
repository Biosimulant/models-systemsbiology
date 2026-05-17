# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lei2001_Yeast_Aerobic_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lei2001YeastAerobicMetabolismBiomd0000000245Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lei2001_Yeast_Aerobic_Metabolism."""

    _SBML_ID = 'BIOMD0000000245'
    _TITLE = 'Lei2001_Yeast_Aerobic_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s_glu', 's_pyr', 's_acetate', 's_acetald', 's_EtOH', 'x', 'a', 'AcDH', 'CO2', 'Red', 'S_f']
    _SPECIES_LABELS = {'s_glu': 'Glucose', 's_pyr': 'Pyruvate', 's_acetate': 'Acetate', 's_acetald': 'Acetaldehyde', 's_EtOH': 'EtOH', 'x': 'BM', 'a': 'BM(active)', 'AcDH': 'BM(AcDH)', 'CO2': 'CO2', 'Red': 'Red. Equ. (NADH)', 'S_f': 'Glucose(feed)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_feed': ('S_f', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S_f`.'), 'initial_glucose': ('s_glu', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s_glu`.'), 'initial_red_equ_nadh': ('Red', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Red`.'), 'initial_pyruvate': ('s_pyr', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s_pyr`.'), 'initial_et_oh': ('s_EtOH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s_EtOH`.'), 'initial_bm_ac_dh': ('AcDH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AcDH`.')}
    _HEADLINE_OUTPUTS = {'glucose_feed': ('S_f', 'native SBML value', 'Glucose(feed). Maps to SBML symbol `S_f`.'), 'glucose': ('s_glu', 'native SBML value', 'Glucose. Maps to SBML symbol `s_glu`.'), 'red_equ_nadh': ('Red', 'native SBML value', 'Red. Equ. (NADH). Maps to SBML symbol `Red`.'), 'pyruvate': ('s_pyr', 'native SBML value', 'Pyruvate. Maps to SBML symbol `s_pyr`.'), 'et_oh': ('s_EtOH', 'native SBML value', 'EtOH. Maps to SBML symbol `s_EtOH`.'), 'bm_ac_dh': ('AcDH', 'native SBML value', 'BM(AcDH). Maps to SBML symbol `AcDH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000245.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
