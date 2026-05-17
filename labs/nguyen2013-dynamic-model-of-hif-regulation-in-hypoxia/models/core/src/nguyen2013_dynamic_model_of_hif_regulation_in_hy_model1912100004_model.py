# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nguyen2013 - Dynamic model of HIF regulation in hypoxia."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nguyen2013DynamicModelOfHifRegulationInHyModel1912100004Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nguyen2013 - Dynamic model of HIF regulation in hypoxia."""

    _SBML_ID = 'MODEL1912100004'
    _TITLE = 'Nguyen2013 - Dynamic model of HIF regulation in hypoxia'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['HIFalpha', 'HIFalpha_pOH', 'VHL', 'FIH', 'HIFalpha_aOH', 'PHD', 'HIFalpha_aOHpOH', 'O2', 'HIFalpha_n', 'PHD_n', 'HIFalpha_n_pOH', 'VHL_n', 'HIFalpha_n_aOH', 'HIFalpha_n_aOHpOH', 'HIFB', 'HIFd', 'HIFd_HRE', 'HRE', 'mRNA', 'Protein', 'Luciferase', 'FIH_n']
    _SPECIES_LABELS = {'HIFalpha': 'HIFalpha', 'HIFalpha_pOH': 'HIFalpha-pOH', 'VHL': 'VHL', 'FIH': 'FIH', 'HIFalpha_aOH': 'HIFalpha-aOH', 'PHD': 'PHD', 'HIFalpha_aOHpOH': 'HIFalpha-aOHpOH', 'O2': 'O2', 'HIFalpha_n': 'HIFalpha_n', 'PHD_n': 'PHD_n', 'HIFalpha_n_pOH': 'HIFalpha_n-pOH', 'VHL_n': 'VHL_n', 'HIFalpha_n_aOH': 'HIFalpha_n-aOH', 'HIFalpha_n_aOHpOH': 'HIFalpha_n-aOHpOH', 'HIFB': 'HIFB', 'HIFd': 'HIFd', 'HIFd_HRE': 'HIFd_HRE', 'HRE': 'HRE', 'mRNA': 'mRNA', 'Protein': 'Protein', 'Luciferase': 'Luciferase', 'FIH_n': 'FIH_n'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mrna': ('mRNA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mRNA`.'), 'initial_protein': ('Protein', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Protein`.'), 'initial_luciferase': ('Luciferase', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Luciferase`.'), 'initial_vhl_n': ('VHL_n', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `VHL_n`.'), 'initial_fih_n': ('FIH_n', 40.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FIH_n`.'), 'initial_phd_n': ('PHD_n', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PHD_n`.')}
    _HEADLINE_OUTPUTS = {'mrna': ('mRNA', 'native SBML value', 'mRNA. Maps to SBML symbol `mRNA`.'), 'protein': ('Protein', 'native SBML value', 'Protein. Maps to SBML symbol `Protein`.'), 'luciferase': ('Luciferase', 'native SBML value', 'Luciferase. Maps to SBML symbol `Luciferase`.'), 'vhl_n': ('VHL_n', 'native SBML value', 'VHL_n. Maps to SBML symbol `VHL_n`.'), 'fih_n': ('FIH_n', 'native SBML value', 'FIH_n. Maps to SBML symbol `FIH_n`.'), 'phd_n': ('PHD_n', 'native SBML value', 'PHD_n. Maps to SBML symbol `PHD_n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912100004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
