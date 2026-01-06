import pytest
from lib.open_library_api import Search


def test_get_search_results_returns_bytes():
    """Test that get_search_results() returns bytes"""
    result = Search().get_search_results()
    assert isinstance(result, bytes)


def test_get_search_results_json_returns_dict():
    """Test that get_search_results_json() returns a dict with proper structure"""
    result = Search().get_search_results_json()
    assert isinstance(result, dict)
    assert "docs" in result
    assert isinstance(result["docs"], list)
    assert len(result["docs"]) > 0
    doc = result["docs"][0]
    assert "title" in doc
    assert "author_name" in doc


def test_get_user_search_results_returns_formatted_string():
    """Test that get_user_search_results(search_term) returns formatted string"""
    result = Search().get_user_search_results("the lord of the rings")
    assert isinstance(result, str)
    assert "Title:" in result
    assert "Author:" in result

