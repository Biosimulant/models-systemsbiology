# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rodriguez-Caso2006_Polyamine_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class RodriguezCaso2006PolyamineMetabolismBiomd0000000190Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rodriguez-Caso2006_Polyamine_Metabolism."""

    _SBML_ID = 'BIOMD0000000190'
    _TITLE = 'Rodriguez-Caso2006_Polyamine_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['SAM', 'A', 'P', 'S', 'D', 'aS', 'aD', 'Met', 'ORN', 'AcCoA', 'CoA']
    _SPECIES_LABELS = {'SAM': 'S-adenosyl-L-methionine', 'A': 'S-adenosylmethioninamine', 'P': 'Putrescine', 'S': 'Spermine', 'D': 'Spermidine', 'aS': 'N1-Acetylspermine', 'aD': 'N1-Acetylspermidine', 'Met': 'Methionine', 'ORN': 'L-Ornithine', 'AcCoA': 'Acetyl-CoA', 'CoA': 'CoA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_l_ornithine': ('ORN', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ORN`.'), 'initial_methionine': ('Met', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Met`.'), 'initial_acetyl_co_a': ('AcCoA', 39.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AcCoA`.'), 'initial_s_adenosyl_l_methionine': ('SAM', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SAM`.'), 'initial_n1_acetylspermine': ('aS', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `aS`.'), 'initial_n1_acetylspermidine': ('aD', 0.01, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `aD`.')}
    _HEADLINE_OUTPUTS = {'l_ornithine': ('ORN', 'native SBML value', 'L-Ornithine. Maps to SBML symbol `ORN`.'), 'methionine': ('Met', 'native SBML value', 'Methionine. Maps to SBML symbol `Met`.'), 'acetyl_co_a': ('AcCoA', 'native SBML value', 'Acetyl-CoA. Maps to SBML symbol `AcCoA`.'), 's_adenosyl_l_methionine': ('SAM', 'native SBML value', 'S-adenosyl-L-methionine. Maps to SBML symbol `SAM`.'), 'n1_acetylspermine': ('aS', 'native SBML value', 'N1-Acetylspermine. Maps to SBML symbol `aS`.'), 'n1_acetylspermidine': ('aD', 'native SBML value', 'N1-Acetylspermidine. Maps to SBML symbol `aD`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000190.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
