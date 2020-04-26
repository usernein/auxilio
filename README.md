# auxilio.py
Programa não-oficial para consultar a situação de solicitações do Auxílio Emergencial.

## Instalação
`pip3 install https://github.com/usernein/auxilio`

## Modo de uso:
### CLI
Apenas execute `auxilio` no terminal. O programa lhe perguntará o CPF e o código de acesso (recebido por SMS). Se realizada com sucesso, a consulta retornará o JSON retornado pela API do auxilio.caixa.gov.br.

### Programaticamente
```python
import auxilio

cpf = 00000000000
code = 000000

try:
    status = auxilio.status(cpf, code) # objeto JSON retornado pela API (em forma de dicionário Python)
except auxilio.InvalidCode:
    # Código inválido ou expirado
except auxilio.InvalidResponse:
    # Resposta inválida (o retorno da API não é um JSON válido ou é um objeto vazio)
```