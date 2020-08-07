
#imports
import numpy as np
import pandas as pd
import pickle
import csv
import sys,os
import ForTestMultiPredModelAPI as PredictionModel


#files
root='data/'
deepgo_prefix_train='data/train-'
deepgo_prefix_test='data/test-'
pklsuffix='.pkl'
multipred_prefix_train='data/multimodaltrain-'
multipred_prefix_test='data/multimodaltest-'
multipred='data/combined-multimodal-'
accession_status_file='AccessionNumber_Structure_StatusFileWithAccessionIndex.pkl'
accession_status_file_path=root+accession_status_file
df1 = pd.read_pickle(accession_status_file_path)
accession=""
ontology=""

Accesion_No_IndexDict = dict()
global RETURN_OBJECT
RETURN_OBJECT=dict()
PAYLOAD=dict()
def generate_dictionary(index_list):
    counter=0
    for ele in index_list:
        if ele not in Accesion_No_IndexDict:
            Accesion_No_IndexDict[ele]=counter
            counter=counter+1
        else:
            counter=counter+1




#level 2 function
def get_results(ontology,accession):
    res_file="data/Results"+ontology+".pkl"
    results_list = pd.read_pickle(res_file)
    print(results_list)
    results = results_list['results']
    # print(results)
    try:
        pred_list = results.loc[accession]
    except:
        pred_list=[]
    return pred_list





#level 1 function 
def load_train_test_data(accession_object,ontology):
    RETURN_OBJECT={}
    accession_number=accession_object['accession']
    ontology_flag=accession_object[ontology]
    if(accession_object['status']==True):
        if (ontology == "bp" and ontology_flag):
            prediction_list = get_results('bp',accession_number)
            RETURN_OBJECT['ot']=prediction_list
        else:
            if(ontology == "bp"):
                return "Accession no does not have Biological Function"
        if (ontology=="cc" and ontology_flag):
            prediction_list=get_results('cc',accession_number)
            RETURN_OBJECT['ot']=prediction_list
        else:
            if(ontology=="cc"):
                return "Accession no does not have Cellular Component"
        
        if(ontology=="mf" and ontology_flag):
            prediction_list=get_results('mf',accession_number)
            RETURN_OBJECT['ot']=prediction_list
        else:
            if(ontology=="mf"):
                return "Accession no does not have Molecular Function"
        return RETURN_OBJECT

    elif(accession_object['status']==False):
        return "This accession no's  structural information is not present in our database"
    else:
        return "This accession no's sequence, structure, PPIN information is not present in our database"



#root function
def analyze_accession_status(accession_number,ontology):
    accession_number=str(accession_number)
    ontology = str(ontology)
    try:
        df1 = pd.read_pickle(accession_status_file_path)
        accession_object = df1.loc[accession_number]
        print("Status of Accession No in following Ontologies 1 denote aceesion no has functionality in following ontology")
        print(accession_object)
        PAYLOAD = load_train_test_data(accession_object,ontology)
    except:
        PAYLOAD={"Sorry errorenous data"}
    return PAYLOAD
    


if __name__=='__main__':
    accession=raw_input("Please enter the accession no \t")
    ontology=raw_input("Please enter the ontology \t")
    message=analyze_accession_status(accession,ontology)
    print(message)
    # return message
    
    
