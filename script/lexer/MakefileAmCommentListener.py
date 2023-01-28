# Generated from MakefileAmComment.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MakefileAmCommentParser import MakefileAmCommentParser
else:
    from MakefileAmCommentParser import MakefileAmCommentParser

# This class defines a complete listener for a parse tree produced by MakefileAmCommentParser.
class MakefileAmCommentListener(ParseTreeListener):

    # Enter a parse tree produced by MakefileAmCommentParser#file.
    def enterFile(self, ctx:MakefileAmCommentParser.FileContext):
        pass

    # Exit a parse tree produced by MakefileAmCommentParser#file.
    def exitFile(self, ctx:MakefileAmCommentParser.FileContext):
        pass


    # Enter a parse tree produced by MakefileAmCommentParser#command_invocation.
    def enterCommand_invocation(self, ctx:MakefileAmCommentParser.Command_invocationContext):
        pass

    # Exit a parse tree produced by MakefileAmCommentParser#command_invocation.
    def exitCommand_invocation(self, ctx:MakefileAmCommentParser.Command_invocationContext):
        pass


    # Enter a parse tree produced by MakefileAmCommentParser#single_argument.
    def enterSingle_argument(self, ctx:MakefileAmCommentParser.Single_argumentContext):
        pass

    # Exit a parse tree produced by MakefileAmCommentParser#single_argument.
    def exitSingle_argument(self, ctx:MakefileAmCommentParser.Single_argumentContext):
        pass


    # Enter a parse tree produced by MakefileAmCommentParser#compound_argument.
    def enterCompound_argument(self, ctx:MakefileAmCommentParser.Compound_argumentContext):
        pass

    # Exit a parse tree produced by MakefileAmCommentParser#compound_argument.
    def exitCompound_argument(self, ctx:MakefileAmCommentParser.Compound_argumentContext):
        pass



del MakefileAmCommentParser