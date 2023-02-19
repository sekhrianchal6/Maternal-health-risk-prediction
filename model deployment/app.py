import pickle
import streamlit as st

pickle_in = open("rf_model.pkl", "rb")
classifier = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_risk(age, systolicbp, diastolicbp, bs, bodytemp):
    prediction = classifier.predict([[age, systolicbp, diastolicbp, bs, bodytemp]])
    print(prediction)
    return prediction


def main():
    st.title("Maternal Health Risk Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Maternal Health Risk Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("Age", "Type Here")
    systolicbp = st.text_input("SystolicBP", "Type Here")
    diastolicbp = st.text_input("DiastolicBP", "Type Here")
    bs = st.text_input("BS", "Type Here")
    bodytemp = st.text_input("BodyTemp", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_risk(age, systolicbp, diastolicbp, bs, bodytemp)
        if result == [2.0]:
            result = "High"
        elif result == [1.0]:
            result = "Mid"
        elif result == [0.0]:
            result = "Low"
    st.success('The risk level is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
