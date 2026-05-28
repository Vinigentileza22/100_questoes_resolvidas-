import importlib # 

while True:
    n = input("\nQual questão testar? (0 para sair): ")
    if n == '0': #
        break
    
    try:#
       
        modulo = importlib.import_module(f"questao_{n}") #
        getattr(modulo, f"q_{n}")() #
    except Exception:
        print("[!] Questão não encontrada ou erro na execução.")
        
        #explique o erro