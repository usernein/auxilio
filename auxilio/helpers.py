import re

def valid_cpf(cpf):
    # remove non-digit
    cpf = re.sub(r'\D', '', cpf)
    
    # check length
    return (len(cpf) == 11)