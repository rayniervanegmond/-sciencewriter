#!/usr/bin/env python

"""Tests for `sciencewriter` package."""

import pytest


from sciencewriter import sciencewriter
from sciencewriter.informationmodel import Argument, AuthorInfo, Bibliography, BiblioReference, Claim, Conclusion, CoreConcept, Evidence, Note, Reason, SciencePaper, Warrant

def test_pytest_installed():
    assert 1==1

def test_coreconcept_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    pass

def test_author_info_guuid():
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = AuthorInfo()
    assert cc.notes is not None
    assert cc.guuid is not None

    cc.call_name = "callname"
    cc.contact_email = "email://"
    cc.contact_webpage = "http://"
    cc.family_name = "familyname"
    cc.middle_initials = "mi"
    
    assert cc.call_name == "callname"
    pass

def test_science_paper_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = SciencePaper()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.authors is not None
    pass

def test_bibliography_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Bibliography()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.references is not None
    pass

def test_biblioreference_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = BiblioReference()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.authors is not None
    pass

def test_note_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Note()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.core_concepts is not None
    pass

def test_claim_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Claim()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.reasons is not None
    pass

def test_reason_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Reason()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.evidences is not None
    pass

def test_evidence_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Evidence()
    assert cc.notes is not None
    assert cc.guuid is not None
    assert cc.sources is not None
    pass

def test_warrant_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Warrant()
    assert cc.notes is not None
    assert cc.guuid is not None
    pass

def test_conclusion_guuid(): 
    """This test asserts that the new coreconcepts always get their uudid assigned.
    """
    cc = Conclusion()
    assert cc.notes is not None
    assert cc.guuid is not None
    pass
