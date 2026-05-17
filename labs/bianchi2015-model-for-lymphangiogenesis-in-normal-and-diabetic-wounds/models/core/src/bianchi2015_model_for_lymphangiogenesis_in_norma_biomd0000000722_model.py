# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bianchi2015 -Model for lymphangiogenesis in normal and diabetic wounds."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bianchi2015ModelForLymphangiogenesisInNormaBiomd0000000722Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bianchi2015 -Model for lymphangiogenesis in normal and diabetic wounds."""

    _SBML_ID = 'BIOMD0000000722'
    _TITLE = 'Bianchi2015 -Model for lymphangiogenesis in normal and diabetic wounds'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Active_TGF_beta', 'Macrophages', 'VEGF', 'LECs', 'Capillaries']
    _SPECIES_LABELS = {'Active_TGF_beta': 'Active TGF-beta', 'Macrophages': 'Macrophages', 'VEGF': 'VEGF', 'LECs': 'LECs', 'Capillaries': 'Capillaries'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_active_tgf_beta': ('Active_TGF_beta', 30.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Active_TGF_beta`.'), 'initial_macrophages': ('Macrophages', 1875.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Macrophages`.'), 'initial_vegf': ('VEGF', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VEGF`.'), 'initial_le_cs': ('LECs', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LECs`.'), 'initial_capillaries': ('Capillaries', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Capillaries`.')}
    _HEADLINE_OUTPUTS = {'active_tgf_beta': ('Active_TGF_beta', 'native SBML value', 'Active TGF-beta. Maps to SBML symbol `Active_TGF_beta`.'), 'macrophages': ('Macrophages', 'native SBML value', 'Macrophages. Maps to SBML symbol `Macrophages`.'), 'vegf': ('VEGF', 'native SBML value', 'VEGF. Maps to SBML symbol `VEGF`.'), 'le_cs': ('LECs', 'native SBML value', 'LECs. Maps to SBML symbol `LECs`.'), 'capillaries': ('Capillaries', 'native SBML value', 'Capillaries. Maps to SBML symbol `Capillaries`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000722.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
