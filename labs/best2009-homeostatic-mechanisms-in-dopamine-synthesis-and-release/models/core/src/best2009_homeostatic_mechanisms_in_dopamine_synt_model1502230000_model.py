# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Best2009 - Homeostatic mechanisms in dopamine synthesis and release."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Best2009HomeostaticMechanismsInDopamineSyntModel1502230000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Best2009 - Homeostatic mechanisms in dopamine synthesis and release."""

    _SBML_ID = 'MODEL1502230000'
    _TITLE = 'Best2009 - Homeostatic mechanisms in dopamine synthesis and release'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['btyr', 'hva', 'eda', 'SAM', 'SAH', 'NADP', 'NADPH', 'bh4', 'bh2', 'tyr', 'tyrpool', 'l_dopa', 'cda', 'vda']
    _SPECIES_LABELS = {'btyr': 'btyr', 'hva': 'hva', 'eda': 'eda', 'SAM': 'SAM', 'SAH': 'SAH', 'NADP': 'NADP+', 'NADPH': 'NADPH', 'bh4': 'bh4', 'bh2': 'bh2', 'tyr': 'tyr', 'tyrpool': 'tyrpool', 'l_dopa': 'l-dopa', 'cda': 'cda', 'vda': 'vda'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tyrpool': ('tyrpool', 1260.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tyrpool`.'), 'initial_model_state_bh4': ('bh4', 319.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bh4`.'), 'initial_model_state_tyr': ('tyr', 126.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tyr`.'), 'initial_btyr': ('btyr', 97.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `btyr`.'), 'initial_model_state_vda': ('vda', 81.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `vda`.'), 'initial_model_state_bh2': ('bh2', 41.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bh2`.')}
    _HEADLINE_OUTPUTS = {'tyrpool': ('tyrpool', 'native SBML value', 'tyrpool. Maps to SBML symbol `tyrpool`.'), 'bh4': ('bh4', 'native SBML value', 'bh4. Maps to SBML symbol `bh4`.'), 'tyr': ('tyr', 'native SBML value', 'tyr. Maps to SBML symbol `tyr`.'), 'btyr': ('btyr', 'native SBML value', 'btyr. Maps to SBML symbol `btyr`.'), 'vda': ('vda', 'native SBML value', 'vda. Maps to SBML symbol `vda`.'), 'bh2': ('bh2', 'native SBML value', 'bh2. Maps to SBML symbol `bh2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1502230000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
