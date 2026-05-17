# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wang2008 - Mimicking the inhibitory effect of riluzole on membrane conductance in skeletal fibres."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wang2008MimickingTheInhibitoryEffectOfRiluBiomd0000000693Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wang2008 - Mimicking the inhibitory effect of riluzole on membrane conductance in skeletal fibres."""

    _SBML_ID = 'BIOMD0000000693'
    _TITLE = 'Wang2008 - Mimicking the inhibitory effect of riluzole on membrane conductance in skeletal fibres'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Vm', 'm', 'h', 'n', 'Vt', 'd', 'o', 'c', 'cer', 'INa', 'IT', 'IKCa', 'ICa', 'IL', 'IK', 'Stimulus', 'beta_n', 'beta_m', 'beta_h', 'alpha_n', 'alpha_m', 'alpha_h', 'w', 'jmem', 'jleak', 'jserca', 'jer']
    _SPECIES_LABELS = {'Vm': 'Vm', 'm': 'm', 'h': 'h', 'n': 'n', 'Vt': 'Vt', 'd': 'd', 'o': 'o', 'c': 'c', 'cer': 'cer', 'INa': 'INa', 'IT': 'IT', 'IKCa': 'IKCa', 'ICa': 'ICa', 'IL': 'IL', 'IK': 'IK', 'Stimulus': 'Stimulus', 'beta_n': 'beta_n', 'beta_m': 'beta_m', 'beta_h': 'beta_h', 'alpha_n': 'alpha_n', 'alpha_m': 'alpha_m', 'alpha_h': 'alpha_h', 'w': 'w', 'jmem': 'jmem', 'jleak': 'jleak', 'jserca': 'jserca', 'jer': 'jer'}
    _PARAMETER_INPUTS = {'stimulus_duration': ('Stimulus_Duration', 1.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Stimulus_Duration`.'), 'stimulus_magnitude': ('Stimulus_Magnitude', 2.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Stimulus_Magnitude`.'), 'stimulus_period': ('Stimulus_Period', 50.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Stimulus_Period`.'), 'stimulus_start': ('Stimulus_Start', 5.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Stimulus_Start`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'cer': ('cer', 'native SBML value', 'cer. Maps to SBML symbol `cer`.'), 'beta_m': ('beta_m', 'native SBML value', 'beta_m. Maps to SBML symbol `beta_m`.'), 'alpha_h': ('alpha_h', 'native SBML value', 'alpha_h. Maps to SBML symbol `alpha_h`.'), 'alpha_m': ('alpha_m', 'native SBML value', 'alpha_m. Maps to SBML symbol `alpha_m`.'), 'beta_n': ('beta_n', 'native SBML value', 'beta_n. Maps to SBML symbol `beta_n`.'), 'jleak': ('jleak', 'native SBML value', 'jleak. Maps to SBML symbol `jleak`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000693.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
