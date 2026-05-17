# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Dokos1996_SinoatrialNode."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dokos1996SinoatrialnodeModel0912503622Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Dokos1996_SinoatrialNode."""

    _SBML_ID = 'MODEL0912503622'
    _TITLE = 'Dokos1996_SinoatrialNode'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['E_membrane', 'dL', 'fL', 'fL2', 'dT', 'fT', 'm', 'h', 'x', 'y', 'Nai', 'Nao', 'Ki', 'Ko', 'Cai_ion_concentrations', 'Cao', 'Caup', 'Carel']
    _SPECIES_LABELS = {'E_membrane': 'E Membrane', 'dL': 'DL', 'fL': 'FL', 'fL2': 'FL2', 'dT': 'DT', 'fT': 'FT', 'm': 'M', 'h': 'H', 'x': 'X', 'y': 'Y', 'Nai': 'Nai', 'Nao': 'Nao', 'Ki': 'Ki', 'Ko': 'Ko', 'Cai_ion_concentrations': 'Cai Ion Concentrations', 'Cao': 'Cao', 'Caup': 'Caup', 'Carel': 'Carel'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_nao': ('Nao', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nao`.'), 'initial_model_state_nai': ('Nai', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nai`.'), 'initial_model_state_ko': ('Ko', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ko`.'), 'initial_model_state_ki': ('Ki', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ki`.'), 'initial_model_state_ft': ('fT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fT`.'), 'initial_model_state_fl2': ('fL2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fL2`.')}
    _HEADLINE_OUTPUTS = {'nao': ('Nao', 'native SBML value', 'Nao. Maps to SBML symbol `Nao`.'), 'nai': ('Nai', 'native SBML value', 'Nai. Maps to SBML symbol `Nai`.'), 'model_state_ko': ('Ko', 'native SBML value', 'Ko. Maps to SBML symbol `Ko`.'), 'model_state_ki': ('Ki', 'native SBML value', 'Ki. Maps to SBML symbol `Ki`.'), 'model_state_ft': ('fT', 'native SBML value', 'FT. Maps to SBML symbol `fT`.'), 'fl2': ('fL2', 'native SBML value', 'FL2. Maps to SBML symbol `fL2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0912503622.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
