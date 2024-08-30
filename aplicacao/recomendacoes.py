from surprise import Reader, Dataset, SVD, KNNBasic
from surprise.model_selection import cross_validate

# Carregar os dados
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Criar os modelos
algo_svd = SVD()
algo_knn = KNNBasic()

# Combinar os modelos (uma das abordagens)
def combine_predictions(predictions_svd, predictions_knn):
    return (predictions_svd + predictions_knn) / 2

def combine_predictions(predictions_svd, predictions_knn, weight_svd=0.6, weight_knn=0.4):
    return weight_svd * predictions_svd + weight_knn * predictions_knn

# Avaliar os modelos
cross_validate(algo_svd, data, measures=['RMSE'], cv=5)
cross_validate(algo_knn, data, measures=['RMSE'], cv=5)

# Fazer previsões para um usuário específico
uid = 'user_id_1'
iid = 'item_id_2'
pred = algo_svd.predict(uid, iid)
print(pred)