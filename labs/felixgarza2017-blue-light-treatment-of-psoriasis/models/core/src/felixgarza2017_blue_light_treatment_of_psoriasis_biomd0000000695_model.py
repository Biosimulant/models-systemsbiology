# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for FelixGarza2017 - Blue Light Treatment of Psoriasis (simplified)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Felixgarza2017BlueLightTreatmentOfPsoriasisBiomd0000000695Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for FelixGarza2017 - Blue Light Treatment of Psoriasis (simplified)."""

    _SBML_ID = 'BIOMD0000000695'
    _TITLE = 'FelixGarza2017 - Blue Light Treatment of Psoriasis (simplified)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['xFinal_1', 'xFinal_2', 'xFinal_3', 'xFinal_4', 'xFinal_5', 'xFinal_6', 'xFinal_7', 'xFinal_8', 'xFinal_9', 'xFinal_10', 'xFinal_11', 'xFinal_12']
    _SPECIES_LABELS = {'xFinal_1': 'Stem Cells', 'xFinal_2': 'Transit Amplifying Cells', 'xFinal_3': 'Growth Arrested Cells', 'xFinal_4': 'Spinous cells', 'xFinal_5': 'Granular Cells', 'xFinal_6': 'Corneocytes', 'xFinal_7': 'Stem Cells', 'xFinal_8': 'Transit Amplifying Cells', 'xFinal_9': 'Growth Arrested Cells', 'xFinal_10': 'Spinous cells', 'xFinal_11': 'Granular Cells', 'xFinal_12': 'Corneocytes'}
    _PARAMETER_INPUTS = {'treatment_duration': ('Treatment_Duration', 1.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Treatment_Duration`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'growth_arrested_cells': ('xFinal_9', 'native SBML value', 'Growth Arrested Cells. Maps to SBML symbol `xFinal_9`.'), 'growth_arrested_cells_2': ('xFinal_3', 'native SBML value', 'Growth Arrested Cells. Maps to SBML symbol `xFinal_3`.'), 'spinous_cells': ('xFinal_10', 'native SBML value', 'Spinous cells. Maps to SBML symbol `xFinal_10`.'), 'corneocytes': ('xFinal_12', 'native SBML value', 'Corneocytes. Maps to SBML symbol `xFinal_12`.'), 'transit_amplifying_cells': ('xFinal_8', 'native SBML value', 'Transit Amplifying Cells. Maps to SBML symbol `xFinal_8`.'), 'stem_cells': ('xFinal_7', 'native SBML value', 'Stem Cells. Maps to SBML symbol `xFinal_7`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000695.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
