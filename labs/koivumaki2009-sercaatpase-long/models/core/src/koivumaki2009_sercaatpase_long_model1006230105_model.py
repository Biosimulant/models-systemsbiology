# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Koivumaki2009_SERCAATPase_long."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koivumaki2009SercaatpaseLongModel1006230105Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Koivumaki2009_SERCAATPase_long."""

    _SBML_ID = 'MODEL1006230105'
    _TITLE = 'Koivumaki2009_SERCAATPase_long'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Ca_cyt', 'LTRPN', 'PLB_dephosph', 'Ca_serca']
    _SPECIES_LABELS = {'Ca_cyt': 'Ca Cyt', 'LTRPN': 'LTRPN', 'PLB_dephosph': 'PLB Dephosph', 'Ca_serca': 'Ca Serca'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_plb_dephosph': ('PLB_dephosph', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PLB_dephosph`.'), 'initial_ltrpn': ('LTRPN', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LTRPN`.'), 'initial_ca_serca': ('Ca_serca', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_serca`.'), 'initial_ca_cyt': ('Ca_cyt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_cyt`.')}
    _HEADLINE_OUTPUTS = {'plb_dephosph': ('PLB_dephosph', 'native SBML value', 'PLB Dephosph. Maps to SBML symbol `PLB_dephosph`.'), 'ltrpn': ('LTRPN', 'native SBML value', 'LTRPN. Maps to SBML symbol `LTRPN`.'), 'ca_serca': ('Ca_serca', 'native SBML value', 'Ca Serca. Maps to SBML symbol `Ca_serca`.'), 'ca_cyt': ('Ca_cyt', 'native SBML value', 'Ca Cyt. Maps to SBML symbol `Ca_cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230105.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
