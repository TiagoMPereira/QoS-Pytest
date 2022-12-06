# S206_pytest

Repositório contendo a aplicação referente ao seminário de Qualidade de Software (2º semestre - 2022).

O pytest é uma ferramenta utilizada para criar e executar testes em python. Sua instalação, aplicação e execução são simples e serão descritas em passos posteriores.

<div align='center'>
<img src='img/pytest_img.png' width=250px></img>
</div>

---
## Clonando projeto
O primeiro passo para executar o projeto é cloná-lo na sua máquina. Para isso, abra o terminal de comando, navegue até o diretório onde deseja alocar o projeto e entre com o seguinte comando:  
```https://github.com/TiagoMPereira/S206_pytest.git```  
Em seguida entre no diretório clonado  
```cd S206_pytest```  

---
## Gerência de dependências
No python a gerência de dependências é feita criando um ambiente virtual e especificando quais pacotes (e quais suas versões) serão utilizados no projeto. Para criar um ambiente virtual basta digitar o seguinte comando no terminal:  
```python -m venv env_projeto```  
Uma vez criado, é preciso ativar o ambiente virtual:  
```env_projeto\Scripts\activate.bat``` (Windows cmd)  
```env_projeto\Scripts\Activate.ps1``` (Windows powershell)  
```env_projeto/bin/activate``` (Linux/MacOS)  

Com o ambiente ativado basta importar as dependências:  
```pip install -r requirements.txt```  
Da mesma forma, é possível gerar o arquivo de dependências com todos os pacotes e versões utilizadas digitando:  
```pip freeze > requirements.txt```  

---
## Instalação
Caso o pytest não esteja nos requisitos instalados pelo requirements.txt é possível instalá-lo a parte.  

```pip install pytest```  


---
## Como usar

1) Crie um arquivo de testes com o prefixo "test_" (Ex.: test_requests.py)  
2) Dentro do arquivo criado, coloque seus casos de teste. Cada caso deve ser uma função nomeada com o prefixo "test_"  
3) Para executar os testes você pode rodar no prompt de comando:  
- ```pytest``` -> para executar todos os testes
- ```pytest -v``` -> para executar os testes detalhadamente
- ```pytest --cov``` -> para gerar o relatório de cobertura de testes
- ```pytest --cov-report html --cov=tests/ tests/``` -> para gerar o relatório de cobertura e salvar em um html