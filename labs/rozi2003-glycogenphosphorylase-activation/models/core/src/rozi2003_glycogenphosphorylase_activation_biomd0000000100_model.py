# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rozi2003_GlycogenPhosphorylase_Activation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rozi2003GlycogenphosphorylaseActivationBiomd0000000100Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rozi2003_GlycogenPhosphorylase_Activation."""

    _SBML_ID = 'BIOMD0000000100'
    _TITLE = 'Rozi2003_GlycogenPhosphorylase_Activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EC', 'Z', 'A', 'Y', 'GP']
    _SPECIES_LABELS = {'EC': 'Extracellular Calcium', 'Z': 'Cytosolic Calcium', 'A': 'IP3', 'Y': 'Intravesicular Calcium', 'GP': 'Glycogen Phosphorylase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_extracellular_calcium': ('EC', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`.'), 'initial_glycogen_phosphorylase': ('GP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GP`.'), 'initial_model_state_ip3': ('A', 0.45, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`.'), 'initial_intravesicular_calcium': ('Y', 0.36, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_cytosolic_calcium': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.')}
    _HEADLINE_OUTPUTS = {'extracellular_calcium': ('EC', 'native SBML value', 'Extracellular Calcium. Maps to SBML symbol `EC`.'), 'glycogen_phosphorylase': ('GP', 'native SBML value', 'Glycogen Phosphorylase. Maps to SBML symbol `GP`.'), 'ip3': ('A', 'native SBML value', 'IP3. Maps to SBML symbol `A`.'), 'intravesicular_calcium': ('Y', 'native SBML value', 'Intravesicular Calcium. Maps to SBML symbol `Y`.'), 'cytosolic_calcium': ('Z', 'native SBML value', 'Cytosolic Calcium. Maps to SBML symbol `Z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000100.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
