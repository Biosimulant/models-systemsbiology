# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kuznetsov2016(II) - α-syn aggregation kinetics in Parkinson's Disease."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kuznetsov2016IiSynAggregationKineticsInParBiomd0000000615Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kuznetsov2016(II) - α-syn aggregation kinetics in Parkinson's Disease."""

    _SBML_ID = 'BIOMD0000000615'
    _TITLE = "Kuznetsov2016(II) - α-syn aggregation kinetics in Parkinson's Disease"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['As', 'Bs', 'Asyn', 'Bsyn']
    _SPECIES_LABELS = {'As': 'As', 'Bs': 'Bs', 'Asyn': 'Asyn', 'Bsyn': 'Bsyn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_as_value': ('As', 0.006, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `As`.'), 'initial_bsyn': ('Bsyn', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bsyn`.'), 'initial_model_state_bs': ('Bs', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bs`.'), 'initial_asyn': ('Asyn', 0.0, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Asyn`.')}
    _HEADLINE_OUTPUTS = {'as_value': ('As', 'mole', 'As. Maps to SBML symbol `As`.'), 'bsyn': ('Bsyn', 'mole', 'Bsyn. Maps to SBML symbol `Bsyn`.'), 'model_state_bs': ('Bs', 'mole', 'Bs. Maps to SBML symbol `Bs`.'), 'asyn': ('Asyn', 'mole', 'Asyn. Maps to SBML symbol `Asyn`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000615.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
