import streamlit as st
import pandas as pd
from keras.models import load_model
model=load_model('model_.h5')
st.title('Grid Stability Prediction')
st.write('Developed by Adil')
st.write("""
This app predicts the stability of the power grid""")
st.sidebar.header('Input Features')
def user_input_features():
	tau1=st.sidebar.slider('tau1',0.5,9.9)
	tau2=st.sidebar.slider('tau2',0.5,9.9)
	tau3=st.sidebar.slider('tau3',0.5,9.9)
	tau4=st.sidebar.slider('tau4',0.5,9.9)
	p1=st.sidebar.slider('p1',1.58, 5.86)
	p2=st.sidebar.slider('p2',-1.99, -0.50)
	p3=st.sidebar.slider('p3',-1.99,-0.50)
	p4=st.sidebar.slider('p4',-1.99,-0.50)
	g1=st.sidebar.slider('g1',0.05,9.9)
	g2=st.sidebar.slider('g2',0.05,9.9)
	g3=st.sidebar.slider('g3',0.05,9.9)
	g4=st.sidebar.slider('g4',0.05,9.9)

	data={'tau1':tau1,
		  'tau2':tau2,
		  'tau3':tau3,
		  'tau4':tau4,
		  'p1':p1,
		  'p2':p2,
		  'p3':p3,
		  'p4':p4,
		  'g1':g1,
		  'g2':g2,
		  'g3':g3,
		  'g4':g4}
	features=pd.DataFrame(data,index=[0])
	return features
df=user_input_features()
st.write(df)

pred_=model.predict(df)
pred_[pred_ <= 0.5] = 0
pred_[pred_ > 0.5] = 1
st.write('*****Prediction*****')
st.write('***')
if pred_ > 0.5:
	st.write('Stable System')
elif pred_ < 0.5:
	st.write('Unstable System')
st.write(pred_)
