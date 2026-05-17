# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bakker2001_Glycolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bakker2001GlycolysisBiomd0000000071Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bakker2001_Glycolysis."""

    _SBML_ID = 'BIOMD0000000071'
    _TITLE = 'Bakker2001_Glycolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GlcI', 'Pg', 'Glc6P', 'Fru6P', 'Fru16BP', 'DHAP', 'GAP', 'NAD', 'BPGA13', 'NADH', 'Pyr', 'Nb', 'Pc', 'PyrE', 'Gly', 'GlcE', 'Gly3P', 'ATPc', 'ADPc', 'ATPg', 'ADPg', 'DHAPg', 'DHAPc', 'Gly3Pc', 'Gly3Pg', 'PGAg', 'PEPc']
    _SPECIES_LABELS = {'GlcI': 'Glucose', 'Pg': 'Phosphates in Glycosome', 'Glc6P': 'Glucose 6-phosphate', 'Fru6P': 'Fructose 6-phosphate', 'Fru16BP': 'Fructose 1,6-bisphosphate', 'DHAP': 'Dihydroxyacetone phosphate', 'GAP': 'Glyceraldehyde 3-phosphate', 'NAD': 'NAD', 'BPGA13': '1,3-bisphosphoglycerate', 'NADH': 'NADH', 'Pyr': 'Pyruvate', 'Nb': '3-PGA 2-PGA PEP', 'Pc': 'Phosphates cytosol', 'PyrE': 'Pyruvate external', 'Gly': 'Glycerol', 'GlcE': 'Glucose external', 'Gly3P': 'Glycerol 3-phosphate', 'ATPc': 'ATP cyt.', 'ADPc': 'ADP cyt.', 'ATPg': 'ATP gly.', 'ADPg': 'ADP gly.', 'DHAPg': 'DHAP gly.', 'DHAPc': 'DHAP cyt.', 'Gly3Pc': 'Gy3P c.', 'Gly3Pg': 'Gy3P g.', 'PGAg': '3-PGA g.', 'PEPc': 'PEP c.'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_external': ('GlcE', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GlcE`.'), 'initial_pyruvate_external': ('PyrE', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PyrE`.'), 'initial_fructose_1_6_bisphosphate': ('Fru16BP', 16.5371, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fru16BP`.'), 'initial_phosphates_in_glycosome': ('Pg', 7.63936, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pg`.'), 'initial_phosphates_cytosol': ('Pc', 6.51839, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pc`.'), 'initial_pyruvate': ('Pyr', 4.77413, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pyr`.')}
    _HEADLINE_OUTPUTS = {'glucose_external': ('GlcE', 'native SBML value', 'Glucose external. Maps to SBML symbol `GlcE`.'), 'pyruvate_external': ('PyrE', 'native SBML value', 'Pyruvate external. Maps to SBML symbol `PyrE`.'), 'fructose_1_6_bisphosphate': ('Fru16BP', 'native SBML value', 'Fructose 1,6-bisphosphate. Maps to SBML symbol `Fru16BP`.'), 'phosphates_in_glycosome': ('Pg', 'native SBML value', 'Phosphates in Glycosome. Maps to SBML symbol `Pg`.'), 'phosphates_cytosol': ('Pc', 'native SBML value', 'Phosphates cytosol. Maps to SBML symbol `Pc`.'), 'pyruvate': ('Pyr', 'native SBML value', 'Pyruvate. Maps to SBML symbol `Pyr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000071.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
