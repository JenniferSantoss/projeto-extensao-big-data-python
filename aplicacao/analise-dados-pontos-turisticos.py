import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# transfomando meu json em dataframe
with open('aplicacao\pontos-turisticos.json', 'r') as f:
    dados_pontosturisticos = json.load(f)
df_pontosturisticos = pd.DataFrame(dados_pontosturisticos)

# explorando os dados do dataframe gerado
print(df_pontosturisticos.head())
print(df_pontosturisticos.info())
print(df_pontosturisticos.describe())
print(df_pontosturisticos.isnull().sum())

# limpeza dos dados
df_pontosturisticos.drop_duplicates(inplace=True)
df_pontosturisticos.fillna(df_pontosturisticos.mean(), inplace=True)
categorical_columns = df_pontosturisticos.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df_pontosturisticos[column].fillna(df_pontosturisticos[column].mode()[0], inplace=True)
print(df_pontosturisticos.isnull().sum())

# ajustando alguns nomes incorretos
scaler = MinMaxScaler()
numeric_columns = ['idade', 'frequencia_viagens']  
df_pontosturisticos[numeric_columns] = scaler.fit_transform(df_pontosturisticos[numeric_columns])

label_encoder = LabelEncoder()
categorical_columns = ['tipo_viajante', 'preferencia_acomodacao']  
for column in categorical_columns:
    df_pontosturisticos[column] = label_encoder.fit_transform(df_pontosturisticos[column])

print(df_pontosturisticos.head())

# visualizando os dados
sns.histplot(df_pontosturisticos['idade'], kde=True)
plt.title('Distribuição de Idades dos Usuários')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

sns.countplot(x='tipo_viajante', data=df_pontosturisticos)
plt.title('Distribuição dos Tipos de Viajante')
plt.xlabel('Tipo de Viajante')
plt.ylabel('Frequência')
plt.show()

sns.heatmap(df_pontosturisticos.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Calor das Correlações entre Variáveis')
plt.show()

