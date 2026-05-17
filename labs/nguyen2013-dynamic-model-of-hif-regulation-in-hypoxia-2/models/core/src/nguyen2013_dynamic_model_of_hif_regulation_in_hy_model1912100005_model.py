# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nguyen2013 - Dynamic model of HIF regulation in hypoxia (reduced model)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nguyen2013DynamicModelOfHifRegulationInHyModel1912100005Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nguyen2013 - Dynamic model of HIF regulation in hypoxia (reduced model)."""

    _SBML_ID = 'MODEL1912100005'
    _TITLE = 'Nguyen2013 - Dynamic model of HIF regulation in hypoxia (reduced model)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['HIFalpha', 'FIH', 'HIFalpha_aOH', 'O2', 'HIFalpha_n', 'HIFalpha_aOH_n', 'FIH_n']
    _SPECIES_LABELS = {'HIFalpha': 'HIFalpha', 'FIH': 'FIH', 'HIFalpha_aOH': 'HIFalpha-aOH', 'O2': 'O2', 'HIFalpha_n': 'HIFalpha_n', 'HIFalpha_aOH_n': 'HIFalpha-aOH_n', 'FIH_n': 'FIH_n'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fih_n': ('FIH_n', 40.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FIH_n`.'), 'initial_hi_falpha_n': ('HIFalpha_n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HIFalpha_n`.'), 'initial_hi_falpha_a_oh_n': ('HIFalpha_aOH_n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HIFalpha_aOH_n`.'), 'initial_hi_falpha_a_oh': ('HIFalpha_aOH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HIFalpha_aOH`.'), 'initial_model_state_fih': ('FIH', 110.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FIH`.'), 'initial_model_state_o2': ('O2', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O2`.')}
    _HEADLINE_OUTPUTS = {'fih_n': ('FIH_n', 'native SBML value', 'FIH_n. Maps to SBML symbol `FIH_n`.'), 'hi_falpha_n': ('HIFalpha_n', 'native SBML value', 'HIFalpha_n. Maps to SBML symbol `HIFalpha_n`.'), 'hi_falpha_a_oh_n': ('HIFalpha_aOH_n', 'native SBML value', 'HIFalpha-aOH_n. Maps to SBML symbol `HIFalpha_aOH_n`.'), 'hi_falpha_a_oh': ('HIFalpha_aOH', 'native SBML value', 'HIFalpha-aOH. Maps to SBML symbol `HIFalpha_aOH`.'), 'fih': ('FIH', 'native SBML value', 'FIH. Maps to SBML symbol `FIH`.'), 'model_state_o2': ('O2', 'native SBML value', 'O2. Maps to SBML symbol `O2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912100005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
