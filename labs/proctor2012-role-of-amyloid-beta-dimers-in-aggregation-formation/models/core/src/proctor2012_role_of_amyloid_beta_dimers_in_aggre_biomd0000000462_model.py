# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2012 - Role of Amyloid-beta dimers in aggregation formation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2012RoleOfAmyloidBetaDimersInAggreBiomd0000000462Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2012 - Role of Amyloid-beta dimers in aggregation formation."""

    _SBML_ID = 'BIOMD0000000462'
    _TITLE = 'Proctor2012 - Role of Amyloid-beta dimers in aggregation formation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Abeta', 'AbDim', 'AbP', 'Nep']
    _SPECIES_LABELS = {'Abeta': 'AbetaMonomer', 'AbDim': 'AbetaDimer', 'AbP': 'AbetaPlaque', 'Nep': 'Neprilysin'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_neprilysin': ('Nep', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nep`.'), 'initial_abeta_plaque': ('AbP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AbP`.'), 'initial_abeta_monomer': ('Abeta', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Abeta`.'), 'initial_abeta_dimer': ('AbDim', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AbDim`.')}
    _HEADLINE_OUTPUTS = {'neprilysin': ('Nep', 'native SBML value', 'Neprilysin. Maps to SBML symbol `Nep`.'), 'abeta_plaque': ('AbP', 'native SBML value', 'AbetaPlaque. Maps to SBML symbol `AbP`.'), 'abeta_monomer': ('Abeta', 'native SBML value', 'AbetaMonomer. Maps to SBML symbol `Abeta`.'), 'abeta_dimer': ('AbDim', 'native SBML value', 'AbetaDimer. Maps to SBML symbol `AbDim`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000462.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
