# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Barr2017 - Dynamics of p21 in hTert-RPE1 cells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Barr2017DynamicsOfP21InHtertRpe1CellsBiomd0000000660Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Barr2017 - Dynamics of p21 in hTert-RPE1 cells."""

    _SBML_ID = 'BIOMD0000000660'
    _TITLE = 'Barr2017 - Dynamics of p21 in hTert-RPE1 cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['MrnaP21', 'MrnaCy', 'MrnaP53', 'P21', 'Cy', 'CyP21', 'aPcna', 'Rc', 'pRc', 'aRc', 'iRc', 'Dna', 'Dam', 'P53', 'Skp2', 'Cdt2', 'iPcna', 'tP21', 'tCy', 'tPcna']
    _SPECIES_LABELS = {'MrnaP21': 'MrnaP21', 'MrnaCy': 'MrnaCy', 'MrnaP53': 'MrnaP53', 'P21': 'P21', 'Cy': 'Cy', 'CyP21': 'CyP21', 'aPcna': 'aPcna', 'Rc': 'Rc', 'pRc': 'pRc', 'aRc': 'aRc', 'iRc': 'iRc', 'Dna': 'Dna', 'Dam': 'Dam', 'P53': 'P53', 'Skp2': 'Skp2', 'Cdt2': 'Cdt2', 'iPcna': 'iPcna', 'tP21': 'tP21', 'tCy': 'tCy', 'tPcna': 'tPcna'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mrna_p53': ('MrnaP53', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MrnaP53`.'), 'initial_mrna_p21': ('MrnaP21', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MrnaP21`.'), 'initial_mrna_cy': ('MrnaCy', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MrnaCy`.'), 'initial_t_p21': ('tP21', 0.72, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tP21`.'), 'initial_t_pcna': ('tPcna', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `tPcna`.'), 'initial_a_pcna': ('aPcna', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `aPcna`.')}
    _HEADLINE_OUTPUTS = {'mrna_p53': ('MrnaP53', 'native SBML value', 'MrnaP53. Maps to SBML symbol `MrnaP53`.'), 'mrna_p21': ('MrnaP21', 'native SBML value', 'MrnaP21. Maps to SBML symbol `MrnaP21`.'), 'mrna_cy': ('MrnaCy', 'native SBML value', 'MrnaCy. Maps to SBML symbol `MrnaCy`.'), 't_p21': ('tP21', 'native SBML value', 'tP21. Maps to SBML symbol `tP21`.'), 't_pcna': ('tPcna', 'native SBML value', 'tPcna. Maps to SBML symbol `tPcna`.'), 'a_pcna': ('aPcna', 'native SBML value', 'aPcna. Maps to SBML symbol `aPcna`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000660.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
