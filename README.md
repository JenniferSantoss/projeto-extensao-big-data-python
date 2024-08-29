## Projeto de Extensão Estacio

### Ideia principal: 
Aplicativo de cadastro pontos turísticos e perfil usuários para uma agência de viagens

### Detalhamento do projeto
#### FASE 1:
A primeira fase desse projeto tem como objetivo cadastrar no banco de dados pontos turísticos de diversos lugares e perfil de usuários com as suas preferências (tipos de atividades, orçamento e interesses) para que esses dados sejam usados posteriormente em um sistema de recomendação que sugere atividades, passeios e experiências de acordo com o interesse do usuário. 
#### FASE 2:
A segunda fase desse projeto tem como objetivo conectar o perfil do usuário com os pontos turísticos oferecendo recomendações relevantes. Levando em consideração que o cliente já possui duas tabelas de dados salvos em banco de dados, uma com dados pontos turísticos de diversos lugares e outra com perfil de usuários com as suas preferências, nosso objetivo é acessar esses dados e utilizar técnicas de aprendizado de máquina para identificar padrões nos dados e gerar recomendações personalizadas.

### Relato da dor do cliente: 
A agente de turismo precisa fazer diariamente sugestões de guia de viagem para seus clientes e não possui as características do perfil de seus clientes. Ela também precisa fazer diariamente sugestões personalizadas de viagens para seus clientes. Ela faz esse processo manualmente toda vida que um cliente faz diretamente essa solicitação. Para os clientes que não solicitam nada, como clientes antigos da empresa que não viajaram recentemente, ela acaba enviando sugestões gerais para todos. Ela gostaria muito de personalizar essas ofertas e assim, atingir um maior número de pessoas.

### Detalhamento do sistema que será desenvolvido:
#### FASE 1:
Nesta fase do projeto será desenvolvido um CRUD de pontos turísticos com localização, valores, tipos de atividades (culinária, aventura, cultura) e horário de funcionamento dos pontos turísticos. Será permitido o cadastro de pontos turísticos individuais ou via planilha csv.
Além disso, um CRUD de perfil de usuários, incluindo nome, idade, preferências de tipos de atividades, preferências de países e estados e média de gasto estimado. Ambos sendo salvos em banco de dados relacional Postgresql usando a linguagem JAVA.
#### FASE 2:
Levando em consideração que o cliente já possui duas tabelas salvas em banco de dados, uma com dados pontos turísticos de diversos lugares e outra com perfil de usuários com as suas preferências, nessa fase do projeto iremos:
Extrair os dados: Acessar as tabelas de perfis de usuários e pontos turísticos no banco de dados.
Processar os dados: Limpar, transformar e integrar os dados para criar um conjunto de dados unificado e utilizável.
Criar um modelo de recomendação: Utilizar técnicas de aprendizado de máquina para identificar padrões nos dados e gerar recomendações personalizadas.
Implementar o aplicativo: Desenvolver a interface do usuário e integrar o modelo de recomendação para fornecer as sugestões ao usuário.