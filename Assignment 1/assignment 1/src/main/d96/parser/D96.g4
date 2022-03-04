grammar D96;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options {
	language = Python3;
}

program: class_declaration EOF;
//class_declaration
class_declaration: class_declaration_part+;
class_declaration_part: CLASS (main_keyword|ID|Program) (COLON ID)? LP member* RP; 
class_keyword: CLASS;
member: attribute_lit | method_lit;

//Attribute declaration
attribute_lit: (VAL|VAR) attribute_list COLON type_name (ASSIGN expr_list)? SEMI;
attribute_list: attribute (CM attribute)*;
attribute: ID|DO_ID;
type_name: INT|FLOAT|BOOLEAN|STRING|array_declaration|attribute;


///Method declaration
method_lit: normal_method | method_constructor | main_destructor;

method_constructor: CONSTRUCTOR (LB parameter_list? RB)? block_stm_no_return;
main_destructor:(main_keyword|DESTRUCTOR) (LB RB)? block_stm_no_return;
normal_method: identifier (LB parameter_list? RB)? block_stm;

parameter_list: identifier_list (SEMI identifier_list)*;
identifier_list: identifier (CM identifier)* COLON type_name; 

//Block statement in 6.9


//6. Statement
///6.9 Block statement

block_stm_no_return: LP stm_no_return* RP;

stm_no_return: 
    variable_statement SEMI
    | assignment_statement SEMI
    | if_statement
    | for_in_statement
    | break_statement SEMI
    | continue_statement SEMI
    | method_statement SEMI
    ;


block_stm: LP stm*  RP;

stm: 
    variable_statement SEMI
    | assignment_statement SEMI
    | if_statement
    | for_in_statement
    | break_statement SEMI
    | continue_statement SEMI
    | return_statement SEMI
    | method_statement SEMI
    ;

/// 6.1 Variable statement
variable_statement: (VAR|VAL) variable_list COLON type_name (ASSIGN expr_list)?;
variable_list: ID (CM ID)*;

///6.2 Assignment statement
assignment_statement: (ID|index_expr|method_statement|array_attribute) ASSIGN expr;

//6.3 if statement
if_statement: 
        IF LB expr RB block_stm
        (ELSEIF LB expr RB block_stm)*
        (ELSE block_stm)?;

//6.4 For/In statement
for_in_statement:
        FOREACH LB ID IN expr DOUBLE_DOT expr (By_keyword expr)? RB 
        block_stm; 
By_keyword: BY;
//6.5 Breack statement
break_statement: BREAK;

//6.6 Continue statement:
continue_statement: CONTINUE;

//6.7 Return statement:
return_statement: Return_word expr?;
Return_word: RETURN;

//6.8 Method invocation statement
method_statement: (ID|DO_ID|Self) (DOT (ID|method_statement))* (LB expr_list? RB)? 
| (ID) (DOUBLE_COLON (DO_ID|method_statement))* (LB expr_list? RB)? ;


//5.9 Operator precedence and associativity
expr_list: expr (CM expr)*;
expr: string_expr;
string_expr: relational_expr string_op relational_expr | relational_expr;
relational_expr: logical_expr relational_op logical_expr | logical_expr;
logical_expr: logical_expr logical_op add_expr | add_expr;
add_expr: add_expr add_op mul_expr | mul_expr;
mul_expr: mul_expr multi_op log_expr | log_expr;
log_expr: negation_op log_expr | sign_expr;
sign_expr: negation_number sign_expr | index_expr;
index_expr: index_expr index_op | instance_access_expr;
instance_access_expr: instance_access_expr instance_element | static_access_expr;
static_access_expr: static_element | new_expr;
new_expr: NEW ID (LB expr_list? RB)? | parenth_exp;
parenth_exp: LB expr RB | operative;
operative: literal|array_component|array_attribute|Self| ID ;

literal: boollit| NONZERO_INT | INT_LIT | FLOAT_LIT | STRING_LIT;

instance_element: DOT ID (LB expr_list? RB)?;
static_element: ID DOUBLE_COLON DO_ID (LB expr_list? RB)?;
array_component: ARRAY LB (expr_list)? RB; 

string_op: COMPARE_STRING|ADD_STRING;
relational_op: EQUAL|DIFFER|LESS|GREATER|LESS_EQUAL|GREATER_EQUAL;
relational_op_bool: EQUAL|DIFFER;
relational_op_number: LESS|GREATER|LESS_EQUAL|GREATER_EQUAL|EQUAL;
logical_op: AND|OR;
add_op: ADD|MINUS;
multi_op: PRODUCT|DIVIDE;
negation_op: NOT;
negation_number: MINUS;
index_op: (LS expr RS)+ ;



//KEYWORDS
////KEYWORDS: [A-Z][a-z]+;
Program: 'Program';
main_keyword: 'main';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
//5.8 Self
Self: 'Self';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
TRUE: 'True';
FALSE: 'False';


//Identifier
fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment UNDERSCORE: '_';

ID: (LOWERCASE|UPPERCASE|UNDERSCORE)(LOWERCASE|UPPERCASE|UNDERSCORE|DIGIT)*;
DO_ID: '$'(LOWERCASE|UPPERCASE|UNDERSCORE|DIGIT)+;
identifier: ID|DO_ID;




//OPERATORS

///Arithmetic operators

ADD: '+';
MINUS: '-';
PRODUCT: '*';
DIVIDE: '/';
MOD: '%';
///Boolean operators
NOT: '!';
AND: '&&';
OR: '||';
//String Operators
COMPARE_STRING: '==.';
ADD_STRING: '+.';	
//Relational operators
EQUAL: '==';			//Int/Boolean
ASSIGN: '=';
DIFFER: '!=';			//Int/Boolean
LESS: '<';		    	//Int/Float
LESS_EQUAL: '<=';		//Int/Float
GREATER: '>';			//Int/Float
GREATER_EQUAL: '>=';	//Int/Float
DOUBLE_COLON: '::';


