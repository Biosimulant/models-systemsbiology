# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Singh2006_TCA_Ecoli_glucose."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Singh2006TcaEcoliGlucoseBiomd0000000222Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Singh2006_TCA_Ecoli_glucose."""

    _SBML_ID = 'BIOMD0000000222'
    _TITLE = 'Singh2006_TCA_Ecoli_glucose'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['aca', 'oaa', 'coa', 'cit', 'icit', 'akg', 'sca', 'suc', 'fa', 'mal', 'gly', 'biosyn']
    _SPECIES_LABELS = {'aca': 'Aca', 'oaa': 'Oaa', 'coa': 'Coa', 'cit': 'Cit', 'icit': 'Icit', 'akg': 'Akg', 'sca': 'Sca', 'suc': 'Suc', 'fa': 'Fa', 'mal': 'Mal', 'gly': 'Gly', 'biosyn': 'Biosyn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_gly': ('gly', 4.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `gly`.'), 'initial_model_state_cit': ('cit', 3.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cit`.'), 'initial_model_state_mal': ('mal', 1.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mal`.'), 'initial_model_state_suc': ('suc', 0.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `suc`.'), 'initial_model_state_aca': ('aca', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `aca`.'), 'initial_model_state_fa': ('fa', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fa`.')}
    _HEADLINE_OUTPUTS = {'gly': ('gly', 'native SBML value', 'Gly. Maps to SBML symbol `gly`.'), 'cit': ('cit', 'native SBML value', 'Cit. Maps to SBML symbol `cit`.'), 'mal': ('mal', 'native SBML value', 'Mal. Maps to SBML symbol `mal`.'), 'suc': ('suc', 'native SBML value', 'Suc. Maps to SBML symbol `suc`.'), 'aca': ('aca', 'native SBML value', 'Aca. Maps to SBML symbol `aca`.'), 'model_state_fa': ('fa', 'native SBML value', 'Fa. Maps to SBML symbol `fa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000222.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
