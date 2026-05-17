# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Scheidel2016 - In Silico Knockout Studies of Xenophagy Capturing of Salmonella."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Scheidel2016InSilicoKnockoutStudiesOfXenopModel1904150001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Scheidel2016 - In Silico Knockout Studies of Xenophagy Capturing of Salmonella."""

    _SBML_ID = 'MODEL1904150001'
    _TITLE = 'Scheidel2016 - In Silico Knockout Studies of Xenophagy Capturing of Salmonella'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P384', 'P1', 'P257', 'P6', 'P7', 'P136', 'P10', 'P140', 'P142', 'P400', 'P276', 'P277', 'P408', 'P280', 'P152', 'P154', 'P155', 'P284', 'P156', 'P413', 'P158', 'P415', 'P289', 'P294', 'P295', 'P423', 'P296', 'P298', 'P301', 'P303', 'P304', 'P305', 'P306', 'P51', 'P323', 'P325', 'P338', 'P339', 'P340', 'P341', 'P342', 'P343', 'P344', 'P345', 'P347', 'P351', 'P352', 'P353', 'P227', 'P356', 'P357', 'P230', 'P113', 'P374', 'P246', 'P247', 'P378', 'P250', 'P382', 'P383', 'P255']
    _SPECIES_LABELS = {'P384': 'mTORC1:ULK1comp_', 'P1': 'S-cyt', 'P257': 'N/S', 'P6': 'E3_ligase', 'P7': 'p62', 'P136': 'S-damagedSCV__', 'P10': 'LRSAM1', 'P140': 'Gal8', 'P142': 'S:Gal8', 'P400': 'SignalSCVdamage_', 'P276': 'S:Gal8:Ub:NDP52', 'P277': "NDP52'", 'P408': 'SignalAutophagyInduction_', 'P280': 'S:Gal8:Ub:p62_', 'P152': 'S:Gal8:NDP52_', 'P154': 'S:Gal8:Ub_', 'P155': 'S:Gal8:Ub:NDP52:OPTN:p62:N/S__', 'P284': "OPTN'", 'P156': 'S:Gal8:Ub:OPTN_', 'P413': 'AA_', 'P158': 'S:Gal8:Ub:NDP52:OPTN:p62__', 'P415': 'mTORC1:ULK1comp:SCV__', 'P289': 'S:Gal8:Ub:NDP52:OPTN:p62:N/S:diTBK1__', 'P294': "diTBK1'", 'P295': "diTBK1'i", 'P423': 'SCV_', 'P296': 'S:Gal8:Ub:NDP52:OPTN:p62:N/S:diTBK1i__', 'P298': 'S:Gal8:Ub:NDP52:N/S_', 'P301': "N/S'", 'P303': 'S:Ub_', 'P304': 'S:Ub:p62_', 'P305': 'S:Ub:OPTN_', 'P306': 'S:Ub:NDP52_', 'P51': 'TBK1', 'P323': 'S:Ub:NDP52:OPTN:p62__', 'P325': 'S:Ub:NDP52:OPTN:p62:N/S__', 'P338': 'S:Ub:NDP52:OPTN:p62:N/S:diTBK1__', 'P339': 'S:Ub:NDP52:OPTN:p62:N/S:diTBK1i__', 'P340': "diTBK1'ii", 'P341': "diTBK1'iii", 'P342': 'S:Ub:NDP52:OPTN:p62:N/S:OligoTBK1__', 'P343': 'Ap:Ub_', 'P344': 'Ap:Ub:N/S__', 'P345': 'Ap:Ub:OPTNp_', 'P347': "p62'", 'P351': "OPTN'i", 'P352': "p62'i", 'P353': "NDP52'i", 'P227': 'S:Gal8:Ub:NDP52:p62:OPTNp.N/S:OligoTBK1__', 'P356': 'S:Ub:NDP52:N/S_', 'P357': "N/S'i", 'P230': 'Ap:Gal8:Ub:OPTNp_', 'P113': 'LC3/GABARAP_', 'P374': 'Ap:Gal8', 'P246': 'Ap:Gal8:Ub:N/S_', 'P247': 'Ap:Gal8:Ub_', 'P378': 'AAstarvation_', 'P250': 'OPTN_', 'P382': 'mTORC1inactive', 'P383': 'ULK1comp_', 'P255': 'NDP52'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_m_torc1inactive': ('P382', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P382`.'), 'initial_m_torc1_ulk1comp': ('P384', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P384`.'), 'initial_m_torc1_ulk1comp_scv': ('P415', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P415`.'), 'initial_signal_sc_vdamage': ('P400', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P400`.'), 'initial_signal_autophagy_induction': ('P408', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P408`.'), 'initial_p62_i': ('P352', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P352`.')}
    _HEADLINE_OUTPUTS = {'m_torc1inactive': ('P382', 'native SBML value', 'mTORC1inactive. Maps to SBML symbol `P382`.'), 'm_torc1_ulk1comp': ('P384', 'native SBML value', 'mTORC1:ULK1comp_. Maps to SBML symbol `P384`.'), 'm_torc1_ulk1comp_scv': ('P415', 'native SBML value', 'mTORC1:ULK1comp:SCV__. Maps to SBML symbol `P415`.'), 'signal_sc_vdamage': ('P400', 'native SBML value', 'SignalSCVdamage_. Maps to SBML symbol `P400`.'), 'signal_autophagy_induction': ('P408', 'native SBML value', 'SignalAutophagyInduction_. Maps to SBML symbol `P408`.'), 'p62_i': ('P352', 'native SBML value', "p62'i. Maps to SBML symbol `P352`.")}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1904150001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
