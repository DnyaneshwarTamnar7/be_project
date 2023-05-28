import pickle
from anxiety import result

pickle_out=open("anxiety.pkl","wb")
pickle.dump(result,pickle_out)
pickle_out.close()

pickle_in=open("anxiety.pkl","rb")
res=pickle.load(pickle_in)
print(res([0,0,0,0,0,0,0,0,0,1,2,3,4,1]))