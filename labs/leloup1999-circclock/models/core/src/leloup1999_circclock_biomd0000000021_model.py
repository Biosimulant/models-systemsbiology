# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Leloup1999_CircClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leloup1999CircclockBiomd0000000021Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Leloup1999_CircClock."""

    _SBML_ID = 'BIOMD0000000021'
    _TITLE = 'Leloup1999_CircClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P0', 'T0', 'P1', 'T1', 'P2', 'T2', 'CC', 'Cn', 'Mp', 'Mt']
    _SPECIES_LABELS = {'P0': 'PER Protein (unphosphorylated)', 'T0': 'TIM Protein (unphosphorylated)', 'P1': 'PER Protein (mono-phosphorylated)', 'T1': 'TIM Protein (mono-phosphorylated)', 'P2': 'PER Protein (bi-phosphorylated)', 'T2': 'TIM Protein (bi-phosphorylated)', 'CC': 'Cytosolic PER-TIM Complex', 'Cn': 'Nuclear PER-TIM Complex', 'Mp': 'PER mRNA', 'Mt': 'TIM mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tim_mrna': ('Mt', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mt`.'), 'initial_tim_protein_unphosphorylated': ('T0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T0`.'), 'initial_tim_protein_mono_phosphorylated': ('T1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T1`.'), 'initial_tim_protein_bi_phosphorylated': ('T2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T2`.'), 'initial_per_mrna': ('Mp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mp`.'), 'initial_per_protein_unphosphorylated': ('P0', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P0`.')}
    _HEADLINE_OUTPUTS = {'tim_mrna': ('Mt', 'native SBML value', 'TIM mRNA. Maps to SBML symbol `Mt`.'), 'tim_protein_unphosphorylated': ('T0', 'native SBML value', 'TIM Protein (unphosphorylated). Maps to SBML symbol `T0`.'), 'tim_protein_mono_phosphorylated': ('T1', 'native SBML value', 'TIM Protein (mono-phosphorylated). Maps to SBML symbol `T1`.'), 'tim_protein_bi_phosphorylated': ('T2', 'native SBML value', 'TIM Protein (bi-phosphorylated). Maps to SBML symbol `T2`.'), 'per_mrna': ('Mp', 'native SBML value', 'PER mRNA. Maps to SBML symbol `Mp`.'), 'per_protein_unphosphorylated': ('P0', 'native SBML value', 'PER Protein (unphosphorylated). Maps to SBML symbol `P0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000021.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
