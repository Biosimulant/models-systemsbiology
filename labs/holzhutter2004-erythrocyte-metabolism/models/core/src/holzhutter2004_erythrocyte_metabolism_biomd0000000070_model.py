# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Holzhutter2004_Erythrocyte_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Holzhutter2004ErythrocyteMetabolismBiomd0000000070Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Holzhutter2004_Erythrocyte_Metabolism."""

    _SBML_ID = 'BIOMD0000000070'
    _TITLE = 'Holzhutter2004_Erythrocyte_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Glcin', 'MgATP', 'Glc6P', 'MgADP', 'Fru6P', 'Fru16P2', 'GraP', 'DHAP', 'Phi', 'NAD', 'Gri13P2', 'NADH', 'Gri3P', 'Gri23P2f', 'Gri2P', 'PEP', 'Pyr', 'Lac', 'NADPHf', 'NADPf', 'AMPf', 'ADPf', 'GlcA6P', 'Rul5P', 'GSSG', 'GSH', 'Xul5P', 'Rib5P', 'Sed7P', 'E4P', 'MgAMP', 'ATPf', 'Mgf', 'MgGri23P2', 'P1NADP', 'P1f', 'P1NADPH', 'P2NADP', 'P2f', 'P2NADPH', 'PRPP', 'Lacex', 'Pyrex', 'Glcout', 'Phiex']
    _SPECIES_LABELS = {'Glcin': 'Glucose in', 'MgATP': 'MgATP', 'Glc6P': 'Glucose 6-phosphate', 'MgADP': 'MgADP', 'Fru6P': 'Fructose 6-phosphate', 'Fru16P2': 'Fructose 1,6-phosphate', 'GraP': 'Glyceraldehyde 3-phosphate', 'DHAP': 'Dihydroxyacetone phosphate', 'Phi': 'Phosphate', 'NAD': 'NAD', 'Gri13P2': '1,3-Bisphospho-D-glycerate', 'NADH': 'NADH', 'Gri3P': '3-Phospho-D-glycerate', 'Gri23P2f': '2,3-Bisphospho-D-glycerate', 'Gri2P': '2-Phospho-D-glycerate', 'PEP': 'Phosphoenolpyruvate', 'Pyr': 'Pyruvate', 'Lac': 'Lactate', 'NADPHf': 'NADPH', 'NADPf': 'NADP', 'AMPf': 'AMP', 'ADPf': 'ADP', 'GlcA6P': 'Phospho-D-glucono-1,5-lactone', 'Rul5P': 'Ribulose 5-phosphate', 'GSSG': 'Oxidized Glutathione', 'GSH': 'Reduced Glutathione', 'Xul5P': 'Xylulose 5-phosphate', 'Rib5P': 'Ribose 5-phosphate', 'Sed7P': 'Sedoheptulose 7-phosphate', 'E4P': 'Erythrose 4-phosphate', 'MgAMP': 'MgAMP', 'ATPf': 'ATP', 'Mgf': 'Mg', 'MgGri23P2': 'MgGri23P2', 'P1NADP': 'Protein1 bound NADP', 'P1f': 'Protein1', 'P1NADPH': 'Protein1 bound NADPH', 'P2NADP': 'Protein2 bound NADP', 'P2f': 'Protein2', 'P2NADPH': 'Protein2 bound NADPH', 'PRPP': 'PRPP', 'Lacex': 'External Lactate', 'Pyrex': 'External Pyruvate', 'Glcout': 'Glucose outside', 'Phiex': 'Phosphate external'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_external_lactate': ('Lacex', 1.68, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Lacex`.'), 'initial_phosphate_external': ('Phiex', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Phiex`.'), 'initial_external_pyruvate': ('Pyrex', 0.084, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pyrex`.'), 'initial_protein2_bound_nadph': ('P2NADPH', 0.024, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2NADPH`.'), 'initial_protein1_bound_nadph': ('P1NADPH', 0.024, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1NADPH`.'), 'initial_protein2_bound_nadp': ('P2NADP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2NADP`.')}
    _HEADLINE_OUTPUTS = {'external_lactate': ('Lacex', 'native SBML value', 'External Lactate. Maps to SBML symbol `Lacex`.'), 'phosphate_external': ('Phiex', 'native SBML value', 'Phosphate external. Maps to SBML symbol `Phiex`.'), 'external_pyruvate': ('Pyrex', 'native SBML value', 'External Pyruvate. Maps to SBML symbol `Pyrex`.'), 'protein2_bound_nadph': ('P2NADPH', 'native SBML value', 'Protein2 bound NADPH. Maps to SBML symbol `P2NADPH`.'), 'protein1_bound_nadph': ('P1NADPH', 'native SBML value', 'Protein1 bound NADPH. Maps to SBML symbol `P1NADPH`.'), 'protein2_bound_nadp': ('P2NADP', 'native SBML value', 'Protein2 bound NADP. Maps to SBML symbol `P2NADP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000070.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
