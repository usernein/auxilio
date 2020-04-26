import json
import requests
import time

from .exceptions import InvalidCode, InvalidResponse

VALIDATION_URL = "https://auxilio.caixa.gov.br/api/sms/validarLogin"
LOGIN_URL = "https://auxilio.caixa.gov.br/api/cadastro/validarLogin/{cpf}"
HEADERS = {
    "content-type": "application/json; charset=utf-8"
}

def status(cpf, code):
    payload = json.dumps({
        "cpf": int(cpf)
     })
    consulta = requests.post(VALIDATION_URL, headers=HEADERS, data=payload)
    msg = consulta.json()['mensagem'].upper()
    
    if 'VÁLIDO' in msg:
        payload = json.dumps({
            "code": str(code)
        })
        
        request = requests.put(LOGIN_URL.format(cpf=cpf), headers=HEADERS, data=payload)
        dados = request.json()
        
        if not dados:
            raise InvalidResponse(request.data())
        
        if dados.get('codigo') == 401:
            raise InvalidCode
        
        return dados
        """
            Nome: {dados['noPessoa']}
            CPF: {dados['cpf']}
            Situação: {dados['situacao']} | {dados['nuSituacaoCadastro']}
            Motivo: {dados['motivo']}
            Banco: {dados['banco']}
            Bolsa Família: {dados['bolsa_familia']}
            Solicitação inicial: {dados['dhFinalizacaoCadastro']}
        """
    else:
        raise InvalidCode
