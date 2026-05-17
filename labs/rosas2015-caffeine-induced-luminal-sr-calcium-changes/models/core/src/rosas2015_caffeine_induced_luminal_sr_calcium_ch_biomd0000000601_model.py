# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rosas2015 - Caffeine-induced luminal SR calcium changes."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rosas2015CaffeineInducedLuminalSrCalciumChBiomd0000000601Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rosas2015 - Caffeine-induced luminal SR calcium changes."""

    _SBML_ID = 'BIOMD0000000601'
    _TITLE = 'Rosas2015 - Caffeine-induced luminal SR calcium changes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['mwd805cc43_4a96_472f_a894_c119a6aa895f', 'mw447078ee_8bc8_4358_abcd_ade10dba93b0', 'mw40a96ef6_32da_46d1_9712_4f53f60bad43', 'mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6', 'mw168e0d8a_b9f7_4d4c_b437_a81206c5d381']
    _SPECIES_LABELS = {'mwd805cc43_4a96_472f_a894_c119a6aa895f': 'Ca_SR_Total', 'mw447078ee_8bc8_4358_abcd_ade10dba93b0': 'Ca_SR', 'mw40a96ef6_32da_46d1_9712_4f53f60bad43': 'Ca_i_Total', 'mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6': 'Ca_i', 'mw168e0d8a_b9f7_4d4c_b437_a81206c5d381': 'caff'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ca_sr_total': ('mwd805cc43_4a96_472f_a894_c119a6aa895f', 0.00165, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mwd805cc43_4a96_472f_a894_c119a6aa895f`.'), 'initial_ca_sr': ('mw447078ee_8bc8_4358_abcd_ade10dba93b0', 7.8e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw447078ee_8bc8_4358_abcd_ade10dba93b0`.'), 'initial_ca_i_total': ('mw40a96ef6_32da_46d1_9712_4f53f60bad43', 7.5e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw40a96ef6_32da_46d1_9712_4f53f60bad43`.'), 'initial_ca_i': ('mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6', 7.5e-08, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6`.'), 'initial_caff': ('mw168e0d8a_b9f7_4d4c_b437_a81206c5d381', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw168e0d8a_b9f7_4d4c_b437_a81206c5d381`.')}
    _HEADLINE_OUTPUTS = {'ca_sr_total': ('mwd805cc43_4a96_472f_a894_c119a6aa895f', 'native SBML value', 'Ca_SR_Total. Maps to SBML symbol `mwd805cc43_4a96_472f_a894_c119a6aa895f`.'), 'ca_sr': ('mw447078ee_8bc8_4358_abcd_ade10dba93b0', 'native SBML value', 'Ca_SR. Maps to SBML symbol `mw447078ee_8bc8_4358_abcd_ade10dba93b0`.'), 'ca_i_total': ('mw40a96ef6_32da_46d1_9712_4f53f60bad43', 'native SBML value', 'Ca_i_Total. Maps to SBML symbol `mw40a96ef6_32da_46d1_9712_4f53f60bad43`.'), 'ca_i': ('mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6', 'native SBML value', 'Ca_i. Maps to SBML symbol `mwe1a0a651_d2d5_4f75_8d45_9336c60eb9a6`.'), 'caff': ('mw168e0d8a_b9f7_4d4c_b437_a81206c5d381', 'native SBML value', 'caff. Maps to SBML symbol `mw168e0d8a_b9f7_4d4c_b437_a81206c5d381`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000601.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
