# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Romond1999_CellCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Romond1999CellcycleBiomd0000000207Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Romond1999_CellCycle."""

    _SBML_ID = 'BIOMD0000000207'
    _TITLE = 'Romond1999_CellCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C1', 'M1', 'X1', 'C2', 'M2', 'X2']
    _SPECIES_LABELS = {'C1': 'cyclinB', 'M1': 'cdk1', 'X1': 'ubiquitin ligase', 'C2': 'cyclinE', 'M2': 'cdk2', 'X2': 'Ubiquitin ligase 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cyclin_b': ('C1', 2.0, 'micromole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C1`.'), 'initial_cdk1': ('M1', 1.0, 'dimensionless', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M1`.'), 'initial_ubiquitin_ligase': ('X1', 0.0, 'dimensionless', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X1`.'), 'initial_cyclin_e': ('C2', 0.0, 'micromole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C2`.'), 'initial_cdk2': ('M2', 0.0, 'dimensionless', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M2`.'), 'initial_ubiquitin_ligase_2': ('X2', 0.0, 'dimensionless', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X2`.')}
    _HEADLINE_OUTPUTS = {'cyclin_b': ('C1', 'micromole', 'cyclinB. Maps to SBML symbol `C1`.'), 'cdk1': ('M1', 'dimensionless', 'cdk1. Maps to SBML symbol `M1`.'), 'ubiquitin_ligase': ('X1', 'dimensionless', 'ubiquitin ligase. Maps to SBML symbol `X1`.'), 'cyclin_e': ('C2', 'micromole', 'cyclinE. Maps to SBML symbol `C2`.'), 'cdk2': ('M2', 'dimensionless', 'cdk2. Maps to SBML symbol `M2`.'), 'ubiquitin_ligase_2': ('X2', 'dimensionless', 'Ubiquitin ligase 2. Maps to SBML symbol `X2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000207.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
