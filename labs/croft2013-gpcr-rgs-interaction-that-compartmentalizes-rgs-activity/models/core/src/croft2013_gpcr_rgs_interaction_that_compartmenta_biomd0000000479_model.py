# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Croft2013 - GPCR-RGS interaction that compartmentalizes RGS activity."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Croft2013GpcrRgsInteractionThatCompartmentaBiomd0000000479Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Croft2013 - GPCR-RGS interaction that compartmentalizes RGS activity."""

    _SBML_ID = 'BIOMD0000000479'
    _TITLE = 'Croft2013 - GPCR-RGS interaction that compartmentalizes RGS activity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'R', 'LR', 'Gabg', 'RGabg', 'LRGabg', 'RRGSm', 'LRRGSm', 'RRGSmGabg', 'LRRGSmGabg', 'GaGTP', 'Gbg', 'Effector', 'GaGTPEffector', 'RGSc', 'RGSm', 'RGSmGaGTP', 'GaGTPEffectorOFF', 'RGSmGaGTPEffectorOFF', 'GaGDPP', 'LRRGSmGaGTP', 'RRGSmGaGTP', 'LRRGSmGaGTPEffectorOFF', 'GaGDP', 'P', 'z1', 'z2', 'z3']
    _SPECIES_LABELS = {'L': 'L', 'R': 'R', 'LR': 'LR', 'Gabg': 'Gabg', 'RGabg': 'RGabg', 'LRGabg': 'LRGabg', 'RRGSm': 'RRGSm', 'LRRGSm': 'LRRGSm', 'RRGSmGabg': 'RRGSmGabg', 'LRRGSmGabg': 'LRRGSmGabg', 'GaGTP': 'GaGTP', 'Gbg': 'Gbg', 'Effector': 'Effector', 'GaGTPEffector': 'GaGTPEffector', 'RGSc': 'RGSc', 'RGSm': 'RGSm', 'RGSmGaGTP': 'RGSmGaGTP', 'GaGTPEffectorOFF': 'GaGTPEffectorOFF', 'RGSmGaGTPEffectorOFF': 'RGSmGaGTPEffectorOFF', 'GaGDPP': 'GaGDPP', 'LRRGSmGaGTP': 'LRRGSmGaGTP', 'RRGSmGaGTP': 'RRGSmGaGTP', 'LRRGSmGaGTPEffectorOFF': 'LRRGSmGaGTPEffectorOFF', 'GaGDP': 'GaGDP', 'P': 'P', 'z1': 'z1', 'z2': 'z2', 'z3': 'z3'}
    _PARAMETER_INPUTS = {'ligand_conc': ('Ligand_conc', 0.1, 'nanoMolar', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Ligand_conc`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_z3': ('z3', 'nanomole', 'z3. Maps to SBML symbol `z3`.'), 'model_state_z2': ('z2', 'nanomole', 'z2. Maps to SBML symbol `z2`.'), 'model_state_z1': ('z1', 'nanomole', 'z1. Maps to SBML symbol `z1`.'), 'effector': ('Effector', 'nanomole', 'Effector. Maps to SBML symbol `Effector`.'), 'gbg': ('Gbg', 'nanomole', 'Gbg. Maps to SBML symbol `Gbg`.'), 'ga_gdp': ('GaGDP', 'nanomole', 'GaGDP. Maps to SBML symbol `GaGDP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000479.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
