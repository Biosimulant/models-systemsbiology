# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir1_in_muscle)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2017IdentifyingMicrornaForMuscleRegeModel1704110000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir1_in_muscle)."""

    _SBML_ID = 'MODEL1704110000'
    _TITLE = 'Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir1_in_muscle)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR1', 'miR1_Pax3_mRNA', 'miR1_gene', 'miR1_gene_MyoD', 'MyoD', 'MyoD_gene', 'MyoD_gene_Pax3', 'Pax3', 'Pax3_mRNA', 'Sink', 'Source']
    _SPECIES_LABELS = {'miR1': 'MiR1', 'miR1_Pax3_mRNA': 'MiR1 Pax3 MRNA', 'miR1_gene': 'MiR1 Gene', 'miR1_gene_MyoD': 'MiR1 Gene MyoD', 'MyoD': 'MyoD', 'MyoD_gene': 'MyoD Gene', 'MyoD_gene_Pax3': 'MyoD Gene Pax3', 'Pax3': 'Pax3', 'Pax3_mRNA': 'Pax3 MRNA', 'Sink': 'Sink', 'Source': 'Source'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_myo_d': ('MyoD', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`.'), 'initial_mi_r1': ('miR1', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR1`.'), 'initial_pax3_mrna': ('Pax3_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pax3_mRNA`.'), 'initial_pax3': ('Pax3', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pax3`.'), 'initial_myo_d_gene': ('MyoD_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_gene`.'), 'initial_mi_r1_gene': ('miR1_gene', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR1_gene`.')}
    _HEADLINE_OUTPUTS = {'myo_d': ('MyoD', 'native SBML value', 'MyoD. Maps to SBML symbol `MyoD`.'), 'mi_r1': ('miR1', 'native SBML value', 'MiR1. Maps to SBML symbol `miR1`.'), 'pax3_mrna': ('Pax3_mRNA', 'native SBML value', 'Pax3 MRNA. Maps to SBML symbol `Pax3_mRNA`.'), 'pax3': ('Pax3', 'native SBML value', 'Pax3. Maps to SBML symbol `Pax3`.'), 'myo_d_gene': ('MyoD_gene', 'native SBML value', 'MyoD Gene. Maps to SBML symbol `MyoD_gene`.'), 'mi_r1_gene': ('miR1_gene', 'native SBML value', 'MiR1 Gene. Maps to SBML symbol `miR1_gene`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1704110000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
