# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Marwan2003 - Genetics, regulatory hierarchy between genes."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Marwan2003GeneticsRegulatoryHierarchyBetweenBiomd0000000037Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Marwan2003 - Genetics, regulatory hierarchy between genes."""

    _SBML_ID = 'BIOMD0000000037'
    _TITLE = 'Marwan2003 - Genetics, regulatory hierarchy between genes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pfr', 'Pr', 'Xi', 'Xa', 'prepreS', 'preS', 'Ya', 'S', 'Gluc', 'Yi', 'V', 'Pi']
    _SPECIES_LABELS = {'Pfr': 'Pfr', 'Pr': 'Pr', 'Xi': 'Xi', 'Xa': 'Xa', 'prepreS': 'PrepreS', 'preS': 'PreS', 'Ya': 'Ya', 'S': 'S', 'Gluc': 'Gluc', 'Yi': 'Yi', 'V': 'V', 'Pi': 'Pi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_prepre_s': ('prepreS', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `prepreS`.'), 'initial_model_state_pfr': ('Pfr', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pfr`.'), 'initial_model_state_xi': ('Xi', 6.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xi`.'), 'initial_model_state_ya': ('Ya', 0.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ya`.'), 'initial_model_state_yi': ('Yi', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Yi`.'), 'initial_model_state_xa': ('Xa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa`.')}
    _HEADLINE_OUTPUTS = {'prepre_s': ('prepreS', 'native SBML value', 'PrepreS. Maps to SBML symbol `prepreS`.'), 'pfr': ('Pfr', 'native SBML value', 'Pfr. Maps to SBML symbol `Pfr`.'), 'model_state_xi': ('Xi', 'native SBML value', 'Xi. Maps to SBML symbol `Xi`.'), 'model_state_ya': ('Ya', 'native SBML value', 'Ya. Maps to SBML symbol `Ya`.'), 'model_state_yi': ('Yi', 'native SBML value', 'Yi. Maps to SBML symbol `Yi`.'), 'model_state_xa': ('Xa', 'native SBML value', 'Xa. Maps to SBML symbol `Xa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000037.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
