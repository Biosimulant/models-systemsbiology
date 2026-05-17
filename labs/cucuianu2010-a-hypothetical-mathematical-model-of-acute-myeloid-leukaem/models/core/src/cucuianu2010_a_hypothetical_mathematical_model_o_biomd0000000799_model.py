# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cucuianu2010 - A hypothetical-mathematical model of acute myeloid leukaemia pathogenesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cucuianu2010AHypotheticalMathematicalModelOBiomd0000000799Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cucuianu2010 - A hypothetical-mathematical model of acute myeloid leukaemia pathogenesis."""

    _SBML_ID = 'BIOMD0000000799'
    _TITLE = 'Cucuianu2010 - A hypothetical-mathematical model of acute myeloid leukaemia pathogenesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Normal_Hematopoietic_Stem_Cell', 'y_Leukemic_Cell']
    _SPECIES_LABELS = {'x_Normal_Hematopoietic_Stem_Cell': 'x_Normal_Hematopoietic_Stem_Cell', 'y_Leukemic_Cell': 'y_Leukemic_Cell'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_y_leukemic_cell': ('y_Leukemic_Cell', 1.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_Leukemic_Cell`.'), 'initial_x_normal_hematopoietic_stem_cell': ('x_Normal_Hematopoietic_Stem_Cell', 4.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x_Normal_Hematopoietic_Stem_Cell`.')}
    _HEADLINE_OUTPUTS = {'y_leukemic_cell': ('y_Leukemic_Cell', 'native SBML value', 'y_Leukemic_Cell. Maps to SBML symbol `y_Leukemic_Cell`.'), 'x_normal_hematopoietic_stem_cell': ('x_Normal_Hematopoietic_Stem_Cell', 'native SBML value', 'x_Normal_Hematopoietic_Stem_Cell. Maps to SBML symbol `x_Normal_Hematopoietic_Stem_Cell`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000799.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
