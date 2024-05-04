from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from docx import Document
import streamlit as st
import os
import dotenv
dotenv.load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',''' your are an ai research agent well trained and having expertise in medical field of EchoCardioDiagram report sheet documentation helping my medical research purpose the doctor gives the echoCardioDiagram report data of the patient make a case sheet based on the data provided by him'''),
        ('user','''here is the patient data for you to read evaluate analyze and make a EchoCardioDiagram report sheet
          patient data: {cssheet}
         
         this is an example case sheet format you should generate 

         {{

Quanty

De Gaspada M

DH. Voda MD

Dr. Vijes Praiad

Dept. of Radindogy & Imaging

DeKalagens MD

Dr. Zales AbMD

Dr. N. V as MDS

IMMMD


ECHOCARDIOGRAM REPORT

Name: Mrs. M. Aruna Kumari

Id. No.: F/46 Years/101895318

Organ: ECHOCARDIOGRAM

Ref by: Dr. K. Venkateswara Rao MD (Chest)

2D ECHO

Mitral Valve - Normal

Tricuspid Valve - Normal

Pulmonary Valve - Normal

Aortic Valve - Normal

Left Ventricle - 4.6 x 2.8 cm, LVPW-0.7 cm

Left Atrium - 3.2 cm

Ao - 2.9 cm

Right Ventricle - Normal


Right Atrium - Normal

Interatrial Septum - Intact

Interventricular Septum - 0.8 cm

PA - normal

EF - 70%

FS  - 39%

Doppler: Mitral flow - E<A

         Pulmonary flow - 0.8 m/sec

         Aortic flow - 1.5 m/sec


Impression: PARADOXICAL SEPTAL MOTION

            NORMAL CHAMBERS/NORMAL VALVES

            NO RWMA OF LV

            NO MR/NO AR/NO TR/NO PAH

            GOOD LV/RV SYSTOLIC FUNCTION

            GRADE-I LV DIASTOLIC DYSFUNCTION

            NO PERICARDIAL EFFUSION

            NO LV CLOTS
}}
Note: This is a sample case sheet and the specific details may vary depending on the individual patient and their presentation.
         
         ''')

    ]

)



llm= ChatGoogleGenerativeAI(model='gemini-pro')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


st.title('Med AI🩺')
input_text=st.text_input('enter your data')

st.session_state.modified = None

if input_text:
     output = (chain.invoke({'cssheet':input_text}))
     st.write(output)
            