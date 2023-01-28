import glob, os, re, sys
from antlr4 import Token, Lexer, InputStream
from lexer.CMakeLexer import CMakeLexer
from lexer.MakefileCommentLexer import MakefileCommentLexer
from lexer.MakefileAmCommentLexer import MakefileAmCommentLexer
from lexer.CPP14Lexer import CPP14Lexer
import pandas as pd
from lexer.propertiesLexer import propertiesLexer
from lxml import etree as ElementTree
from subprocess import PIPE, run

# comment class contains text, line, endline, start char position
class _Comment:
        
    def __init__(self, text, line, char_position_in_line, end_line = None):
        if end_line == None: self.end_line = line
        else: self.end_line = end_line
        self.text = text
        self.line = line
        self.char_position_in_line = char_position_in_line

    def is_continue(self, line, charpos):
        return (self.end_line == line) or (self.end_line + 1 == line and self.char_position_in_line == charpos)
    
    def get_len(self):
        return self.end_line - self.line  + 1
    
    def append(self, text, line):
        if self.end_line == line:
            self.text += " " + text
        else:
            self.text += "" + text
            self.end_line = line
    # avoid last new line from ANTLR4 module
    def get_text(self):
        if self.text[-1:] == '\n': return self.text[:-1]
        else: return self.text
    
    def to_string(self):
        return self.text + " (line=" + str(self.line) + ", endLine=" + str(self.end_line)+ ", charPos=" + str(self.char_position_in_line) + ")"

# identify_mulcomments 
def identify_comments(lexer):
    comments = []
    index = -1
    last_comment = None
    t = lexer.nextToken()
    last_type = None
    extra_line = ''
    no_extra_line = 2
    if isinstance(lexer, CPP14Lexer): 
        extra_line ='\n'
        no_extra_line = 1

    while t.type != Token.EOF:
        if t.channel == lexer.HIDDEN:
            if last_comment != None and last_comment.is_continue(t.line,t.column) and last_type != None and last_type == t.type:
                if last_type != None and last_type == t.type:
                    last_comment.append(extra_line + t.text, t.line)
                else: last_comment.append(t.text, t.line)
            else:
                if len(t.text.split('\n')) > no_extra_line: 
                    end_line = t.line + len(t.text.split('\n')) - 1
                    last_comment = _Comment(t.text, t.line, t.column, end_line)
                else:
                    last_comment = _Comment(t.text, t.line, t.column)
                comments.append(last_comment)
        last_type = t.type
        t = lexer.nextToken()
        
    return comments

    

# ixml to get comment and for loop these comments to get position of comments by using index
def xml_lexer(file, content):
    lines =  content.split('\n')
    try:
        parser = ElementTree.XMLParser(recover=True, resolve_entities=False)
        tree = ElementTree.parse(file, parser)
        comments = tree.xpath('//comment()')
    except AssertionError:
        return []
    _comments = []
    char_before_comment = 0
    for comment in comments:
        text = '<!--' + comment.text + '-->'
        char_before_comment = content.find(text.split('\n')[0],char_before_comment)
        start = content[:char_before_comment].count('\n') + 1
        end = start + text.count('\n')
        char = char_before_comment - content[:char_before_comment].rfind('\n') - 1
        char_before_comment += len(text)
        _comment = _Comment(text, start, char)
        _comment.end_line = end
        _comments.append(_comment)
    return _comments

# get line of source code (line of codes + line of comments) by excluding empty lines
def get_los(content):
    los = 0
    for line in content.split('\n'):
        if line.strip(): los +=1
    i = 0
    for line in content.split('\n'):
        if re.match(r'^\s*$', line): i +=1
    return los

def identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, build_system):
    global SATD_comments, Comments_with_no_keywords
    
    for comment in comments:
        text = comment.get_text().replace('\n',' ').replace('\r',' ')
        
    
        keywords = [keyword for keyword in keywords_debt if re.search(r"\b" + re.escape(keyword.lower()) + r"\b", comment.get_text().lower())]
        linkLocation = 'https://github.com/{}/blob/{}/{}#L{}'.format(repoName,commitHash, file, comment.line)
        if len(keywords) > 0:
            SATD_comments = SATD_comments.append(pd.Series(
                                                [repoIndex, repoName, linkLocation, comment.get_text(), keywords, build_system, comment.char_position_in_line, comment.line, comment.end_line],
                                                index=SATD_comments.columns), ignore_index=True)
        else:
            Comments_with_no_keywords = Comments_with_no_keywords.append(pd.Series(
                                                [repoIndex, repoName, linkLocation, comment.get_text(), keywords, build_system, comment.char_position_in_line, comment.line, comment.end_line],
                                                index=Comments_with_no_keywords.columns), ignore_index=True)



def out(command,inp):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True, input=inp)
    return result.stdout


def identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, build_system):
    global Comments, LinkLocations, BuildSystemsinFile, CharPositions, StartLines, EndLines, Texts
    
    for comment in comments:
        text = comment.get_text().replace('\n',' ').replace('\r',' ') + '\n'
        if text == '/exit\n': text = '/Exit\n'
        Texts += text
        # output = out("java -jar {}/satd_detector.jar test".format(dir_path), text +"/exit")
        # output = output.replace('>','').replace('\n','')

        LinkLocations.append('https://github.com/{}/blob/{}/{}#L{}'.format(repoName,commitHash, file, comment.line))
        Comments.append(comment.get_text())
        BuildSystemsinFile.append(build_system)
        CharPositions.append(comment.char_position_in_line)
        StartLines.append(comment.line)
        EndLines.append(comment.end_line)
        # if output == 'SATD': 
        #     SATD_comments = SATD_comments.append(pd.Series(
        #                                         [repoIndex, repoName, linkLocation, comment.get_text(), build_system, comment.char_position_in_line, comment.line, comment.end_line],
        #                                         index=SATD_comments.columns), ignore_index=True)
        # else:
        #     Comments_with_no_keywords = Comments_with_no_keywords.append(pd.Series(
        #                                         [repoIndex, repoName, linkLocation, comment.get_text(), build_system, comment.char_position_in_line, comment.line, comment.end_line],
        #                                         index=Comments_with_no_keywords.columns), ignore_index=True)

def extract_SATD_comments_from_Ant_Ivy_build_files(Ant_properties_build_files, Ant_xml_build_files, Ivy_build_files, repoIndex, repoName, commitHash):


    for file in Ant_properties_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Ant')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Ant')

    for file in Ant_xml_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Ant')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Ant')

    for file in Ivy_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Ivy')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Ivy')


# calculate maven investiment by pom.xml, maven([123])?.xml
def extract_SATD_comments_from_Maven_build_files(Maven_build_files, repoIndex, repoName, commitHash):

    for file in Maven_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Maven')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Maven')


# calculate autotools investiment by [Cc]onfigure.(ac|in), ac(local|site).m4, [Mm]akefile.(am|in), config.h.in
def extract_SATD_comments_from_Autotool_build_files(Autotools_am_build_files, Autotools_in_build_files, Autotools_configure_h_in_build_files, Autotools_ac_build_files, Autotools_m4_build_files, repoIndex, repoName, commitHash):

    for file in Autotools_am_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        input_stream = InputStream(content)
        # am file will not have dnl comments
        comments = identify_comments(MakefileAmCommentLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Autotool')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Autotool')


    for file in Autotools_in_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Autotool')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Autotool')

    for file in Autotools_configure_h_in_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CPP14Lexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Autotool')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Autotool')

    for file in Autotools_ac_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Autotool')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Autotool')

    for file in Autotools_m4_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'Autotool')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'Autotool')


# calculate autotools investiment by CMakeLists.txt, *.cmake
def extract_SATD_comments_from_CMake_build_files(CMake_txt_build_files, CMake_cmake_build_files, repoIndex, repoName, commitHash):

    for file in CMake_txt_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'CMake')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'CMake')

    for file in CMake_cmake_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        if is_detector:
            identify_SATD_comments_by_detector(comments, repoIndex, repoName, commitHash, file, 'CMake')
        else:
            identify_SATD_comments_by_keywords(comments, repoIndex, repoName, commitHash, file, 'CMake')


def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

with open('../data/keywords_list.txt', 'r') as file:
        keywords_debt = file.read().split(', ')

is_detector  = False
if is_detector:
    Comments = []
    LinkLocations = []
    BuildSystemsinFile = []
    CharPositions = []
    StartLines = []
    EndLines = []
    Texts = ''
    SATD_output_folder =  '../data/SATD_comment_detector'
    Non_SATD_output_folder = '../data/Non_SATD_comments_detector'
else:   
    columns = ['repoIndex', 'repoName', 'linkLocation', 'comment', 'keywords', 'buildSysteminFile', 'charPosition', 'startLine', 'endLine']
    SATD_comments = pd.DataFrame(columns=columns, dtype=object)
    Comments_with_no_keywords = pd.DataFrame(columns=columns, dtype=object) 
    SATD_output_folder =  '../data/SATD_comment'
    Non_SATD_output_folder = '../data/Comments_with_no_keywords' 

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(SATD_output_folder):
   os.makedirs(SATD_output_folder)

if not os.path.exists(Non_SATD_output_folder):
   os.makedirs(Non_SATD_output_folder)

import glob, os, re, sys
from pathlib import Path
def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0



