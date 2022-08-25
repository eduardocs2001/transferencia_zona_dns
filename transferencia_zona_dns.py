import subprocess

class transferencia_zona:
    
    def __init__(self):
        self.__dns: str(input("DNS: "))
        
    def transferencia(self):
        name_servers = (subprocess.getoutput(f'host -t ns {dns} | cut -d " " -f 4')).split("\n")
        for x in name_servers:
            transeferencia = subprocess.getoutput(f'host -l -a {dns} {x}')
            if "Transfer failed." not in transeferencia:
                print(f"Servidor: {x}\n{transeferencia}")
            else: 
                print(f"Transferência de zona para o servidor {x} foi recusada")
    


        
        
if __name__ == '__main__':
    script = transferencia_zona()
    script.transferencia()
