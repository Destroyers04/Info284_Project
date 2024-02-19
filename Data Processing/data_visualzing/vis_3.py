import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

your_dataframe = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

# Meldingstidspunkt is in the format "dd.mm.yyyy HH:mm"
your_dataframe[['Meldingdato', 'Meldingklokkeslett']] = your_dataframe['Meldingstidspunkt'].str.split(' ', expand=True)

your_dataframe['Meldingdato'] = pd.to_datetime(your_dataframe['Meldingdato'], format='%d.%m.%Y')
your_dataframe['Meldingklokkeslett'] = pd.to_datetime(your_dataframe['Meldingklokkeslett'], format='%H:%M')

your_dataframe['Meldingstidspunkt'] = your_dataframe['Meldingdato'] + pd.to_timedelta(your_dataframe['Meldingklokkeslett'].dt.hour, unit='h') + pd.to_timedelta(your_dataframe['Meldingklokkeslett'].dt.minute, unit='m')

plt.figure(figsize=(10, 6))
plt.plot(your_dataframe['Meldingstidspunkt'], your_dataframe['Rundvekt'])
plt.title('Time Series Analysis of Rundvekt Over Time')
plt.xlabel('Meldingstidspunkt')
plt.ylabel('Rundvekt')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.show()
