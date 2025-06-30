class ElementSimpleList:
  def __init__(self, numero, cor):
    self.numero = numero
    self.cor = cor
    self.proximo = None
    
  def __repr__(self):
    return f'[{self.cor}, {self.numero}]'
    
class SimpleList:
  def __init__(self):
    self.head = None
    self.card_green = 1
    self.card_yellow = 201
    
  def inserirSemPrioridade (self, nodo):
    current_node = self.head
    while True:
      if current_node.proximo is not None:
        current_node = current_node.proximo
        
      else:
        current_node.proximo = nodo
        break
      
  def inserirComPrioridade(self, nodo):
    current_node = self.head
    if self.head is None or current_node.cor == 'V':
     nodo.proximo = self.head
     self.head = nodo
     return 
    while current_node is not None:
        if current_node.cor == 'A' and current_node.proximo is None:
          current_node.proximo = nodo
          return
        if current_node.cor == 'A' and current_node.proximo.cor == 'V':
          nodo.proximo = current_node.proximo
          current_node.proximo = nodo
          return
        else:
          current_node = current_node.proximo
          
  def inserir(self):
    numero_do_paciente = None
    cor = str(input("Informe a cor do cartão (A/V): ")).upper()
    
    if cor == 'V':
      numero_do_paciente = self.card_green
      self.card_green += 1
    elif cor == 'A':
      numero_do_paciente = self.card_yellow 
      self.card_yellow  += 1
    print(f"Informe o número do cartão: {numero_do_paciente}")
    nodo = ElementSimpleList(numero_do_paciente, cor)
    
    if self.head is None:
      self.head = nodo
    elif cor == 'V':
      self.inserirSemPrioridade(nodo)
    elif cor == 'A':
      self.inserirComPrioridade(nodo)  
  
  def imprimirListaEspera(self):
    current_node  = self.head
    todos_pacientes = []
    while current_node is not None:
      todos_pacientes.append(str(current_node))
      current_node = current_node.proximo
    print(f'Lista -> {" ".join(todos_pacientes)}')
  
  def chamarPaciente(self):
    print(f"Atendendo o paciente cartão {self.head.cor} e número {self.head.numero}")
    self.head = self.head.proximo


novo_paciente = SimpleList()
    
while True:
  print("1 - Adicionar paciente a fila")
  print("2 - Mostrar pacientes na fila")
  print("3 - Chamar paciente")
  print(f"4 - Sair\n")
  option_user = int(input(">> "))
  if option_user == 1:
    novo_paciente.inserir()
  elif option_user == 2:
    novo_paciente.imprimirListaEspera()
  elif option_user == 3:
    novo_paciente.chamarPaciente()
  elif option_user == 4:
    break