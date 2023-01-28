# Generated from properties.g4 by ANTLR 4.10
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
        4,1,6,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,0,
        14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,3,2,27,
        8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,3,4,31,
        0,13,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,28,1,0,0,0,8,30,1,0,0,0,
        10,32,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,
        0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,
        22,3,10,5,0,20,22,3,4,2,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,
        0,23,24,3,6,3,0,24,26,5,1,0,0,25,27,3,8,4,0,26,25,1,0,0,0,26,27,
        1,0,0,0,27,5,1,0,0,0,28,29,5,3,0,0,29,7,1,0,0,0,30,31,7,0,0,0,31,
        9,1,0,0,0,32,33,5,5,0,0,33,11,1,0,0,0,3,15,21,26
    ]

class propertiesParser ( Parser ):

    grammarFileName = "properties.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Escape_identity", "TEXT", 
                      "STRING", "COMMENT", "TERMINATOR" ]

    RULE_propertiesFile = 0
    RULE_row = 1
    RULE_decl = 2
    RULE_key = 3
    RULE_value = 4
    RULE_comment = 5

    ruleNames =  [ "propertiesFile", "row", "decl", "key", "value", "comment" ]

    EOF = Token.EOF
    T__0=1
    Escape_identity=2
    TEXT=3
    STRING=4
    COMMENT=5
    TERMINATOR=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PropertiesFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(propertiesParser.EOF, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(propertiesParser.RowContext)
            else:
                return self.getTypedRuleContext(propertiesParser.RowContext,i)


        def getRuleIndex(self):
            return propertiesParser.RULE_propertiesFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertiesFile" ):
                listener.enterPropertiesFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertiesFile" ):
                listener.exitPropertiesFile(self)




    def propertiesFile(self):

        localctx = propertiesParser.PropertiesFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_propertiesFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.row()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==propertiesParser.TEXT or _la==propertiesParser.COMMENT):
                    break

            self.state = 17
            self.match(propertiesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self):
            return self.getTypedRuleContext(propertiesParser.CommentContext,0)


        def decl(self):
            return self.getTypedRuleContext(propertiesParser.DeclContext,0)


        def getRuleIndex(self):
            return propertiesParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = propertiesParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [propertiesParser.COMMENT]:
                self.state = 19
                self.comment()
                pass
            elif token in [propertiesParser.TEXT]:
                self.state = 20
                self.decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(propertiesParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(propertiesParser.ValueContext,0)


        def getRuleIndex(self):
            return propertiesParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = propertiesParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.key()
            self.state = 24
            self.match(propertiesParser.T__0)
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 25
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(propertiesParser.TEXT, 0)

        def getRuleIndex(self):
            return propertiesParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = propertiesParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(propertiesParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(propertiesParser.TEXT, 0)

        def STRING(self):
            return self.getToken(propertiesParser.STRING, 0)

        def getRuleIndex(self):
            return propertiesParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = propertiesParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==propertiesParser.TEXT or _la==propertiesParser.STRING):
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(propertiesParser.COMMENT, 0)

        def getRuleIndex(self):
            return propertiesParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = propertiesParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(propertiesParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





