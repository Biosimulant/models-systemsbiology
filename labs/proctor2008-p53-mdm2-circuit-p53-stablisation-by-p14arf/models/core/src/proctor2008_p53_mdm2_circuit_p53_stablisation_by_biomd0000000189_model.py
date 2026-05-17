# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2008 - p53/Mdm2 circuit - p53 stablisation by p14ARF."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2008P53Mdm2CircuitP53StablisationByBiomd0000000189Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2008 - p53/Mdm2 circuit - p53 stablisation by p14ARF."""

    _SBML_ID = 'BIOMD0000000189'
    _TITLE = 'Proctor2008 - p53/Mdm2 circuit - p53 stablisation by p14ARF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mdm2', 'p53', 'Mdm2_p53', 'Mdm2_mRNA', 'ARF', 'ARF_Mdm2', 'damDNA', 'Sink', 'Source', 'p53deg', 'p53syn', 'mdm2deg', 'mdm2syn', 'Mdm2mRNAdeg', 'Mdm2mRNAsyn', 'totdamDNA', 'totp53', 'totMdm2']
    _SPECIES_LABELS = {'Mdm2': 'Mdm2', 'p53': 'P53', 'Mdm2_p53': 'Mdm2 P53', 'Mdm2_mRNA': 'Mdm2 MRNA', 'ARF': 'ARF', 'ARF_Mdm2': 'ARF Mdm2', 'damDNA': 'DamDNA', 'Sink': 'Sink', 'Source': 'Source', 'p53deg': 'P53deg', 'p53syn': 'P53syn', 'mdm2deg': 'Mdm2deg', 'mdm2syn': 'Mdm2syn', 'Mdm2mRNAdeg': 'Mdm2mRNAdeg', 'Mdm2mRNAsyn': 'Mdm2mRNAsyn', 'totdamDNA': 'TotdamDNA', 'totp53': 'Totp53', 'totMdm2': 'TotMdm2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mdm2m_rn_adeg': ('Mdm2mRNAdeg', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2mRNAdeg`.'), 'initial_mdm2m_rn_asyn': ('Mdm2mRNAsyn', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2mRNAsyn`.'), 'initial_mdm2_mrna': ('Mdm2_mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_mRNA`.'), 'initial_mdm2_p53': ('Mdm2_p53', 95.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_p53`.'), 'initial_model_state_p53': ('p53', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`.'), 'initial_mdm2': ('Mdm2', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2`.')}
    _HEADLINE_OUTPUTS = {'mdm2m_rn_adeg': ('Mdm2mRNAdeg', 'native SBML value', 'Mdm2mRNAdeg. Maps to SBML symbol `Mdm2mRNAdeg`.'), 'mdm2m_rn_asyn': ('Mdm2mRNAsyn', 'native SBML value', 'Mdm2mRNAsyn. Maps to SBML symbol `Mdm2mRNAsyn`.'), 'mdm2_mrna': ('Mdm2_mRNA', 'native SBML value', 'Mdm2 MRNA. Maps to SBML symbol `Mdm2_mRNA`.'), 'mdm2_p53': ('Mdm2_p53', 'native SBML value', 'Mdm2 P53. Maps to SBML symbol `Mdm2_p53`.'), 'p53': ('p53', 'native SBML value', 'P53. Maps to SBML symbol `p53`.'), 'mdm2': ('Mdm2', 'native SBML value', 'Mdm2. Maps to SBML symbol `Mdm2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000189.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
