# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Brands2002 - Monosaccharide-casein systems."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Brands2002MonosaccharideCaseinSystemsBiomd0000000052Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Brands2002 - Monosaccharide-casein systems."""

    _SBML_ID = 'BIOMD0000000052'
    _TITLE = 'Brands2002 - Monosaccharide-casein systems'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Glu', 'Fru', 'Formic_acid', 'Triose', 'Acetic_acid', 'Cn', 'Amadori', 'AMP', 'C5', 'lys_R', 'Melanoidin']
    _SPECIES_LABELS = {'Glu': 'Glu', 'Fru': 'Fru', 'Formic_acid': 'Formic Acid', 'Triose': 'Triose', 'Acetic_acid': 'Acetic Acid', 'Cn': 'Cn', 'Amadori': 'Amadori', 'AMP': 'AMP', 'C5': 'C5', 'lys_R': 'Lys R', 'Melanoidin': 'Melanoidin'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_glu': ('Glu', 160.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glu`.'), 'initial_lys_r': ('lys_R', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `lys_R`.'), 'initial_triose': ('Triose', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Triose`.'), 'initial_melanoidin': ('Melanoidin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Melanoidin`.'), 'initial_model_state_fru': ('Fru', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fru`.'), 'initial_formic_acid': ('Formic_acid', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Formic_acid`.')}
    _HEADLINE_OUTPUTS = {'glu': ('Glu', 'native SBML value', 'Glu. Maps to SBML symbol `Glu`.'), 'lys_r': ('lys_R', 'native SBML value', 'Lys R. Maps to SBML symbol `lys_R`.'), 'triose': ('Triose', 'native SBML value', 'Triose. Maps to SBML symbol `Triose`.'), 'melanoidin': ('Melanoidin', 'native SBML value', 'Melanoidin. Maps to SBML symbol `Melanoidin`.'), 'fru': ('Fru', 'native SBML value', 'Fru. Maps to SBML symbol `Fru`.'), 'formic_acid': ('Formic_acid', 'native SBML value', 'Formic Acid. Maps to SBML symbol `Formic_acid`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000052.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
