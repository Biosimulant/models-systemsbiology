# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mandlik2015 - Tristable genetic circuit of Leishmania."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mandlik2015TristableGeneticCircuitOfLeishmaBiomd0000000584Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mandlik2015 - Tristable genetic circuit of Leishmania."""

    _SBML_ID = 'BIOMD0000000584'
    _TITLE = 'Mandlik2015 - Tristable genetic circuit of Leishmania'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AUR1', 'IPTG', 'LACI', 'LAMDAR', 'SLS1', 'SLS4', 'TETR', 'as1', 'ia1_ActiveTF', 'ia1_InactiveTF', 'ope1', 'p1', 'p2', 'p3', 'pAUR1', 'pSLS1', 'pSLS4', 'proAUR1', 'proLACI', 'proLAMDAR', 'proSLS1', 'proSLS4', 'proTETR', 'rs1', 'rs2', 'rs3', 'rs4', 'rs5', 'rs6', 'ter1', 'ter2', 'ter3', 'ter4', 'ter5', 'ter6']
    _SPECIES_LABELS = {'AUR1': 'AUR1', 'IPTG': 'IPTG', 'LACI': 'LACI', 'LAMDAR': 'LAMDAR', 'SLS1': 'SLS1', 'SLS4': 'SLS4', 'TETR': 'TETR', 'as1': 'as1', 'ia1_ActiveTF': 'ia1_ActiveTF', 'ia1_InactiveTF': 'ia1_InactiveTF', 'ope1': 'ope1', 'p1': 'p1', 'p2': 'p2', 'p3': 'p3', 'pAUR1': 'pAUR1', 'pSLS1': 'pSLS1', 'pSLS4': 'pSLS4', 'proAUR1': 'proAUR1', 'proLACI': 'proLACI', 'proLAMDAR': 'proLAMDAR', 'proSLS1': 'proSLS1', 'proSLS4': 'proSLS4', 'proTETR': 'proTETR', 'rs1': 'rs1', 'rs2': 'rs2', 'rs3': 'rs3', 'rs4': 'rs4', 'rs5': 'rs5', 'rs6': 'rs6', 'ter1': 'ter1', 'ter2': 'ter2', 'ter3': 'ter3', 'ter4': 'ter4', 'ter5': 'ter5', 'ter6': 'ter6'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ia1_inactive_tf': ('ia1_InactiveTF', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ia1_InactiveTF`.'), 'initial_ia1_active_tf': ('ia1_ActiveTF', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ia1_ActiveTF`.'), 'initial_ter6': ('ter6', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ter6`.'), 'initial_ter5': ('ter5', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ter5`.'), 'initial_ter4': ('ter4', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ter4`.'), 'initial_ter3': ('ter3', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ter3`.')}
    _HEADLINE_OUTPUTS = {'ia1_inactive_tf': ('ia1_InactiveTF', 'native SBML value', 'ia1_InactiveTF. Maps to SBML symbol `ia1_InactiveTF`.'), 'ia1_active_tf': ('ia1_ActiveTF', 'native SBML value', 'ia1_ActiveTF. Maps to SBML symbol `ia1_ActiveTF`.'), 'ter6': ('ter6', 'native SBML value', 'ter6. Maps to SBML symbol `ter6`.'), 'ter5': ('ter5', 'native SBML value', 'ter5. Maps to SBML symbol `ter5`.'), 'ter4': ('ter4', 'native SBML value', 'ter4. Maps to SBML symbol `ter4`.'), 'ter3': ('ter3', 'native SBML value', 'ter3. Maps to SBML symbol `ter3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000584.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
