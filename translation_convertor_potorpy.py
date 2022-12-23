from fileinput import FileInput
from glob import glob
import os
import shutil
import re

# ATTENTION: there must not be 2 equal key or value
# regex: https://www.w3schools.com/python/python_regex.asp
dict = {
    # search_text : replace_text
    # start
    r'\n"Plural-Forms(.*)':         r'',
    r'\n"X-Crowdin-Pr(.*)':         r'',
    r'\n"X-Crowdin-Pr(.*)':         r'',
    r'\n"X-Crowdin-La(.*)':         r'',
    r'\n"X-Crowdin-Fi(.*)':         r'',
    r'\n"X-Crowdin-Fi(.*)':         r'',
    r'\n"Project-Id-V(.*)':         r'',
    r'\n"Content-Type(.*)':         r'',
    r'\n"Language-Tea(.*)':         r'',
    r'\n"Language:(.*)':         r'',
    r'\n"PO-Revision-(.*)':         r'',
    r'\n"Большой(.*)':         r'',
    r'msgid ""\nmsgstr ""':         r'',
    r'\\n"\n"':                     r'\\n',
    r'\\'+'"':                      r'§§§§§§§§',
    # Effect
    r' \[nointeract\]"':            r'" nointeract',
    r' \[withfade\]"':              r'" with fade',
    r' \[withdissolve\]"':          r'" with dissolve',
    r' \[withslowdissolve\]"':      r'" with slowdissolve',
    r' \[withhpunch\]"':            r'" with hpunch',
    r' \[withflash\]"':             r'" with flash',
    r' \[withvpunch\]"':            r'" with vpunch',
    r' \[withDissolve20\]"':        r'" with Dissolve(2.0)',
    r' \[withDissolve1\]"':        r'" with Dissolve(1)',
    r' \[withDissolvey3\]"':        r'" with Dissolve(.3)',
    r' \[multiple2\]"':        r'" (multiple=2)',
    r'msgid "\[nvl_clear\]"':       r'    # nvl clear',
    r'msgstr "\[nvl_clear\]"':      r'    nvl clear',
    # first
    r'msgid "(.*?) \[special_delimiter\] (.*?)"':       r'    # "\1" "\2"',
    r'msgstr "(.*?) \[special_delimiter\] (.*?)"':      r'    "\1" "\2"',
    r':\nmsgid "(.*?)"':                                r':\n    # "\1"',
    r'    #(.*?)\nmsgstr "\[_(.*?)\_] (.*?)"':            r'    #\1\n    \2 "\3"',
    r'    # (.*?)\nmsgstr "(.*?)"':                     r'    # \1\n    "\2"',
    # after
    r'    # "\[_(.*?)\_] (.*?)"':                         r'    # \1 "\2"',
    # Comment
    r':\n    # ':                                                   r':\n\n    # ',
    r'rpy:(.*?) #-#-# translate':                                   r'rpy:\1\ntranslate',
    r'strings: #\|#\|# # ':                                         r'strings:\n\n# ',
    r'updated at (.*?)-(.*?)-(.*?) (.*?):(.*?) #\|#\|# # ':         r'updated at \1-\2-\3 \4:\5\n\n# ',
    # end
    r'msgid "(.*?)"':                       r'    old "\1"',
    r'msgstr "(.*?)"':                      r'    new "\1"',
    r'\n#(.*?)\n    old "':                 r'\n    #\1\n    old "',
    r'\n\n# TODO: Translation updated':     r'# TODO: Translation updated',
    r'§§§§§§§§':                            r'\\'+'"',
    r'# TODO: Translation updated at (.*?)-(.*?)-(.*?) (.*?):(.*?) #\|#\|# # §translate ': r'# TODO: Translation updated at \1-\2-\3 \4:\5\n\ntranslate ',
    r'\n# §translate':                      r'\ntranslate',
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile, languege):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # c = re.compile(search_text)

    # Replace the target string
    # filedata = filedata.replace(search_text, replace_text)
    filedata = re.sub(search_text, replace_text, filedata)
    # TODO: to improve
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r'"\n    (.*?)_s_(.*?) "',
                      r'"\n    \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r':\n\n    # (.*?)_s_(.*?) "',
                      r':\n\n    # \1 \2 "', filedata)
    filedata = re.sub(r'crowdin', languege, filedata)

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}, languege="crowdin"):
    newpathFile = fileRename(pathFile, extension=".rpy")
    print(pathFile)
    for search_text in dict.keys():
        replacetext(pathFile=newpathFile, search_text=search_text,
                    replace_text=dict[search_text], languege=languege)


def getListFiles(extension, languege="**"):
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + languege+"/*"+extension, recursive=True)
    if languege != "**":
        dir_list = dir_list + \
            glob(path + languege+"/**/*"+extension, recursive=True)
    return dir_list


def potorpy(languege):
    for path in getListFiles(extension=".po", languege=languege):
        replaceDictionary(path, dict=dict, languege=languege)


def fileRename(pathFile, extension):
    pre, ext = os.path.splitext(pathFile)
    shutil.copyfile(pathFile, pre + extension)
    return pre + extension


potorpy("crowdin")
