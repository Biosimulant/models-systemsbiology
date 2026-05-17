# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nucleus Pulposus Regulatory Network."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class NucleusPulposusRegulatoryNetworkModel2411040001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nucleus Pulposus Regulatory Network."""

    _SBML_ID = 'MODEL2411040001'
    _TITLE = 'Nucleus Pulposus Regulatory Network'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ACAN', 'COL1A', 'COL2A', 'COL10A1', 'IFN_gamma', 'TNF', 'IL_1alpha', 'IL_1beta', 'IL_6', 'IL_8', 'IL_12A', 'IL_17A', 'IL_18', 'IL_1RA', 'IL_4', 'IL_10', 'CCL', 'CCL22', 'TGF_beta', 'CCN2', 'IGF1', 'CSF2', 'GDF5', 'PGRN', 'MMP1', 'MMP2', 'MMP3', 'MMP9', 'MMP13', 'ADAMTS4_5', 'TIMP1_2', 'TIMP3', 'VEGF']
    _SPECIES_LABELS = {'ACAN': 'ACAN', 'COL1A': 'COL1A', 'COL2A': 'COL2A', 'COL10A1': 'COL10A1', 'IFN_gamma': 'IFN-γ', 'TNF': 'TNF', 'IL_1alpha': 'IL-1α', 'IL_1beta': 'IL-1β', 'IL_6': 'IL-6', 'IL_8': 'IL-8', 'IL_12A': 'IL-12A', 'IL_17A': 'IL-17A', 'IL_18': 'IL-18', 'IL_1RA': 'IL-1RA', 'IL_4': 'IL-4', 'IL_10': 'IL-10', 'CCL': 'CCL', 'CCL22': 'CCL22', 'TGF_beta': 'TGF-β', 'CCN2': 'CCN2', 'IGF1': 'IGF1', 'CSF2': 'CSF2', 'GDF5': 'GDF5', 'PGRN': 'PGRN', 'MMP1': 'MMP1', 'MMP2': 'MMP2', 'MMP3': 'MMP3', 'MMP9': 'MMP9', 'MMP13': 'MMP13', 'ADAMTS4_5': 'ADAMTS4/5', 'TIMP1_2': 'TIMP1/2', 'TIMP3': 'TIMP3', 'VEGF': 'VEGF'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_il_17_a': ('IL_17A', 0.969909852161994, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_17A`.'), 'initial_il_1': ('IL_1beta', 0.866176145774935, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_1beta`.'), 'initial_il_18': ('IL_18', 0.832442640800422, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_18`.'), 'initial_il_8': ('IL_8', 0.708072577796045, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_8`.'), 'initial_timp1_2': ('TIMP1_2', 0.607544851901438, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TIMP1_2`.'), 'initial_il_6': ('IL_6', 0.601115011743209, 'molar', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL_6`.')}
    _HEADLINE_OUTPUTS = {'il_17_a': ('IL_17A', 'molar', 'IL-17A. Maps to SBML symbol `IL_17A`.'), 'il_1': ('IL_1beta', 'molar', 'IL-1β. Maps to SBML symbol `IL_1beta`.'), 'il_18': ('IL_18', 'molar', 'IL-18. Maps to SBML symbol `IL_18`.'), 'il_8': ('IL_8', 'molar', 'IL-8. Maps to SBML symbol `IL_8`.'), 'timp1_2': ('TIMP1_2', 'molar', 'TIMP1/2. Maps to SBML symbol `TIMP1_2`.'), 'il_6': ('IL_6', 'molar', 'IL-6. Maps to SBML symbol `IL_6`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2411040001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
