# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for stseranidou2024 - Nucleus Pulposus Cell Network Modelling in the Intervertebral Disc."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Stseranidou2024NucleusPulposusCellNetworkMoModel2407080001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for stseranidou2024 - Nucleus Pulposus Cell Network Modelling in the Intervertebral Disc."""

    _SBML_ID = 'MODEL2407080001'
    _TITLE = 'stseranidou2024 - Nucleus Pulposus Cell Network Modelling in the Intervertebral Disc'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ACAN', 'COL2A', 'COL10A1', 'COL1A', 'IFN_gamma', 'TNF', 'IL_12A', 'IL_17A', 'IL_18', 'IL_1alpha', 'IL_1beta', 'IL_6', 'IL_8', 'IL_1RA', 'IL_4', 'IL_10', 'TGF_beta', 'IGF1', 'CSF2', 'GDF5', 'PGRN', 'CCL', 'CCL22', 'MMP1', 'MMP13', 'MMP2', 'MMP3', 'MMP9', 'VEGF', 'ADAMTS4_5', 'TIMP1_2', 'TIMP3']
    _SPECIES_LABELS = {'ACAN': 'ACAN', 'COL2A': 'COL2A', 'COL10A1': 'COL10A1', 'COL1A': 'COL1A', 'IFN_gamma': 'IFN-γ', 'TNF': 'TNF', 'IL_12A': 'IL-12A', 'IL_17A': 'IL-17A', 'IL_18': 'IL-18', 'IL_1alpha': 'IL-1α', 'IL_1beta': 'IL-1β', 'IL_6': 'IL-6', 'IL_8': 'IL-8', 'IL_1RA': 'IL-1RA', 'IL_4': 'IL-4', 'IL_10': 'IL-10', 'TGF_beta': 'TGF-β', 'IGF1': 'IGF1', 'CSF2': 'CSF2', 'GDF5': 'GDF5', 'PGRN': 'PGRN', 'CCL': 'CCL', 'CCL22': 'CCL22', 'MMP1': 'MMP1', 'MMP13': 'MMP13', 'MMP2': 'MMP2', 'MMP3': 'MMP3', 'MMP9': 'MMP9', 'VEGF': 'VEGF', 'ADAMTS4_5': 'ADAMTS4/5', 'TIMP1_2': 'TIMP1/2', 'TIMP3': 'TIMP3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_tnf': ('TNF', 0.242055398721897, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNF`.'), 'initial_il_10': ('IL_10', 0.90617019258096, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_10`.'), 'initial_il_1': ('IL_1beta', 0.864763827973558, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_1beta`.'), 'initial_model_state_tgf': ('TGF_beta', 0.861111547821175, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGF_beta`.'), 'initial_il_8': ('IL_8', 0.782046880665663, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_8`.'), 'initial_il_6': ('IL_6', 0.675385391287549, 'concentration_unit', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_6`.')}
    _HEADLINE_OUTPUTS = {'tnf': ('TNF', 'concentration_unit', 'TNF. Maps to SBML symbol `TNF`.'), 'il_10': ('IL_10', 'concentration_unit', 'IL-10. Maps to SBML symbol `IL_10`.'), 'il_1': ('IL_1beta', 'concentration_unit', 'IL-1β. Maps to SBML symbol `IL_1beta`.'), 'tgf': ('TGF_beta', 'concentration_unit', 'TGF-β. Maps to SBML symbol `TGF_beta`.'), 'il_8': ('IL_8', 'concentration_unit', 'IL-8. Maps to SBML symbol `IL_8`.'), 'il_6': ('IL_6', 'concentration_unit', 'IL-6. Maps to SBML symbol `IL_6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2407080001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
