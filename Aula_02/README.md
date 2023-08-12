# CONFIGURAÇÃOES INICIAIS

1 - Verifique se você tem o gerenciador de pacotes do python o ```pip``` 
  - para isso faça o seguinte, procure da barra de pesquisa do windows pesquise por ```Prompt de Comando``` e execute como adiministrador, depois digite ```pip -V```, se não estiver instalado siga os passos deste tutorial <a href="https://dicasdeprogramacao.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/">clique aqui</a>
  
2 - Você deve criar uma pasta com o nome apropriado para o projeto

3 - Apos, abra está pasta no Visual studio code (vs code)

4 - Abra o terminal do vscode e digite estes comandos

  - ```pip install django``` ira instalr o django
  - ```python -m django startproject "nome do projeto"``` vai criar o projeto
  - ```cd "nome do projeto"``` entra na pasta do projeto e ```code .``` para abrir um novo vscode como o projeto
  - no terminal do vscode novo digite ```python -m venv ""nome da sua venv```
  - Para ativar a venv digite
    - Linux: ```source env/bin/activate```
    - Windows: ```env\Scripts\activate``` ou ```env\Scripts\activate.bat``` ou ```source venv/Scripts/activate```
      
  - ```pip install djangorestframework``` instala o  djangorestframework
  - ```python -m django startapp "nome do app"``` criar um app dentro do projeto
  - ```python manage.py runserver``` executa a aplicação, abra no link que aparecer no seu terminal

Se estiver parecido com está imagem abaixo tudo deu certo 

<div align="center">
  <img src="https://github.com/jeovanedossantossantos/Curso_Pyhton_para_Web/assets/60934938/7ccc73d0-864b-4830-a6b0-f2bcace51b7a" width=300/>
</div>
