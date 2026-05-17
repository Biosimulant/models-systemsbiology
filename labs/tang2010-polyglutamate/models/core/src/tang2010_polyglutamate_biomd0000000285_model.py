# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Tang2010_PolyGlutamate."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tang2010PolyglutamateBiomd0000000285Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Tang2010_PolyGlutamate."""

    _SBML_ID = 'BIOMD0000000285'
    _TITLE = 'Tang2010_PolyGlutamate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PolyQ', 'Proteasome', 'NatP', 'MisP', 'MisP_Proteasome', 'AggP1', 'AggP2', 'AggP3', 'AggP4', 'AggP5', 'AggPolyQ1', 'AggPolyQ2', 'AggPolyQ3', 'AggPolyQ4', 'AggPolyQ5', 'SeqAggP', 'AggP_Proteasome', 'mRFPu', 'mRFPu_Proteasome', 'PolyQ_Proteasome', 'ROS', 'p38_P', 'p38', 'Source', 'Sink', 'p38death', 'PIdeath']
    _SPECIES_LABELS = {'PolyQ': 'PolyQ', 'Proteasome': 'Proteasome', 'NatP': 'NatP', 'MisP': 'MisP', 'MisP_Proteasome': 'MisP Proteasome', 'AggP1': 'AggP1', 'AggP2': 'AggP2', 'AggP3': 'AggP3', 'AggP4': 'AggP4', 'AggP5': 'AggP5', 'AggPolyQ1': 'AggPolyQ1', 'AggPolyQ2': 'AggPolyQ2', 'AggPolyQ3': 'AggPolyQ3', 'AggPolyQ4': 'AggPolyQ4', 'AggPolyQ5': 'AggPolyQ5', 'SeqAggP': 'SeqAggP', 'AggP_Proteasome': 'AggP Proteasome', 'mRFPu': 'MRFPu', 'mRFPu_Proteasome': 'MRFPu Proteasome', 'PolyQ_Proteasome': 'PolyQ Proteasome', 'ROS': 'ROS', 'p38_P': 'P38 P', 'p38': 'P38', 'Source': 'Source', 'Sink': 'Sink', 'p38death': 'P38death', 'PIdeath': 'PIdeath'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nat_p': ('NatP', 19500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NatP`.'), 'initial_p_ideath': ('PIdeath', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIdeath`.'), 'initial_p38death': ('p38death', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p38death`.'), 'initial_proteasome': ('Proteasome', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Proteasome`.'), 'initial_poly_q': ('PolyQ', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PolyQ`.'), 'initial_mrf_pu': ('mRFPu', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mRFPu`.')}
    _HEADLINE_OUTPUTS = {'nat_p': ('NatP', 'native SBML value', 'NatP. Maps to SBML symbol `NatP`.'), 'p_ideath': ('PIdeath', 'native SBML value', 'PIdeath. Maps to SBML symbol `PIdeath`.'), 'p38death': ('p38death', 'native SBML value', 'P38death. Maps to SBML symbol `p38death`.'), 'proteasome': ('Proteasome', 'native SBML value', 'Proteasome. Maps to SBML symbol `Proteasome`.'), 'poly_q': ('PolyQ', 'native SBML value', 'PolyQ. Maps to SBML symbol `PolyQ`.'), 'mrf_pu': ('mRFPu', 'native SBML value', 'MRFPu. Maps to SBML symbol `mRFPu`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000285.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
