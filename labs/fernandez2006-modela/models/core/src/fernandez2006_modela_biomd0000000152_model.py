# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fernandez2006_ModelA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fernandez2006ModelaBiomd0000000152Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fernandez2006_ModelA."""

    _SBML_ID = 'BIOMD0000000152'
    _TITLE = 'Fernandez2006_ModelA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['D', 'CDK5', 'D_CDK5', 'D75', 'CK1', 'D_CK1', 'D137', 'PKA', 'D_PKA', 'D34', 'D34_CDK5', 'D34_CK1', 'PP2B', 'D34_PP2B', 'D34_75', 'D34_137', 'D75CK1', 'D75_PKA', 'PP2A', 'D75_PP2A', 'PP2AP', 'D75_PP2AP', 'D75_137', 'D137_CDK5', 'D137_PKA', 'D137_PP2C', 'PP2C', 'D34_75_CK1', 'D34_137_CDK5', 'D34_75_137', 'D75_137_PKA', 'D34_75_PP2B', 'D34_137_PP2B', 'D34_75_137_PP2B', 'D34_75_PP2A', 'D75_137_PP2A', 'D34_75_134_PP2A', 'D34_75_PP2AP', 'D75_137_PP2AP', 'D34_75_137_PP2AP', 'D34_137_PP2C', 'D75_137_PP2C', 'PDE', 'PP2Binactive', 'D34_75_137_PP2C', 'CK1P', 'CK1P_PP2B', 'PDE_PKA', 'PDEP', 'PP2A_PKA', 'Ca', 'PP2BinactiveCa2', 'R2C2', 'cAMP', 'cAMP_R2C2', 'cAMP2_R2C2', 'cAMP3_R2C2', 'cAMP4_R2C2', 'cAMP4_R2C', 'cAMP4_R2', 'cAMP_PDE', 'AMP', 'cAMP_PDEP', 'Empty']
    _SPECIES_LABELS = {'D': 'D', 'CDK5': 'CDK5', 'D_CDK5': 'D_CDK5', 'D75': 'D75', 'CK1': 'CK1', 'D_CK1': 'D_CK1', 'D137': 'D137', 'PKA': 'PKA', 'D_PKA': 'D_PKA', 'D34': 'D34', 'D34_CDK5': 'D34_CDK5', 'D34_CK1': 'D34_CK1', 'PP2B': 'PP2B', 'D34_PP2B': 'D34_PP2B', 'D34_75': 'D34:75', 'D34_137': 'D34:137', 'D75CK1': 'D75_CK1', 'D75_PKA': 'D75_PKA', 'PP2A': 'PP2A', 'D75_PP2A': 'D75_PP2A', 'PP2AP': 'PP2AP', 'D75_PP2AP': 'D75_PP2AP', 'D75_137': 'D75:137', 'D137_CDK5': 'D137_CDK5', 'D137_PKA': 'D137_PKA', 'D137_PP2C': 'D137_PP2C', 'PP2C': 'PP2C', 'D34_75_CK1': 'D34:75_CK1', 'D34_137_CDK5': 'D34:137_CDK5', 'D34_75_137': 'D34:75:137', 'D75_137_PKA': 'D75:137_PKA', 'D34_75_PP2B': 'D34:75_PP2B', 'D34_137_PP2B': 'D34:137_PP2B', 'D34_75_137_PP2B': 'D34:75:137_PP2B', 'D34_75_PP2A': 'D34:75_PP2A', 'D75_137_PP2A': 'D75:137_PP2A', 'D34_75_134_PP2A': 'D34:75:137_PP2A', 'D34_75_PP2AP': 'D34:75_PP2AP', 'D75_137_PP2AP': 'D75:137_PP2AP', 'D34_75_137_PP2AP': 'D34:75:137_PP2AP', 'D34_137_PP2C': 'D34:137_PP2C', 'D75_137_PP2C': 'D75:137_PP2C', 'PDE': 'PDE', 'PP2Binactive': 'PP2Binactive', 'D34_75_137_PP2C': 'D34:75:137_PP2C', 'CK1P': 'CK1P', 'CK1P_PP2B': 'CK1P_PP2B', 'PDE_PKA': 'PDE_PKA', 'PDEP': 'PDEP', 'PP2A_PKA': 'PP2A_PKA', 'Ca': 'Ca', 'PP2BinactiveCa2': 'PP2BinactiveCa2', 'R2C2': 'R2C2', 'cAMP': 'cAMP', 'cAMP_R2C2': 'cAMP_R2C2', 'cAMP2_R2C2': 'cAMP2_R2C2', 'cAMP3_R2C2': 'cAMP3_R2C2', 'cAMP4_R2C2': 'cAMP4_R2C2', 'cAMP4_R2C': 'cAMP4_R2C', 'cAMP4_R2': 'cAMP4_R2', 'cAMP_PDE': 'cAMP_PDE', 'AMP': 'AMP', 'cAMP_PDEP': 'cAMP_PDEP', 'Empty': 'Empty'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_camp_r2_c2': ('cAMP_R2C2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP_R2C2`.'), 'initial_camp_pdep': ('cAMP_PDEP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP_PDEP`.'), 'initial_camp_pde': ('cAMP_PDE', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP_PDE`.'), 'initial_camp4_r2_c2': ('cAMP4_R2C2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP4_R2C2`.'), 'initial_camp4_r2_c': ('cAMP4_R2C', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP4_R2C`.'), 'initial_camp4_r2': ('cAMP4_R2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cAMP4_R2`.')}
    _HEADLINE_OUTPUTS = {'camp_r2_c2': ('cAMP_R2C2', 'native SBML value', 'cAMP_R2C2. Maps to SBML symbol `cAMP_R2C2`.'), 'camp_pdep': ('cAMP_PDEP', 'native SBML value', 'cAMP_PDEP. Maps to SBML symbol `cAMP_PDEP`.'), 'camp_pde': ('cAMP_PDE', 'native SBML value', 'cAMP_PDE. Maps to SBML symbol `cAMP_PDE`.'), 'camp4_r2_c2': ('cAMP4_R2C2', 'native SBML value', 'cAMP4_R2C2. Maps to SBML symbol `cAMP4_R2C2`.'), 'camp4_r2_c': ('cAMP4_R2C', 'native SBML value', 'cAMP4_R2C. Maps to SBML symbol `cAMP4_R2C`.'), 'camp4_r2': ('cAMP4_R2', 'native SBML value', 'cAMP4_R2. Maps to SBML symbol `cAMP4_R2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000152.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
