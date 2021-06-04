#!/usr/bin/env python

"""Tests for `sciencewriter` package."""

import pytest


from sciencewriter import sciencewriter

def test_pytest_installed():
    assert 1==1



@pytest.mark.skip(reason="just scaffolding tests")
def test_create_paper():
    """This test asserts that the application can created a new science paper.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_archive_paper():
    """This test asserts that the application can archive a science paper which removes it from accessible list but still keeps it in the internal state.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_purge_paper():
    """This test asserts that the application can remove a science paper its internal state but at that time first archives the internal state for safekeeping of any work.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_author_non_existing_to_paper():
    """This test asserts that the application can a a new author to the paper.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_author_non_existing_to_paper_added_to_application():
    """This test asserts that the application asserts/adds a new author in the application records.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_refuse_author_existing_to_paper():
    """This test asserts that the application will not add the same natural person to a given paper more than once.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_return_authors_from_paper():
    """This test asserts that the application can return the list of assigned authors for the paper.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_remove_existing_single_author_from_paper():
    """This test asserts that the application can remove the indicated author from the list of assigned authors for the paper and is returned to the caller. It returns None if the author is not found on the author list. Note authors are never purged.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_remove_non_existing_single_author_from_paper():
    """This test asserts that the application can remove the indicated author from the list of assigned authors for the paper and is returned to the caller. It returns None if the author is not found on the author list.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_titles_to_paper():
    """This test asserts that the application can add title and subtitle texts to the paper that it will always overwrite.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_initial_claim_to_paper():
    """This test asserts that the application can add the initial claim information to the paper and it will return the Claim instance object. Assert that the partial model is instantiated as needed.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_initial_claim_on_paper():
    """This test asserts that the application can overwrite an existing initial claim object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_new_reason_to_paper():
    """This test asserts that the application can add new reason information to the paper and it will return the Reason instance object. Assert that the partial model is instantiated as needed.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_reason_on_paper():
    """This test asserts that the application can overwrite an existing reason object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_new_conclusion_to_paper():
    """This test asserts that the application can add the overall conclusion to the paper and it will return the Conclusion instance object. Assert that the empty model is instantiated as needed.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_conclusion_on_paper():
    """This test asserts that the application can overwrite an existing conclusion object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_new_evidence_to_reason():
    """This test asserts that the application can add new new envidence to an existing reason in the argumentation and returns the Reason object. The partially instantiated evidence record is returned to the caller.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_evidence_on_paper():
    """This test asserts that the application can overwrite an existing evidence object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_supporting_claim_to_paper():
    """This test asserts that the application can add the supporting claim information to the paper and it will return the Claim instance object. Assert that the partial model is instantiated as needed.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_supporting_claim_on_paper():
    """This test asserts that the application can overwrite an existing supporting claim object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_warrant_to_paper():
    """This test asserts that the application can add the warrant information to the paper and it will return the Warrant instance object. Assert that the partial model is instantiated as needed.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_warrant_on_paper():
    """This test asserts that the application can overwrite an existing warrant object in the paper. This is part of the get-partial-inject-update cycle for the model objects and returns updated object.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_get_notes_from_core_concept_():
    """This test asserts that the application can return a list of notes from the specific kind of core concept.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_note_to_core_concept_():
    """This test asserts that the application can add a new note to the specific kind of core concept.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_remove_note_from_core_concept_():
    """This test asserts that the application can remove the given note (as identified by it guuid) from the core concept.
    """
    pass