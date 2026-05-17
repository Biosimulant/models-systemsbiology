# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Farhy2007_hGHregulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Farhy2007HghregulationModel0912096133Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Farhy2007_hGHregulation."""

    _SBML_ID = 'MODEL0912096133'
    _TITLE = 'Farhy2007_hGHregulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['GH', 'SRIF_PeV', 'SRIF_ArC', 'GHRH', 'ghr_GHRH']
    _SPECIES_LABELS = {'GH': 'GH', 'SRIF_PeV': 'SRIF PeV', 'SRIF_ArC': 'SRIF ArC', 'GHRH': 'GHRH', 'ghr_GHRH': 'Ghr GHRH'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_srif_pe_v': ('SRIF_PeV', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SRIF_PeV`.'), 'initial_srif_ar_c': ('SRIF_ArC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SRIF_ArC`.'), 'initial_ghr_ghrh': ('ghr_GHRH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ghr_GHRH`.'), 'initial_ghrh': ('GHRH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GHRH`.'), 'initial_model_state_gh': ('GH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GH`.')}
    _HEADLINE_OUTPUTS = {'srif_pe_v': ('SRIF_PeV', 'native SBML value', 'SRIF PeV. Maps to SBML symbol `SRIF_PeV`.'), 'srif_ar_c': ('SRIF_ArC', 'native SBML value', 'SRIF ArC. Maps to SBML symbol `SRIF_ArC`.'), 'ghr_ghrh': ('ghr_GHRH', 'native SBML value', 'Ghr GHRH. Maps to SBML symbol `ghr_GHRH`.'), 'ghrh': ('GHRH', 'native SBML value', 'GHRH. Maps to SBML symbol `GHRH`.'), 'model_state_gh': ('GH', 'native SBML value', 'GH. Maps to SBML symbol `GH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912096133.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
