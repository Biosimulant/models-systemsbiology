# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for DeCaluwe2016 - Circadian Clock."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Decaluwe2016CircadianClockBiomd0000000631Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for DeCaluwe2016 - Circadian Clock."""

    _SBML_ID = 'BIOMD0000000631'
    _TITLE = 'DeCaluwe2016 - Circadian Clock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CL_m', 'CL_p', 'P97_m', 'P97_p', 'P51_m', 'P51_p', 'EL_m', 'EL_p', 'PIF_m', 'PIF_p', 'hypocotyl', 'P']
    _SPECIES_LABELS = {'CL_m': 'CCA1/LHY mRNA', 'CL_p': 'CCA1/LHY protein', 'P97_m': 'PRR9/PRR7 mRNA', 'P97_p': 'PRR9/PRR7 protein', 'P51_m': 'PRR5/TOC1 mRNA', 'P51_p': 'PRR5/TOC1 protein', 'EL_m': 'ELF4/LUX mRNA', 'EL_p': 'ELF4/LUX protein', 'PIF_m': 'PIF4/PIF5 mRNA', 'PIF_p': 'PIF4/PIF5 protein', 'hypocotyl': 'Hypocotyl length', 'P': 'P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_prr9_prr7_protein': ('P97_p', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P97_p`.'), 'initial_prr9_prr7_mrna': ('P97_m', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P97_m`.'), 'initial_prr5_toc1_protein': ('P51_p', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P51_p`.'), 'initial_prr5_toc1_mrna': ('P51_m', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P51_m`.'), 'initial_pif4_pif5_protein': ('PIF_p', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIF_p`.'), 'initial_pif4_pif5_mrna': ('PIF_m', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIF_m`.')}
    _HEADLINE_OUTPUTS = {'prr9_prr7_protein': ('P97_p', 'native SBML value', 'PRR9/PRR7 protein. Maps to SBML symbol `P97_p`.'), 'prr9_prr7_mrna': ('P97_m', 'native SBML value', 'PRR9/PRR7 mRNA. Maps to SBML symbol `P97_m`.'), 'prr5_toc1_protein': ('P51_p', 'native SBML value', 'PRR5/TOC1 protein. Maps to SBML symbol `P51_p`.'), 'prr5_toc1_mrna': ('P51_m', 'native SBML value', 'PRR5/TOC1 mRNA. Maps to SBML symbol `P51_m`.'), 'pif4_pif5_protein': ('PIF_p', 'native SBML value', 'PIF4/PIF5 protein. Maps to SBML symbol `PIF_p`.'), 'pif4_pif5_mrna': ('PIF_m', 'native SBML value', 'PIF4/PIF5 mRNA. Maps to SBML symbol `PIF_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000631.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
