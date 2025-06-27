class ElementLinkedList:
  def __init__(self, id_number, color):
    self.id_number = id_number
    self.color = color
    self.next = None
    
  def __repr__(self):
    return f'[{self.color}, {self.id_number}]'
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.card_green = 1
    self.card_yellow = 201
    
  def inserirSemPrioridade (self, nodo):
    current_node = self.head
    while True:
      if current_node.next is not None:
        current_node = current_node.next
      else:
        current_node.next = nodo
        break
      
  def imprimirListaEspera(self):
    current_node  = self.head
    todos_pacientes = []
    while current_node is not None:
      todos_pacientes.append(str(current_node))
      current_node = current_node.next
    print(f'Lista -> {" ".join(todos_pacientes)}')
    
  def inserir(self):
    numero_do_paciente = None
    color = str(input("Informe a cor do cartão (A/V): ")).upper()
    
    if color == 'V':
      numero_do_paciente = self.card_green
      self.card_green += 1
    elif color == 'A':
      numero_do_paciente = self.card_yellow 
      self.card_yellow  += 1
    print(f"Número do cartão: {numero_do_paciente}")
    nodo = ElementLinkedList(numero_do_paciente, color)
    
    if self.head is None:
      self.head = nodo
    elif color == 'V':
      self.inserirSemPrioridade(nodo)

novo_paciente = LinkedList()
    
while True:
  print("1 - Adicionar paciente a fila")
  print("2 - Mostrar pacientes na fila")
  print(f"3 - Chamar paciente\n")
  option_user = int(input(">> "))
  if option_user == 1:
    novo_paciente.inserir()
  elif option_user == 2:
    novo_paciente.imprimirListaEspera()
  else:
    break