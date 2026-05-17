# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ferreira2003_CML_generation2."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ferreira2003CmlGeneration2Biomd0000000053Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ferreira2003_CML_generation2."""

    _SBML_ID = 'BIOMD0000000053'
    _TITLE = 'Ferreira2003_CML_generation2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Glucose', 'Lysine', 'Schiff', 'Amadori', 'Glyoxal', 'CML']
    _SPECIES_LABELS = {'Glucose': 'Glucose', 'Lysine': 'Lysine', 'Schiff': 'Schiff', 'Amadori': 'Amadori', 'Glyoxal': 'Glyoxal', 'CML': 'CML'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('Glucose', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glucose`.'), 'initial_lysine': ('Lysine', 0.0034, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lysine`.'), 'initial_schiff': ('Schiff', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Schiff`.'), 'initial_glyoxal': ('Glyoxal', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glyoxal`.'), 'initial_model_state_cml': ('CML', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CML`.'), 'initial_amadori': ('Amadori', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Amadori`.')}
    _HEADLINE_OUTPUTS = {'glucose': ('Glucose', 'native SBML value', 'Glucose. Maps to SBML symbol `Glucose`.'), 'lysine': ('Lysine', 'native SBML value', 'Lysine. Maps to SBML symbol `Lysine`.'), 'schiff': ('Schiff', 'native SBML value', 'Schiff. Maps to SBML symbol `Schiff`.'), 'glyoxal': ('Glyoxal', 'native SBML value', 'Glyoxal. Maps to SBML symbol `Glyoxal`.'), 'cml': ('CML', 'native SBML value', 'CML. Maps to SBML symbol `CML`.'), 'amadori': ('Amadori', 'native SBML value', 'Amadori. Maps to SBML symbol `Amadori`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000053.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
