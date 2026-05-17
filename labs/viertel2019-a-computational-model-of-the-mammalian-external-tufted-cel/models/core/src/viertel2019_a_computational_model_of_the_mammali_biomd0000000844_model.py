# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Viertel2019 - A Computational model of the mammalian external tufted cell."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Viertel2019AComputationalModelOfTheMammaliBiomd0000000844Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Viertel2019 - A Computational model of the mammalian external tufted cell."""

    _SBML_ID = 'BIOMD0000000844'
    _TITLE = 'Viertel2019 - A Computational model of the mammalian external tufted cell'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'Ca', 'nK', 'hNaP', 'hH', 'mLVA', 'hLVA', 'mBK', 'nHVK']
    _SPECIES_LABELS = {'V': 'V', 'Ca': 'Ca', 'nK': 'nK', 'hNaP': 'hNaP', 'hH': 'hH', 'mLVA': 'mLVA', 'hLVA': 'hLVA', 'mBK': 'mBK', 'nHVK': 'nHVK'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_h_lva': ('hLVA', 0.216830183163897, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hLVA`.'), 'initial_model_state_h_h': ('hH', 0.157733123889777, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hH`.'), 'initial_h_na_p': ('hNaP', 0.139259083672574, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hNaP`.'), 'initial_m_bk': ('mBK', 0.118223401083348, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mBK`.'), 'initial_model_state_n_k': ('nK', 0.055706295559466, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nK`.'), 'initial_n_hvk': ('nHVK', 0.049382804823416, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nHVK`.')}
    _HEADLINE_OUTPUTS = {'h_lva': ('hLVA', 'native SBML value', 'hLVA. Maps to SBML symbol `hLVA`.'), 'h_h': ('hH', 'native SBML value', 'hH. Maps to SBML symbol `hH`.'), 'h_na_p': ('hNaP', 'native SBML value', 'hNaP. Maps to SBML symbol `hNaP`.'), 'm_bk': ('mBK', 'native SBML value', 'mBK. Maps to SBML symbol `mBK`.'), 'n_k': ('nK', 'native SBML value', 'nK. Maps to SBML symbol `nK`.'), 'n_hvk': ('nHVK', 'native SBML value', 'nHVK. Maps to SBML symbol `nHVK`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000844.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
