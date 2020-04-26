import json
import sys

from . import status
from .exceptions import InvalidCode, InvalidResponse
from .helpers import valid_cpf

def main():
    cpf = sys.argv[1] if len(sys.argv) > 1 else input('CPF: ')
    code = sys.argv[2] if len(sys.argv) > 2 else  input('CÓDIGO: ')
    
    assert valid_cpf(cpf), "CPF inválido!"
    
    try:
        data = status(cpf, code)
        print(json.dumps(data, indent=4))
    except InvalidCode:
        print('Código inválido ou expirado!')
    except InvalidResponse as e:
        print(f'Resposta inválida da API: {e}')

if __name__ == '__main__':
    main()
