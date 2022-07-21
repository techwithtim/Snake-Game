from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """# XX## game""",
    """:

    # """: """:
msgid \"""",
    """    old \"""": """msgid \"[mschoice] """,
    """    new \"""": """msgstr \"[mschoice] """,
    # Effect
    """\" nointeract""": """ [nointeract]\"""",
    """\" with fade""": """ [withfade]\"""",
    """\" with dissolve""": """ [withdissolve]\"""",
    """\" with slowdissolve""": """ [withslowdissolve]\"""",
    """\" with hpunch""": """ [withhpunch]\"""",
    """\" with flash""": """ [withflash]\"""",
    """\" with vpunch""": """ [withvpunch]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",

    """\n    """: """\nmsgstr \"""",
    # ch
    # """ \"Max \"""": """ \"[Max] """,

    """ \"extend \"""": """ \"[extend] """,

    # """ \"Cab driver\" \"""": """ \"Cab driver || """,
    
    # Fix
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",
    #Final
    """\n ## translate crowdin strings:\n\n""": """\n\n# XXtranslate crowdin strings:XX\n""",
    """:XX\n# XX## game""": """:XX# XX## game""",
    # date
    """21:03\n\n# game""": """HH:HH# game""",
    """21:03\n\n# XXtranslate""": """HH:HH# XXtranslate""",
    # only rpytopo
    """msgid \"\"""": """msgid \"""",
    """msgstr \"\"""": """msgstr \"""",
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(search_text, replace_text)

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}, reverse=False):
    print(pathFile)
    if(reverse):
        for item in reversed(list(dict.items())):
            replacetext(pathFile=pathFile,
                        search_text=item[1], replace_text=item[0])
    else:
        for search_text in dict.keys():
            replacetext(pathFile=pathFile, search_text=search_text,
                        replace_text=dict[search_text])


def getListFiles():
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + "/**/*.po", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


rpytopo()
