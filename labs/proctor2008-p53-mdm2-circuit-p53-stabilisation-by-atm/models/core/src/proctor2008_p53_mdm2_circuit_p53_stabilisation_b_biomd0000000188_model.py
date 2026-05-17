# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2008 - p53/Mdm2 circuit - p53 stabilisation by ATM."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2008P53Mdm2CircuitP53StabilisationBBiomd0000000188Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2008 - p53/Mdm2 circuit - p53 stabilisation by ATM."""

    _SBML_ID = 'BIOMD0000000188'
    _TITLE = 'Proctor2008 - p53/Mdm2 circuit - p53 stabilisation by ATM'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mdm2', 'p53', 'Mdm2_p53', 'Mdm2_mRNA', 'p53_mRNA', 'ATMA', 'ATMI', 'p53_P', 'Mdm2_P', 'damDNA', 'totp53', 'totMdm2']
    _SPECIES_LABELS = {'Mdm2': 'Mdm2', 'p53': 'P53', 'Mdm2_p53': 'Mdm2 P53', 'Mdm2_mRNA': 'Mdm2 MRNA', 'p53_mRNA': 'P53 MRNA', 'ATMA': 'ATMA', 'ATMI': 'ATMI', 'p53_P': 'P53 P', 'Mdm2_P': 'Mdm2 P', 'damDNA': 'DamDNA', 'totp53': 'Totp53', 'totMdm2': 'TotMdm2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p53_mrna': ('p53_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_mRNA`.'), 'initial_mdm2_mrna': ('Mdm2_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_mRNA`.'), 'initial_atmi': ('ATMI', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATMI`.'), 'initial_mdm2_p53': ('Mdm2_p53', 95.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_p53`.'), 'initial_model_state_p53': ('p53', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`.'), 'initial_mdm2': ('Mdm2', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2`.')}
    _HEADLINE_OUTPUTS = {'p53_mrna': ('p53_mRNA', 'native SBML value', 'P53 MRNA. Maps to SBML symbol `p53_mRNA`.'), 'mdm2_mrna': ('Mdm2_mRNA', 'native SBML value', 'Mdm2 MRNA. Maps to SBML symbol `Mdm2_mRNA`.'), 'atmi': ('ATMI', 'native SBML value', 'ATMI. Maps to SBML symbol `ATMI`.'), 'mdm2_p53': ('Mdm2_p53', 'native SBML value', 'Mdm2 P53. Maps to SBML symbol `Mdm2_p53`.'), 'p53': ('p53', 'native SBML value', 'P53. Maps to SBML symbol `p53`.'), 'mdm2': ('Mdm2', 'native SBML value', 'Mdm2. Maps to SBML symbol `Mdm2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000188.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
