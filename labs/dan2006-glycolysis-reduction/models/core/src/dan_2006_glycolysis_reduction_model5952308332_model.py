# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Danø2006_Glycolysis_Reduction."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dan2006GlycolysisReductionModel5952308332Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Danø2006_Glycolysis_Reduction."""

    _SBML_ID = 'MODEL5952308332'
    _TITLE = 'Danø2006_Glycolysis_Reduction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['source', 'GlcX', 'Glc', 'ATP', 'trioseP', 'ADP', 'NAD', 'BPG', 'NADH', 'ACA', 'ACAX', 'sink']
    _SPECIES_LABELS = {'source': 'source', 'GlcX': 'GlcX', 'Glc': 'Glc', 'ATP': 'ATP', 'trioseP': 'trioseP', 'ADP': 'ADP', 'NAD': 'NAD', 'BPG': 'BPG', 'NADH': 'NADH', 'ACA': 'ACA', 'ACAX': 'ACAX', 'sink': 'sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_aca': ('ACA', 8.332760788, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ACA`.'), 'initial_acax': ('ACAX', 1.312175379, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ACAX`.'), 'initial_triose_p': ('trioseP', 7.847433523, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `trioseP`.'), 'initial_source': ('source', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `source`.'), 'initial_sink': ('sink', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `sink`.'), 'initial_glc_x': ('GlcX', 6.719449303, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GlcX`.')}
    _HEADLINE_OUTPUTS = {'aca': ('ACA', 'native SBML value', 'ACA. Maps to SBML symbol `ACA`.'), 'acax': ('ACAX', 'native SBML value', 'ACAX. Maps to SBML symbol `ACAX`.'), 'triose_p': ('trioseP', 'native SBML value', 'trioseP. Maps to SBML symbol `trioseP`.'), 'source': ('source', 'native SBML value', 'source. Maps to SBML symbol `source`.'), 'sink': ('sink', 'native SBML value', 'sink. Maps to SBML symbol `sink`.'), 'glc_x': ('GlcX', 'native SBML value', 'GlcX. Maps to SBML symbol `GlcX`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL5952308332.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
