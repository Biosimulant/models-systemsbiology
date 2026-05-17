# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Passos2010_DNAdamage_CellularSenescence."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Passos2010DnadamageCellularsenescenceBiomd0000000287Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Passos2010_DNAdamage_CellularSenescence."""

    _SBML_ID = 'BIOMD0000000287'
    _TITLE = 'Passos2010_DNAdamage_CellularSenescence'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mdm2', 'p53', 'Mdm2_p53', 'Mdm2_mRNA', 'p53_mRNA', 'ATMA', 'ATMI', 'p21', 'p21_mRNA', 'p21step1', 'p21step2', 'p53_P', 'Mdm2_P', 'p21_basal', 'p38', 'p38_P', 'GADD45', 'IR', 'damDNA', 'ROS', 'basalROS']
    _SPECIES_LABELS = {'Mdm2': 'Mdm2', 'p53': 'P53', 'Mdm2_p53': 'Mdm2 P53', 'Mdm2_mRNA': 'Mdm2 MRNA', 'p53_mRNA': 'P53 MRNA', 'ATMA': 'ATMA', 'ATMI': 'ATMI', 'p21': 'P21', 'p21_mRNA': 'P21 MRNA', 'p21step1': 'P21step1', 'p21step2': 'P21step2', 'p53_P': 'P53 P', 'Mdm2_P': 'Mdm2 P', 'p21_basal': 'P21 Basal', 'p38': 'P38', 'p38_P': 'P38 P', 'GADD45': 'GADD45', 'IR': 'IR', 'damDNA': 'DamDNA', 'ROS': 'ROS', 'basalROS': 'BasalROS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p53_mrna': ('p53_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53_mRNA`.'), 'initial_mdm2_mrna': ('Mdm2_mRNA', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_mRNA`.'), 'initial_p21_mrna': ('p21_mRNA', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p21_mRNA`.'), 'initial_atmi': ('ATMI', 200.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATMI`.'), 'initial_model_state_p38': ('p38', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p38`.'), 'initial_mdm2_p53': ('Mdm2_p53', 95.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_p53`.')}
    _HEADLINE_OUTPUTS = {'p53_mrna': ('p53_mRNA', 'native SBML value', 'P53 MRNA. Maps to SBML symbol `p53_mRNA`.'), 'mdm2_mrna': ('Mdm2_mRNA', 'native SBML value', 'Mdm2 MRNA. Maps to SBML symbol `Mdm2_mRNA`.'), 'p21_mrna': ('p21_mRNA', 'native SBML value', 'P21 MRNA. Maps to SBML symbol `p21_mRNA`.'), 'atmi': ('ATMI', 'native SBML value', 'ATMI. Maps to SBML symbol `ATMI`.'), 'p38': ('p38', 'native SBML value', 'P38. Maps to SBML symbol `p38`.'), 'mdm2_p53': ('Mdm2_p53', 'native SBML value', 'Mdm2 P53. Maps to SBML symbol `Mdm2_p53`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000287.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
