import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# transfomando meu json em dataframe
with open('aplicacao\perfil-clientes.json', 'r') as f:
    dados_usuarios = json.load(f)
df_usuarios = pd.DataFrame(dados_usuarios)

# explorando os dados do dataframe gerado
print(df_usuarios.head())
print(df_usuarios.info())
print(df_usuarios.describe())
print(df_usuarios.isnull().sum())

# limpeza dos dados
df_usuarios.drop_duplicates(inplace=True)
df_usuarios.fillna(df_usuarios.mean(), inplace=True)
categorical_columns = df_usuarios.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df_usuarios[column].fillna(df_usuarios[column].mode()[0], inplace=True)
print(df_usuarios.isnull().sum())

# ajustando alguns nomes incorretos
scaler = MinMaxScaler()
numeric_columns = ['idade', 'frequencia_viagens']  
df_usuarios[numeric_columns] = scaler.fit_transform(df_usuarios[numeric_columns])

label_encoder = LabelEncoder()
categorical_columns = ['tipo_viajante', 'preferencia_acomodacao']  
for column in categorical_columns:
    df_usuarios[column] = label_encoder.fit_transform(df_usuarios[column])

print(df_usuarios.head())

# visualizando os dados
sns.histplot(df_usuarios['idade'], kde=True)
plt.title('Distribuição de Idades dos Usuários')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

#tentando gerar um grafico simples
fig = px.histogram(df_usuarios, x="idade", nbins=20, title="Distribuição de Idades dos Usuários")
fig.update_layout(xaxis_title="Idade", yaxis_title="Frequência")
fig.show()

sns.countplot(x='tipo_viajante', data=df_usuarios)
plt.title('Distribuição dos Tipos de Viajante')
plt.xlabel('Tipo de Viajante')
plt.ylabel('Frequência')
plt.show()

sns.heatmap(df_usuarios.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Calor das Correlações entre Variáveis')
plt.show()

