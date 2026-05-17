# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Phillips2007_AscendingArousalSystem_SleepWakeDynamics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Phillips2007AscendingarousalsystemSleepwakedynBiomd0000000917Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Phillips2007_AscendingArousalSystem_SleepWakeDynamics."""

    _SBML_ID = 'BIOMD0000000917'
    _TITLE = 'Phillips2007_AscendingArousalSystem_SleepWakeDynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Monoaminergic__MA__voltage', 'Ventrolateral_preopticarea__VLPO__voltage', 'Somnogen_level_H']
    _SPECIES_LABELS = {'Monoaminergic__MA__voltage': 'Monoaminergic (MA) voltage', 'Ventrolateral_preopticarea__VLPO__voltage': 'Ventrolateral preopticarea (VLPO) voltage', 'Somnogen_level_H': 'Somnogen level H'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_somnogen_level_h': ('Somnogen_level_H', 10.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Somnogen_level_H`.'), 'initial_ventrolateral_preopticarea_vlpo_voltage': ('Ventrolateral_preopticarea__VLPO__voltage', -10.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ventrolateral_preopticarea__VLPO__voltage`.'), 'initial_monoaminergic_ma_voltage': ('Monoaminergic__MA__voltage', 1.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Monoaminergic__MA__voltage`.')}
    _HEADLINE_OUTPUTS = {'somnogen_level_h': ('Somnogen_level_H', 'substance', 'Somnogen level H. Maps to SBML symbol `Somnogen_level_H`.'), 'ventrolateral_preopticarea_vlpo_voltage': ('Ventrolateral_preopticarea__VLPO__voltage', 'substance', 'Ventrolateral preopticarea (VLPO) voltage. Maps to SBML symbol `Ventrolateral_preopticarea__VLPO__voltage`.'), 'monoaminergic_ma_voltage': ('Monoaminergic__MA__voltage', 'substance', 'Monoaminergic (MA) voltage. Maps to SBML symbol `Monoaminergic__MA__voltage`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000917.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
