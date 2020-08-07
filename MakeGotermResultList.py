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

output_pickle='data/multi-predgo-results'+ontology+'.pkl'
goterm_name_dict=pd.read_pickle('GotermNameFile.pkl')
cname=goterm_name_dict['combined_name']
def transformation_of_results(gos):
        print(gos)
        for i in range(0,len(gos)):
                res=[]
                for ele in gos[i]:
                        try: 
                                name=cname.loc[ele]
                                print(name)
                        except:
                                pass
                        res.append(name)
                gos[i]=res
          
        return gos
        
                




# new_dict = pd.read_pickle(input_pickle)
print(results)
accessions= results['accessions'].values
gos=results['gos']
print(accessions)
print("******check1******")
print(gos)
print("******check2******")
# raw_input()
gos=transformation_of_results(gos)
print(gos.values)



res_df = pd.DataFrame({
        'accessions': accessions,
        'results': gos.values},index=accessions)
print res_df
raw_input()

res_df.to_pickle("data/Results"+ontology+".pkl")


print(res_df)
