# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Ota2015 - Positive regulation of Rho GTPase activity by RhoGDIs as a result of their direct interaction with GAPs (GDI integrated)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ota2015PositiveRegulationOfRhoGtpaseActiviBiomd0000000899Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Ota2015 - Positive regulation of Rho GTPase activity by RhoGDIs as a result of their direct interaction with GAPs (GDI integrated)."""

    _SBML_ID = 'BIOMD0000000899'
    _TITLE = 'Ota2015 - Positive regulation of Rho GTPase activity by RhoGDIs as a result of their direct interaction with GAPs (GDI integrated)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's13', 's16']
    _SPECIES_LABELS = {'s1': 'Activator', 's2': 'Degrade', 's3': 'GEF', 's4': 'Active GEF', 's5': 'GDP-Rho', 's6': 'GTP-Rho', 's7': 'GDI', 's8': 'GAP', 's9': 'Effector', 's10': 'GDI·GDP-Rho', 's13': 'GDI·GTP-Rho', 's16': 'Effector·GTP-Rho'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_gdigdp_rho': ('s10', 1.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s10`.'), 'initial_effector': ('s9', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s9`.'), 'initial_activator': ('s1', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s1`.'), 'initial_model_state_gef': ('s3', 0.31, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s3`.'), 'initial_model_state_gap': ('s8', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s8`.'), 'initial_gtp_rho': ('s6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s6`.')}
    _HEADLINE_OUTPUTS = {'gdigdp_rho': ('s10', 'native SBML value', 'GDI·GDP-Rho. Maps to SBML symbol `s10`.'), 'effector': ('s9', 'native SBML value', 'Effector. Maps to SBML symbol `s9`.'), 'activator': ('s1', 'native SBML value', 'Activator. Maps to SBML symbol `s1`.'), 'gef': ('s3', 'native SBML value', 'GEF. Maps to SBML symbol `s3`.'), 'gap': ('s8', 'native SBML value', 'GAP. Maps to SBML symbol `s8`.'), 'gtp_rho': ('s6', 'native SBML value', 'GTP-Rho. Maps to SBML symbol `s6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000899.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
