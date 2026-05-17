# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for GiantsosAdams2013 - Growth of glycocalyx under static conditions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Giantsosadams2013GrowthOfGlycocalyxUnderStaBiomd0000000830Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for GiantsosAdams2013 - Growth of glycocalyx under static conditions."""

    _SBML_ID = 'BIOMD0000000830'
    _TITLE = 'GiantsosAdams2013 - Growth of glycocalyx under static conditions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's6', 's4', 'release', 'shedding']
    _SPECIES_LABELS = {'s1': 'HS surface', 's2': 'early endosome', 's3': 'late endosome', 's6': 'golgi', 's4': 'lysosome', 'release': 'release', 'shedding': 'shedding'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lysosome': ('s4', 1.23, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s4`.'), 'initial_late_endosome': ('s3', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s3`.'), 'initial_early_endosome': ('s2', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s2`.'), 'initial_hs_surface': ('s1', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_golgi': ('s6', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s6`.'), 'initial_shedding': ('shedding', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `shedding`.')}
    _HEADLINE_OUTPUTS = {'lysosome': ('s4', 'native SBML value', 'lysosome. Maps to SBML symbol `s4`.'), 'late_endosome': ('s3', 'native SBML value', 'late endosome. Maps to SBML symbol `s3`.'), 'early_endosome': ('s2', 'native SBML value', 'early endosome. Maps to SBML symbol `s2`.'), 'hs_surface': ('s1', 'native SBML value', 'HS surface. Maps to SBML symbol `s1`.'), 'golgi': ('s6', 'native SBML value', 'golgi. Maps to SBML symbol `s6`.'), 'shedding': ('shedding', 'native SBML value', 'shedding. Maps to SBML symbol `shedding`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000830.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
