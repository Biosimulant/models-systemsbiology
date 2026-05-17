# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Li2010_YeastGlycolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Li2010YeastglycolysisModel1012110001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Li2010_YeastGlycolysis."""

    _SBML_ID = 'MODEL1012110001'
    _TITLE = 'Li2010_YeastGlycolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M_276', 'M_172', 'M_273', 'M_292', 'M_4', 'M_135', 'M_36', 'M_289', 'M_411', 'M_454', 'M_304', 'M_57', 'M_329', 'M_446', 'M_483', 'M_234', 'M_330', 'M_412', 'M_121', 'M_203', 'E_375', 'Cx_40', 'E_417', 'E_670', 'E_352', 'E_426', 'E_502', 'E_336', 'E_726', 'E_24']
    _SPECIES_LABELS = {'M_276': 'D-Fructose 1,6-bisphosphate', 'M_172': 'ATP', 'M_273': 'D-Fructose 6-phosphate', 'M_292': 'D-Glucose 6-phosphate', 'M_4': '3-Phospho-D-glyceroyl phosphate', 'M_135': 'ADP', 'M_36': 'D-Glycerate 2-phosphate', 'M_289': 'Glyceraldehyde 3-phosphate', 'M_411': 'Nicotinamide adenine dinucleotide', 'M_454': 'Phosphate', 'M_304': 'D-Glucose', 'M_57': '3-Phospho-D-glycerate', 'M_329': 'H+', 'M_446': 'Phosphoenolpyruvate', 'M_483': 'Pyruvate', 'M_234': 'Dihydroxyacetone phosphate', 'M_330': 'H2O', 'M_412': 'Nicotinamide adenine dinucleotide - reduced', 'M_121': 'Acetaldehyde', 'M_203': 'CO2', 'E_375': 'YKL060C', 'Cx_40': 'YGR240C:YMR205C', 'E_417': 'YBR196C', 'E_670': 'YCR012W', 'E_352': 'YGR254W', 'E_426': 'YJL052W', 'E_502': 'YFR053C', 'E_336': 'YKL152C', 'E_726': 'YAL038W', 'E_24': 'YLR044C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_d_glucose': ('M_304', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_304`.'), 'initial_phosphate': ('M_454', 4.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_454`.'), 'initial_nicotinamide_adenine_dinucleotide': ('M_411', 4.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_411`.'), 'initial_model_state_h': ('M_329', 4.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_329`.'), 'initial_model_state_atp': ('M_172', 3.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `M_172`.'), 'initial_yal038_w': ('E_726', 0.29788672074056, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E_726`.')}
    _HEADLINE_OUTPUTS = {'d_glucose': ('M_304', 'native SBML value', 'D-Glucose. Maps to SBML symbol `M_304`.'), 'phosphate': ('M_454', 'native SBML value', 'Phosphate. Maps to SBML symbol `M_454`.'), 'nicotinamide_adenine_dinucleotide': ('M_411', 'native SBML value', 'Nicotinamide adenine dinucleotide. Maps to SBML symbol `M_411`.'), 'model_state_h': ('M_329', 'native SBML value', 'H+. Maps to SBML symbol `M_329`.'), 'atp': ('M_172', 'native SBML value', 'ATP. Maps to SBML symbol `M_172`.'), 'yal038_w': ('E_726', 'native SBML value', 'YAL038W. Maps to SBML symbol `E_726`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1012110001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
