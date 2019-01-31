import re

def plus_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)\+([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def sub_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)-([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def multi_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)\*([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def div_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)\/([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def greater_than_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)>([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def less_than_method(matchs):
    matchs = re.findall(r"([0-9]*\.[0-9]*)<([0-9]*\.[0-9]*)", matchs)
    if len(matchs) != 0:
        return matchs[0]
    else:
        return False

def and_method(matchs):
    matchs = re.findall(r"AND\((.*)\),", matchs)
    if len(matchs) != 0:
        match = matchs[0]
        match = match.split(',')
        return match
    else:
        return False

def or_method(matchs):
    matchs = re.findall(r"OR\((.*)\)", matchs)
    if len(matchs) != 0:
        match = matchs[0]
        match = match.split(',')
        return match
    else:
        return False

def if_method(macro):
    matchs = re.findall(r"=IF\((.*)\)", macro)
    if len(matchs) != 0:
        result = matchs[0].split(',')
        res = result[-2:]
        formura = ','.join(result[:-2])
        return [formura, res]
    else:
        return False

def get_value(key):
    if key in dic:
        return dic[key]
    else:
        return None

def sub(MACRO):
    sub_re = r'[0-9]*\.[0-9]*[0-9]-[0-9]*\.[0-9]*[0-9]'
    if sub_method(MACRO) is not False:
        result = sub_method(MACRO)
        a = float(result[0])
        b = float(result[1])
        num =  a - b
        MACRO = re.sub(sub_re, str(num), MACRO)
        return MACRO

def plus(MACRO):
    plus_re = r'[0-9]*\.[0-9]*[0-9]\+[0-9]*\.[0-9]*[0-9]'
    if plus_method(MACRO) is not False:
        result = plus_method(MACRO)
        a = float(result[0])
        b = float(result[1])
        num =  a + b
        MACRO = re.sub(plus_re, str(num), MACRO)
        return MACRO

def less(MACRO):
    less_re = r'[0-9]*\.[0-9]*[0-9]<[0-9]*\.[0-9]*[0-9]'
    if less_than_method(MACRO) is not False:
        result = less_than_method(MACRO)
        a = float(result[0])
        b = float(result[1])
        if a < b:
            MACRO = re.sub(less_re, "True", MACRO)
        else:
            MACRO = re.sub(less_re, "False", MACRO)
        return MACRO

def greater(MACRO):
    less_re = r'[0-9]*\.[0-9]*[0-9]>[0-9]*\.[0-9]*[0-9]'
    if greater_than_method(MACRO) is not False:
        result = greater_than_method(MACRO)
        a = float(result[0])
        b = float(result[1])
        if a > b:
            MACRO = re.sub(less_re, "True", MACRO)
        else:
            MACRO = re.sub(less_re, "False", MACRO)
        return MACRO

def AND(MACRO):
    and_re = r'AND\((.*)\),'
    if and_method(MACRO) is not False:
        result = and_method(MACRO)
        if result[0] == "True" and result[1] == "True":
            MACRO = re.sub(and_re, "True,", MACRO)
        else:
            MACRO = re.sub(and_re, "False,", MACRO)
        return MACRO

def IF(MACRO):
    if_re = r'=IF\((True|False).*\)'
    result = re.findall(if_re, MACRO)
    if result[0] == "True":
        return "OK"
    else:
        return "FALSE"

MACRO = '=IF(AND(A16-A11<Z11,A16+A12>Z12), "OK", "FALSE")'
A16 = 88.000
A11 = 0.015
A12 = 0.009
Z11 = 87.996
Z12 = 88.006

value_re = r'([A-Z]+[0-9]+'

result = re.findall(r'([A-Z]+[0-9]+)', MACRO)
print(result)

dic = { "A16":A16, "A11":A11, "A12":A12, "Z11":Z11, "Z12":Z12 }

for k, v in dic.items():
    MACRO = MACRO.replace(k, str(v))

MACRO = sub(MACRO)
MACRO = plus(MACRO)
MACRO = less(MACRO)
MACRO = greater(MACRO)
MACRO = AND(MACRO)
result = IF(MACRO)

print(result)
