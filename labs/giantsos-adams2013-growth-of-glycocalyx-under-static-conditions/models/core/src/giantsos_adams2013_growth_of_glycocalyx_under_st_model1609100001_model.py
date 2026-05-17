# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Giantsos-Adams2013 - Growth of glycocalyx under static conditions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GiantsosAdams2013GrowthOfGlycocalyxUnderStModel1609100001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Giantsos-Adams2013 - Growth of glycocalyx under static conditions."""

    _SBML_ID = 'MODEL1609100001'
    _TITLE = 'Giantsos-Adams2013 - Growth of glycocalyx under static conditions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's5', 's6', 's8', 's4']
    _SPECIES_LABELS = {'s1': 'HS surface', 's2': 'early endosome', 's3': 'late endosome', 's5': 's5', 's6': 'golgi', 's8': 's8', 's4': 'lysosome'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lysosome': ('s4', 1.23, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s4`.'), 'initial_late_endosome': ('s3', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s3`.'), 'initial_early_endosome': ('s2', 0.4, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s2`.'), 'initial_hs_surface': ('s1', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_golgi': ('s6', 0.05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s6`.'), 'initial_model_state_s8': ('s8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s8`.')}
    _HEADLINE_OUTPUTS = {'lysosome': ('s4', 'native SBML value', 'lysosome. Maps to SBML symbol `s4`.'), 'late_endosome': ('s3', 'native SBML value', 'late endosome. Maps to SBML symbol `s3`.'), 'early_endosome': ('s2', 'native SBML value', 'early endosome. Maps to SBML symbol `s2`.'), 'hs_surface': ('s1', 'native SBML value', 'HS surface. Maps to SBML symbol `s1`.'), 'golgi': ('s6', 'native SBML value', 'golgi. Maps to SBML symbol `s6`.'), 'model_state_s8': ('s8', 'native SBML value', 's8. Maps to SBML symbol `s8`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1609100001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
