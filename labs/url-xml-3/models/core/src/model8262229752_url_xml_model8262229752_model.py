# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for MODEL8262229752_url.xml."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Model8262229752UrlXmlModel8262229752Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for MODEL8262229752_url.xml."""

    _SBML_ID = 'MODEL8262229752'
    _TITLE = 'MODEL8262229752_url.xml'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Nutrients', 'Met', 'SAM', 'SAH', 'Decarb_SAM', 'Putrescine', 'Pfs_mRNA', 'pfs_gene', 'Pfs_prot', 'Adenine', 'SRH', 'LuxS_gene', 'LuxS_mRNA', 'LuxS_prot', 'DPD', 'Homocys', 'MTA', 'Spermidine', 'MTR', 'AI2_intra', 'AI2_extra']
    _SPECIES_LABELS = {'Nutrients': 'Nutrients', 'Met': 'Met', 'SAM': 'SAM', 'SAH': 'SAH', 'Decarb_SAM': 'Decarb SAM', 'Putrescine': 'Putrescine', 'Pfs_mRNA': 'Pfs MRNA', 'pfs_gene': 'Pfs Gene', 'Pfs_prot': 'Pfs Prot', 'Adenine': 'Adenine', 'SRH': 'SRH', 'LuxS_gene': 'LuxS Gene', 'LuxS_mRNA': 'LuxS MRNA', 'LuxS_prot': 'LuxS Prot', 'DPD': 'DPD', 'Homocys': 'Homocys', 'MTA': 'MTA', 'Spermidine': 'Spermidine', 'MTR': 'MTR', 'AI2_intra': 'AI2 Intra', 'AI2_extra': 'AI2 Extra'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_decarb_sam': ('Decarb_SAM', 220.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Decarb_SAM`.'), 'initial_pfs_mrna': ('Pfs_mRNA', 32.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pfs_mRNA`.'), 'initial_lux_s_mrna': ('LuxS_mRNA', 16.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LuxS_mRNA`.'), 'initial_pfs_gene': ('pfs_gene', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pfs_gene`.'), 'initial_lux_s_gene': ('LuxS_gene', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LuxS_gene`.'), 'initial_nutrients': ('Nutrients', 28350.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nutrients`.')}
    _HEADLINE_OUTPUTS = {'decarb_sam': ('Decarb_SAM', 'native SBML value', 'Decarb SAM. Maps to SBML symbol `Decarb_SAM`.'), 'pfs_mrna': ('Pfs_mRNA', 'native SBML value', 'Pfs MRNA. Maps to SBML symbol `Pfs_mRNA`.'), 'lux_s_mrna': ('LuxS_mRNA', 'native SBML value', 'LuxS MRNA. Maps to SBML symbol `LuxS_mRNA`.'), 'pfs_gene': ('pfs_gene', 'native SBML value', 'Pfs Gene. Maps to SBML symbol `pfs_gene`.'), 'lux_s_gene': ('LuxS_gene', 'native SBML value', 'LuxS Gene. Maps to SBML symbol `LuxS_gene`.'), 'nutrients': ('Nutrients', 'native SBML value', 'Nutrients. Maps to SBML symbol `Nutrients`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL8262229752.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
