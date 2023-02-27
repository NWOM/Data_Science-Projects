import numpy as  np
import pickle

loaded_model=pickle.load(open('C:/Users/suman/OneDrive/Desktop/Data Science Internship/prj2/resources/data/trained_model.sav','rb'))
input_data=(6,139,46,20,182,23.4,0.871,55)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print('Not Diabetic')
else:
  print('Diabetic')  