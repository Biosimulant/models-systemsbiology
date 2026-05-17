# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Chassagnole2001_Threonine Synthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chassagnole2001ThreonineSynthesisBiomd0000000066Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Chassagnole2001_Threonine Synthesis."""

    _SBML_ID = 'BIOMD0000000066'
    _TITLE = 'Chassagnole2001_Threonine Synthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['aspp', 'asa', 'hs', 'hsp', 'phos', 'thr', 'asp', 'nadp', 'nadph', 'adp', 'atp']
    _SPECIES_LABELS = {'aspp': 'Aspartyl phosphate', 'asa': 'Aspartate beta-semialdehyde', 'hs': 'Homoserine', 'hsp': 'O-Phospho-homoserine', 'phos': 'Phos', 'thr': 'Threonine', 'asp': 'Aspartate', 'nadp': 'NADP', 'nadph': 'NADPH', 'adp': 'ADP', 'atp': 'ATP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nadph': ('nadph', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nadph`.'), 'initial_nadp': ('nadp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nadp`.'), 'initial_model_state_atp': ('atp', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`.'), 'initial_model_state_adp': ('adp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `adp`.'), 'initial_threonine': ('thr', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `thr`.'), 'initial_aspartate': ('asp', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `asp`.')}
    _HEADLINE_OUTPUTS = {'nadph': ('nadph', 'native SBML value', 'NADPH. Maps to SBML symbol `nadph`.'), 'nadp': ('nadp', 'native SBML value', 'NADP. Maps to SBML symbol `nadp`.'), 'atp': ('atp', 'native SBML value', 'ATP. Maps to SBML symbol `atp`.'), 'adp': ('adp', 'native SBML value', 'ADP. Maps to SBML symbol `adp`.'), 'threonine': ('thr', 'native SBML value', 'Threonine. Maps to SBML symbol `thr`.'), 'aspartate': ('asp', 'native SBML value', 'Aspartate. Maps to SBML symbol `asp`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000066.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
