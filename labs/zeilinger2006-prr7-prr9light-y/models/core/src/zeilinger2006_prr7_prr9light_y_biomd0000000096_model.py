# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zeilinger2006_PRR7-PRR9light-Y."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zeilinger2006Prr7Prr9lightYBiomd0000000096Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zeilinger2006_PRR7-PRR9light-Y."""

    _SBML_ID = 'BIOMD0000000096'
    _TITLE = 'Zeilinger2006_PRR7-PRR9light-Y'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cLc', 'cLm', 'cLn', 'cP7c', 'cP7m', 'cP7n', 'cP9c', 'cP9m', 'cP9n', 'cPn', 'cTc', 'cTm', 'cTn', 'cXc', 'cXm', 'cXn', 'cYc', 'cYm', 'cYn']
    _SPECIES_LABELS = {'cLc': 'cLc', 'cLm': 'cLm', 'cLn': 'cLn', 'cP7c': 'cP7c', 'cP7m': 'cP7m', 'cP7n': 'cP7n', 'cP9c': 'cP9c', 'cP9m': 'cP9m', 'cP9n': 'cP9n', 'cPn': 'cPn', 'cTc': 'cTc', 'cTm': 'cTm', 'cTn': 'cTn', 'cXc': 'cXc', 'cXm': 'cXm', 'cXn': 'cXn', 'cYc': 'cYc', 'cYm': 'cYm', 'cYn': 'cYn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c_yc': ('cYc', 49.2611, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cYc`.'), 'initial_c_yn': ('cYn', 17.4355, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cYn`.'), 'initial_c_xn': ('cXn', 14.7289, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXn`.'), 'initial_c_tc': ('cTc', 5.2235, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTc`.'), 'initial_c_tn': ('cTn', 4.5333, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTn`.'), 'initial_c_tm': ('cTm', 3.6732, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTm`.')}
    _HEADLINE_OUTPUTS = {'c_yc': ('cYc', 'native SBML value', 'cYc. Maps to SBML symbol `cYc`.'), 'c_yn': ('cYn', 'native SBML value', 'cYn. Maps to SBML symbol `cYn`.'), 'c_xn': ('cXn', 'native SBML value', 'cXn. Maps to SBML symbol `cXn`.'), 'c_tc': ('cTc', 'native SBML value', 'cTc. Maps to SBML symbol `cTc`.'), 'c_tn': ('cTn', 'native SBML value', 'cTn. Maps to SBML symbol `cTn`.'), 'c_tm': ('cTm', 'native SBML value', 'cTm. Maps to SBML symbol `cTm`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000096.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
