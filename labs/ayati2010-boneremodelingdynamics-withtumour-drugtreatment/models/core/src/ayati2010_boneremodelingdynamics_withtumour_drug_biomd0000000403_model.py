# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ayati2010_BoneRemodelingDynamics_WithTumour+DrugTreatment."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ayati2010BoneremodelingdynamicsWithtumourDrugBiomd0000000403Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ayati2010_BoneRemodelingDynamics_WithTumour+DrugTreatment."""

    _SBML_ID = 'BIOMD0000000403'
    _TITLE = 'Ayati2010_BoneRemodelingDynamics_WithTumour+DrugTreatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'B', 'z', 'Tumour']
    _SPECIES_LABELS = {'C': 'Osteoclasts', 'B': 'Osteoblasts', 'z': 'BoneMass', 'Tumour': 'Tumour'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_osteoblasts': ('B', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`.'), 'initial_bone_mass': ('z', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.'), 'initial_osteoclasts': ('C', 13.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`.'), 'initial_tumour': ('Tumour', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Tumour`.')}
    _HEADLINE_OUTPUTS = {'osteoblasts': ('B', 'native SBML value', 'Osteoblasts. Maps to SBML symbol `B`.'), 'bone_mass': ('z', 'native SBML value', 'BoneMass. Maps to SBML symbol `z`.'), 'osteoclasts': ('C', 'native SBML value', 'Osteoclasts. Maps to SBML symbol `C`.'), 'tumour': ('Tumour', 'native SBML value', 'Tumour. Maps to SBML symbol `Tumour`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000403.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
