# **Sistema de Gestão **

## **Objetivos do Sistema**
Os principais objetivos do sistema incluem:  
- **Automatizar Processos:** Reduzir o tempo necessário para gerenciar pedidos, atualizar estoque e gerar relatórios.  
- **Aumentar a Eficiência:** Garantir que as informações estejam sempre atualizadas em tempo real, minimizando perdas e desperdícios.  
- **Oferecer Suporte à Tomada de Decisões:** Fornecer relatórios detalhados para análise de vendas, despesas e lucros, facilitando o planejamento estratégico.  
- **Melhorar a Experiência do Cliente:** Garantir que pedidos sejam registrados com precisão e rapidamente atendidos.  

---

## **Funcionalidades Principais**

### **1. Gerenciamento de Funcionários**
- **Descrição:**  
  Gerencia o cadastro de funcionários, incluindo suas informações pessoais, credenciais de acesso e níveis de permissão.  
- **Características:**  
  - Cada funcionário possui um registro com nome, cargo, jornada de trabalho e salário.  
  - Apenas administradores têm permissão para cadastrar, alterar ou excluir funcionários.  
  - Autenticação por usuário e senha, garantindo acesso seguro ao sistema.  
- **Benefício:**  
  Controle eficiente de acessos, garantindo a segurança das informações e a organização do quadro funcional.  

---

### **2. Registro de Pedidos**
- **Descrição:**  
  Permite registrar pedidos feitos presencialmente ou por delivery, detalhando os itens solicitados, quantidade e valor total.  
- **Características:**  
  - Itens são vinculados ao estoque, permitindo atualização automática ao registrar o pedido.  
  - Suporte para pedidos complexos (ex.: múltiplos itens com personalizações).  
  - Informações adicionais, como endereço para delivery ou número da mesa, podem ser incluídas.  
- **Funcionamento:**  
  - O atendente registra os itens do pedido, que são automaticamente vinculados ao estoque.  
  - O sistema calcula o valor total do pedido e apresenta opções de pagamento.  
- **Benefício:**  
  Agilidade no atendimento e precisão no registro de informações, reduzindo erros manuais.  

---

### **3. Controle de Estoque**
- **Descrição:**  
  Gerencia a entrada e saída de produtos, garantindo que o estoque esteja sempre atualizado em tempo real.  
- **Características:**  
  - Registro de entradas (reposição de estoque) e saídas (vendas e desperdícios).  
  - Notificação automática para itens com quantidade abaixo de um limite pré-definido.  
  - Produtos são organizados por categorias para facilitar consultas.  
- **Funcionamento:**  
  - Cada venda reduz automaticamente a quantidade do produto no estoque.  
  - Alertas são exibidos para reposição de produtos com estoque crítico.  
- **Benefício:**  
  Minimiza desperdícios, evita falta de produtos e facilita o controle de insumos.  

---

### **4. Geração de Relatórios**
- **Descrição:**  
  Gera relatórios detalhados que auxiliam na gestão financeira e no planejamento estratégico.  
- **Características:**  
  - **Relatórios de vendas:** Itens mais vendidos, horários de pico, volume de vendas.  
  - **Relatórios financeiros:** Despesas, receitas e lucro líquido.  
  - **Relatórios de estoque:** Produtos em baixa quantidade, histórico de movimentações.  
- **Funcionamento:**  
  - Os dados são extraídos automaticamente com base nos registros do sistema.  
  - Relatórios podem ser gerados em formato visual (tabelas e gráficos) ou exportados para planilhas.  
- **Benefício:**  
  Fornece uma visão ampla e detalhada das operações, apoiando decisões estratégicas para otimização do negócio.  

---

## **Tecnologias Utilizadas**

### **Linguagem de Programação**  
- O sistema foi desenvolvido utilizando **Python**, devido à sua versatilidade e amplo suporte para bibliotecas úteis para automação e gestão.

### **Banco de Dados**  
- Utiliza **PostgreSQL** para armazenar informações de pedidos, estoque, funcionários e relatórios. O banco de dados foi escolhido por sua robustez e capacidade de lidar com grandes volumes de dados.

### **Bibliotecas Python**  
- **`abc`:** Implementação de interfaces e classes abstratas para organizar a lógica do sistema.  
- **`psycopg2`:** Conexão e manipulação do banco de dados PostgreSQL.  
- **`datetime`:** Controle de datas e horários, essencial para pedidos e relatórios.  

---

## **Arquitetura do Sistema**

### **Módulos do Sistema**
1. **Autenticação:**  
   - Garante que apenas usuários autorizados tenham acesso às funcionalidades do sistema.  

2. **Pedidos:**  
   - Registra e gerencia pedidos, vinculando-os ao estoque e aos relatórios financeiros.  

3. **Estoque:**  
   - Monitora os produtos, atualizando automaticamente as quantidades disponíveis com base nas vendas.  

4. **Relatórios:**  
   - Gera informações precisas para análise e planejamento estratégico.  


