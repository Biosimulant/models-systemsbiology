# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Graham2013 - Role of osteocytes in targeted bone remodeling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Graham2013RoleOfOsteocytesInTargetedBoneRBiomd0000000721Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Graham2013 - Role of osteocytes in targeted bone remodeling."""

    _SBML_ID = 'BIOMD0000000721'
    _TITLE = 'Graham2013 - Role of osteocytes in targeted bone remodeling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Osteocytes__S', 'Pre_Osteoblasts__P', 'Osteoblasts__B', 'Osteoclasts__C', 'Bone_volume__z']
    _SPECIES_LABELS = {'Osteocytes__S': 'Osteocytes (S)', 'Pre_Osteoblasts__P': 'Pre-Osteoblasts (P)', 'Osteoblasts__B': 'Osteoblasts (B)', 'Osteoclasts__C': 'Osteoclasts (C)', 'Bone_volume__z': 'Bone volume (z)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_osteocytes_s': ('Osteocytes__S', 180.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Osteocytes__S`.'), 'initial_bone_volume_z': ('Bone_volume__z', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bone_volume__z`.'), 'initial_pre_osteoblasts_p': ('Pre_Osteoblasts__P', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pre_Osteoblasts__P`.'), 'initial_osteoclasts_c': ('Osteoclasts__C', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Osteoclasts__C`.'), 'initial_osteoblasts_b': ('Osteoblasts__B', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Osteoblasts__B`.')}
    _HEADLINE_OUTPUTS = {'osteocytes_s': ('Osteocytes__S', 'native SBML value', 'Osteocytes (S). Maps to SBML symbol `Osteocytes__S`.'), 'bone_volume_z': ('Bone_volume__z', 'native SBML value', 'Bone volume (z). Maps to SBML symbol `Bone_volume__z`.'), 'pre_osteoblasts_p': ('Pre_Osteoblasts__P', 'native SBML value', 'Pre-Osteoblasts (P). Maps to SBML symbol `Pre_Osteoblasts__P`.'), 'osteoclasts_c': ('Osteoclasts__C', 'native SBML value', 'Osteoclasts (C). Maps to SBML symbol `Osteoclasts__C`.'), 'osteoblasts_b': ('Osteoblasts__B', 'native SBML value', 'Osteoblasts (B). Maps to SBML symbol `Osteoblasts__B`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000721.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
