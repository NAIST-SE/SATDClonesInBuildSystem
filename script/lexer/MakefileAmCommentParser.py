# Generated from MakefileAmComment.g4 by ANTLR 4.10
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,
        1,1,1,2,1,2,1,3,1,3,1,3,5,3,33,8,3,10,3,12,3,36,9,3,1,3,1,3,1,3,
        0,0,4,0,2,4,6,0,1,2,0,3,4,6,7,40,0,11,1,0,0,0,2,16,1,0,0,0,4,27,
        1,0,0,0,6,29,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,
        1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,
        15,1,1,0,0,0,16,17,5,3,0,0,17,22,5,1,0,0,18,21,3,4,2,0,19,21,3,6,
        3,0,20,18,1,0,0,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,
        1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,2,0,0,26,3,1,0,0,0,27,
        28,7,0,0,0,28,5,1,0,0,0,29,34,5,1,0,0,30,33,3,4,2,0,31,33,3,6,3,
        0,32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,
        1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,2,0,0,38,7,1,0,0,0,5,
        11,20,22,32,34
    ]

class MakefileAmCommentParser ( Parser ):

    grammarFileName = "MakefileAmComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "Unquoted_argument", "Escape_sequence", "Quoted_argument", 
                      "Bracket_argument", "Line_comment", "Newline", "Space" ]

    RULE_file = 0
    RULE_command_invocation = 1
    RULE_single_argument = 2
    RULE_compound_argument = 3

    ruleNames =  [ "file", "command_invocation", "single_argument", "compound_argument" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Identifier=3
    Unquoted_argument=4
    Escape_sequence=5
    Quoted_argument=6
    Bracket_argument=7
    Line_comment=8
    Newline=9
    Space=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MakefileAmCommentParser.EOF, 0)

        def command_invocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileAmCommentParser.Command_invocationContext)
            else:
                return self.getTypedRuleContext(MakefileAmCommentParser.Command_invocationContext,i)


        def getRuleIndex(self):
            return MakefileAmCommentParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = MakefileAmCommentParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MakefileAmCommentParser.Identifier:
                self.state = 8
                self.command_invocation()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(MakefileAmCommentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Command_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MakefileAmCommentParser.Identifier, 0)

        def single_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileAmCommentParser.Single_argumentContext)
            else:
                return self.getTypedRuleContext(MakefileAmCommentParser.Single_argumentContext,i)


        def compound_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileAmCommentParser.Compound_argumentContext)
            else:
                return self.getTypedRuleContext(MakefileAmCommentParser.Compound_argumentContext,i)


        def getRuleIndex(self):
            return MakefileAmCommentParser.RULE_command_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand_invocation" ):
                listener.enterCommand_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand_invocation" ):
                listener.exitCommand_invocation(self)




    def command_invocation(self):

        localctx = MakefileAmCommentParser.Command_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(MakefileAmCommentParser.Identifier)
            self.state = 17
            self.match(MakefileAmCommentParser.T__0)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MakefileAmCommentParser.T__0) | (1 << MakefileAmCommentParser.Identifier) | (1 << MakefileAmCommentParser.Unquoted_argument) | (1 << MakefileAmCommentParser.Quoted_argument) | (1 << MakefileAmCommentParser.Bracket_argument))) != 0):
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MakefileAmCommentParser.Identifier, MakefileAmCommentParser.Unquoted_argument, MakefileAmCommentParser.Quoted_argument, MakefileAmCommentParser.Bracket_argument]:
                    self.state = 18
                    self.single_argument()
                    pass
                elif token in [MakefileAmCommentParser.T__0]:
                    self.state = 19
                    self.compound_argument()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(MakefileAmCommentParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MakefileAmCommentParser.Identifier, 0)

        def Unquoted_argument(self):
            return self.getToken(MakefileAmCommentParser.Unquoted_argument, 0)

        def Bracket_argument(self):
            return self.getToken(MakefileAmCommentParser.Bracket_argument, 0)

        def Quoted_argument(self):
            return self.getToken(MakefileAmCommentParser.Quoted_argument, 0)

        def getRuleIndex(self):
            return MakefileAmCommentParser.RULE_single_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_argument" ):
                listener.enterSingle_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_argument" ):
                listener.exitSingle_argument(self)




    def single_argument(self):

        localctx = MakefileAmCommentParser.Single_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_single_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MakefileAmCommentParser.Identifier) | (1 << MakefileAmCommentParser.Unquoted_argument) | (1 << MakefileAmCommentParser.Quoted_argument) | (1 << MakefileAmCommentParser.Bracket_argument))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileAmCommentParser.Single_argumentContext)
            else:
                return self.getTypedRuleContext(MakefileAmCommentParser.Single_argumentContext,i)


        def compound_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileAmCommentParser.Compound_argumentContext)
            else:
                return self.getTypedRuleContext(MakefileAmCommentParser.Compound_argumentContext,i)


        def getRuleIndex(self):
            return MakefileAmCommentParser.RULE_compound_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_argument" ):
                listener.enterCompound_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_argument" ):
                listener.exitCompound_argument(self)




    def compound_argument(self):

        localctx = MakefileAmCommentParser.Compound_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compound_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MakefileAmCommentParser.T__0)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MakefileAmCommentParser.T__0) | (1 << MakefileAmCommentParser.Identifier) | (1 << MakefileAmCommentParser.Unquoted_argument) | (1 << MakefileAmCommentParser.Quoted_argument) | (1 << MakefileAmCommentParser.Bracket_argument))) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MakefileAmCommentParser.Identifier, MakefileAmCommentParser.Unquoted_argument, MakefileAmCommentParser.Quoted_argument, MakefileAmCommentParser.Bracket_argument]:
                    self.state = 30
                    self.single_argument()
                    pass
                elif token in [MakefileAmCommentParser.T__0]:
                    self.state = 31
                    self.compound_argument()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(MakefileAmCommentParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





