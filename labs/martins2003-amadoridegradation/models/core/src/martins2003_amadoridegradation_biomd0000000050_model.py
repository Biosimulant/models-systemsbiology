# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Martins2003_AmadoriDegradation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Martins2003AmadoridegradationBiomd0000000050Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Martins2003_AmadoriDegradation."""

    _SBML_ID = 'BIOMD0000000050'
    _TITLE = 'Martins2003_AmadoriDegradation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['DFG', 'E1', 'E2', 'Cn', 'Gly', '_3DG', 'FA', '_1DG', 'AA', 'Man', 'Glu', 'MG', 'Mel', 'Fru']
    _SPECIES_LABELS = {'DFG': 'DFG', 'E1': 'E1', 'E2': 'E2', 'Cn': 'Cn', 'Gly': 'Gly', '_3DG': '3DG', 'FA': 'FA', '_1DG': '1DG', 'AA': 'AA', 'Man': 'Man', 'Glu': 'Glu', 'MG': 'MG', 'Mel': 'Mel', 'Fru': 'Fru'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_dfg': ('DFG', 9.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DFG`.'), 'initial_model_state_mel': ('Mel', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mel`.'), 'initial_model_state_man': ('Man', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Man`.'), 'initial_model_state_mg': ('MG', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MG`.'), 'initial_model_state_gly': ('Gly', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`.'), 'initial_model_state_glu': ('Glu', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glu`.')}
    _HEADLINE_OUTPUTS = {'dfg': ('DFG', 'native SBML value', 'DFG. Maps to SBML symbol `DFG`.'), 'mel': ('Mel', 'native SBML value', 'Mel. Maps to SBML symbol `Mel`.'), 'man': ('Man', 'native SBML value', 'Man. Maps to SBML symbol `Man`.'), 'model_state_mg': ('MG', 'native SBML value', 'MG. Maps to SBML symbol `MG`.'), 'gly': ('Gly', 'native SBML value', 'Gly. Maps to SBML symbol `Gly`.'), 'glu': ('Glu', 'native SBML value', 'Glu. Maps to SBML symbol `Glu`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000050.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
