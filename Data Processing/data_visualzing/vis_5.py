import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

selected_features = ['Startposisjon bredde', 'Startposisjon lengde', 'Havdybde start', 'Varighet', 'Trekkavstand']

for column in selected_features:
    if df[column].dtype == 'O':  # Check if the column is of string type
        df[column] = df[column].str.replace(',', '.').astype(float)

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(df[selected_features])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

isolation_forest_model = IsolationForest(contamination=0.05) 
isolation_forest_model.fit(X_scaled)

predictions = isolation_forest_model.predict(X_scaled)

df['Anomaly'] = predictions

anomalies = df[df['Anomaly'] == -1]
print(anomalies)
