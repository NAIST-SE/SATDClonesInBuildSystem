import glob, os, re, sys
from pathlib import Path
from antlr4 import Token, Lexer, InputStream
from lexer.CMakeLexer import CMakeLexer
from lexer.MakefileCommentLexer import MakefileCommentLexer
from lexer.MakefileAmCommentLexer import MakefileAmCommentLexer
from lexer.CPP14Lexer import CPP14Lexer
import pandas as pd
from lexer.propertiesLexer import propertiesLexer
from lxml import etree as ElementTree

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
    # newline operator will be different in cpp grammer and others (e.g., /* */ and # \n)
    if isinstance(lexer, MakefileCommentLexer) or isinstance(lexer, MakefileAmCommentLexer) or isinstance(lexer, propertiesLexer) or isinstance(lexer, CMakeLexer):
        len_newline = 2
    elif isinstance(lexer, CPP14Lexer):
        len_newline = 1
    # identify multiline comment stop when end of file or next line is not starting comment sign
    while t.type != Token.EOF:
        if t.channel == lexer.HIDDEN:
            if last_comment != None and last_comment.is_continue(t.line,t.column) and last_type != None and last_type == t.type:
                last_comment.append(t.text, t.line)
            else:
                if len(t.text.split('\n')) > len_newline: 
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

# calculate ant+ivy investiment by build.properties, build.xml, and ivy.xml
def calculate_Ant_Ivy_investiment(Ant_properties_build_files, Ant_xml_build_files, Ivy_build_files):
    sum_line_of_comment, sum_line_of_code = 0, 0

    for file in Ant_properties_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Ant_xml_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Ivy_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    return (sum_line_of_comment, sum_line_of_code)

# calculate maven investiment by pom.xml, maven([123])?.xml
def calculate_Maven_investiment(Maven_build_files):
    sum_line_of_comment, sum_line_of_code = 0, 0

    for file in Maven_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue
        comments = xml_lexer(file, content)
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    return (sum_line_of_comment, sum_line_of_code)

# calculate autotools investiment by [Cc]onfigure.(ac|in), ac(local|site).m4, [Mm]akefile.(am|in), config.h.in
def calculate_Autotool_investiment(Autotools_am_build_files, Autotools_in_build_files, Autotools_configure_h_in_build_files, Autotools_ac_build_files, Autotools_m4_build_files):
    sum_line_of_comment, sum_line_of_code = 0, 0

    for file in Autotools_am_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content) 
        if line_of_source == 0: continue
        input_stream = InputStream(content)
        # am file will not have dnl comments
        comments = identify_comments(MakefileAmCommentLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Autotools_in_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Autotools_configure_h_in_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CPP14Lexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Autotools_ac_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in Autotools_m4_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(MakefileCommentLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    return (sum_line_of_comment, sum_line_of_code)


# calculate autotools investiment by CMakeLists.txt, *.cmake
def calculate_Cmake_investiment(CMake_txt_build_files, CMake_cmake_build_files):
    sum_line_of_comment, sum_line_of_code = 0, 0

    for file in CMake_txt_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    for file in CMake_cmake_build_files:
        content = open(file, 'r', errors='ignore').read()
        line_of_source = get_los(content)
        if line_of_source == 0: continue 
        input_stream = InputStream(content)
        comments = identify_comments(CMakeLexer(input_stream))
        line_of_comment = sum([comment.get_len() for comment in comments])
        line_of_code = line_of_source - line_of_comment
        sum_line_of_comment += line_of_comment
        sum_line_of_code += line_of_code

    return (sum_line_of_comment, sum_line_of_code)


def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


def main():
    args = sys.argv[1:]
    os.chdir(args[0])
    
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


    ant_ivy_investiment = calculate_Ant_Ivy_investiment(Ant_properties_build_files, Ant_xml_build_files, Ivy_build_files)

    maven_investiment = calculate_Maven_investiment(Maven_build_files)

    autotool_investiment = calculate_Autotool_investiment(Autotools_am_build_files, Autotools_in_build_files, Autotools_configure_h_in_build_files, Autotools_ac_build_files, Autotools_m4_build_files)
    
    cmake_investiment = calculate_Cmake_investiment(CMake_txt_build_files, CMake_cmake_build_files)

    build_comment_investiment = [ant_ivy_investiment[0], maven_investiment[0], autotool_investiment[0], cmake_investiment[0]]
    build_code_investiment = [ant_ivy_investiment[1], maven_investiment[1], autotool_investiment[1], cmake_investiment[1]]
    
    max_build_code_investiment = max(build_code_investiment)
    # select preliminary build system by number of code
    if build_code_investiment.index(max_build_code_investiment) == 0:
        if sum(build_code_investiment) == 0: preliminary_build_system = 'none'
        else: preliminary_build_system = 'ant+ivy'
    elif build_code_investiment.index(max_build_code_investiment) == 1: preliminary_build_system = 'maven'
    elif build_code_investiment.index(max_build_code_investiment) == 2: preliminary_build_system = 'autotool'
    elif build_code_investiment.index(max_build_code_investiment) == 3: preliminary_build_system = 'cmake'

    print('{},{},{},{},{},{},{},{},{},{},{}'.format(args[0].split('/')[-1], args[1], preliminary_build_system,
        ant_ivy_investiment[0], ant_ivy_investiment[1], 
        maven_investiment[0], maven_investiment[1], 
        autotool_investiment[0], autotool_investiment[1], 
        cmake_investiment[0], cmake_investiment[1]
    ))
    exit()


if __name__ == '__main__':
    main()
