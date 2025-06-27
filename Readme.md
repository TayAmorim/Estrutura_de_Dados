# Atividade Prática de Estrutura de Dados / Programação III - UNINTER

## Descrição do Projeto

Este repositório contém a resolução da Atividade Prática da disciplina de Estrutura de Dados / Programação III da UNINTER. O projeto consiste em um programa em Python que implementa duas estruturas de dados fundamentais: uma Lista Encadeada Simples para gerenciar uma fila de atendimento hospitalar com prioridades e uma Tabela Hash com endereçamento em cadeia para um sistema de emplacamento de veículos. O objetivo é demonstrar a aplicação prática e o domínio de conceitos como nodos, ponteiros, inserção, remoção e funções hash.

## Questões Abordadas

### Questão 1: Lista Encadeada - Sistema de Triagem Hospitalar

**Enunciado:**
Desenvolvimento de um sistema de triagem hospitalar utilizando uma Lista Encadeada Simples para organizar a fila de atendimento. O sistema gerencia pacientes com cartões numerados "Verde" (V) para menor urgência e "Amarelo" (A) para maior urgência.

**Regras de Prioridade:**

* [cite_start]Pacientes com cartão "Amarelo" (A) são chamados antes dos pacientes com cartão "Verde" [V].
* [cite_start]Entre pacientes com a mesma cor de cartão, aqueles com numeração menor são atendidos antes.
* [cite_start]Numeração de cartões Verdes (V) inicia em 1.
* [cite_start]Numeração de cartões Amarelos (A) inicia em 201.

**Funcionalidades Implementadas:**

* [cite_start]Implementação de uma Lista Encadeada Simples onde o Nodo representa um cartão contendo `número`, `cor` e `próximo`.
* [cite_start]Função `inserirSemPrioridade(nodo)`: Insere o nodo no final da lista [para cartões 'V'].
* [cite_start]Função `inserirComPrioridade(nodo)`: Insere o nodo após todos os 'A's existentes e antes de todos os 'V's (para cartões 'A'), mantendo a ordem numérica entre eles.
* [cite_start]Função `inserir()`: Solicita a cor ao usuário, atribui o número automaticamente e cria o nodo, chamando a função de inserção adequada
* [cite_start]Função `imprimirListaEspera()`: Imprime todos os cartões e seus respectivos números na ordem da fila
* [cite_start]Função `atenderPaciente()`: Remove o primeiro paciente da fila e informa seu atendimento
* [cite_start]Menu interativo para utilização do sistema [adicionar, mostrar, chamar, sair]

### Questão 2: Tabela Hash - Sistema de Emplacamento de Veículos

**Enunciado:**
Criação de um sistema de emplacamento de veículos para o Distrito Federal, onde o último número da placa representa o estado de registro. O sistema utiliza uma Tabela Hash com endereçamento em cadeia.

**Detalhes da Tabela Hash:**

* [cite_start]Tabela com 10 posições [0 a 9](cite: 54).
* [cite_start]Cada posição do vetor é uma Lista Encadeada Simples.
* [cite_start]O Nodo da Lista Encadeada representa um Estado com `sigla`, `nomeEstado` e `próximo`.
* [cite_start]A inserção nas listas encadeadas é sempre no início.

**Função Hash:**

* [cite_start]Entrada: String de 2 letras [sigla do estado/DF].
* [cite_start]Se a sigla for "DF", o retorno é sempre 7.
* [cite_start]Caso contrário: `posição = (CHAR1ASCII + CHAR2ASCII) MOD 10`.
  * [cite_start]`CHAR1ASCII` e `CHAR2ASCII` são os valores ASCII da primeira e segunda letra, respectivamente.

**Funcionalidades Implementadas:**

* [cite_start]Tabela Hash inicializada com 10 posições `None`.
* [cite_start]Implementação da função hash conforme as regras do enunciado.
* [cite_start]Inserção dos 26 estados e o Distrito Federal (DF) na tabela hash.
* [cite_start]Inserção de um estado fictício com nome completo e siglas geradas a partir da primeira letra do nome e do último sobrenome.
* [cite_start]Função para imprimir a tabela hash, mostrando as siglas dos nodos separados por posição.

## Como Executar o Projeto

1. **Pré-requisitos:** Certifique-se de ter o Python (preferencialmente 3.x) instalado em sua máquina.
2. **Executar o Script:**

    ```bash
    python main.py
    ```

## Instruções de Uso

Ao executar o programa, você será apresentado a um menu interativo para a Questão 1 (Sistema de Triagem Hospitalar). Siga as opções apresentadas no console:

* **1 - Adicionar paciente à fila:** Permite inserir um novo paciente, solicitando a cor do cartão ('A' ou 'V'). O número é gerado automaticamente.
* **2 - Mostrar pacientes na fila:** Exibe a lista atual de pacientes na fila, respeitando as prioridades.
* **3 - Chamar paciente:** Remove o primeiro paciente da fila para atendimento.
* **4 - Sair:** Encerra o programa.

Para a Questão 2 (Tabela Hash), a execução irá imprimir o estado da tabela hash em diferentes etapas (vazia, com estados e com estado fictício) diretamente no console, conforme o script preenche a tabela.

## Autor(es)

* [Tayanna Amorim]
