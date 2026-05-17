# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Arnold2011_Medlyn2002_RuBisCO-CalvinCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arnold2011Medlyn2002RubiscoCalvincycleBiomd0000000384Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Arnold2011_Medlyn2002_RuBisCO-CalvinCycle."""

    _SBML_ID = 'BIOMD0000000384'
    _TITLE = 'Arnold2011_Medlyn2002_RuBisCO-CalvinCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RuBP', 'PGA', 'NADPH', 'CO2', 'O2', 'NADP']
    _SPECIES_LABELS = {'RuBP': 'RuBP', 'PGA': 'PGA', 'NADPH': 'NADPH', 'CO2': 'CO2', 'O2': 'O2', 'NADP': 'NADP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_co2': ('CO2', 245.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CO2`.'), 'initial_model_state_o2': ('O2', 210.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O2`.'), 'initial_model_state_pga': ('PGA', 2.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`.'), 'initial_ru_bp': ('RuBP', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`.'), 'initial_nadp': ('NADP', 0.29, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`.'), 'initial_nadph': ('NADPH', 0.21, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`.')}
    _HEADLINE_OUTPUTS = {'co2': ('CO2', 'native SBML value', 'CO2. Maps to SBML symbol `CO2`.'), 'model_state_o2': ('O2', 'native SBML value', 'O2. Maps to SBML symbol `O2`.'), 'pga': ('PGA', 'native SBML value', 'PGA. Maps to SBML symbol `PGA`.'), 'ru_bp': ('RuBP', 'native SBML value', 'RuBP. Maps to SBML symbol `RuBP`.'), 'nadp': ('NADP', 'native SBML value', 'NADP. Maps to SBML symbol `NADP`.'), 'nadph': ('NADPH', 'native SBML value', 'NADPH. Maps to SBML symbol `NADPH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000384.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
