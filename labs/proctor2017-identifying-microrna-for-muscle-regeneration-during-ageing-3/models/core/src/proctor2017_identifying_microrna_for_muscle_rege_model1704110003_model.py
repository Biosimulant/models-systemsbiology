# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir143_in_muscle)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017IdentifyingMicrornaForMuscleRegeModel1704110003Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir143_in_muscle)."""

    _SBML_ID = 'MODEL1704110003'
    _TITLE = 'Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir143_in_muscle)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Akt', 'Akt_P', 'Igf2', 'Igf2_Igfbp5', 'Igfbp5', 'Igfbp5_mRNA', 'Igfbp5_mRNA_miR143', 'IL6', 'miR143', 'miR143_gene', 'miR143_gene_IL6', 'miR143_gene_MyoD', 'MyoD', 'Myogenin', 'Sink', 'Source']
    _SPECIES_LABELS = {'Akt': 'Akt', 'Akt_P': 'Akt P', 'Igf2': 'Igf2', 'Igf2_Igfbp5': 'Igf2 Igfbp5', 'Igfbp5': 'Igfbp5', 'Igfbp5_mRNA': 'Igfbp5 MRNA', 'Igfbp5_mRNA_miR143': 'Igfbp5 MRNA MiR143', 'IL6': 'IL6', 'miR143': 'MiR143', 'miR143_gene': 'MiR143 Gene', 'miR143_gene_IL6': 'MiR143 Gene IL6', 'miR143_gene_MyoD': 'MiR143 Gene MyoD', 'MyoD': 'MyoD', 'Myogenin': 'Myogenin', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_myo_d': ('MyoD', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`.'), 'initial_igf2': ('Igf2', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Igf2`.'), 'initial_model_state_il6': ('IL6', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL6`.'), 'initial_mi_r143': ('miR143', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR143`.'), 'initial_igfbp5': ('Igfbp5', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Igfbp5`.'), 'initial_model_state_akt': ('Akt', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Akt`.')}
    _HEADLINE_OUTPUTS = {'myo_d': ('MyoD', 'native SBML value', 'MyoD. Maps to SBML symbol `MyoD`.'), 'igf2': ('Igf2', 'native SBML value', 'Igf2. Maps to SBML symbol `Igf2`.'), 'il6': ('IL6', 'native SBML value', 'IL6. Maps to SBML symbol `IL6`.'), 'mi_r143': ('miR143', 'native SBML value', 'MiR143. Maps to SBML symbol `miR143`.'), 'igfbp5': ('Igfbp5', 'native SBML value', 'Igfbp5. Maps to SBML symbol `Igfbp5`.'), 'akt': ('Akt', 'native SBML value', 'Akt. Maps to SBML symbol `Akt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1704110003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
