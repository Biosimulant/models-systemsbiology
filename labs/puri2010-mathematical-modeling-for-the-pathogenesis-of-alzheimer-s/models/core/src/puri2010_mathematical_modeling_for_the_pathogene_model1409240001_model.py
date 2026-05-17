# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Puri2010 - Mathematical Modeling for the Pathogenesis of Alzheimer's Disease."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Puri2010MathematicalModelingForThePathogeneModel1409240001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Puri2010 - Mathematical Modeling for the Pathogenesis of Alzheimer's Disease."""

    _SBML_ID = 'MODEL1409240001'
    _TITLE = "Puri2010 - Mathematical Modeling for the Pathogenesis of Alzheimer's Disease"
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ns', 'Nd', 'Aq', 'Ap', 'M2', 'M1', 'Abeta']
    _SPECIES_LABELS = {'Ns': 'Ns', 'Nd': 'Nd', 'Aq': 'Aq', 'Ap': 'Ap', 'M2': 'M2', 'M1': 'M1', 'Abeta': 'Abeta'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_m2': ('M2', 100000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M2`.'), 'initial_model_state_aq': ('Aq', 100000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Aq`.'), 'initial_model_state_ns': ('Ns', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ns`.'), 'initial_model_state_m1': ('M1', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M1`.'), 'initial_model_state_ap': ('Ap', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ap`.'), 'initial_abeta': ('Abeta', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Abeta`.')}
    _HEADLINE_OUTPUTS = {'model_state_m2': ('M2', 'native SBML value', 'M2. Maps to SBML symbol `M2`.'), 'model_state_aq': ('Aq', 'native SBML value', 'Aq. Maps to SBML symbol `Aq`.'), 'model_state_ns': ('Ns', 'native SBML value', 'Ns. Maps to SBML symbol `Ns`.'), 'model_state_m1': ('M1', 'native SBML value', 'M1. Maps to SBML symbol `M1`.'), 'model_state_ap': ('Ap', 'native SBML value', 'Ap. Maps to SBML symbol `Ap`.'), 'abeta': ('Abeta', 'native SBML value', 'Abeta. Maps to SBML symbol `Abeta`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1409240001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
