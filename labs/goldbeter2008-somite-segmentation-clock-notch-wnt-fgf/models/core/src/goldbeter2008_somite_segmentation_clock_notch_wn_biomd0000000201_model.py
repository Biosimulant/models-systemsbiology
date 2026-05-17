# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Goldbeter2008_Somite_Segmentation_Clock_Notch_Wnt_FGF."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter2008SomiteSegmentationClockNotchWnBiomd0000000201Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Goldbeter2008_Somite_Segmentation_Clock_Notch_Wnt_FGF."""

    _SBML_ID = 'BIOMD0000000201'
    _TITLE = 'Goldbeter2008_Somite_Segmentation_Clock_Notch_Wnt_FGF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'Na', 'Nan', 'MF', 'F', 'Bp', 'BN', 'A', 'K', 'B', 'MAx', 'Rasa', 'ERKa', 'Xa', 'MDusp', 'Dusp', 'Rasi', 'ERKi', 'Xi', 'Rast', 'ERKt', 'Xt', 'D', 'AK', 'Kt', 'Fgf']
    _SPECIES_LABELS = {'N': 'Notch protein', 'Na': 'cytosolic NicD', 'Nan': 'nuclear NicD', 'MF': 'Lunatic fringe mRNA', 'F': 'Lunatic Fringe protein', 'Bp': 'phosph. beta-catenin', 'BN': 'nuclear beta-catenin', 'A': 'Axin2 protein', 'K': 'Gsk3', 'B': 'beta-catenin', 'MAx': 'Axin2 mRNA', 'Rasa': 'active Ras', 'ERKa': 'active ERK', 'Xa': 'active TF X', 'MDusp': 'Dusp6 mRNA', 'Dusp': 'Dusp6 protein', 'Rasi': 'inactive Ras', 'ERKi': 'inactive ERK', 'Xi': 'inactive TF X', 'Rast': 'Ras total', 'ERKt': 'ERK total', 'Xt': 'X total', 'D': 'Dsh protein', 'AK': 'Axin2/Gsk3 destruction complex', 'Kt': 'Kt', 'Fgf': 'Fgf'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ras_total': ('Rast', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rast`.'), 'initial_erk_total': ('ERKt', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ERKt`.'), 'initial_active_ras': ('Rasa', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rasa`.'), 'initial_active_erk': ('ERKa', 0.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ERKa`.'), 'initial_lunatic_fringe_mrna': ('MF', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MF`.'), 'initial_dusp6_protein': ('Dusp', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Dusp`.')}
    _HEADLINE_OUTPUTS = {'ras_total': ('Rast', 'native SBML value', 'Ras total. Maps to SBML symbol `Rast`.'), 'erk_total': ('ERKt', 'native SBML value', 'ERK total. Maps to SBML symbol `ERKt`.'), 'active_ras': ('Rasa', 'native SBML value', 'active Ras. Maps to SBML symbol `Rasa`.'), 'active_erk': ('ERKa', 'native SBML value', 'active ERK. Maps to SBML symbol `ERKa`.'), 'lunatic_fringe_mrna': ('MF', 'native SBML value', 'Lunatic fringe mRNA. Maps to SBML symbol `MF`.'), 'dusp6_protein': ('Dusp', 'native SBML value', 'Dusp6 protein. Maps to SBML symbol `Dusp`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000201.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
