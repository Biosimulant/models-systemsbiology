# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Cardiomyocyte Telomere Damage by ROS without Cell Division."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CardiomyocyteTelomereDamageByRosWithoutCelModel1608250001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Cardiomyocyte Telomere Damage by ROS without Cell Division."""

    _SBML_ID = 'MODEL1608250001'
    _TITLE = 'Cardiomyocyte Telomere Damage by ROS without Cell Division'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['intact', 'one_taf', 'two_taf', 'three_taf', 'four_taf', 'ROS', 'Source', 'Sink', 'div_marker']
    _SPECIES_LABELS = {'intact': 'Intact', 'one_taf': 'One Taf', 'two_taf': 'Two Taf', 'three_taf': 'Three Taf', 'four_taf': 'Four Taf', 'ROS': 'ROS', 'Source': 'Source', 'Sink': 'Sink', 'div_marker': 'Div Marker'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ros': ('ROS', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ROS`.'), 'initial_intact': ('intact', 75.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `intact`.'), 'initial_one_taf': ('one_taf', 25.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `one_taf`.'), 'initial_source': ('Source', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Source`.'), 'initial_two_taf': ('two_taf', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `two_taf`.'), 'initial_three_taf': ('three_taf', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `three_taf`.')}
    _HEADLINE_OUTPUTS = {'ros': ('ROS', 'native SBML value', 'ROS. Maps to SBML symbol `ROS`.'), 'intact': ('intact', 'native SBML value', 'Intact. Maps to SBML symbol `intact`.'), 'one_taf': ('one_taf', 'native SBML value', 'One Taf. Maps to SBML symbol `one_taf`.'), 'source': ('Source', 'native SBML value', 'Source. Maps to SBML symbol `Source`.'), 'two_taf': ('two_taf', 'native SBML value', 'Two Taf. Maps to SBML symbol `two_taf`.'), 'three_taf': ('three_taf', 'native SBML value', 'Three Taf. Maps to SBML symbol `three_taf`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1608250001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
