# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Hockin1999_BloodCoagulation_VaInactivation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hockin1999BloodcoagulationVainactivationBiomd0000000365Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Hockin1999_BloodCoagulation_VaInactivation."""

    _SBML_ID = 'BIOMD0000000365'
    _TITLE = 'Hockin1999_BloodCoagulation_VaInactivation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['APC', 'Va', 'Va_APC', 'Va3', 'Va3_APC', 'Va5', 'Va5_APC', 'Va53', 'Va53_APC', 'Va56', 'Va56_APC', 'Va36', 'Va36_APC', 'Va536', 'Va536_APC', 'HC', 'LC', 'HC5', 'HC3', 'HC56', 'HC36', 'HC536', 'LC_APC', 'HC53', 'VaA3', 'VaA53', 'VaA36', 'VaA536', 'VaLCA1', 'VaLCA1_APC']
    _SPECIES_LABELS = {'APC': 'APC', 'Va': 'Va', 'Va_APC': 'Va_APC', 'Va3': 'Va3', 'Va3_APC': 'Va3_APC', 'Va5': 'Va5', 'Va5_APC': 'Va5_APC', 'Va53': 'Va53', 'Va53_APC': 'Va53_APC', 'Va56': 'Va56', 'Va56_APC': 'Va56_APC', 'Va36': 'Va36', 'Va36_APC': 'Va36_APC', 'Va536': 'Va536', 'Va536_APC': 'Va536_APC', 'HC': 'HC', 'LC': 'LC', 'HC5': 'HC5', 'HC3': 'HC3', 'HC56': 'HC56', 'HC36': 'HC36', 'HC536': 'HC536', 'LC_APC': 'LC_APC', 'HC53': 'HC53', 'VaA3': 'VaA3', 'VaA53': 'VaA53', 'VaA36': 'VaA36', 'VaA536': 'VaA536', 'VaLCA1': 'VaLCA1', 'VaLCA1_APC': 'VaLCA1_APC'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_va_apc': ('Va_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va_APC`.'), 'initial_va_lca1_apc': ('VaLCA1_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VaLCA1_APC`.'), 'initial_va5_apc': ('Va5_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va5_APC`.'), 'initial_va56_apc': ('Va56_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va56_APC`.'), 'initial_va53_apc': ('Va53_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va53_APC`.'), 'initial_va536_apc': ('Va536_APC', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Va536_APC`.')}
    _HEADLINE_OUTPUTS = {'va_apc': ('Va_APC', 'native SBML value', 'Va_APC. Maps to SBML symbol `Va_APC`.'), 'va_lca1_apc': ('VaLCA1_APC', 'native SBML value', 'VaLCA1_APC. Maps to SBML symbol `VaLCA1_APC`.'), 'va5_apc': ('Va5_APC', 'native SBML value', 'Va5_APC. Maps to SBML symbol `Va5_APC`.'), 'va56_apc': ('Va56_APC', 'native SBML value', 'Va56_APC. Maps to SBML symbol `Va56_APC`.'), 'va53_apc': ('Va53_APC', 'native SBML value', 'Va53_APC. Maps to SBML symbol `Va53_APC`.'), 'va536_apc': ('Va536_APC', 'native SBML value', 'Va536_APC. Maps to SBML symbol `Va536_APC`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000365.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
