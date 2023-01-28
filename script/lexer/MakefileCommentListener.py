# Generated from MakefileComment.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MakefileCommentParser import MakefileCommentParser
else:
    from MakefileCommentParser import MakefileCommentParser

# This class defines a complete listener for a parse tree produced by MakefileCommentParser.
class MakefileCommentListener(ParseTreeListener):

    # Enter a parse tree produced by MakefileCommentParser#file.
    def enterFile(self, ctx:MakefileCommentParser.FileContext):
        pass

    # Exit a parse tree produced by MakefileCommentParser#file.
    def exitFile(self, ctx:MakefileCommentParser.FileContext):
        pass


    # Enter a parse tree produced by MakefileCommentParser#command_invocation.
    def enterCommand_invocation(self, ctx:MakefileCommentParser.Command_invocationContext):
        pass

    # Exit a parse tree produced by MakefileCommentParser#command_invocation.
    def exitCommand_invocation(self, ctx:MakefileCommentParser.Command_invocationContext):
        pass


    # Enter a parse tree produced by MakefileCommentParser#single_argument.
    def enterSingle_argument(self, ctx:MakefileCommentParser.Single_argumentContext):
        pass

    # Exit a parse tree produced by MakefileCommentParser#single_argument.
    def exitSingle_argument(self, ctx:MakefileCommentParser.Single_argumentContext):
        pass


    # Enter a parse tree produced by MakefileCommentParser#compound_argument.
    def enterCompound_argument(self, ctx:MakefileCommentParser.Compound_argumentContext):
        pass

    # Exit a parse tree produced by MakefileCommentParser#compound_argument.
    def exitCompound_argument(self, ctx:MakefileCommentParser.Compound_argumentContext):
        pass



del MakefileCommentParser