# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Reed2004 - Methionine Cycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reed2004MethionineCycleBiomd0000000698Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Reed2004 - Methionine Cycle."""

    _SBML_ID = 'BIOMD0000000698'
    _TITLE = 'Reed2004 - Methionine Cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Metin', 'Methionine', 'AdoMet', 'AdoHcy', 'Homocysteine', '_5mTHF', 'Cystathionine']
    _SPECIES_LABELS = {'Metin': 'Metin', 'Methionine': 'Methionine', 'AdoMet': 'AdoMet', 'AdoHcy': 'AdoHcy', 'Homocysteine': 'Homocysteine', '_5mTHF': '5mTHF', 'Cystathionine': 'Cystathionine'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cystathionine': ('Cystathionine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cystathionine`.'), 'initial_metin': ('Metin', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Metin`.'), 'initial_ado_met': ('AdoMet', 137.6, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AdoMet`.'), 'initial_methionine': ('Methionine', 53.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Methionine`.'), 'initial_ado_hcy': ('AdoHcy', 13.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AdoHcy`.'), 'initial_model_state_5m_thf': ('_5mTHF', 5.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `_5mTHF`.')}
    _HEADLINE_OUTPUTS = {'cystathionine': ('Cystathionine', 'native SBML value', 'Cystathionine. Maps to SBML symbol `Cystathionine`.'), 'metin': ('Metin', 'native SBML value', 'Metin. Maps to SBML symbol `Metin`.'), 'ado_met': ('AdoMet', 'native SBML value', 'AdoMet. Maps to SBML symbol `AdoMet`.'), 'methionine': ('Methionine', 'native SBML value', 'Methionine. Maps to SBML symbol `Methionine`.'), 'ado_hcy': ('AdoHcy', 'native SBML value', 'AdoHcy. Maps to SBML symbol `AdoHcy`.'), 'model_state_5m_thf': ('_5mTHF', 'native SBML value', '5mTHF. Maps to SBML symbol `_5mTHF`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000698.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
