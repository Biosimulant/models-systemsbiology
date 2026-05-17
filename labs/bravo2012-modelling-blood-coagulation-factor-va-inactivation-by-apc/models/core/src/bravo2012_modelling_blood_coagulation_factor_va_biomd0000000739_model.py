# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bravo2012 - Modelling blood coagulation factor Va inactivation by APC."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bravo2012ModellingBloodCoagulationFactorVaBiomd0000000739Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bravo2012 - Modelling blood coagulation factor Va inactivation by APC."""

    _SBML_ID = 'BIOMD0000000739'
    _TITLE = 'Bravo2012 - Modelling blood coagulation factor Va inactivation by APC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['APC', 'APC_Va', 'Va', 'Va_i_506', 'Va_i_306', 'APC_Va_i_506', 'APC_Va_i_306', 'Va_i_306_506', 'Va_1_306_Va_LC', 'Va_307_506', 'Va_507_679_709', 'APC_Va_1_306_Va_LC', 'Xa', 'Xa_Va', 'Xa_Va_i_506', 'Xa_Va_i_306_506', 'Xa_Va_i_306', 'Va_307_679_709', 'PT', 'Va_PT', 'Xa_Va_PT', 'Xa_Va_i_506_PT', 'Xa_Va_i_306_PT', 'Xa_Va_i_306_506_PT']
    _SPECIES_LABELS = {'APC': 'APC', 'APC_Va': 'APC:Va', 'Va': 'Va', 'Va_i_506': 'Va_i_506', 'Va_i_306': 'Va_i_306', 'APC_Va_i_506': 'APC:Va_i_506', 'APC_Va_i_306': 'APC:Va_i_306', 'Va_i_306_506': 'Va_i_306/506', 'Va_1_306_Va_LC': 'Va_1-306:Va_LC', 'Va_307_506': 'Va_307-506', 'Va_507_679_709': 'Va_507-679/709', 'APC_Va_1_306_Va_LC': 'APC:Va_1-306:Va_LC', 'Xa': 'Xa', 'Xa_Va': 'Xa:Va', 'Xa_Va_i_506': 'Xa:Va_i_506', 'Xa_Va_i_306_506': 'Xa:Va_i_306/506', 'Xa_Va_i_306': 'Xa:Va_i_306', 'Va_307_679_709': 'Va_307-679/709', 'PT': 'PT', 'Va_PT': 'Va:PT', 'Xa_Va_PT': 'Xa:Va:PT', 'Xa_Va_i_506_PT': 'Xa:Va_i_506:PT', 'Xa_Va_i_306_PT': 'Xa:Va_i_306:PT', 'Xa_Va_i_306_506_PT': 'Xa:Va_i_306/506:PT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_xa_va_i_506_pt': ('Xa_Va_i_506_PT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_506_PT`.'), 'initial_xa_va_i_506': ('Xa_Va_i_506', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_506`.'), 'initial_xa_va_i_306_pt': ('Xa_Va_i_306_PT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_306_PT`.'), 'initial_xa_va_i_306_506_pt': ('Xa_Va_i_306_506_PT', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_306_506_PT`.'), 'initial_xa_va_i_306_506': ('Xa_Va_i_306_506', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_306_506`.'), 'initial_xa_va_i_306': ('Xa_Va_i_306', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_i_306`.')}
    _HEADLINE_OUTPUTS = {'xa_va_i_506_pt': ('Xa_Va_i_506_PT', 'native SBML value', 'Xa:Va_i_506:PT. Maps to SBML symbol `Xa_Va_i_506_PT`.'), 'xa_va_i_506': ('Xa_Va_i_506', 'native SBML value', 'Xa:Va_i_506. Maps to SBML symbol `Xa_Va_i_506`.'), 'xa_va_i_306_pt': ('Xa_Va_i_306_PT', 'native SBML value', 'Xa:Va_i_306:PT. Maps to SBML symbol `Xa_Va_i_306_PT`.'), 'xa_va_i_306_506_pt': ('Xa_Va_i_306_506_PT', 'native SBML value', 'Xa:Va_i_306/506:PT. Maps to SBML symbol `Xa_Va_i_306_506_PT`.'), 'xa_va_i_306_506': ('Xa_Va_i_306_506', 'native SBML value', 'Xa:Va_i_306/506. Maps to SBML symbol `Xa_Va_i_306_506`.'), 'xa_va_i_306': ('Xa_Va_i_306', 'native SBML value', 'Xa:Va_i_306. Maps to SBML symbol `Xa_Va_i_306`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000739.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
