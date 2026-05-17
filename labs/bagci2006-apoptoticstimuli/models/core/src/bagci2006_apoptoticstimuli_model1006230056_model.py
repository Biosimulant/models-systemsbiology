# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bagci2006_ApoptoticStimuli."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bagci2006ApoptoticstimuliModel1006230056Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bagci2006_ApoptoticStimuli."""

    _SBML_ID = 'MODEL1006230056'
    _TITLE = 'Bagci2006_ApoptoticStimuli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Casp8', 'Casp8Bid', 'Apaf_1', 'CytcApaf_1', 'Cytc', 'Cytc_mito', 'Bax_2', 'tBid_mito', 'tBid', 'tBidBax', 'Bax', 'Bcl_2', 'Casp3Bcl_2', 'Casp3Bid', 'Bid', 'Casp3IAP', 'Casp3', 'Apop', 'Pro9', 'ApopPro9', 'ApopPro9_2', 'ApopCasp9_2Pro3', 'Casp9Pro3', 'Pro3', 'Casp9IAP', 'ApopCasp9IAP', 'ApopCasp9_2IAP', 'IAP', 'ApopCasp9', 'Casp9', 'ApopCasp9_2']
    _SPECIES_LABELS = {'Casp8': 'Casp8', 'Casp8Bid': 'Casp8Bid', 'Apaf_1': 'Apaf 1', 'CytcApaf_1': 'CytcApaf 1', 'Cytc': 'Cytc', 'Cytc_mito': 'Cytc Mito', 'Bax_2': 'Bax 2', 'tBid_mito': 'TBid Mito', 'tBid': 'TBid', 'tBidBax': 'TBidBax', 'Bax': 'Bax', 'Bcl_2': 'Bcl 2', 'Casp3Bcl_2': 'Casp3Bcl 2', 'Casp3Bid': 'Casp3Bid', 'Bid': 'Bid', 'Casp3IAP': 'Casp3IAP', 'Casp3': 'Casp3', 'Apop': 'Apop', 'Pro9': 'Pro9', 'ApopPro9': 'ApopPro9', 'ApopPro9_2': 'ApopPro9 2', 'ApopCasp9_2Pro3': 'ApopCasp9 2Pro3', 'Casp9Pro3': 'Casp9Pro3', 'Pro3': 'Pro3', 'Casp9IAP': 'Casp9IAP', 'ApopCasp9IAP': 'ApopCasp9IAP', 'ApopCasp9_2IAP': 'ApopCasp9 2IAP', 'IAP': 'IAP', 'ApopCasp9': 'ApopCasp9', 'Casp9': 'Casp9', 'ApopCasp9_2': 'ApopCasp9 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytc_apaf_1': ('CytcApaf_1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CytcApaf_1`.'), 'initial_casp9_pro3': ('Casp9Pro3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Casp9Pro3`.'), 'initial_casp9_iap': ('Casp9IAP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Casp9IAP`.'), 'initial_casp9': ('Casp9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Casp9`.'), 'initial_casp8_bid': ('Casp8Bid', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Casp8Bid`.'), 'initial_casp8': ('Casp8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Casp8`.')}
    _HEADLINE_OUTPUTS = {'cytc_apaf_1': ('CytcApaf_1', 'native SBML value', 'CytcApaf 1. Maps to SBML symbol `CytcApaf_1`.'), 'casp9_pro3': ('Casp9Pro3', 'native SBML value', 'Casp9Pro3. Maps to SBML symbol `Casp9Pro3`.'), 'casp9_iap': ('Casp9IAP', 'native SBML value', 'Casp9IAP. Maps to SBML symbol `Casp9IAP`.'), 'casp9': ('Casp9', 'native SBML value', 'Casp9. Maps to SBML symbol `Casp9`.'), 'casp8_bid': ('Casp8Bid', 'native SBML value', 'Casp8Bid. Maps to SBML symbol `Casp8Bid`.'), 'casp8': ('Casp8', 'native SBML value', 'Casp8. Maps to SBML symbol `Casp8`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230056.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
