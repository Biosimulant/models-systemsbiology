# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Phillips2013 - physiologically based modeling explaining Mammalian rest/activity patterns."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Phillips2013PhysiologicallyBasedModelingExplBiomd0000001072Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Phillips2013 - physiologically based modeling explaining Mammalian rest/activity patterns."""

    _SBML_ID = 'BIOMD0000001072'
    _TITLE = 'Phillips2013 - physiologically based modeling explaining Mammalian rest/activity patterns'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V_v', 'V_m', 'H', 'n', 'X', 'Y']
    _SPECIES_LABELS = {'V_v': 'V_v(mean_cell_body_potential_VLPO)', 'V_m': 'V_m(mean_cell_body_potential_MA)', 'H': 'H(sleep_homeostatic_drive)', 'n': 'n(fraction_of_photoreceptors_that_are_activated)', 'X': 'x(SCN_activity)', 'Y': 'y(complement_of_x)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_h_sleep_homeostatic_drive': ('H', 5.57377096632541, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`.'), 'initial_v_m_mean_cell_body_potential_ma': ('V_m', -17.5981186613022, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_m`.'), 'initial_v_v_mean_cell_body_potential_vlpo': ('V_v', 3.82007920893978, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_v`.'), 'initial_y_complement_of_x': ('Y', -0.803527836803535, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_x_scn_activity': ('X', -0.644229940134898, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.'), 'initial_n_fraction_of_photoreceptors_that_are_activated': ('n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`.')}
    _HEADLINE_OUTPUTS = {'h_sleep_homeostatic_drive': ('H', 'native SBML value', 'H(sleep_homeostatic_drive). Maps to SBML symbol `H`.'), 'v_m_mean_cell_body_potential_ma': ('V_m', 'native SBML value', 'V_m(mean_cell_body_potential_MA). Maps to SBML symbol `V_m`.'), 'v_v_mean_cell_body_potential_vlpo': ('V_v', 'native SBML value', 'V_v(mean_cell_body_potential_VLPO). Maps to SBML symbol `V_v`.'), 'y_complement_of_x': ('Y', 'native SBML value', 'y(complement_of_x). Maps to SBML symbol `Y`.'), 'x_scn_activity': ('X', 'native SBML value', 'x(SCN_activity). Maps to SBML symbol `X`.'), 'n_fraction_of_photoreceptors_that_are_activated': ('n', 'native SBML value', 'n(fraction_of_photoreceptors_that_are_activated). Maps to SBML symbol `n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001072.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