//3.7 LITERALS
//Int
NONZERO_INT: [1-9][0-9]*;
INT_LIT: (OCTAL|HEXA|BINARY|DEC) {self.text = self.text.replace('_','')};

fragment OCTAL: '0' [1-7] (UNDERSCORE? OCTAL_DIGIT (UNDERSCORE OCTAL_DIGIT)?)* ;
fragment HEXA: '0' ('x'|'X') [1-9A-F](UNDERSCORE? HEX_DIGIT (UNDERSCORE HEX_DIGIT)?)* ;
fragment BINARY: '0'('b'|'B')'1'(UNDERSCORE? BINARY_DIGIT (UNDERSCORE BINARY_DIGIT)?)* ;
fragment DEC: '0'|[1-9] (UNDERSCORE? DIGIT (UNDERSCORE DIGIT)?)* ;

fragment BINARY_DIGIT: [0-1];
fragment HEX_DIGIT: [0-9A-F];
fragment OCTAL_DIGIT: [0-7];
fragment DIGIT: [0-9];
///Float

FLOAT_LIT: FLOAT_LIT_PART  {self.text = self.text.replace('_','')};
fragment FLOAT_LIT_PART: INT_PART (DEC_PART| EXP_PART|DEC_PART EXP_PART) | DEC_PART EXP_PART; 
fragment INT_PART: DEC;
fragment DEC_PART: (DOT DIGIT*) ;
fragment EXP_PART: ('e'|'E')[+-]?DIGIT+;




// String

fragment ESCAPE_SEQUENCE: 
    '\\\''
	| '\\\\'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
    | '\'';
fragment CHAR_STRING : ~["\\\r\n] | ESCAPE_SEQUENCE | '\'"'; 
STRING_LIT: '"' CHAR_STRING* '"' {self.text = self.text.strip('"')};
ILLEGAL_ESCAPE: '"' CHAR_STRING* ('\\' ~([bfanrt\\] | '\'') )  {self.text = self.text.replace('"','',1)};
UNCLOSE_STRING: '"' CHAR_STRING* {self.text = self.text.replace('"','',1)}; 


///Array declaration
array_declaration: ARRAY LS ((type_name CM)? array_type? RS);
array_attribute: ID (LS expr RS)+;
array_type: NONZERO_INT|INT_LIT;
//Array
array_lit: ARRAY LB (expr_list)? RB;
mul_array: ARRAY LB (array_lit (CM array_lit)*) RB;

// array_lit: array_int | array_float | array_boolean | array_string | array_expr;

// array_int: ARRAY LB (INT_LIT (CM INT_LIT)*)? RB;
// array_float: ARRAY LB (FLOAT_LIT (CM FLOAT_LIT)*)? RB;
// array_boolean: ARRAY LB (boollit (CM boollit)*)? RB;
// array_string: ARRAY LB (STRING_LIT (CM STRING_LIT)*)? RB;
// array_expr: ARRAY LB (expr_list)? RB;

///Lexer
ARRAY_LIT: ARRAY_INT | ARRAY_FLOAT | ARRAY_BOOLEAN| ARRAY_STRING;
fragment ARRAY_INT: ARRAY LB (INT_LIT INT_LIST)? RB;
fragment ARRAY_FLOAT: ARRAY LB (FLOAT_LIT FLOAT_LIST)? RB;
fragment ARRAY_BOOLEAN: ARRAY LB ((TRUE|FALSE) BOOLEAN_LIST)? RB;
fragment ARRAY_STRING: ARRAY LB (STRING_LIT STRING_LIST)? RB;

fragment INT_LIST: (CM  INT_LIT INT_LIST)?;
fragment FLOAT_LIST: (CM FLOAT_LIT FLOAT_LIST)?;
fragment BOOLEAN_LIST: (CM (TRUE|FALSE) BOOLEAN_LIST)?;
fragment STRING_LIST: (CM STRING_LIT STRING_LIST)?;


//Multi Array
// mul_array: ARRAY LB mul_array_lit RB;
// mul_array_lit: mul_array_int | mul_array_float | mul_array_boolean | mul_array_string ;

// mul_array_int: array_int(CM array_int)*;
// mul_array_float: array_float(CM array_float)*;
// mul_array_boolean: array_boolean(CM array_boolean)*;
// mul_array_string: array_string(CM array_string)*;

////Lexer
MUL_ARRAY: ARRAY LB MUL_ARRAY_LIT RB;
fragment MUL_ARRAY_LIT: MUL_ARRAY_INT | MUL_ARRAY_FLOAT | MUL_ARRAY_BOOLEAN | MUL_ARRAY_STRING;

fragment MUL_ARRAY_INT: ARRAY_INT (CM ARRAY_INT)*; 
fragment MUL_ARRAY_FLOAT: ARRAY_FLOAT (CM ARRAY_FLOAT)*; 
fragment MUL_ARRAY_BOOLEAN: ARRAY_BOOLEAN (CM ARRAY_BOOLEAN)*; 
fragment MUL_ARRAY_STRING: ARRAY_STRING (CM ARRAY_STRING)*; 
///Boolean
boollit: TRUE | FALSE;

// 3.6 Seperators

LB: '(';
RB: ')';
LP: '{';
RP: '}';
LS: '[';
RS: ']';
COLON: ':';
DOT: '.';
DOUBLE_DOT: '..';
CM: ',';
SEMI: ';';


COMMENT: '##' .*? '##' -> skip;


WS: ([ \t\r\n\b\f]+) -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