def main():
    args = sys.argv[1:]
    repoIndex = args[0]
    repoName = args[1]
    commitHash = args[2]
    if is_detector:
        global SATD_comments, Comments_with_no_keywords

    os.chdir('/data/satd-clone-2022/'+str(repoIndex))
    # os.chdir('/Users/xiaotao/Documents/GitHub/'+str(repoIndex))
    xml_files = [str(f) for f in Path('.').glob('**/*.xml') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    Ant_properties_build_files = [str(f) for f in Path('.').glob('**/build.properties') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    ac_files = [str(f) for f in Path('.').glob('**/*.ac') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    in_files = [str(f) for f in Path('.').glob('**/*.in') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    m4_files = [str(f) for f in Path('.').glob('**/*.m4') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    am_files = [str(f) for f in Path('.').glob('**/*.am') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    CMake_txt_build_files = [str(f) for f in Path('.').glob('**/CMakeLists.txt') if is_non_zero_file(str(f)) and (not os.path.islink(f))]
    CMake_cmake_build_files = [str(f) for f in Path('.').glob('**/*.cmake') if is_non_zero_file(str(f)) and (not os.path.islink(f))]

    Ant_xml_build_files = []
    Maven_build_files = []
    Ivy_build_files = []
    for filepath in xml_files:
        if re.match(r'^build\.xml$', filepath.split('/')[-1]):
            Ant_xml_build_files.append(filepath)
        elif re.match(r'^(pom\.xml|maven[123]?\.xml)$', filepath.split('/')[-1]):
            Maven_build_files.append(filepath)
        elif re.match(r'^ivy\.xml$', filepath.split('/')[-1]):
            Ivy_build_files.append(filepath)

    Autotools_ac_build_files = []
    for filepath in ac_files:
        if re.match(r'^[Cc]onfigure.ac$', filepath.split('/')[-1]):
            Autotools_ac_build_files.append(filepath)
        
    Autotools_in_build_files = []        
    for filepath in in_files:
        if re.match(r'^([Cc]onfigure.in|[Mm]akefile.in)$', filepath.split('/')[-1]):
            Autotools_in_build_files.append(filepath)
        
    Autotools_configure_h_in_build_files = []        
    for filepath in in_files:
        if re.match(r'^config.h.in$', filepath.split('/')[-1]):
            Autotools_configure_h_in_build_files.append(filepath)

    Autotools_m4_build_files = []        
    for filepath in m4_files:
        if re.match(r'^ac(local|site).m4$', filepath.split('/')[-1]):
            Autotools_m4_build_files.append(filepath)
            
    Autotools_am_build_files = []        
    for filepath in am_files:
        if re.match(r'^[Mm]akefile.am$', filepath.split('/')[-1]):
            Autotools_am_build_files.append(filepath)


    extract_SATD_comments_from_Ant_Ivy_build_files(Ant_properties_build_files, Ant_xml_build_files, Ivy_build_files, repoIndex, repoName, commitHash)

    extract_SATD_comments_from_Maven_build_files(Maven_build_files, repoIndex, repoName, commitHash)

    extract_SATD_comments_from_Autotool_build_files(Autotools_am_build_files, Autotools_in_build_files, Autotools_configure_h_in_build_files, Autotools_ac_build_files, Autotools_m4_build_files, repoIndex, repoName, commitHash)
    
    extract_SATD_comments_from_CMake_build_files(CMake_txt_build_files, CMake_cmake_build_files, repoIndex, repoName, commitHash)

    if is_detector:
        output = out("java -jar {}/satd_detector.jar test".format(dir_path), Texts +"/exit")
        isSATDs = output.replace('>','').split('\n')[:-2]
        columns = ['repoIndex', 'repoName', 'linkLocation', 'comment', 'buildSysteminFile', 'charPosition', 'startLine', 'endLine']
        SATD_comments = pd.DataFrame(columns=columns, dtype=object) 
        Comments_with_no_keywords = pd.DataFrame(columns=columns, dtype=object)  
        for comment, linkLocation, buildSysteminFile, charPosition, startLine, endLine, isSATD in zip(Comments, LinkLocations, BuildSystemsinFile, CharPositions, StartLines, EndLines, isSATDs):
            if isSATD == 'SATD':
                SATD_comments = SATD_comments.append(pd.Series(
                                                    [repoIndex, repoName, linkLocation, comment, buildSysteminFile, charPosition, startLine, endLine],
                                                    index=SATD_comments.columns), ignore_index=True)
            else:
                Comments_with_no_keywords = Comments_with_no_keywords.append(pd.Series(
                                                    [repoIndex, repoName, linkLocation, comment, buildSysteminFile, charPosition, startLine, endLine],
                                                    index=Comments_with_no_keywords.columns), ignore_index=True)


    SATD_comments.to_csv('{}/{}/{}.csv'.format(dir_path, SATD_output_folder, repoIndex),index=None)
    Comments_with_no_keywords.to_csv('{}/{}/{}.csv'.format(dir_path, Non_SATD_output_folder, repoIndex),index=None)

    exit()


if __name__ == '__main__':
    main()

