import numpy as np
import pickle
import streamlit as st
#loading the saved model
loaded_model=pickle.load(open('C:/Users/suman/OneDrive/Desktop/Data Science Internship/prj2/resources/data/trained_model.sav','rb'))
def diabetes_prediction(input_data):
	input_data_as_numpy_array=np.asarray(input_data)
	input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
	prediction=loaded_model.predict(input_data_reshaped)
	print(prediction)
	if(prediction[0]==0):
		print('Not Diabetic')
	else:
		print('Diabetic')
		
	


    


    


    
def main():
	st.title('Diabetes Prediction web App')
	Pregnancies=st.text_input('Number of Pregnancies')
	Glucose=st.text_input('Blood Glucose Level')
	BloodPressure=st.text_input('Blood Pressure Value')
	SkinThickness=st.text_input('Skin Thickness value')
	Insulin=st.text_input('Insulin Level')
	BMI=st.text_input('BMI Value')
	DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree function Value')
	Age=st.text_input('Age Of the person')



	#code for prediction
	diagnosis=' '
	#creating a button for prediction
	if st.button('Test Result'):
		diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

	st.success(diagnosis)	






if __name__=='__main__':
	main()
