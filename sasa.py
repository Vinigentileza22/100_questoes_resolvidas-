import importlib # é uma funçao q importa a biblioteca importlib

while True:
    n = input("\nQual questão testar? (0 para sair): ")
    if n == '0': # se n for igual a 0 break faz o programa acabar !
        break
    
    try:# significa tente executar esse codigo, caso o programa de um erro ele n pare de funcionar !
       
        modulo = importlib.import_module(f"questao_{n}") #'importlib.import_module': serve para importar um arquivo Python, já o f"questao_{n}" ele acessa o arquivo automaticamente, e o modulo  guarda o módulo na variável
        getattr(modulo, f"q_{n}")() # chama função do modulo !
    except Exception:
        print("[!] Questão não encontrada ou erro na execução.")
        
        #explique o erro: o erro era o caminho das linha 10  