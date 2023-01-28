# Generated from properties.g4 by ANTLR 4.10
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,4,2,23,8,2,11,2,12,2,24,1,3,
        1,3,1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,3,1,3,1,4,1,4,5,4,40,8,
        4,10,4,12,4,43,9,4,1,4,1,4,1,5,4,5,48,8,5,11,5,12,5,49,0,0,6,1,1,
        3,2,5,3,7,4,9,5,11,6,1,0,3,7,0,32,32,37,37,44,58,64,90,95,95,97,
        123,125,125,1,0,34,34,2,0,10,10,13,13,56,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,
        19,1,0,0,0,5,22,1,0,0,0,7,26,1,0,0,0,9,37,1,0,0,0,11,47,1,0,0,0,
        13,14,5,61,0,0,14,2,1,0,0,0,15,16,5,92,0,0,16,20,9,0,0,0,17,18,5,
        92,0,0,18,20,3,11,5,0,19,15,1,0,0,0,19,17,1,0,0,0,20,4,1,0,0,0,21,
        23,7,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,6,1,0,0,0,26,32,5,34,0,0,27,28,5,34,0,0,28,31,5,34,0,0,29,31,
        8,1,0,0,30,27,1,0,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,
        32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,34,0,0,36,8,1,
        0,0,0,37,41,5,35,0,0,38,40,8,2,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,
        39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,6,4,0,
        0,45,10,1,0,0,0,46,48,7,2,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,
        1,0,0,0,49,50,1,0,0,0,50,12,1,0,0,0,7,0,19,24,30,32,41,49,1,0,1,
        0
    ]

class propertiesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Escape_identity = 2
    TEXT = 3
    STRING = 4
    COMMENT = 5
    TERMINATOR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "Escape_identity", "TEXT", "STRING", "COMMENT", "TERMINATOR" ]

    ruleNames = [ "T__0", "Escape_identity", "TEXT", "STRING", "COMMENT", 
                  "TERMINATOR" ]

    grammarFileName = "properties.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


