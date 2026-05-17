# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nag2011_ChloroplasticStarchDegradation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nag2011ChloroplasticstarchdegradationBiomd0000000353Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nag2011_ChloroplasticStarchDegradation."""

    _SBML_ID = 'BIOMD0000000353'
    _TITLE = 'Nag2011_ChloroplasticStarchDegradation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cpd_C00080_CY', 'cpd_C00369_CS', 'cpd_C00369Glc_CS', 'cpd_C00369db_CS', 'cpd_C00208_CY', 'cpd_C00208_CS', 'cpd_C01835_CS', 'cpd_G00343_CS', 'cpd_C00031_CS', 'cpd_C00031_CY', 'cpd_C00569_CY', 'cpd_C00569Glc_CY', 'cpd_C00002tot_CY', 'cpd_C00008tot_CY', 'cpd_C00009tot_CY', 'cpd_C00051_CY', 'cpd_C00660tot_CY', 'cpd_C03339tot_CY', 'cpd_C00103tot_CY', 'cpd_C00092tot_CY', 'ec_3_2_1_2_CS', 'ec_3_2_1_68_CS', 'ec_2_4_1_25_CS', 'ec_2_4_1_25_CY', 'ec_2_4_1_1_CY', 'ec_2_7_1_1_CY', 'tc_2_A_84_1_2_CIMS', 'tc_2_A_1_1_17_CIMS']
    _SPECIES_LABELS = {'cpd_C00080_CY': 'H+', 'cpd_C00369_CS': 'Starch', 'cpd_C00369Glc_CS': 'Starch Glucosyl unit', 'cpd_C00369db_CS': 'Starch exposed to Beta Amylase due to action of Isoamylase (Starch DB)', 'cpd_C00208_CY': 'Maltose', 'cpd_C00208_CS': 'Maltose', 'cpd_C01835_CS': 'Maltotriose', 'cpd_G00343_CS': 'Maltopentaose', 'cpd_C00031_CS': '(D)-Glucose', 'cpd_C00031_CY': '(D)-Glucose', 'cpd_C00569_CY': 'Arabinogalactan (AG)', 'cpd_C00569Glc_CY': 'Glucosyl Arabinogalactan (GlcAG)', 'cpd_C00002tot_CY': 'ATP pool', 'cpd_C00008tot_CY': 'ADP pool', 'cpd_C00009tot_CY': 'Orthophosphate(HPi) pool', 'cpd_C00051_CY': 'Glutathione (reduced)', 'cpd_C00660tot_CY': '(D)-Glucose-1,6-bisphosphate pool', 'cpd_C03339tot_CY': '2,3-Bisphosphoglycerate pool', 'cpd_C00103tot_CY': 'G1P pool', 'cpd_C00092tot_CY': 'G6P pool', 'ec_3_2_1_2_CS': 'Beta amylase', 'ec_3_2_1_68_CS': 'Isoamylase', 'ec_2_4_1_25_CS': 'Disproportionating enzyme 1(DPE1)', 'ec_2_4_1_25_CY': 'Disproportionating enzyme 2(DPE2)', 'ec_2_4_1_1_CY': 'Cytosolic Glucan phosphorylase', 'ec_2_7_1_1_CY': 'Hexokinase', 'tc_2_A_84_1_2_CIMS': 'Maltose exporter (MEX)', 'tc_2_A_1_1_17_CIMS': 'Glucose transporter (pGlcT)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp_pool': ('cpd_C00002tot_CY', 1.579698e-08, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cpd_C00002tot_CY`.'), 'initial_adp_pool': ('cpd_C00008tot_CY', 1.579698e-08, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cpd_C00008tot_CY`.'), 'initial_d_glucose_1_6_bisphosphate_pool': ('cpd_C00660tot_CY', 1.579698e-08, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cpd_C00660tot_CY`.'), 'initial_d_glucose': ('cpd_C00031_CY', 1.579698e-11, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cpd_C00031_CY`.'), 'initial_d_glucose_2': ('cpd_C00031_CS', 3.534e-12, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cpd_C00031_CS`.'), 'initial_glucose_transporter_p_glc_t': ('tc_2_A_1_1_17_CIMS', 1.4136e-13, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tc_2_A_1_1_17_CIMS`.')}
    _HEADLINE_OUTPUTS = {'atp_pool': ('cpd_C00002tot_CY', 'substance', 'ATP pool. Maps to SBML symbol `cpd_C00002tot_CY`.'), 'adp_pool': ('cpd_C00008tot_CY', 'substance', 'ADP pool. Maps to SBML symbol `cpd_C00008tot_CY`.'), 'd_glucose_1_6_bisphosphate_pool': ('cpd_C00660tot_CY', 'substance', '(D)-Glucose-1,6-bisphosphate pool. Maps to SBML symbol `cpd_C00660tot_CY`.'), 'd_glucose': ('cpd_C00031_CY', 'substance', '(D)-Glucose. Maps to SBML symbol `cpd_C00031_CY`.'), 'd_glucose_2': ('cpd_C00031_CS', 'substance', '(D)-Glucose. Maps to SBML symbol `cpd_C00031_CS`.'), 'glucose_transporter_p_glc_t': ('tc_2_A_1_1_17_CIMS', 'substance', 'Glucose transporter (pGlcT). Maps to SBML symbol `tc_2_A_1_1_17_CIMS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000353.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
