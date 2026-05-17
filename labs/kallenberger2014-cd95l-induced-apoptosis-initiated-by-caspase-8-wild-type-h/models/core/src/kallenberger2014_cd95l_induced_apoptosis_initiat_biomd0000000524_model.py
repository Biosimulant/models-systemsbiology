# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kallenberger2014 - CD95L induced apoptosis initiated by caspase-8, wild-type HeLa cells (cis/trans variant)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kallenberger2014Cd95lInducedApoptosisInitiatBiomd0000000524Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kallenberger2014 - CD95L induced apoptosis initiated by caspase-8, wild-type HeLa cells (cis/trans variant)."""

    _SBML_ID = 'BIOMD0000000524'
    _TITLE = 'Kallenberger2014 - CD95L induced apoptosis initiated by caspase-8, wild-type HeLa cells (cis/trans variant)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CD95', 'FADD', 'p55free', 'Bid', 'PrNES_mCherry', 'PrER_mGFP', 'DISC', 'DISCp55', 'p30', 'p43', 'p18', 'p18inactive', 'tBid', 'PrNES', 'mCherry', 'PrER', 'mGFP', 'CD95L']
    _SPECIES_LABELS = {'CD95': 'CD95', 'FADD': 'FADD', 'p55free': 'p55free', 'Bid': 'Bid', 'PrNES_mCherry': 'PrNES_mCherry', 'PrER_mGFP': 'PrER_mGFP', 'DISC': 'DISC', 'DISCp55': 'DISCp55', 'p30': 'p30', 'p43': 'p43', 'p18': 'p18', 'p18inactive': 'p18inactive', 'tBid': 'tBid', 'PrNES': 'PrNES', 'mCherry': 'mCherry', 'PrER': 'PrER', 'mGFP': 'mGFP', 'CD95L': 'CD95L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pr_er_m_gfp': ('PrER_mGFP', 3316.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PrER_mGFP`.'), 'initial_pr_nes_m_cherry': ('PrNES_mCherry', 1909.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PrNES_mCherry`.'), 'initial_p55free': ('p55free', 127.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p55free`.'), 'initial_t_bid': ('tBid', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tBid`.'), 'initial_model_state_p43': ('p43', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p43`.'), 'initial_model_state_p30': ('p30', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p30`.')}
    _HEADLINE_OUTPUTS = {'pr_er_m_gfp': ('PrER_mGFP', 'native SBML value', 'PrER_mGFP. Maps to SBML symbol `PrER_mGFP`.'), 'pr_nes_m_cherry': ('PrNES_mCherry', 'native SBML value', 'PrNES_mCherry. Maps to SBML symbol `PrNES_mCherry`.'), 'p55free': ('p55free', 'native SBML value', 'p55free. Maps to SBML symbol `p55free`.'), 't_bid': ('tBid', 'native SBML value', 'tBid. Maps to SBML symbol `tBid`.'), 'p43': ('p43', 'native SBML value', 'p43. Maps to SBML symbol `p43`.'), 'p30': ('p30', 'native SBML value', 'p30. Maps to SBML symbol `p30`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000524.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
