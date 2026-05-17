# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wang2007 - ATP induced intracellular Calcium Oscillation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wang2007AtpInducedIntracellularCalciumOscilBiomd0000000145Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wang2007 - ATP induced intracellular Calcium Oscillation."""

    _SBML_ID = 'BIOMD0000000145'
    _TITLE = 'Wang2007 - ATP induced intracellular Calcium Oscillation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Galpha_GTP', 'APLC', 'IP3', 'Ca_ER', 'Ca_Cyt', 'PLC', 'DG']
    _SPECIES_LABELS = {'Galpha_GTP': 'Galpha_GTP', 'APLC': 'APLC', 'IP3': 'IP3', 'Ca_ER': 'Calcium', 'Ca_Cyt': 'Calcium', 'PLC': 'PLC', 'DG': 'Diacylglycerol'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium': ('Ca_ER', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_ER`.'), 'initial_calcium_2': ('Ca_Cyt', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_Cyt`.'), 'initial_galpha_gtp': ('Galpha_GTP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Galpha_GTP`.'), 'initial_diacylglycerol': ('DG', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DG`.'), 'initial_aplc': ('APLC', 9.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `APLC`.'), 'initial_model_state_plc': ('PLC', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PLC`.')}
    _HEADLINE_OUTPUTS = {'calcium': ('Ca_ER', 'native SBML value', 'Calcium. Maps to SBML symbol `Ca_ER`.'), 'calcium_2': ('Ca_Cyt', 'native SBML value', 'Calcium. Maps to SBML symbol `Ca_Cyt`.'), 'galpha_gtp': ('Galpha_GTP', 'native SBML value', 'Galpha_GTP. Maps to SBML symbol `Galpha_GTP`.'), 'diacylglycerol': ('DG', 'native SBML value', 'Diacylglycerol. Maps to SBML symbol `DG`.'), 'aplc': ('APLC', 'native SBML value', 'APLC. Maps to SBML symbol `APLC`.'), 'plc': ('PLC', 'native SBML value', 'PLC. Maps to SBML symbol `PLC`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000145.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
