# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir378_in_muscle)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017IdentifyingMicrornaForMuscleRegeModel1704110002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir378_in_muscle)."""

    _SBML_ID = 'MODEL1704110002'
    _TITLE = 'Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir378_in_muscle)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR378', 'miR378_gene', 'miR378_gene_MyoD', 'miR378_gene_Msc', 'miR378_Msc_mRNA', 'MyoD', 'MyoD_gene', 'MyoD_mRNA', 'Msc', 'Msc_gene', 'Msc_mRNA', 'Sink', 'Source']
    _SPECIES_LABELS = {'miR378': 'MiR378', 'miR378_gene': 'MiR378 Gene', 'miR378_gene_MyoD': 'MiR378 Gene MyoD', 'miR378_gene_Msc': 'MiR378 Gene Msc', 'miR378_Msc_mRNA': 'MiR378 Msc MRNA', 'MyoD': 'MyoD', 'MyoD_gene': 'MyoD Gene', 'MyoD_mRNA': 'MyoD MRNA', 'Msc': 'Msc', 'Msc_gene': 'Msc Gene', 'Msc_mRNA': 'Msc MRNA', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_myo_d': ('MyoD', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`.'), 'initial_model_state_msc': ('Msc', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Msc`.'), 'initial_msc_mrna': ('Msc_mRNA', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Msc_mRNA`.'), 'initial_myo_d_mrna': ('MyoD_mRNA', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_mRNA`.'), 'initial_mi_r378': ('miR378', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR378`.'), 'initial_myo_d_gene': ('MyoD_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_gene`.')}
    _HEADLINE_OUTPUTS = {'myo_d': ('MyoD', 'native SBML value', 'MyoD. Maps to SBML symbol `MyoD`.'), 'msc': ('Msc', 'native SBML value', 'Msc. Maps to SBML symbol `Msc`.'), 'msc_mrna': ('Msc_mRNA', 'native SBML value', 'Msc MRNA. Maps to SBML symbol `Msc_mRNA`.'), 'myo_d_mrna': ('MyoD_mRNA', 'native SBML value', 'MyoD MRNA. Maps to SBML symbol `MyoD_mRNA`.'), 'mi_r378': ('miR378', 'native SBML value', 'MiR378. Maps to SBML symbol `miR378`.'), 'myo_d_gene': ('MyoD_gene', 'native SBML value', 'MyoD Gene. Maps to SBML symbol `MyoD_gene`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1704110002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
