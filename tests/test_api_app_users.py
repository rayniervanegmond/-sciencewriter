#!/usr/bin/env python

"""Tests for `sciencewriter` package."""

import pytest


from sciencewriter import sciencewriter

def test_pytest_installed():
    assert 1==1


@pytest.mark.skip(reason="just scaffolding tests")
def test_instantiate_app():
    """This test asserts that the application can be instantiated.
    """
    pass


@pytest.mark.skip(reason="just scaffolding tests")
def test_shutdown_app_if_persistence_valid():
    """This test asserts that the persistence location is asked for if not known or valid.
    """
    pass


@pytest.mark.skip(reason="just scaffolding tests")
def test_shutdown_app_if_persistence_known():
    """This test asserts that the persistence location is provided/accepted if a shutdown is requested.
    """
    pass


@pytest.mark.skip(reason="just scaffolding tests")
def test_shutdown_app_if_dirty():
    """This test asserts that the application can be shutdown based on dirty_state.
    """
    pass


@pytest.mark.skip(reason="just scaffolding tests")
def test_shutdown_app_if_clean():
    """This test asserts that the application can be shutdown based on dirty_state.
    """
    pass


@pytest.mark.skip(reason="just scaffolding tests")
def test_shutdown_app_persist():
    """This test asserts that if the application can be shutdown and it persists its internal state.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_app_archive():
    """This test asserts that if the application can archive its internal state to a location where it won't be overwritten.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_reload_app_warning():
    """This test asserts that if the application wants to reload it warns that current state will be overwritten and accepts the reply.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_reload_app_if_persisted():
    """This test asserts that if the application can reload its persisted state as its internal state.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_reload_app_from_archive():
    """This test asserts that if the application can reload its persisted state as its internal state.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_author_non_exist():
    """This test asserts that if the author is new (which includes the author record id) the information will be stored and a new AuthorInfoItem item is returned.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_add_author_warn_exist():
    """This test asserts that if the author is not new in the system (the author record id exists) the application warns the caller while returning the existing AuthorInfoItem.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_change_author_info(): 
    """This test asserts that the provided information (which includes the author record id) will overwrite the existing AuthorInfoItem and the new updated items is returned.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_remove_author():
    """This test asserts that the provided author identification matches an existing author and the information is removed from the list while the "deleted" information is returned to the caller.
    """
    pass



@pytest.mark.skip(reason="just scaffolding tests")
def test_get_author_info(): 
    """This test asserts that the provided author record identification exists and returns the record or None if no record with the provided key exists.
    """
    pass

