from commit import *
from codeCommit import *
from change import *
import pytest

@pytest.mark.parametrize("change", [Add("promena")])
def testAddChange(change): #test za add change metodu u codecommit klasi
    
    objekat = CodeCommit(0, None)
    objekat.changes.append(change)
    assert objekat.changes[-1] == change

@pytest.mark.parametrize("content", [0])
def testValidateContent(content):
    with pytest.raises(ValueError) as err:
        added = Add(content)
        added.validate_content
        assert str(err.value) == "kontent mora da bude string"

@pytest.mark.parametrize("content", [0])
def testValidateContent(content):

    with pytest.raises(ValueError) as err:
        deleted = Delete(content)
        deleted.validate_content
        assert str(err.value) == "kontent mora da bude string"

@pytest.mark.parametrize("content", [0])
def testValidateContent(content):
    
    with pytest.raises(ValueError) as err:
        modifikacija = Modifikacija(content)
        modifikacija.validate_content()
        assert str(err.value) == "kontent mora da bude string"

       
