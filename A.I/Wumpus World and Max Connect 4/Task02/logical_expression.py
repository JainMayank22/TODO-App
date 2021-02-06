
import sys

class logical_expression:
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    if expression.symbol[0]:
        sys.stdout.write('%s' % expression.symbol[0])

    elif expression == 0 or expression == None or expression == '':
        print ('\nINVALID\n')

    else:  # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':  # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print ('\nUnexpected end of input.\n')
            return 0

        if input_string[counter[0]] == ' ':  # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':  # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                  (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                  (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
            expression.connective[0].lower() != 'or' and \
            expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def get_symbols(expression, symbols):
    if expression.symbol[0]:
        symbols.append(expression.symbol[0])
    for subexpression in expression.subexpressions:
        get_symbols(subexpression, symbols)


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1


def model_expansion(model, sym_key, value):
    model[sym_key] = value
    return model


def pl_true(expression, model):
    if expression.connective[0].lower() == 'or':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value or pl_true(subexpression, model)
        return tru_value
    elif expression.connective[0].lower() == 'and':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value and pl_true(subexpression, model)
        return tru_value

    elif expression.connective[0].lower() == 'xor':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value ^ pl_true(subexpression, model)
        return tru_value

    elif expression.connective[0].lower() == 'not':
        tru_value = not pl_true(expression.subexpressions[0], model)
        return tru_value
    elif expression.connective[0].lower() == 'iff':
        exp1 = pl_true(expression.subexpressions[0], model)
        exp2 = pl_true(expression.subexpressions[1], model)
        return ((not exp1) or exp2) and ((not exp2) or exp1)

    elif expression.connective[0].lower() == 'if':
        exp1 = pl_true(expression.subexpressions[0], model)
        exp2 = pl_true(expression.subexpressions[1], model)
        return ((not exp1) or exp2)
    return model[expression.symbol[0]]



def all_check_tt(kb, alpha, symbols, model):
    if not symbols:
        if not pl_true(kb, model):
            return True
        else:
            return pl_true(alpha, model)
    p = symbols[0]
    rest = symbols[1:]
    return all_check_tt(kb, alpha, rest, model_expansion(model, p, True)) \
           and all_check_tt(kb, alpha, rest, model_expansion(model, p, False))


# Add all your functions here
def check_true_false(knowledge_base, statement, symbolslist, negation, symbols, model):
    try:
        output_file = open('result.txt', 'w')
    except:
        print('failed to create output file')
    statement_true = all_check_tt(knowledge_base, statement, symbols, model)
    statement_false = all_check_tt(knowledge_base, negation, symbols, model)
    if statement_true == False and statement_false == True:
        output_file.write('definitely false')
        print ('definitely false')
    elif statement_true == True and statement_false == False:
        output_file.write('definitely true')
        print ('definitely true')

    elif statement_true == True and statement_false == True:
        output_file.write('both true and false')
        print ('both true and false')


    elif statement_true == False and statement_false == False:
        output_file.write('possibly true, possibly false')
        print ('possibly true, possibly false')
    else:
        output_file.write('Error')
    print
    output_file.close()
