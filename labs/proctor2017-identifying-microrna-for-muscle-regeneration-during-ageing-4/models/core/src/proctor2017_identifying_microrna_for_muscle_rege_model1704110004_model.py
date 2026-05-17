# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mirs_in_muscle)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017IdentifyingMicrornaForMuscleRegeModel1704110004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mirs_in_muscle)."""

    _SBML_ID = 'MODEL1704110004'
    _TITLE = 'Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mirs_in_muscle)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR1', 'miR1_Pax3_mRNA', 'miR1_gene', 'miR1_gene_MyoD', 'MyoD', 'MyoD_gene', 'MyoD_gene_Pax3', 'Pax3', 'Pax3_mRNA', 'Sink', 'Source', 'FoxO3', 'FoxO3_Sirt1', 'HoxA11', 'HoxA11_mRNA', 'Mafbx', 'miR181', 'miR181_HoxA11_mRNA', 'miR181_Sirt1_mRNA', 'miR181_gene', 'MyoD_gene_FoxO3', 'MyoD_gene_HoxA11', 'Sirt1', 'Sirt1_mRNA', 'miR378', 'miR378_gene', 'miR378_gene_MyoD', 'miR378_gene_Msc', 'miR378_Msc_mRNA', 'MyoD_mRNA', 'Msc', 'Msc_gene', 'Msc_mRNA', 'Akt', 'Akt_P', 'Igf2', 'Igf2_Igfbp5', 'Igfbp5', 'Igfbp5_mRNA', 'Igfbp5_mRNA_miR143', 'IL6', 'miR143', 'miR143_gene', 'miR143_gene_IL6', 'miR143_gene_MyoD', 'Myogenin', 'miR1_gene_Msc', 'miR143_gene_Msc']
    _SPECIES_LABELS = {'miR1': 'MiR1', 'miR1_Pax3_mRNA': 'MiR1 Pax3 MRNA', 'miR1_gene': 'MiR1 Gene', 'miR1_gene_MyoD': 'MiR1 Gene MyoD', 'MyoD': 'MyoD', 'MyoD_gene': 'MyoD Gene', 'MyoD_gene_Pax3': 'MyoD Gene Pax3', 'Pax3': 'Pax3', 'Pax3_mRNA': 'Pax3 MRNA', 'Sink': 'Sink', 'Source': 'Source', 'FoxO3': 'FoxO3', 'FoxO3_Sirt1': 'FoxO3 Sirt1', 'HoxA11': 'HoxA11', 'HoxA11_mRNA': 'HoxA11 MRNA', 'Mafbx': 'Mafbx', 'miR181': 'MiR181', 'miR181_HoxA11_mRNA': 'MiR181 HoxA11 MRNA', 'miR181_Sirt1_mRNA': 'MiR181 Sirt1 MRNA', 'miR181_gene': 'MiR181 Gene', 'MyoD_gene_FoxO3': 'MyoD Gene FoxO3', 'MyoD_gene_HoxA11': 'MyoD Gene HoxA11', 'Sirt1': 'Sirt1', 'Sirt1_mRNA': 'Sirt1 MRNA', 'miR378': 'MiR378', 'miR378_gene': 'MiR378 Gene', 'miR378_gene_MyoD': 'MiR378 Gene MyoD', 'miR378_gene_Msc': 'MiR378 Gene Msc', 'miR378_Msc_mRNA': 'MiR378 Msc MRNA', 'MyoD_mRNA': 'MyoD MRNA', 'Msc': 'Msc', 'Msc_gene': 'Msc Gene', 'Msc_mRNA': 'Msc MRNA', 'Akt': 'Akt', 'Akt_P': 'Akt P', 'Igf2': 'Igf2', 'Igf2_Igfbp5': 'Igf2 Igfbp5', 'Igfbp5': 'Igfbp5', 'Igfbp5_mRNA': 'Igfbp5 MRNA', 'Igfbp5_mRNA_miR143': 'Igfbp5 MRNA MiR143', 'IL6': 'IL6', 'miR143': 'MiR143', 'miR143_gene': 'MiR143 Gene', 'miR143_gene_IL6': 'MiR143 Gene IL6', 'miR143_gene_MyoD': 'MiR143 Gene MyoD', 'Myogenin': 'Myogenin', 'miR1_gene_Msc': 'MiR1 Gene Msc', 'miR143_gene_Msc': 'MiR143 Gene Msc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_myo_d': ('MyoD', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`.'), 'initial_model_state_msc': ('Msc', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Msc`.'), 'initial_igf2': ('Igf2', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Igf2`.'), 'initial_model_state_il6': ('IL6', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL6`.'), 'initial_hox_a11': ('HoxA11', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HoxA11`.'), 'initial_sirt1': ('Sirt1', 400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sirt1`.')}
    _HEADLINE_OUTPUTS = {'myo_d': ('MyoD', 'native SBML value', 'MyoD. Maps to SBML symbol `MyoD`.'), 'msc': ('Msc', 'native SBML value', 'Msc. Maps to SBML symbol `Msc`.'), 'igf2': ('Igf2', 'native SBML value', 'Igf2. Maps to SBML symbol `Igf2`.'), 'il6': ('IL6', 'native SBML value', 'IL6. Maps to SBML symbol `IL6`.'), 'hox_a11': ('HoxA11', 'native SBML value', 'HoxA11. Maps to SBML symbol `HoxA11`.'), 'sirt1': ('Sirt1', 'native SBML value', 'Sirt1. Maps to SBML symbol `Sirt1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1704110004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
