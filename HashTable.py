class ElementLinkedList:
  def __init__(self, sigla, nomeEstado):
    self.sigla = sigla
    self.nomeEstado = nomeEstado
    self.proximo = None
    

class LinkedList:
  def __init__(self):
    self.head = None
    
  def inserir(self, sigla, nomeEstado):
    nodo = ElementLinkedList(sigla, nomeEstado)
    if self.head is None:
      self.head = nodo
      return 0
    else:
      nodo.proximo = self.head
      self.head = nodo
      return 0
    
  def imprimir(self):
    current_node = self.head
    estados_sigla = []
    if current_node is None:
      return "None"
    
    while current_node is not None:
      estados_sigla.append(current_node.sigla)
      current_node = current_node.proximo
    return " -> ".join(estados_sigla) + " -> None"

class HashTable:
  def __init__(self):
    self.tam = 10
    self.length = 0
    self.table = [LinkedList() for i in range(0,self.tam)]
    
  def hasFunction(self, sigla):
    k = list(sigla)
    
    if sigla == 'DF':
      return 7
    else:
      return (ord(k[0]) + ord(k[1])) % self.tam
    
  def inserir(self, sigla, nomeEstado):
    index = self.hasFunction(sigla)
    self.table[index].inserir(sigla, nomeEstado)
    self.length += 1
  
  def imprimir(self):
    for i in range(0, self.tam):
      print(f"{i}: {self.table[i].imprimir()}")
      
todos_estados = dict(
  {"AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia", "CE": "Ceará", 
   "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás", 
   "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul",
   "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná", 
   "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
   "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina",
   "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"}
)
    
new_plate = HashTable()

new_plate.imprimir()
print("-" * 20)

for sigla, nome in todos_estados.items():
  new_plate.inserir(sigla, nome)
new_plate.imprimir()
print("-" * 20)

new_plate.inserir("TA", "Tayanna Amorim")
new_plate.imprimir()