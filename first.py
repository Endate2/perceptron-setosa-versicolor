import pandas as pd
import requests
import io

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)
response.raise_for_status()  # Проверка успешности запроса
data = response.content.decode('utf-8')
df = pd.read_csv(io.StringIO(data), header=None)
print(df.tail())
