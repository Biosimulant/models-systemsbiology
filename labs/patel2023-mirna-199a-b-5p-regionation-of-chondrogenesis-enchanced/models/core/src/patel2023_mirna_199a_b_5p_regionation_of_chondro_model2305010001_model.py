# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Patel2023 - miRNA-199a/b-5p regionation of chondrogenesis - enchanced."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Patel2023Mirna199aB5pRegionationOfChondroModel2305010001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Patel2023 - miRNA-199a/b-5p regionation of chondrogenesis - enchanced."""

    _SBML_ID = 'MODEL2305010001'
    _TITLE = 'Patel2023 - miRNA-199a/b-5p regionation of chondrogenesis - enchanced'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['SRC', 'MIR199b_5p', 'Cav1', 'TGFB3', 'HP199b', 'Sox9mRNA', 'Acan', 'Col2a1', 'MIR199a_5p', 'MIR140_5p', 'HP199a', 'SOX9Protein', 'SOX9PhosphoProtein', 'GAG', 'FZD6', 'ITGA3', 'OtherTargets', 'OtherTargetsRegulators']
    _SPECIES_LABELS = {'SRC': 'SRC', 'MIR199b_5p': 'MIR199b_5p', 'Cav1': 'CAV1', 'TGFB3': 'TGFB3', 'HP199b': 'HP199b', 'Sox9mRNA': 'SOX9mRNA', 'Acan': 'ACAN', 'Col2a1': 'COL2A1', 'MIR199a_5p': 'MIR199a_5p', 'MIR140_5p': 'MIR140_5p', 'HP199a': 'HP199a', 'SOX9Protein': 'SOX9Protein', 'SOX9PhosphoProtein': 'SOX9PhosphoProtein', 'GAG': 'GAG', 'FZD6': 'FZD6', 'ITGA3': 'ITGA3', 'OtherTargets': 'OtherTargets', 'OtherTargetsRegulators': 'OtherTargetsRegulators'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cav1': ('Cav1', 13.21139434, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cav1`.'), 'initial_acan': ('Acan', 6.257096819, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Acan`.'), 'initial_tgfb3': ('TGFB3', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFB3`.'), 'initial_mir199a_5p': ('MIR199a_5p', 10.5401385, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MIR199a_5p`.'), 'initial_sox9mrna': ('Sox9mRNA', 8.76039807, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sox9mRNA`.'), 'initial_mir140_5p': ('MIR140_5p', 6.5582925, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MIR140_5p`.')}
    _HEADLINE_OUTPUTS = {'cav1': ('Cav1', 'native SBML value', 'CAV1. Maps to SBML symbol `Cav1`.'), 'acan': ('Acan', 'native SBML value', 'ACAN. Maps to SBML symbol `Acan`.'), 'tgfb3': ('TGFB3', 'native SBML value', 'TGFB3. Maps to SBML symbol `TGFB3`.'), 'mir199a_5p': ('MIR199a_5p', 'native SBML value', 'MIR199a_5p. Maps to SBML symbol `MIR199a_5p`.'), 'sox9mrna': ('Sox9mRNA', 'native SBML value', 'SOX9mRNA. Maps to SBML symbol `Sox9mRNA`.'), 'mir140_5p': ('MIR140_5p', 'native SBML value', 'MIR140_5p. Maps to SBML symbol `MIR140_5p`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2305010001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
