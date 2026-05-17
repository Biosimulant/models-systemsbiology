# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Gupta2019 - Restoration of cytosolic calcium inhibits Mycobacterium tuberculosis intracellular growth."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gupta2019RestorationOfCytosolicCalciumInhibModel1911120004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Gupta2019 - Restoration of cytosolic calcium inhibits Mycobacterium tuberculosis intracellular growth."""

    _SBML_ID = 'MODEL1911120004'
    _TITLE = 'Gupta2019 - Restoration of cytosolic calcium inhibits Mycobacterium tuberculosis intracellular growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ci', 'Ce', 'K', 'P']
    _SPECIES_LABELS = {'Ci': 'Ci', 'Ce': 'Ce', 'K': 'K', 'P': 'P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ci': ('Ci', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ci`.'), 'initial_model_state_ce': ('Ce', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ce`.'), 'initial_model_state_k': ('K', 0.375, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `K`.'), 'initial_model_state_p': ('P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P`.')}
    _HEADLINE_OUTPUTS = {'model_state_ci': ('Ci', 'native SBML value', 'Ci. Maps to SBML symbol `Ci`.'), 'model_state_ce': ('Ce', 'native SBML value', 'Ce. Maps to SBML symbol `Ce`.'), 'model_state_k': ('K', 'native SBML value', 'K. Maps to SBML symbol `K`.'), 'model_state_p': ('P', 'native SBML value', 'P. Maps to SBML symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911120004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
