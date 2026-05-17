# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cronwright2002_Glycerol_Synthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cronwright2002GlycerolSynthesisBiomd0000000076Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cronwright2002_Glycerol_Synthesis."""

    _SBML_ID = 'BIOMD0000000076'
    _TITLE = 'Cronwright2002_Glycerol_Synthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G3P', 'Gly', 'DHAP']
    _SPECIES_LABELS = {'G3P': 'Glycerol 3-phosphate', 'Gly': 'Glycerol', 'DHAP': 'DHAP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glycerol': ('Gly', 15.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`.'), 'initial_glycerol_3_phosphate': ('G3P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3P`.'), 'initial_dhap': ('DHAP', 0.59, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DHAP`.')}
    _HEADLINE_OUTPUTS = {'glycerol': ('Gly', 'native SBML value', 'Glycerol. Maps to SBML symbol `Gly`.'), 'glycerol_3_phosphate': ('G3P', 'native SBML value', 'Glycerol 3-phosphate. Maps to SBML symbol `G3P`.'), 'dhap': ('DHAP', 'native SBML value', 'DHAP. Maps to SBML symbol `DHAP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000076.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
