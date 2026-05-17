# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Albeck2008_extrinsic_apoptosis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Albeck2008ExtrinsicApoptosisBiomd0000000220Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Albeck2008_extrinsic_apoptosis."""

    _SBML_ID = 'BIOMD0000000220'
    _TITLE = 'Albeck2008_extrinsic_apoptosis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'R', 'flip', 'pC8', 'C8', 'C6', 'BAR', 'pC3', 'C3', 'Bid', 'tBid', 'pC6', 'XIAP', 'C3_Ub', 'PARP', 'CPARP', 'Smac', 'Bcl2c', 'Bax', 'Bax_hash', 'Bcl2', 'L_R', 'R_hash', 'flip_R_hash', 'R_hash_pC8', 'C6_pC8', 'BAR_C8', 'C8_pC3', 'pC3_Apop', 'Apop', 'C8_Bid', 'C3_pC6', 'XIAP_C3', 'PARP_C3', 'Apop_XIAP', 'Smac_XIAP', 'Bcl2c_tBid', 'Bax_tBid', 'Baxm_Bcl2', 'Bax4', 'Bax2_Bcl2', 'Bax4_Bcl2', 'M', 'Bax4_M', 'M_hash', 'Smacm', 'M_hash_Smacm', 'Smacr', 'CytoCm', 'M_hash_CytoCm', 'CytoCr', 'CytoC', 'Apaf', 'CytoC_Apaf', 'Apaf_hash', 'pC9', 'Baxm', 'Bax2']
    _SPECIES_LABELS = {'L': 'L', 'R': 'R', 'flip': 'flip', 'pC8': 'proC8', 'C8': 'casp8', 'C6': 'casp6', 'BAR': 'BAR', 'pC3': 'proC3', 'C3': 'casp3', 'Bid': 'Bid', 'tBid': 'tBid', 'pC6': 'proC6', 'XIAP': 'XIAP', 'C3_Ub': 'Ub C3', 'PARP': 'PARP', 'CPARP': 'cPARP', 'Smac': 'Smac', 'Bcl2c': 'cytosolic Bcl-2', 'Bax': 'Bax', 'Bax_hash': 'Bax#', 'Bcl2': 'Bcl-2', 'L_R': 'L:R', 'R_hash': 'R#', 'flip_R_hash': 'flip:R#', 'R_hash_pC8': 'R#:pC8', 'C6_pC8': 'C6:pC8', 'BAR_C8': 'BAR:C8', 'C8_pC3': 'C8:pC3', 'pC3_Apop': 'pC3:Apop', 'Apop': 'Apop', 'C8_Bid': 'C8:Bid', 'C3_pC6': 'C3:pC6', 'XIAP_C3': 'XIAP:C3', 'PARP_C3': 'PARP:C3', 'Apop_XIAP': 'Apop:XIAP', 'Smac_XIAP': 'Smac:XIAP', 'Bcl2c_tBid': 'Bcl2c:tBid', 'Bax_tBid': 'Bax:tBid', 'Baxm_Bcl2': 'Baxm:Bcl2', 'Bax4': 'Bax4', 'Bax2_Bcl2': 'Bax2:Bcl2', 'Bax4_Bcl2': 'Bax4:Bcl2', 'M': 'M', 'Bax4_M': 'Bax4:M', 'M_hash': 'M#', 'Smacm': 'Smac_m', 'M_hash_Smacm': 'M#:Smac_m', 'Smacr': 'Smac released', 'CytoCm': 'CytoC_m', 'M_hash_CytoCm': 'M#:CytoC_m', 'CytoCr': 'CytoC released', 'CytoC': 'CytoC', 'Apaf': 'Apaf', 'CytoC_Apaf': 'CytoC:Apaf', 'Apaf_hash': 'Apaf#', 'pC9': 'proC9', 'Baxm': 'Baxm', 'Bax2': 'Bax2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cyto_c_m': ('CytoCm', 500000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CytoCm`.'), 'initial_pro_c9': ('pC9', 100000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pC9`.'), 'initial_smac_m': ('Smacm', 100000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Smacm`.'), 'initial_pro_c8': ('pC8', 20000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pC8`.'), 'initial_cytosolic_bcl_2': ('Bcl2c', 20000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bcl2c`.'), 'initial_bcl_2': ('Bcl2', 20000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Bcl2`.')}
    _HEADLINE_OUTPUTS = {'cyto_c_m': ('CytoCm', 'native SBML value', 'CytoC_m. Maps to SBML symbol `CytoCm`.'), 'pro_c9': ('pC9', 'native SBML value', 'proC9. Maps to SBML symbol `pC9`.'), 'smac_m': ('Smacm', 'native SBML value', 'Smac_m. Maps to SBML symbol `Smacm`.'), 'pro_c8': ('pC8', 'native SBML value', 'proC8. Maps to SBML symbol `pC8`.'), 'cytosolic_bcl_2': ('Bcl2c', 'native SBML value', 'cytosolic Bcl-2. Maps to SBML symbol `Bcl2c`.'), 'bcl_2': ('Bcl2', 'native SBML value', 'Bcl-2. Maps to SBML symbol `Bcl2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000220.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
