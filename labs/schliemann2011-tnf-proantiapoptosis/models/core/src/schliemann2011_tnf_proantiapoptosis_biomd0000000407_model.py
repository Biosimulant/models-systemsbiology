# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Schliemann2011_TNF_ProAntiApoptosis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schliemann2011TnfProantiapoptosisBiomd0000000407Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Schliemann2011_TNF_ProAntiApoptosis."""

    _SBML_ID = 'BIOMD0000000407'
    _TITLE = 'Schliemann2011_TNF_ProAntiApoptosis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TNFR_E', 'TNF_E', 'TNF_TNFR_E', 'TNFR', 'RIP', 'TRADD', 'TRAF2', 'FADD', 'TNF_TNFR_TRADD', 'TNFRC1', 'TNFRCint1', 'TNFRCint2', 'TNFRCint3', 'TNFRC2', 'FLIP', 'TNFRC2_FLIP', 'TNFRC2_pCasp8', 'TNFRC2_FLIP_FLIP', 'TNFRC2_pCasp8_pCasp8', 'TNFRC2_FLIP_pCasp8', 'TNFRC2_FLIP_pCasp8_RIP_TRAF2', 'IKK', 'IKKa', 'A20', 'NFkB', 'IkBa', 'IkBa_NFkB', 'PIkBa', 'NFkB_N', 'IkBa_N', 'IkBa_NFkB_N', 'A20_mRNA', 'IkBa_mRNA', 'XIAP_mRNA', 'FLIP_mRNA', 'BAR', 'XIAP', 'pCasp8', 'pCasp3', 'pCasp6', 'Casp8', 'Casp3', 'Casp6', 'BAR_Casp8', 'XIAP_Casp3', 'PARP', 'cPARP']
    _SPECIES_LABELS = {'TNFR_E': 'TNFR_E', 'TNF_E': 'TNF_E', 'TNF_TNFR_E': 'TNF:TNFR_E', 'TNFR': 'TNFR', 'RIP': 'RIP', 'TRADD': 'TRADD', 'TRAF2': 'TRAF2', 'FADD': 'FADD', 'TNF_TNFR_TRADD': 'TNF:TNFR:TRADD', 'TNFRC1': 'TNFRC1', 'TNFRCint1': 'TNFRCint1', 'TNFRCint2': 'TNFRCint2', 'TNFRCint3': 'TNFRCint3', 'TNFRC2': 'TNFRC2', 'FLIP': 'FLIP', 'TNFRC2_FLIP': 'TNFRC2:FLIP', 'TNFRC2_pCasp8': 'TNFRC2:pCasp8', 'TNFRC2_FLIP_FLIP': 'TNFRC2:FLIP:FLIP', 'TNFRC2_pCasp8_pCasp8': 'TNFRC2:pCasp8:pCasp8', 'TNFRC2_FLIP_pCasp8': 'TNFRC2:FLIP:pCasp8', 'TNFRC2_FLIP_pCasp8_RIP_TRAF2': 'TNFRC2:FLIP:pCasp8:RIP:TRAF2', 'IKK': 'IKK', 'IKKa': 'IKKa', 'A20': 'A20', 'NFkB': 'NFkB', 'IkBa': 'IkBa', 'IkBa_NFkB': 'IkBa:NFkB', 'PIkBa': 'PIkBa', 'NFkB_N': 'NFkB_N', 'IkBa_N': 'IkBa_N', 'IkBa_NFkB_N': 'IkBa:NFkB_N', 'A20_mRNA': 'A20_mRNA', 'IkBa_mRNA': 'IkBa_mRNA', 'XIAP_mRNA': 'XIAP_mRNA', 'FLIP_mRNA': 'FLIP_mRNA', 'BAR': 'BAR', 'XIAP': 'XIAP', 'pCasp8': 'pCasp8', 'pCasp3': 'pCasp3', 'pCasp6': 'pCasp6', 'Casp8': 'Casp8', 'Casp3': 'Casp3', 'Casp6': 'Casp6', 'BAR_Casp8': 'BAR:Casp8', 'XIAP_Casp3': 'XIAP:Casp3', 'PARP': 'PARP', 'cPARP': 'cPARP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p_casp8': ('pCasp8', 3.2, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pCasp8`.'), 'initial_p_casp3': ('pCasp3', 0.8, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pCasp3`.'), 'initial_tnf_e': ('TNF_E', 0.2688, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNF_E`.'), 'initial_p_casp6': ('pCasp6', 0.064, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pCasp6`.'), 'initial_ik_ba_n_fk_b': ('IkBa_NFkB', 0.0151032, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkBa_NFkB`.'), 'initial_tnfr_e': ('TNFR_E', 0.005, 'a_mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNFR_E`.')}
    _HEADLINE_OUTPUTS = {'p_casp8': ('pCasp8', 'a_mole', 'pCasp8. Maps to SBML symbol `pCasp8`.'), 'p_casp3': ('pCasp3', 'a_mole', 'pCasp3. Maps to SBML symbol `pCasp3`.'), 'tnf_e': ('TNF_E', 'a_mole', 'TNF_E. Maps to SBML symbol `TNF_E`.'), 'p_casp6': ('pCasp6', 'a_mole', 'pCasp6. Maps to SBML symbol `pCasp6`.'), 'ik_ba_n_fk_b': ('IkBa_NFkB', 'a_mole', 'IkBa:NFkB. Maps to SBML symbol `IkBa_NFkB`.'), 'tnfr_e': ('TNFR_E', 'a_mole', 'TNFR_E. Maps to SBML symbol `TNFR_E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000407.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
