# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Goldbeter1995_CircClock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter1995CircclockBiomd0000000016Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Goldbeter1995_CircClock."""

    _SBML_ID = 'BIOMD0000000016'
    _TITLE = 'Goldbeter1995_CircClock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EmptySet', 'M', 'P0', 'P1', 'P2', 'Pn', 'Pt']
    _SPECIES_LABELS = {'EmptySet': 'EmptySet', 'M': 'PER mRNA', 'P0': 'unphosphorylated PER', 'P1': 'monophosphorylated PER', 'P2': 'biphosphorylated PER', 'Pn': 'nuclear PER', 'Pt': 'total PER'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_per_mrna': ('M', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M`.'), 'initial_total_per': ('Pt', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pt`.'), 'initial_unphosphorylated_per': ('P0', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P0`.'), 'initial_nuclear_per': ('Pn', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pn`.'), 'initial_monophosphorylated_per': ('P1', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1`.'), 'initial_biphosphorylated_per': ('P2', 0.25, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`.')}
    _HEADLINE_OUTPUTS = {'per_mrna': ('M', 'native SBML value', 'PER mRNA. Maps to SBML symbol `M`.'), 'total_per': ('Pt', 'native SBML value', 'total PER. Maps to SBML symbol `Pt`.'), 'unphosphorylated_per': ('P0', 'native SBML value', 'unphosphorylated PER. Maps to SBML symbol `P0`.'), 'nuclear_per': ('Pn', 'native SBML value', 'nuclear PER. Maps to SBML symbol `Pn`.'), 'monophosphorylated_per': ('P1', 'native SBML value', 'monophosphorylated PER. Maps to SBML symbol `P1`.'), 'biphosphorylated_per': ('P2', 'native SBML value', 'biphosphorylated PER. Maps to SBML symbol `P2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000016.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
