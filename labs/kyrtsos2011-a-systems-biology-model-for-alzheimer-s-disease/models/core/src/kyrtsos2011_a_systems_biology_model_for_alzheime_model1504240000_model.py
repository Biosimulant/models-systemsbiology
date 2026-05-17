# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kyrtsos2011 - A systems biology model for Alzheimer's disease (Cholesterol in AD)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kyrtsos2011ASystemsBiologyModelForAlzheimeModel1504240000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kyrtsos2011 - A systems biology model for Alzheimer's disease (Cholesterol in AD)."""

    _SBML_ID = 'MODEL1504240000'
    _TITLE = "Kyrtsos2011 - A systems biology model for Alzheimer's disease (Cholesterol in AD)"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pyruvate', 'PDH', 'TCA', 'HmgCoA', 'MalonylCoA', 'Mevalonate', 'Cholesterol_N', 'ApoE_A', 'LRP_1', 'APP', 'BACE', 'sAPP', 'gamma_secretase', 'Abeta', 'CTF', 'AICD', 'AcetylCoA', 'Cholesterol_A', 'ApoE']
    _SPECIES_LABELS = {'Pyruvate': 'Pyruvate', 'PDH': 'PDH', 'TCA': 'TCA', 'HmgCoA': 'HmgCoA', 'MalonylCoA': 'MalonylCoA', 'Mevalonate': 'Mevalonate', 'Cholesterol_N': 'Cholesterol_N', 'ApoE_A': 'ApoE_A', 'LRP_1': 'LRP-1', 'APP': 'APP', 'BACE': 'BACE', 'sAPP': 'sAPP', 'gamma_secretase': 'gamma_secretase', 'Abeta': 'Abeta', 'CTF': 'CTF', 'AICD': 'AICD', 'AcetylCoA': 'AcetylCoA', 'Cholesterol_A': 'Cholesterol_A', 'ApoE': 'ApoE'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_tca': ('TCA', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TCA`.'), 'initial_cholesterol_a': ('Cholesterol_A', 1500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cholesterol_A`.'), 'initial_apo_e_a': ('ApoE_A', 750.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ApoE_A`.'), 'initial_cholesterol_n': ('Cholesterol_N', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cholesterol_N`.'), 'initial_s_app': ('sAPP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `sAPP`.'), 'initial_gamma_secretase': ('gamma_secretase', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `gamma_secretase`.')}
    _HEADLINE_OUTPUTS = {'tca': ('TCA', 'native SBML value', 'TCA. Maps to SBML symbol `TCA`.'), 'cholesterol_a': ('Cholesterol_A', 'native SBML value', 'Cholesterol_A. Maps to SBML symbol `Cholesterol_A`.'), 'apo_e_a': ('ApoE_A', 'native SBML value', 'ApoE_A. Maps to SBML symbol `ApoE_A`.'), 'cholesterol_n': ('Cholesterol_N', 'native SBML value', 'Cholesterol_N. Maps to SBML symbol `Cholesterol_N`.'), 's_app': ('sAPP', 'native SBML value', 'sAPP. Maps to SBML symbol `sAPP`.'), 'gamma_secretase': ('gamma_secretase', 'native SBML value', 'gamma_secretase. Maps to SBML symbol `gamma_secretase`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1504240000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
