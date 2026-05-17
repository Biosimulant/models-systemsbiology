# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kierzek2001_LacZ."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kierzek2001LaczModel4821294342Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kierzek2001_LacZ."""

    _SBML_ID = 'MODEL4821294342'
    _TITLE = 'Kierzek2001_LacZ'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['LacZ_slash_Protein', 'LacZ_slash_RBS', 'LacZ_slash_RibRBS', 'LacZ_slash_elRIB', 'LacZ_slash_P_RNAP', 'LacZ_slash_P', 'LacZ_slash_ElRNAP', 'LacZ_slash_TrRNAP', 'LacZ_slash_Ribosome', 'LacZ_slash_AAs', 'LacZ_slash_RNAP', 'LacZ_slash_nucleotides']
    _SPECIES_LABELS = {'LacZ_slash_Protein': 'LacZ Slash Protein', 'LacZ_slash_RBS': 'LacZ Slash RBS', 'LacZ_slash_RibRBS': 'LacZ Slash RibRBS', 'LacZ_slash_elRIB': 'LacZ Slash ElRIB', 'LacZ_slash_P_RNAP': 'LacZ Slash P RNAP', 'LacZ_slash_P': 'LacZ Slash P', 'LacZ_slash_ElRNAP': 'LacZ Slash ElRNAP', 'LacZ_slash_TrRNAP': 'LacZ Slash TrRNAP', 'LacZ_slash_Ribosome': 'LacZ Slash Ribosome', 'LacZ_slash_AAs': 'LacZ Slash AAs', 'LacZ_slash_RNAP': 'LacZ Slash RNAP', 'LacZ_slash_nucleotides': 'LacZ Slash Nucleotides'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lac_z_slash_rnap': ('LacZ_slash_RNAP', 0.0583352778425947, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_RNAP`.'), 'initial_lac_z_slash_tr_rnap': ('LacZ_slash_TrRNAP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_TrRNAP`.'), 'initial_lac_z_slash_protein': ('LacZ_slash_Protein', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_Protein`.'), 'initial_lac_z_slash_p_rnap': ('LacZ_slash_P_RNAP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_P_RNAP`.'), 'initial_lac_z_slash_el_rnap': ('LacZ_slash_ElRNAP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_ElRNAP`.'), 'initial_lac_z_slash_ribosome': ('LacZ_slash_Ribosome', 0.583352778425947, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LacZ_slash_Ribosome`.')}
    _HEADLINE_OUTPUTS = {'lac_z_slash_rnap': ('LacZ_slash_RNAP', 'native SBML value', 'LacZ Slash RNAP. Maps to SBML symbol `LacZ_slash_RNAP`.'), 'lac_z_slash_tr_rnap': ('LacZ_slash_TrRNAP', 'native SBML value', 'LacZ Slash TrRNAP. Maps to SBML symbol `LacZ_slash_TrRNAP`.'), 'lac_z_slash_protein': ('LacZ_slash_Protein', 'native SBML value', 'LacZ Slash Protein. Maps to SBML symbol `LacZ_slash_Protein`.'), 'lac_z_slash_p_rnap': ('LacZ_slash_P_RNAP', 'native SBML value', 'LacZ Slash P RNAP. Maps to SBML symbol `LacZ_slash_P_RNAP`.'), 'lac_z_slash_el_rnap': ('LacZ_slash_ElRNAP', 'native SBML value', 'LacZ Slash ElRNAP. Maps to SBML symbol `LacZ_slash_ElRNAP`.'), 'lac_z_slash_ribosome': ('LacZ_slash_Ribosome', 'native SBML value', 'LacZ Slash Ribosome. Maps to SBML symbol `LacZ_slash_Ribosome`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL4821294342.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
