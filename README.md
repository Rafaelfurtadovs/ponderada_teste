# Teste Automatizado: rota /courses

### Objetivo:
Validar o funcionamento do endpoint /courses para garantir que ele retorna uma lista de cursos válida e que a API está devidamente autenticada.

### Como rodar o teste?
- Para ver o código de status: pytest test.py
- Caso queira ver as informações obtidas use: python test.py

### Pré condições do teste:
- O arquivo .env deve estar configurado com as variáveis BASE_URL (URL base da API) e TOKEN (token de autenticação válido).

- O servidor da API deve estar em funcionamento.

- O endpoint /courses deve estar implementado e acessível.

### Procedimento do teste:
- Configure o ambiente carregando as variáveis do arquivo `.env`.
- Construa a URL completa para o endpoint `/courses`.
- Realize uma requisição HTTP GET para o endpoint.
- Valide os seguintes critérios:
    - O código de status da resposta deve ser `200`.
   - O corpo da resposta deve ser um array JSON.
   - A lista retornada não deve estar vazia.
- Caso queira ver o output rode "python test.py"

### Resultado esperado: 
- O código de status da resposta é `200`.
- O corpo da resposta é um array JSON.
- A lista contém pelo menos um curso.
- Os dados dos cursos são exibidos corretamente no console.

### Resultado Obtido  
- **Caso 1 (Sucesso):**
  - Código de status: `200`.
  - Corpo da resposta: Array JSON contendo cursos.
  - Cursos exibidos no console com sucesso.

- **Caso 2 (Falha):**
  - Código de status diferente de `200` ou erro na autenticação.
  - Corpo da resposta vazio ou em formato inesperado.

### Pós-condições  
- O teste não altera o estado do servidor ou dos dados, uma vez que a operação é apenas de leitura (GET).
- Logs do teste são gerados no console para análise posterior.