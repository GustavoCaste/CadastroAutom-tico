# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
  ## https://dlp.hashtagtreinamentos.com/python/intensivao/login 


import pyautogui 
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar mais de uma tecla -> pyautogui.hotkey
# rolar a tela (scroll) -> pyautogui.scroll

pyautogui.PAUSE = 0.7

# Apertar botão windows

pyautogui.press("win")

# Digitar o nome do programa (microsoft edge)

pyautogui.write("edge")

# Apertar enter

pyautogui.press("enter")

# Digitar link

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Apertar enter

pyautogui.press("enter")

#timer para caso demore de carregar a pagina

time.sleep(7)


# Passo 2 - Fazer login 
# Clicar no campo email

pyautogui.click(x=738, y=451)

# Escrever e-mail

pyautogui.write("pythonimpressionador@gmail.com")

# Passar para o campo senha

pyautogui.press("tab")

# Escrever senha

pyautogui.write("Minhasenha")

# Clicar em Login

pyautogui.click(x=911, y=655)
# Passo 3 - Importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
#para ver a tabela:  print(tabela)

for linha in tabela.index:    
  # Passo 4 - Cadastrar produto
  pyautogui.click(x=750, y=296)
  #Código
  pyautogui.write(str(tabela.loc[linha, "codigo"]))
  pyautogui.press("tab")
  #Marca
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  #Tipo
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  #Categoria
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  #Preço
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  #Custo
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  #Obs
  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
    pyautogui.write(obs)
  
  pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.scroll(3000)
  
# Passo 5 - Repetir Passo 4 ate acabar a base de dados



