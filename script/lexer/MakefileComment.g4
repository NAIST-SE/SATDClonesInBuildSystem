/*
Copyright (c) 2018  zbq.

License for use and distribution: Eclipse Public License

CMake language grammar reference:
https://cmake.org/cmake/help/v3.12/manual/cmake-language.7.html

*/
/*
Modified version for regular Makefiles
*/

grammar MakefileComment;

file
	: command_invocation* EOF
	;

command_invocation
	: Identifier '(' (single_argument|compound_argument)* ')'
	;

single_argument
	: Identifier | Unquoted_argument | Bracket_argument | Quoted_argument
	;

compound_argument
	: '(' (single_argument|compound_argument)* ')'
	;

Identifier
	: [A-Za-z_][A-Za-z0-9_]*
	;

Unquoted_argument
	: (~[ \t\r\n()#"\\] | Escape_sequence)+
	;

Escape_sequence
	: Escape_identity | Escape_encoded | Escape_semicolon
	;

fragment
Escape_identity
	: '\\' . | '\\' Newline 
	;

fragment
Escape_encoded
	: '\\t' | '\\r' | '\\n'
	;

fragment
Escape_semicolon
	: '\\;'
	;

Quoted_argument
	: '"' (~[\\"] | Escape_sequence | Quoted_cont)* '"'
	| '\'' (~[\\"] | Escape_sequence | Quoted_cont)* '\''
	;

fragment
Quoted_cont
	: '\\' ('\r' '\n'? | '\n')
	;

Bracket_argument
	: '[' Bracket_arg_nested ']'
	;

fragment
Bracket_arg_nested
	: '=' Bracket_arg_nested '='
	| '[' .*? ']'
	;

Line_comment
	: '#' (  // #
	  	  | '[' '='*   // #[==
		  | '[' '='* ~('=' | '[' | '\r' | '\n') ~('\r' | '\n')*  // #[==xx
		  | ~('[' | '\r' | '\n') ~('\r' | '\n')*  // #xx
		  ) ('\r' '\n'? | '\n' | EOF)
	-> channel(HIDDEN)
	;

DNL_comment
	: 'dnl' (~('\r' | '\n') | Quoted_cont)* ('\r' '\n'? | '\n' | EOF)
	-> channel(HIDDEN)
	;

Newline
	: ('\r' '\n'? | '\n')+
	-> skip
	;

Space
	: [ \t]+
	-> skip
	;
