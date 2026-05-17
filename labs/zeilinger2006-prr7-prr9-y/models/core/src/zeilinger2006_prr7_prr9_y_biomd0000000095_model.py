# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zeilinger2006_PRR7-PRR9-Y."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zeilinger2006Prr7Prr9YBiomd0000000095Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zeilinger2006_PRR7-PRR9-Y."""

    _SBML_ID = 'BIOMD0000000095'
    _TITLE = 'Zeilinger2006_PRR7-PRR9-Y'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cLc', 'cLm', 'cLn', 'cP7c', 'cP7m', 'cP7n', 'cP9c', 'cP9m', 'cP9n', 'cPn', 'cTc', 'cTm', 'cTn', 'cXc', 'cXm', 'cXn', 'cYc', 'cYm', 'cYn']
    _SPECIES_LABELS = {'cLc': 'cLc', 'cLm': 'cLm', 'cLn': 'cLn', 'cP7c': 'cP7c', 'cP7m': 'cP7m', 'cP7n': 'cP7n', 'cP9c': 'cP9c', 'cP9m': 'cP9m', 'cP9n': 'cP9n', 'cPn': 'cPn', 'cTc': 'cTc', 'cTm': 'cTm', 'cTn': 'cTn', 'cXc': 'cXc', 'cXm': 'cXm', 'cXn': 'cXn', 'cYc': 'cYc', 'cYm': 'cYm', 'cYn': 'cYn'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c_xn': ('cXn', 31.8995, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXn`.'), 'initial_c_p7c': ('cP7c', 20.0554, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cP7c`.'), 'initial_c_xc': ('cXc', 13.0372, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXc`.'), 'initial_c_xm': ('cXm', 8.487, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cXm`.'), 'initial_c_tn': ('cTn', 8.0398, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cTn`.'), 'initial_c_yc': ('cYc', 7.075, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cYc`.')}
    _HEADLINE_OUTPUTS = {'c_xn': ('cXn', 'native SBML value', 'cXn. Maps to SBML symbol `cXn`.'), 'c_p7c': ('cP7c', 'native SBML value', 'cP7c. Maps to SBML symbol `cP7c`.'), 'c_xc': ('cXc', 'native SBML value', 'cXc. Maps to SBML symbol `cXc`.'), 'c_xm': ('cXm', 'native SBML value', 'cXm. Maps to SBML symbol `cXm`.'), 'c_tn': ('cTn', 'native SBML value', 'cTn. Maps to SBML symbol `cTn`.'), 'c_yc': ('cYc', 'native SBML value', 'cYc. Maps to SBML symbol `cYc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000095.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
