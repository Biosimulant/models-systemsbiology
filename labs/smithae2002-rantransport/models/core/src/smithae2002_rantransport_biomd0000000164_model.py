# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for SmithAE2002_RanTransport."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smithae2002RantransportBiomd0000000164Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for SmithAE2002_RanTransport."""

    _SBML_ID = 'BIOMD0000000164'
    _TITLE = 'SmithAE2002_RanTransport'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Carrier_Cytosol', 'Carrier_RanGTP_Cytosol', 'RanGAP_Cytosol', 'RanBP1_Cytosol', 'RanBP1_Carrier_RanGTP_Cytosol', 'NTF2_Nucleus', 'RanGDP_Nucleus', 'RCC1_Nucleus', 'RanGTP_Nucleus', 'NTF2_RanGDP_Nucleus', 'Carrier_Nucleus', 'RanGDP_Cytosol', 'Carrier_RanGTP_Nucleus', 'NTF2_RanGDP_Cytosol', 'FRanGTP_Cytosol', 'FCarrier_RanGTP_Cytosol', 'FRanGDP_Cytosol', 'FNTF2_RanGDP_Cytosol', 'FRanBP1_Carrier_RanGTP_Cytosol', 'FCarrier_RanGTP_Nucleus', 'FRanGDP_Nucleus', 'FNTF2_RanGDP_Nucleus', 'FRanGTP_Nucleus', 'NTF2_Cytosol', 'Pipet_Cytosol', 'RanGTP_Cytosol']
    _SPECIES_LABELS = {'Carrier_Cytosol': 'Carrier_Cytosol', 'Carrier_RanGTP_Cytosol': 'Carrier_RanGTP_Cytosol', 'RanGAP_Cytosol': 'RanGAP_Cytosol', 'RanBP1_Cytosol': 'RanBP1_Cytosol', 'RanBP1_Carrier_RanGTP_Cytosol': 'RanBP1_Carrier_RanGTP_Cytosol', 'NTF2_Nucleus': 'NTF2_Nucleus', 'RanGDP_Nucleus': 'RanGDP_Nucleus', 'RCC1_Nucleus': 'RCC1_Nucleus', 'RanGTP_Nucleus': 'RanGTP_Nucleus', 'NTF2_RanGDP_Nucleus': 'NTF2_RanGDP_Nucleus', 'Carrier_Nucleus': 'Carrier_Nucleus', 'RanGDP_Cytosol': 'RanGDP_Cytosol', 'Carrier_RanGTP_Nucleus': 'Carrier_RanGTP_Nucleus', 'NTF2_RanGDP_Cytosol': 'NTF2_RanGDP_Cytosol', 'FRanGTP_Cytosol': 'FRanGTP_Cytosol', 'FCarrier_RanGTP_Cytosol': 'FCarrier_RanGTP_Cytosol', 'FRanGDP_Cytosol': 'FRanGDP_Cytosol', 'FNTF2_RanGDP_Cytosol': 'FNTF2_RanGDP_Cytosol', 'FRanBP1_Carrier_RanGTP_Cytosol': 'FRanBP1_Carrier_RanGTP_Cytosol', 'FCarrier_RanGTP_Nucleus': 'FCarrier_RanGTP_Nucleus', 'FRanGDP_Nucleus': 'FRanGDP_Nucleus', 'FNTF2_RanGDP_Nucleus': 'FNTF2_RanGDP_Nucleus', 'FRanGTP_Nucleus': 'FRanGTP_Nucleus', 'NTF2_Cytosol': 'NTF2_Cytosol', 'Pipet_Cytosol': 'Pipet_Cytosol', 'RanGTP_Cytosol': 'RanGTP_Cytosol'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_carrier_cytosol': ('Carrier_Cytosol', 11.8952664327711, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Carrier_Cytosol`.'), 'initial_carrier_ran_gtp_nucleus': ('Carrier_RanGTP_Nucleus', 11.5694219089212, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Carrier_RanGTP_Nucleus`.'), 'initial_carrier_nucleus': ('Carrier_Nucleus', 10.8211328580636, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Carrier_Nucleus`.'), 'initial_ran_bp1_cytosol': ('RanBP1_Cytosol', 2.91577340630959, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RanBP1_Cytosol`.'), 'initial_ran_gdp_cytosol': ('RanGDP_Cytosol', 1.75546095870568, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RanGDP_Cytosol`.'), 'initial_ntf2_ran_gdp_cytosol': ('NTF2_RanGDP_Cytosol', 1.47617820113791, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NTF2_RanGDP_Cytosol`.')}
    _HEADLINE_OUTPUTS = {'carrier_cytosol': ('Carrier_Cytosol', 'native SBML value', 'Carrier_Cytosol. Maps to SBML symbol `Carrier_Cytosol`.'), 'carrier_ran_gtp_nucleus': ('Carrier_RanGTP_Nucleus', 'native SBML value', 'Carrier_RanGTP_Nucleus. Maps to SBML symbol `Carrier_RanGTP_Nucleus`.'), 'carrier_nucleus': ('Carrier_Nucleus', 'native SBML value', 'Carrier_Nucleus. Maps to SBML symbol `Carrier_Nucleus`.'), 'ran_bp1_cytosol': ('RanBP1_Cytosol', 'native SBML value', 'RanBP1_Cytosol. Maps to SBML symbol `RanBP1_Cytosol`.'), 'ran_gdp_cytosol': ('RanGDP_Cytosol', 'native SBML value', 'RanGDP_Cytosol. Maps to SBML symbol `RanGDP_Cytosol`.'), 'ntf2_ran_gdp_cytosol': ('NTF2_RanGDP_Cytosol', 'native SBML value', 'NTF2_RanGDP_Cytosol. Maps to SBML symbol `NTF2_RanGDP_Cytosol`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000164.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
