from commit import *
from pomeranje_head import *
from change import *
from comapre import *


import pytest
from unittest.mock import patch
from commit import CodeCommit

@pytest.fixture
def code_commit_instance():

    return CodeCommit("commit_name")

@patch("commit.load_from_commit")
def test_compare_with_no_changes(mock_load_from_commit, code_commit_instance):
    mock_load_from_commit.return_value = "File content"
    
    code_commit_instance.compare(CodeCommit("name")) 
    
    mock_load_from_commit.assert_called_once()

@patch("commit.load_from_commit")
def test_compare_with_changes(mock_load_from_commit, code_commit_instance):
    mock_load_from_commit.side_effect = ["Pre change content", "Post change content"]
    
    code_commit_instance.compare(CodeCommit("different_commit_name"))
    
    assert mock_load_from_commit.call_count == 2

