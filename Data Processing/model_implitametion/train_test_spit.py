# Just a temp file for the including the train test split for the learing modeles 
# sow that we all are using the same metod/random_state
# not done

from sklearn.model_selection import train_test_split
import pandas as pd

pd.set_option("display.max_columns", None)

data_set_path = {"dsp_1": "pass", 
                  "dsp_2": "pass", 
                  "dsp_3": r"C:\Users\Sverre\Documents\VS Studio. filer\INFO284\Obli\Info284_Project\Exam Task\Dataset\elektronisk-rapportering-ers-2018-fangstmelding-dca-simple.csv",
                  "dsp_4": "H:\Informasjonsvitenskap\Programming\Python\Info-284\Info284_Project\Exam Task\Dataset\elektronisk-rapportering-ers-2018-fangstmelding-dca-simple.csv",
                  "dsp_5": "pass"}

try:
    dataset = pd.read_csv(data_set_path["dsp_3"], sep=";")
except:
    print("""
          =====================================================
          The correct pathing for the dataset was not implimented, 
          change the 'data_set_path' variable to the correct path or 
          find the read_csv() function and correct it there.
          =====================================================
          """)
    

dataset["Is_Bycatch"] = (dataset["Hovedart FAO"] == dataset["Art FAO"])

the_colums_to_keep = ["Is_Bycatch", "Hovedart FAO", "Art FAO", "Redskap FAO", "Rundvekt", "Lengdegruppe", "Hovedområde start", "Trekkavstand" ] # This is all the different differnt labels we are using but we also shoud clasefy why we are using ths spesefic and not othere that are of the same type.
data_selected = dataset[the_colums_to_keep]
dataset = data_selected                         # updating the dataset variable to be the new one that only contains the labels we want to use

X = dataset.drop(columns=["Is_Bycatch"])        # This is the "testing data" and everting else exept for the answer
y = dataset["Is_Bycatch"]                       # This is "answer"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) #random_state is selected as 4 becuse the is 4 people in the group

print(dataset.head(5))
print("-- done ---")