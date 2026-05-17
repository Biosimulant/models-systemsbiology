# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Eungdamrong2007_Ras_Activation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Eungdamrong2007RasActivationBiomd0000000161Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Eungdamrong2007_Ras_Activation."""

    _SBML_ID = 'BIOMD0000000161'
    _TITLE = 'Eungdamrong2007_Ras_Activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RasGTP_Golgi_GM', 'EGF_EC', 'CAPRI_cyt', 'serca', 'PIP_PM', 'PI_PM', 'Shc_PM', 'CaCAPRI_PM_PM', 'RactCa', 'Shc_star_PM', 'EGFR_PM', 'PLC_act_PM', 'RasGTP_pal_cyt', 'PLC_PM', 'PIP2_PM', 'Activated_EGFR_PM', 'Ca', 'Ract', 'Rinh', 'RinhCa', 'IP3', 'RasGDP_Golgi_GM', 'Ca_RasGRP_GM_GM', 'DAG_GM_GM', 'RasGRP_DAG_GM', 'CaCAPRI_cyt', 'DAG_PM', 'RasGTP_depal_cyt', 'RasGDP_depal_cyt', 'RasGDP_pal_cyt', 'Ca_PLCe_cyt', 'Ras_CaPLCe_GM', 'PIP2_GM_GM', 'ER_erMembrane', 'Ca_ER', 'Sos_cyt', 'Grb2_cyt', 'PLCe_cyt', 'buffer_cyt', 'ca_buffer_cyt', 'SosGrb2_cyt', 'SGS_PM', 'RasGTP_PM', 'RasGDP_PM', 'RasGRP_cyt', 'CaRasGRP1_cyt']
    _SPECIES_LABELS = {'RasGTP_Golgi_GM': 'RasGTP Golgi GM', 'EGF_EC': 'EGF EC', 'CAPRI_cyt': 'CAPRI Cyt', 'serca': 'Serca', 'PIP_PM': 'PIP PM', 'PI_PM': 'PI PM', 'Shc_PM': 'Shc PM', 'CaCAPRI_PM_PM': 'CaCAPRI PM PM', 'RactCa': 'RactCa', 'Shc_star_PM': 'Shc Star PM', 'EGFR_PM': 'EGFR PM', 'PLC_act_PM': 'PLC Act PM', 'RasGTP_pal_cyt': 'RasGTP Pal Cyt', 'PLC_PM': 'PLC PM', 'PIP2_PM': 'PIP2 PM', 'Activated_EGFR_PM': 'Activated EGFR PM', 'Ca': 'Ca', 'Ract': 'Ract', 'Rinh': 'Rinh', 'RinhCa': 'RinhCa', 'IP3': 'IP3', 'RasGDP_Golgi_GM': 'RasGDP Golgi GM', 'Ca_RasGRP_GM_GM': 'Ca RasGRP GM GM', 'DAG_GM_GM': 'DAG GM GM', 'RasGRP_DAG_GM': 'RasGRP DAG GM', 'CaCAPRI_cyt': 'CaCAPRI Cyt', 'DAG_PM': 'DAG PM', 'RasGTP_depal_cyt': 'RasGTP Depal Cyt', 'RasGDP_depal_cyt': 'RasGDP Depal Cyt', 'RasGDP_pal_cyt': 'RasGDP Pal Cyt', 'Ca_PLCe_cyt': 'Ca PLCe Cyt', 'Ras_CaPLCe_GM': 'RAS CaPLCe GM', 'PIP2_GM_GM': 'PIP2 GM GM', 'ER_erMembrane': 'ER ErMembrane', 'Ca_ER': 'Ca ER', 'Sos_cyt': 'Sos Cyt', 'Grb2_cyt': 'Grb2 Cyt', 'PLCe_cyt': 'PLCe Cyt', 'buffer_cyt': 'Buffer Cyt', 'ca_buffer_cyt': 'Ca Buffer Cyt', 'SosGrb2_cyt': 'SosGrb2 Cyt', 'SGS_PM': 'SGS PM', 'RasGTP_PM': 'RasGTP PM', 'RasGDP_PM': 'RasGDP PM', 'RasGRP_cyt': 'RasGRP Cyt', 'CaRasGRP1_cyt': 'CaRasGRP1 Cyt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ract_ca': ('RactCa', 2.264, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RactCa`.'), 'initial_ca_er': ('Ca_ER', 120400.0, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_ER`.'), 'initial_serca': ('serca', 45.0, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `serca`.'), 'initial_capri_cyt': ('CAPRI_cyt', 30.1, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CAPRI_cyt`.'), 'initial_rinh_ca': ('RinhCa', 3.5375, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RinhCa`.'), 'initial_ras_ca_pl_ce_gm': ('Ras_CaPLCe_GM', 0.0, 'molecules', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ras_CaPLCe_GM`.')}
    _HEADLINE_OUTPUTS = {'ract_ca': ('RactCa', 'molecules', 'RactCa. Maps to SBML symbol `RactCa`.'), 'ca_er': ('Ca_ER', 'molecules', 'Ca ER. Maps to SBML symbol `Ca_ER`.'), 'serca': ('serca', 'molecules', 'Serca. Maps to SBML symbol `serca`.'), 'capri_cyt': ('CAPRI_cyt', 'molecules', 'CAPRI Cyt. Maps to SBML symbol `CAPRI_cyt`.'), 'rinh_ca': ('RinhCa', 'molecules', 'RinhCa. Maps to SBML symbol `RinhCa`.'), 'ras_ca_pl_ce_gm': ('Ras_CaPLCe_GM', 'molecules', 'RAS CaPLCe GM. Maps to SBML symbol `Ras_CaPLCe_GM`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000161.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
