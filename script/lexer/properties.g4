
grammar properties;

propertiesFile
    :
    row+ EOF ;

row
    :
    (comment | decl)
    ;

decl
    : key '=' value?
    ;


Escape_identity
    : '\\' . | '\\' TERMINATOR
    ;
    
key
    :
    TEXT;

value
    :
    TEXT | STRING;

comment
    :
    COMMENT;

TEXT
    :
    [a-zA-Z0-9 @:._/,%{}-]+;

STRING
    :
    '"' ('""'|~'"')* '"' ; // quote-quote is an escaped quote

COMMENT
    : '#' ~ [\r\n]*
    -> channel(HIDDEN)
    ;

TERMINATOR
    : [\r\n]+ 
    ;