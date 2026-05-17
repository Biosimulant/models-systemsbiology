# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Saucerman2006_PKA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Saucerman2006PkaBiomd0000000165Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Saucerman2006_PKA."""

    _SBML_ID = 'BIOMD0000000165'
    _TITLE = 'Saucerman2006_PKA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Gsbg_cell', 'L_cell', 'Gsa_gdp_cell', 'Gsa_gtp_cell', 'b1AR_S464_cell', 'PDEcAMP_cell', 'PDE_cell', 'ATP_cell', 'b1AR_cell', 'Gs_cell', 'A2RC_cell', 'A2R_cell', 'PKAC_cell', 'ARC_cell', 'PKAC_AKAR_cell', 'Propranolol_cell', 'b1ARinhib_cell', 'light_spot_cell', 'AC_cell', 'PKI_cell', 'PKAC_PKI_cell', 'RC_cell', 'b1AR_Gs_cell', 'cAMP_cell', 'GsAC_cell', 'IBMX_cell', 'PDE_IBMX_cell', 'Fsk_cell', 'FskAC_cell', 'b1AR_p_cell', 'L_b1AR_cell', 'AKAR_cell', 'AKARp_cell', 'PP_cell', 'PP_AKARp_cell', 'DMNB_cAMP_cell', 'L_b1AR_Gs_cell']
    _SPECIES_LABELS = {'Gsbg_cell': 'Gsbg', 'L_cell': 'L', 'Gsa_gdp_cell': 'Gsa_gdp', 'Gsa_gtp_cell': 'Gsa_gtp', 'b1AR_S464_cell': 'b1AR_S464', 'PDEcAMP_cell': 'PDEcAMP', 'PDE_cell': 'PDE', 'ATP_cell': 'ATP', 'b1AR_cell': 'b1AR', 'Gs_cell': 'Gs', 'A2RC_cell': 'A2RC', 'A2R_cell': 'A2R', 'PKAC_cell': 'PKAC', 'ARC_cell': 'ARC', 'PKAC_AKAR_cell': 'PKAC_AKAR', 'Propranolol_cell': 'Propranolol', 'b1ARinhib_cell': 'b1ARinhib', 'light_spot_cell': 'light_spot', 'AC_cell': 'AC', 'PKI_cell': 'PKI', 'PKAC_PKI_cell': 'PKAC_PKI', 'RC_cell': 'RC', 'b1AR_Gs_cell': 'b1AR_Gs', 'cAMP_cell': 'cAMP', 'GsAC_cell': 'GsAC', 'IBMX_cell': 'IBMX', 'PDE_IBMX_cell': 'PDE_IBMX', 'Fsk_cell': 'Fsk', 'FskAC_cell': 'FskAC', 'b1AR_p_cell': 'b1AR_p', 'L_b1AR_cell': 'L_b1AR', 'AKAR_cell': 'AKAR', 'AKARp_cell': 'AKARp', 'PP_cell': 'PP', 'PP_AKARp_cell': 'PP_AKARp', 'DMNB_cAMP_cell': 'DMNB_cAMP', 'L_b1AR_Gs_cell': 'L_b1AR_Gs'}
    _PARAMETER_INPUTS = {'toff_global_light_camp_photolysis': ('toff_global_light_cAMP_photolysis', 2165.0, 's', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `toff_global_light_cAMP_photolysis`.'), 'toff_local_light_camp_photolysis': ('toff_local_light_cAMP_photolysis', 0.0, 's', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `toff_local_light_cAMP_photolysis`.'), 'ton_global_light_camp_photolysis': ('ton_global_light_cAMP_photolysis', 2160.0, 's', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `ton_global_light_cAMP_photolysis`.'), 'ton_local_light_camp_photolysis': ('ton_local_light_cAMP_photolysis', 0.0, 's', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `ton_local_light_cAMP_photolysis`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'atp': ('ATP_cell', 'native SBML value', 'ATP. Maps to SBML symbol `ATP_cell`.'), 'akar': ('AKAR_cell', 'native SBML value', 'AKAR. Maps to SBML symbol `AKAR_cell`.'), 'model_state_gs': ('Gs_cell', 'native SBML value', 'Gs. Maps to SBML symbol `Gs_cell`.'), 'dmnb_camp': ('DMNB_cAMP_cell', 'native SBML value', 'DMNB_cAMP. Maps to SBML symbol `DMNB_cAMP_cell`.'), 'model_state_rc': ('RC_cell', 'native SBML value', 'RC. Maps to SBML symbol `RC_cell`.'), 'model_state_pp': ('PP_cell', 'native SBML value', 'PP. Maps to SBML symbol `PP_cell`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000165.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
