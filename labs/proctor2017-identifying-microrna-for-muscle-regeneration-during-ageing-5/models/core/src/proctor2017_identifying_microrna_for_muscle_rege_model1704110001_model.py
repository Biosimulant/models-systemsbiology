# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir181_in_muscle)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017IdentifyingMicrornaForMuscleRegeModel1704110001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir181_in_muscle)."""

    _SBML_ID = 'MODEL1704110001'
    _TITLE = 'Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir181_in_muscle)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FoxO3', 'FoxO3_Sirt1', 'HoxA11', 'HoxA11_mRNA', 'Mafbx', 'miR181', 'miR181_HoxA11_mRNA', 'miR181_Sirt1_mRNA', 'miR181_gene', 'MyoD', 'MyoD_gene', 'MyoD_gene_FoxO3', 'MyoD_gene_HoxA11', 'MyoD_mRNA', 'Sirt1', 'Sirt1_mRNA', 'Sink', 'Source']
    _SPECIES_LABELS = {'FoxO3': 'FoxO3', 'FoxO3_Sirt1': 'FoxO3 Sirt1', 'HoxA11': 'HoxA11', 'HoxA11_mRNA': 'HoxA11 MRNA', 'Mafbx': 'Mafbx', 'miR181': 'MiR181', 'miR181_HoxA11_mRNA': 'MiR181 HoxA11 MRNA', 'miR181_Sirt1_mRNA': 'MiR181 Sirt1 MRNA', 'miR181_gene': 'MiR181 Gene', 'MyoD': 'MyoD', 'MyoD_gene': 'MyoD Gene', 'MyoD_gene_FoxO3': 'MyoD Gene FoxO3', 'MyoD_gene_HoxA11': 'MyoD Gene HoxA11', 'MyoD_mRNA': 'MyoD MRNA', 'Sirt1': 'Sirt1', 'Sirt1_mRNA': 'Sirt1 MRNA', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_hox_a11': ('HoxA11', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HoxA11`.'), 'initial_sirt1': ('Sirt1', 400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sirt1`.'), 'initial_fox_o3': ('FoxO3', 400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FoxO3`.'), 'initial_sirt1_mrna': ('Sirt1_mRNA', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sirt1_mRNA`.'), 'initial_hox_a11_mrna': ('HoxA11_mRNA', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HoxA11_mRNA`.'), 'initial_fox_o3_sirt1': ('FoxO3_Sirt1', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FoxO3_Sirt1`.')}
    _HEADLINE_OUTPUTS = {'hox_a11': ('HoxA11', 'native SBML value', 'HoxA11. Maps to SBML symbol `HoxA11`.'), 'sirt1': ('Sirt1', 'native SBML value', 'Sirt1. Maps to SBML symbol `Sirt1`.'), 'fox_o3': ('FoxO3', 'native SBML value', 'FoxO3. Maps to SBML symbol `FoxO3`.'), 'sirt1_mrna': ('Sirt1_mRNA', 'native SBML value', 'Sirt1 MRNA. Maps to SBML symbol `Sirt1_mRNA`.'), 'hox_a11_mrna': ('HoxA11_mRNA', 'native SBML value', 'HoxA11 MRNA. Maps to SBML symbol `HoxA11_mRNA`.'), 'fox_o3_sirt1': ('FoxO3_Sirt1', 'native SBML value', 'FoxO3 Sirt1. Maps to SBML symbol `FoxO3_Sirt1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1704110001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
