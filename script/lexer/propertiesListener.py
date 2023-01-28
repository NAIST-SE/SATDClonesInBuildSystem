# Generated from properties.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .propertiesParser import propertiesParser
else:
    from propertiesParser import propertiesParser

# This class defines a complete listener for a parse tree produced by propertiesParser.
class propertiesListener(ParseTreeListener):

    # Enter a parse tree produced by propertiesParser#propertiesFile.
    def enterPropertiesFile(self, ctx:propertiesParser.PropertiesFileContext):
        pass

    # Exit a parse tree produced by propertiesParser#propertiesFile.
    def exitPropertiesFile(self, ctx:propertiesParser.PropertiesFileContext):
        pass


    # Enter a parse tree produced by propertiesParser#row.
    def enterRow(self, ctx:propertiesParser.RowContext):
        pass

    # Exit a parse tree produced by propertiesParser#row.
    def exitRow(self, ctx:propertiesParser.RowContext):
        pass


    # Enter a parse tree produced by propertiesParser#decl.
    def enterDecl(self, ctx:propertiesParser.DeclContext):
        pass

    # Exit a parse tree produced by propertiesParser#decl.
    def exitDecl(self, ctx:propertiesParser.DeclContext):
        pass


    # Enter a parse tree produced by propertiesParser#key.
    def enterKey(self, ctx:propertiesParser.KeyContext):
        pass

    # Exit a parse tree produced by propertiesParser#key.
    def exitKey(self, ctx:propertiesParser.KeyContext):
        pass


    # Enter a parse tree produced by propertiesParser#value.
    def enterValue(self, ctx:propertiesParser.ValueContext):
        pass

    # Exit a parse tree produced by propertiesParser#value.
    def exitValue(self, ctx:propertiesParser.ValueContext):
        pass


    # Enter a parse tree produced by propertiesParser#comment.
    def enterComment(self, ctx:propertiesParser.CommentContext):
        pass

    # Exit a parse tree produced by propertiesParser#comment.
    def exitComment(self, ctx:propertiesParser.CommentContext):
        pass



del propertiesParser