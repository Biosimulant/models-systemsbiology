# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Curien2003_MetThr_synthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Curien2003MetthrSynthesisBiomd0000000068Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Curien2003_MetThr_synthesis."""

    _SBML_ID = 'BIOMD0000000068'
    _TITLE = 'Curien2003_MetThr_synthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Phser', 'Thr', 'Cystathionine', 'Hser', 'Phi', 'Cys', 'AdoMet', 'CGS', 'TS']
    _SPECIES_LABELS = {'Phser': 'Phosphohomoserine', 'Thr': 'Threonine', 'Cystathionine': 'Cystathionine', 'Hser': 'Homoserine', 'Phi': 'Inorganic phosphate', 'Cys': 'Cysteine', 'AdoMet': 'S-adenosylmethionine', 'CGS': 'Cystathionine gamma-synthase', 'TS': 'Threonine synthase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cystathionine_gamma_synthase': ('CGS', 0.7, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CGS`.'), 'initial_cystathionine': ('Cystathionine', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cystathionine`.'), 'initial_inorganic_phosphate': ('Phi', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Phi`.'), 'initial_s_adenosylmethionine': ('AdoMet', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AdoMet`.'), 'initial_cysteine': ('Cys', 15.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cys`.'), 'initial_threonine_synthase': ('TS', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TS`.')}
    _HEADLINE_OUTPUTS = {'cystathionine_gamma_synthase': ('CGS', 'native SBML value', 'Cystathionine gamma-synthase. Maps to SBML symbol `CGS`.'), 'cystathionine': ('Cystathionine', 'native SBML value', 'Cystathionine. Maps to SBML symbol `Cystathionine`.'), 'inorganic_phosphate': ('Phi', 'native SBML value', 'Inorganic phosphate. Maps to SBML symbol `Phi`.'), 's_adenosylmethionine': ('AdoMet', 'native SBML value', 'S-adenosylmethionine. Maps to SBML symbol `AdoMet`.'), 'cysteine': ('Cys', 'native SBML value', 'Cysteine. Maps to SBML symbol `Cys`.'), 'threonine_synthase': ('TS', 'native SBML value', 'Threonine synthase. Maps to SBML symbol `TS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000068.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
