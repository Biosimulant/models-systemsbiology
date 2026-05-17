# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rohwer2001_Sucrose."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rohwer2001SucroseBiomd0000000023Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rohwer2001_Sucrose."""

    _SBML_ID = 'BIOMD0000000023'
    _TITLE = 'Rohwer2001_Sucrose'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Fru', 'Glc', 'HexP', 'Suc6P', 'Suc', 'Sucvac', 'glycolysis', 'phos', 'UDP', 'ADP', 'ATP', 'Glcex', 'Fruex']
    _SPECIES_LABELS = {'Fru': 'Fru', 'Glc': 'Glc', 'HexP': 'HexP', 'Suc6P': 'Suc6P', 'Suc': 'Suc', 'Sucvac': 'Sucvac', 'glycolysis': 'Glycolysis', 'phos': 'Phos', 'UDP': 'UDP', 'ADP': 'ADP', 'ATP': 'ATP', 'Glcex': 'Glcex', 'Fruex': 'Fruex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('ATP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 0.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_glycolysis': ('glycolysis', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `glycolysis`.'), 'initial_phos': ('phos', 5.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `phos`.'), 'initial_glcex': ('Glcex', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glcex`.'), 'initial_fruex': ('Fruex', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fruex`.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'glycolysis': ('glycolysis', 'native SBML value', 'Glycolysis. Maps to SBML symbol `glycolysis`.'), 'phos': ('phos', 'native SBML value', 'Phos. Maps to SBML symbol `phos`.'), 'glcex': ('Glcex', 'native SBML value', 'Glcex. Maps to SBML symbol `Glcex`.'), 'fruex': ('Fruex', 'native SBML value', 'Fruex. Maps to SBML symbol `Fruex`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000023.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
