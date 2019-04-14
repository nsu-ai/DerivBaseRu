from lark import Lark

short_parser = Lark(r"""
    value: SIGNED_NUMBER
         | and
         | or
    or : "[" [value] ("|" value)* "]"
    and : [value] ("&" value)

    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')


def normalize_raw_text(raw_text):
    operators = dict()
    logical_form = ''
    round_brackets = 0
    cur_operator = ''
    for c in raw_text:
        if c == '(':
            round_brackets += 1
        if round_brackets == 0:
            logical_form += c
        else:
            cur_operator += c
        if c == ')':
            round_brackets -= 1
            if round_brackets == 0:
                oper_str = cur_operator[1:-1]  # "try plt"
                sep_ind = oper_str.find(',')
                if sep_ind == -1:
                    args = "args={}"
                    mode_and_operator = oper_str
                else:
                    args = "args=" + oper_str[sep_ind + 1:].strip()
                    mode_and_operator = oper_str[:sep_ind]
                mode_and_operator = mode_and_operator.split()
                if len(mode_and_operator) > 1:
                    mode = mode_and_operator[0]
                    operator = mode_and_operator[1]
                else:
                    mode = 'do'
                    operator = mode_and_operator[0]
                operators[len(operators)] = operator + "(word=word, mode='" + mode + "', " + args + ")"
                cur_operator = ''
                logical_form += str(len(operators)-1)
    return logical_form, operators
