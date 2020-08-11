import pandas as pd
import pickle



ontology='cc'
input_pickle_train='data/multimodaltrain-'+ontology+'.pkl'
input_pickle_test='data/multimodaltest-'+ontology+'.pkl'
train= pd.read_pickle(input_pickle_train)
test= pd.read_pickle(input_pickle_test)
new_dict=[train,test]
results = pd.concat([test,train])
results=results.reset_index(drop=True)
file_name='data/'+ontology+'.pkl'
ont = pd.read_pickle(file_name)

def check_participation_in_ontology(accession):
      
        func=ont['functions'].values
        func_list=func.tolist()
        if(str(accession) in func_list):
                return True
        else:
                return False



output_pickle='data/multi-predgo-results'+ontology+'.pkl'
goterm_name_dict=pd.read_pickle('GotermNameFile.pkl')
cname=goterm_name_dict['combined_name']
def transformation_of_results(gos):
        print(gos)
        for i in range(0,len(gos)):
                res=[]
                for ele in gos[i]:
                        if(check_participation_in_ontology(str(ele))):
                                try:
                                        name=cname.loc[ele]
                                        print(name)
                                        res.append(name)
                                except:
                                       res.append(cname)
                        else:
                                pass
                        
                gos[i]=res
          
        return gos
        
                




accessions= results['accessions'].values
gos=results['gos']
gos=transformation_of_results(gos)




res_df = pd.DataFrame({
        'accessions': accessions,
        'results': gos.values},index=accessions)
print res_df
raw_input()

res_df.to_pickle("data/Results"+ontology+".pkl")


print(res_df)
