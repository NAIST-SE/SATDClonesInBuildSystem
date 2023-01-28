# Generated from CMake.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CMakeParser import CMakeParser
else:
    from CMakeParser import CMakeParser

# This class defines a complete listener for a parse tree produced by CMakeParser.
class CMakeListener(ParseTreeListener):

    # Enter a parse tree produced by CMakeParser#file.
    def enterFile(self, ctx:CMakeParser.FileContext):
        pass

    # Exit a parse tree produced by CMakeParser#file.
    def exitFile(self, ctx:CMakeParser.FileContext):
        pass


    # Enter a parse tree produced by CMakeParser#command_invocation.
    def enterCommand_invocation(self, ctx:CMakeParser.Command_invocationContext):
        pass

    # Exit a parse tree produced by CMakeParser#command_invocation.
    def exitCommand_invocation(self, ctx:CMakeParser.Command_invocationContext):
        pass


    # Enter a parse tree produced by CMakeParser#single_argument.
    def enterSingle_argument(self, ctx:CMakeParser.Single_argumentContext):
        pass

    # Exit a parse tree produced by CMakeParser#single_argument.
    def exitSingle_argument(self, ctx:CMakeParser.Single_argumentContext):
        pass


    # Enter a parse tree produced by CMakeParser#compound_argument.
    def enterCompound_argument(self, ctx:CMakeParser.Compound_argumentContext):
        pass

    # Exit a parse tree produced by CMakeParser#compound_argument.
    def exitCompound_argument(self, ctx:CMakeParser.Compound_argumentContext):
        pass



del CMakeParser