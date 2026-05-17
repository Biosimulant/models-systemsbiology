# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Suh2004_KCNQ_Regulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Suh2004KcnqRegulationBiomd0000000081Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Suh2004_KCNQ_Regulation."""

    _SBML_ID = 'BIOMD0000000081'
    _TITLE = 'Suh2004_KCNQ_Regulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GTPgS_C', 'KCNQsites_M', 'PIP2_M', 'GGDPbS_M', 'Mg2_C', 'ATP_C', 'oxoM_EX', 'GDPbS_C', 'GGTPMg_M', 'GDP_C', 'GTP_C', 'GGDPAlF4Mg_M', 'ip3_C', 'AlF4_C', 'G_M', 'GGTP_M', 'GGDPAlF4_M', 'GGTPgS_M', 'PI_M', 'PIP_M', 'PIP2xKCNQ_M', 'GGTPgSMg_M', 'GGDP_M']
    _SPECIES_LABELS = {'GTPgS_C': 'GTPgS_C', 'KCNQsites_M': 'KCNQsites_M', 'PIP2_M': 'PIP2_M', 'GGDPbS_M': 'GGDPbS_M', 'Mg2_C': 'Mg2_C', 'ATP_C': 'ATP_C', 'oxoM_EX': 'oxoM_EX', 'GDPbS_C': 'GDPbS_C', 'GGTPMg_M': 'GGTPMg_M', 'GDP_C': 'GDP_C', 'GTP_C': 'GTP_C', 'GGDPAlF4Mg_M': 'GGDPAIF4Mg_M', 'ip3_C': 'IP3_C', 'AlF4_C': 'AIF4_C', 'G_M': 'G_M', 'GGTP_M': 'GGTP_M', 'GGDPAlF4_M': 'GGDPAIF4_M', 'GGTPgS_M': 'GGTPgS_M', 'PI_M': 'PI_M', 'PIP_M': 'PIP_M', 'PIP2xKCNQ_M': 'PIP2xKCNQ_M', 'GGTPgSMg_M': 'GGTPgSMg_M', 'GGDP_M': 'GGDP_M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp_c': ('ATP_C', 3000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP_C`.'), 'initial_pi_m': ('PI_M', 200000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI_M`.'), 'initial_pip2_m': ('PIP2_M', 5000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP2_M`.'), 'initial_mg2_c': ('Mg2_C', 2100.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mg2_C`.'), 'initial_pip_m': ('PIP_M', 1150.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP_M`.'), 'initial_ggdp_m': ('GGDP_M', 200.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GGDP_M`.')}
    _HEADLINE_OUTPUTS = {'atp_c': ('ATP_C', 'substance', 'ATP_C. Maps to SBML symbol `ATP_C`.'), 'pi_m': ('PI_M', 'substance', 'PI_M. Maps to SBML symbol `PI_M`.'), 'pip2_m': ('PIP2_M', 'substance', 'PIP2_M. Maps to SBML symbol `PIP2_M`.'), 'mg2_c': ('Mg2_C', 'substance', 'Mg2_C. Maps to SBML symbol `Mg2_C`.'), 'pip_m': ('PIP_M', 'substance', 'PIP_M. Maps to SBML symbol `PIP_M`.'), 'ggdp_m': ('GGDP_M', 'substance', 'GGDP_M. Maps to SBML symbol `GGDP_M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000081.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
