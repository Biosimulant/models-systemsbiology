# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Panteleev2010 - Blood Coagulation: Full Model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Panteleev2010BloodCoagulationFullModelBiomd0000000740Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Panteleev2010 - Blood Coagulation: Full Model."""

    _SBML_ID = 'BIOMD0000000740'
    _TITLE = 'Panteleev2010 - Blood Coagulation: Full Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VIIa_TF', 'VII_TF', 'TF', 'VIIa', 'VII', 'IXa', 'IX', 'Xa', 'X', 'IIa', 'II', 'fibrin', 'fibrinogen', 'VIIIa', 'VIII', 'Va', 'V', 'XIa', 'XI', 'AT_III', 'TFPI', 'Xa_TFPI', 'APC', 'PC', 'VIIa_TF_F', 'Xa_VIIa_TF', 'IXa_B_F', 'VIIIa_B_F', 'Xa_Va_b', 'Xa_F', 'X_B', 'IIa_F', 'II_B', 'Va_B', 'Va_B_F', 'alpha2_macroglobulin', 'alpha1_antitrypsin', 'alpha2_antiplasmin', 'heparin_cofactor2', 'ProteinC_Inhibitor', 'C1_inhibitor', 'ProteinS_inhibitor', 'Phospholipid']
    _SPECIES_LABELS = {'VIIa_TF': 'VIIa-TF', 'VII_TF': 'VII-TF', 'TF': 'TF', 'VIIa': 'VIIa', 'VII': 'VII', 'IXa': 'IXa', 'IX': 'IX', 'Xa': 'Xa', 'X': 'X', 'IIa': 'IIa', 'II': 'II', 'fibrin': 'fibrin', 'fibrinogen': 'fibrinogen', 'VIIIa': 'VIIIa', 'VIII': 'VIII', 'Va': 'Va', 'V': 'V', 'XIa': 'XIa', 'XI': 'XI', 'AT_III': 'AT-III', 'TFPI': 'TFPI', 'Xa_TFPI': 'Xa-TFPI', 'APC': 'APC', 'PC': 'PC', 'VIIa_TF_F': 'VIIa-TF^F', 'Xa_VIIa_TF': 'Xa-VIIa-TF', 'IXa_B_F': 'IXa^B^F', 'VIIIa_B_F': 'VIIIa^B^F', 'Xa_Va_b': 'Xa-Va^b', 'Xa_F': 'Xa^F', 'X_B': 'X^B', 'IIa_F': 'IIa^F', 'II_B': 'II^B', 'Va_B': 'Va^B', 'Va_B_F': 'Va^B^F', 'alpha2_macroglobulin': 'alpha2-macroglobulin', 'alpha1_antitrypsin': 'alpha1-antitrypsin', 'alpha2_antiplasmin': 'alpha2-antiplasmin', 'heparin_cofactor2': 'heparin-cofactor2', 'ProteinC_Inhibitor': 'ProteinC-Inhibitor', 'C1_inhibitor': 'C1-inhibitor', 'ProteinS_inhibitor': 'ProteinS-inhibitor', 'Phospholipid': 'Phospholipid'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_protein_s_inhibitor': ('ProteinS_inhibitor', 346.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ProteinS_inhibitor`.'), 'initial_protein_c_inhibitor': ('ProteinC_Inhibitor', 88.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ProteinC_Inhibitor`.'), 'initial_alpha1_antitrypsin': ('alpha1_antitrypsin', 40000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha1_antitrypsin`.'), 'initial_fibrinogen': ('fibrinogen', 7600.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `fibrinogen`.'), 'initial_at_iii': ('AT_III', 3400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AT_III`.'), 'initial_alpha2_macroglobulin': ('alpha2_macroglobulin', 3000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha2_macroglobulin`.')}
    _HEADLINE_OUTPUTS = {'protein_s_inhibitor': ('ProteinS_inhibitor', 'native SBML value', 'ProteinS-inhibitor. Maps to SBML symbol `ProteinS_inhibitor`.'), 'protein_c_inhibitor': ('ProteinC_Inhibitor', 'native SBML value', 'ProteinC-Inhibitor. Maps to SBML symbol `ProteinC_Inhibitor`.'), 'alpha1_antitrypsin': ('alpha1_antitrypsin', 'native SBML value', 'alpha1-antitrypsin. Maps to SBML symbol `alpha1_antitrypsin`.'), 'fibrinogen': ('fibrinogen', 'native SBML value', 'fibrinogen. Maps to SBML symbol `fibrinogen`.'), 'at_iii': ('AT_III', 'native SBML value', 'AT-III. Maps to SBML symbol `AT_III`.'), 'alpha2_macroglobulin': ('alpha2_macroglobulin', 'native SBML value', 'alpha2-macroglobulin. Maps to SBML symbol `alpha2_macroglobulin`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000740.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
