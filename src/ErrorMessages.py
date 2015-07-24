from enum import Enum

class Errors(Enum):
    UNKNOWN="""
    Something went wrong.
    Our koala expert is deeply sorry.
    
    Contact:
    [i]m.seva.ivanov@gmail.com[/i]    
    """,
    CONVERSION_FAILED="""
    Conversion failed. :/      
    We are deeply sorry.        
    """,
    INVALID_LINK="""
    [b]Something went wrong![/b]
    
    1. There is no youtube video in this url. 
    Then stop eating eucalyptus leaves...

    2. We dont support over populated video.
    Ex: Miley Cyrus with 325,909,424 views.
    Too bad. Go back eating leaves.
    """,
