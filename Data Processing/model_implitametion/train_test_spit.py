# Just a temp file for the including the train test split for the learing models 
# sow that we all are using the same metod/random_state
# not done

from sklearn.model_selection import train_test_split
import pandas as pd

data_sett_path = {"dsp_1": "pass", 
                  "dsp_2": "pass", 
                  "dsp_3": r"C:\Users\Sverre\Documents\VS Studio. filer\INFO284\Obli\Info284_Project\Exam Task\Dataset\elektronisk-rapportering-ers-2018-fangstmelding-dca-simple.csv",
                  "dsp_4": "H:\Informasjonsvitenskap\Programming\Python\Info-284\Info284_Project\Exam Task\Dataset\elektronisk-rapportering-ers-2018-fangstmelding-dca-simple.csv",
                  "dsp_5": "pass"}

try:
    dataset = pd.read_csv(data_sett_path["dsp_3"], sep=";")         # Remember to remove before finale submission!
except:
    print("Error with finding the correct path for the datasett")



dataset['bycatch'] = (dataset["Hovedart FAO"] == dataset["Art FAO"])

# the rest down is not done
X = dataset.drop(columns=["bycatch", "all othere colums exscept the features"]) 
y = dataset["target_column"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
