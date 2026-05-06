"""Este modulo implementa el patron proxy para interceptar llamadas
a la clase ping. Si la IP es 192.168.0.254, redirige eñ ómgp a google
usando executefree. """

class ping:
    """simula 10 intentos de ping a una direccion IP
    Solo permite pings a direcciones que comienzan con 192"""
    
    def execute(self, string: str)-> None:
        """realiza 10 pings a la IP si comienza con 192"""
        if string.startswith("192."):
            for i in range(10):
                print(f"Ping {i+1} a {string}: OK")
        else:
            print(f"Error: Lai IP {string} NO comienza con '192.'")
            
    def executefree(self, string: str)-> None:
        """Realiza 10 píngs sin control de direccion IP"""
        for i in range(10):
            print(f"Ping {i+1} a {string}: OK")

class pingproxy:
    """intercepta las llamadas a execute. si la IP es '192.168.0.254' redirige
    el ping a google usando execute free"""
    
    
    def __init__(self)-> None:
        """inicializa el proxy con una instancia de ping"""
        
        self.ping_real= ping()
        
    def execute(self, string: str)-> None:
        """decide si redirigir o reenviar la llamada-"""
        
        if string== "192.168.0.254" :
            print(f"IP {string} detectada. Redirifiengo a www.google.com")
            self.ping_real.executefree("www.google.com")
            
        else:
            self.ping_real.execute(string)
            
def main() -> None:
    """demostracion del praton proxy aploicado a ping"""
    
    print("=== Usando ping directamente ===")
    p = ping()
    
    print("\n--- execute con IP válida ---")
    p.execute("192.168.1.1")
    
    print("\n--- execute con IP inválida ---")
    p.execute("10.0.0.1")
    
    print("\n--- executefree (sin control) ---")
    p.executefree("10.0.0.1")
    
    print("\n=== Usando pingproxy ===")
    proxy = pingproxy()
    
    print("\n--- IP normal (reenvía a ping) ---")
    proxy.execute("192.168.1.1")
    
    print("\n--- IP bloqueada (redirige a google) ---")
    proxy.execute("192.168.0.254")
    
    print("\n--- IP inválida (reenvía a ping) ---")
    proxy.execute("10.0.0.1")


if __name__ == "__main__":
    main()
        