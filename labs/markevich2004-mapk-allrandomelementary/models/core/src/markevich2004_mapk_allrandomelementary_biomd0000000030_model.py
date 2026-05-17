# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Markevich2004_MAPK_AllRandomElementary."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Markevich2004MapkAllrandomelementaryBiomd0000000030Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Markevich2004_MAPK_AllRandomElementary."""

    _SBML_ID = 'BIOMD0000000030'
    _TITLE = 'Markevich2004_MAPK_AllRandomElementary'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'MpY', 'MpT', 'Mpp', 'MAPKK', 'MKP', 'MpY_MAPKK', 'MpT_MAPKK', 'M_MAPKK_Y', 'M_MAPKK_T', 'Mpp_MKP_Y', 'Mpp_MKP_T', 'MpY_MKP_Y', 'MpY_MKP_T', 'MpT_MKP_Y', 'MpT_MKP_T', 'M_MKP_T', 'M_MKP_Y']
    _SPECIES_LABELS = {'M': 'MAPK', 'MpY': 'MAPK-PY', 'MpT': 'MAPK-PT', 'Mpp': 'MAPK-PP', 'MAPKK': 'MAPKK', 'MKP': 'MKP', 'MpY_MAPKK': 'MAPK-PY_MAPKK', 'MpT_MAPKK': 'MAPK-PT_MAPKK', 'M_MAPKK_Y': 'MAPK_MAPKK_Y', 'M_MAPKK_T': 'MAPK_MAPKK_T', 'Mpp_MKP_Y': 'MAPK-PP_MKP_T', 'Mpp_MKP_T': 'MAPK-PP_MKP_Y', 'MpY_MKP_Y': 'MAPK-PY_MKP_Y', 'MpY_MKP_T': 'MAPK-PY_MKP_T', 'MpT_MKP_Y': 'MAPK-PT_MKP_Y', 'MpT_MKP_T': 'MAPK-PT_MKP_T', 'M_MKP_T': 'MAPK_MKP_T', 'M_MKP_Y': 'MAPK_MKP_Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mapk_mkp_y': ('M_MKP_Y', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_MKP_Y`.'), 'initial_mapk_mkp_t': ('M_MKP_T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_MKP_T`.'), 'initial_mapk_mapkk_y': ('M_MAPKK_Y', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_MAPKK_Y`.'), 'initial_mapk_mapkk_t': ('M_MAPKK_T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_MAPKK_T`.'), 'initial_mapk_py_mkp_y': ('MpY_MKP_Y', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MpY_MKP_Y`.'), 'initial_mapk_py_mkp_t': ('MpY_MKP_T', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MpY_MKP_T`.')}
    _HEADLINE_OUTPUTS = {'mapk_mkp_y': ('M_MKP_Y', 'native SBML value', 'MAPK_MKP_Y. Maps to SBML symbol `M_MKP_Y`.'), 'mapk_mkp_t': ('M_MKP_T', 'native SBML value', 'MAPK_MKP_T. Maps to SBML symbol `M_MKP_T`.'), 'mapk_mapkk_y': ('M_MAPKK_Y', 'native SBML value', 'MAPK_MAPKK_Y. Maps to SBML symbol `M_MAPKK_Y`.'), 'mapk_mapkk_t': ('M_MAPKK_T', 'native SBML value', 'MAPK_MAPKK_T. Maps to SBML symbol `M_MAPKK_T`.'), 'mapk_py_mkp_y': ('MpY_MKP_Y', 'native SBML value', 'MAPK-PY_MKP_Y. Maps to SBML symbol `MpY_MKP_Y`.'), 'mapk_py_mkp_t': ('MpY_MKP_T', 'native SBML value', 'MAPK-PY_MKP_T. Maps to SBML symbol `MpY_MKP_T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000030.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
