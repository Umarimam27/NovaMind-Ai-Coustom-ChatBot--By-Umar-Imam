# #from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI


# import streamlit as st
# import os
# #from dotenv import load_dotenv

# os.environ["OPENAI_API_KEY"] = ""
# #os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# ## Langmith tracking
# os.environ["LANGCHAIN_TRACING_V2"]="true"

# os.environ["LANGCHAIN_API_KEY"]= "fec4"
# #os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# ## Prompt Template

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","I am chatbot. I am hear to assist you. Please type your queries"),
#         ("user","Question:{question}")
#     ]
# )

# ## streamlit framework

# st.title('LLM-OPENAI PROJECT - CUSTOM GPT-4 BY PRAKASH SENAPATI')
# input_text=st.text_input("How may I help you")

# # openAI LLm
# llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser

# if input_text:
#     st.write(chain.invoke({'question':input_text}))


#*#*#*#*#**#**#*#*#*#*#*#*#*#**#*#**##**#*#*#*#*#*#*#*#*##*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*##*#**#*#*#


# # This Is The Code For Gemini Custom Chatbot Using Langchain and Streamlit

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# import streamlit as st
# import os

# # --- Configuration ---

# # Set Gemini API Key
# # NOTE: In a real app, use st.secrets or a proper environment variable setup
# # For this example, I'll keep the placeholder structure you provided.
# os.environ["GOOGLE_API_KEY"] = "" 
# MODEL_NAME = "gemini-2.5-flash"

# # Prompt Template
# # The system instruction is crucial for defining the bot's persona.
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful and friendly chatbot powered by Google's Gemini model. Your name is Custom Chatbot. Be concise and accurate."),
#         ("user", "Question: {question}")
#     ]
# )

# # Initialize Gemini LLM
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME, 
#     temperature=0.7 # Increased temperature slightly for more engaging responses
# )

# output_parser = StrOutputParser()

# # LangChain Chain
# chain = prompt | llm | output_parser

# # --- Streamlit App Interface ---

# # 1. Set App Title and Icon
# st.set_page_config(page_title="Custom Chatbot-Made By Umar Imam", page_icon="🤖")
# st.title("🤖 Custom Chatbot-Made By Umar Imam")

# # 2. Initialize Chat History in Session State
# # This list will store tuples/dicts of the conversation: [{"role": "user/assistant", "content": "message"}]
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     # Add an initial welcome message
#     st.session_state.messages.append({"role": "assistant", "content": f"Hello! I am a custom chatbot,Made By- Umar Imam & powered by **{MODEL_NAME}**. How can I assist you today?"})

# # 3. Display Chat History
# # Iterate through the history and display each message using st.chat_message
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # 4. Handle New User Input using st.chat_input
# # This component is the key to the modern chat interface look.
# if prompt_input := st.chat_input("Ask me anything..."):
    
#     # a. Add User Message to History and Display it
#     st.session_state.messages.append({"role": "user", "content": prompt_input})
#     with st.chat_message("user"):
#         st.markdown(prompt_input)

#     # b. Generate and Display AI Response
#     with st.chat_message("assistant"):
#         # Use st.spinner for a loading state
#         with st.spinner(f"Thinking with {MODEL_NAME}..."):
#             try:
#                 # Invoke the LangChain chain
#                 response = chain.invoke({"question": prompt_input})
#                 st.markdown(response)
                
#                 # c. Add AI Response to History
#                 st.session_state.messages.append({"role": "assistant", "content": response})
            
#             except Exception as e:
#                 error_message = f"An error occurred: {e}"
#                 st.error(error_message)
#                 st.session_state.messages.append({"role": "assistant", "content": error_message})



#*#*#**#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#**#*#*#*#*#*#*#*#*#*#**#**#*#*#*#*#*#*#**#*#*#*#*#*#*##**#*#*#*#*#**#*#*#*#*#*#**#*#*#*#*#**#*#



# This is More Modified Code For Gemini Custom Chatbot Using Langchain and Streamlit

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# import os
# from datetime import datetime
# import json
# import base64 # Import included for completeness, though not used in the UI logic changes

# # ------------------ CONFIG ------------------
# # NOTE: The API key is exposed here. In a real-world app, use st.secrets or environment variables securely.
# os.environ["GOOGLE_GENAI_API_KEY"] = ""
# MODEL_NAME = "gemini-2.5-flash"

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful and friendly chatbot powered by Google's Gemini model. Be concise."),
#     ("user", "Question: {question}")
# ])
# # Correct: use the environment variable NAME here
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     temperature=0.7,
#     google_api_key=os.environ["GOOGLE_GENAI_API_KEY"]
# )

# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# # Set layout *before* any other Streamlit calls
# st.set_page_config(page_title="Custom Chatbot - Made By Umar Imam", page_icon="🤖", layout="wide")

# # ------------------ CUSTOM CSS FOR COOL UI ------------------
# # Injecting a dark, sleek theme with custom chat bubble and button styles
# st.markdown(
#     """
#     <style>
#     /* 1. Base Setup & Font */
#     html, body {
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
    
#     /* 2. Main Page Background (Dark Theme) */
#     .stApp {
#         background-color: #1e1e2f; /* Deep blue-violet background */
#         color: #e0e0e0;
#     }
    
#     /* 3. Sidebar Styling */
#     .css-1d3f9ho { /* Specific class for the sidebar container */
#         background-color: #171725; /* Even darker sidebar */
#         border-right: 2px solid #4b0082; /* Purple accent border */
#         box-shadow: 2px 0 10px rgba(0, 0, 0, 0.5);
#     }
    
#     /* 4. Header Separator */
#     .stHorizontalSeparator {
#         border-top: 1px solid #3a3a55; /* Subtle divider */
#     }
    
#     /* 5. Chat Input Area (Bottom) */
#     .stChatInput {
#         padding: 10px 0;
#         background-color: #1e1e2f; /* Match main background */
#     }
    
#     .stTextInput > div > div > input {
#         border-radius: 25px !important; /* Rounded pill shape */
#         border: 2px solid #3a3a55;
#         background-color: #252537; /* Dark input background */
#         color: white;
#         padding: 10px 20px;
#         transition: border-color 0.3s, box-shadow 0.3s;
#     }
    
#     .stTextInput > div > div > input:focus {
#         border-color: #8a2be2; /* Focus glow */
#         box-shadow: 0 0 10px rgba(138, 43, 226, 0.6);
#         outline: none;
#     }
    
#     /* 6. Custom Chat Bubbles (The most 'interactive' part) */
#     /* Bot Message Bubble */
#     [data-testid="stChatMessage"] div:first-child > div:nth-child(2) > div {
#         background-color: #3a3a55; /* Muted Bot background */
#         color: #e0e0e0;
#         border-radius: 18px 18px 18px 5px; /* Rounded with a slight 'tail' */
#         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
#         animation: fadeIn 0.3s ease-out; /* Fade-in effect */
#     }

#     /* User Message Bubble */
#     [data-testid="stChatMessage"][data-state="rendered"] div:last-child > div:nth-child(2) > div {
#         background-color: #4b0082; /* Vibrant User background (Deep Purple) */
#         color: white;
#         border-radius: 18px 18px 5px 18px; /* Rounded with a slight 'tail' */
#         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
#         margin-left: auto; /* Push user message to the right */
#         text-align: right;
#         animation: fadeIn 0.3s ease-out;
#     }
    
#     /* 7. Button Enhancements (Sidebar buttons) */
#     .stButton>button {
#         width: 100%;
#         border-radius: 10px;
#         background-color: #8a2be2; /* Default purple */
#         color: white;
#         border: none;
#         padding: 10px;
#         transition: background-color 0.2s, transform 0.1s;
#     }
    
#     .stButton>button:hover {
#         background-color: #6a11cb; /* Darker purple on hover */
#         transform: translateY(-1px);
#         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
#     }
    
#     /* 8. Text-to-Speech Checkbox */
#     .stCheckbox label span {
#         color: #cfcfcf;
#     }

#     /* 9. Keyframe Animation */
#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(10px); }
#         to { opacity: 1; transform: translateY(0); }
#     }
    
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ------------------ LOGO ------------------
# ROBOT_SVG = """
# <svg width="84" height="84" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
#     <defs>
#         <linearGradient id="g1" x1="0" x2="1">
#             <stop offset="0" stop-color="#4b0082"/> /* Deep Purple */
#             <stop offset="1" stop-color="#8a2be2"/> /* Blue Violet */
#         </linearGradient>
#     </defs>
#     <circle cx="64" cy="64" r="60" fill="url(#g1)"/>
#     <rect x="36" y="44" width="56" height="36" rx="8" fill="white" opacity="0.95"/>
#     <circle cx="56" cy="62" r="6" fill="#333"/>
#     <circle cx="80" cy="62" r="6" fill="#333"/>
#     <rect x="44" y="76" width="40" height="6" rx="3" fill="#e6e6e6"/>
#     <rect x="57" y="30" width="14" height="8" rx="4" fill="#fff" opacity="0.9"/>
# </svg>
# """

# ROBOT_SVG_HTML = f"""<div style="width:84px;height:84px; transform: scale(0.85); transform-origin: top left;">{ROBOT_SVG}</div>""" # Slightly scaled down for header fit

# # ------------------ SESSION STATE ------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": f"Hello! I am a custom chatbot made by **Umar Imam**, powered by **{MODEL_NAME}**.\nHow can I assist you today?",
#             "time": datetime.now().strftime("%H:%M")
#         }
#     ]

# # ------------------ SIDEBAR ------------------
# with st.sidebar:
#     # Enhanced Sidebar Header (Using h3 for better styling control)
#     st.markdown("""
#         <div style="text-align:center; margin-top:8px; margin-bottom:20px; padding: 10px; border-bottom: 1px solid #3a3a55;">
#     <h3 style="
#         margin-bottom:0px;
#         color:#8a2be2; /* Use accent color for title */
#         font-weight:700;
#         letter-spacing:1px;
#         text-shadow: 0 0 5px rgba(138, 43, 226, 0.4);
#     ">
#         🤖 Umar-AI Assistant
#     </h3>
#     <p style="
#     margin-top:0px;
#     font-size:13px;
#     color:#a0a0a0;
#     letter-spacing:0.3px;
# ">
#     Made by <b>Umar Imam</b>
# </p>
# </div>
#     """, 
#     unsafe_allow_html=True)

#     st.markdown("### ⚙️ Options", unsafe_allow_html=True)

#     # Clear Chat Button
#     # Note: The custom CSS above will style this button
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun() # Ensure chat clears immediately

#     st.markdown("---") # Visual separator

#     # Text-to-Speech Toggle
#     tts_enabled = st.checkbox("🔊 Enable Text-to-Speech", value=False)

#     # Download Chat
#     st.download_button(
#         label="⬇️ Download Chat History (.txt)",
#         data=json.dumps(st.session_state.messages, indent=2, ensure_ascii=False),
#         file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
#         mime="text/plain"
#     )

# # ------------------ HEADER ------------------
# col1, col2 = st.columns([1, 9])
# with col1:
#     st.markdown(ROBOT_SVG_HTML, unsafe_allow_html=True)
# with col2:
#     st.markdown("""
#     <h1 style='margin-bottom:0px; color:#ffffff; font-weight:700; letter-spacing:1px;'>Custom Chatbot</h1>
#     <p style='opacity:0.7;margin-top:0px; font-size:16px;'>Developed by <b>Umar Imam</b></p>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# # ------------------ CHAT HISTORY ------------------
# # The custom CSS ensures these messages look 'cool' and animated
# for msg in st.session_state.messages:
#     # The time stamp is currently not visible in the message component,
#     # but the time data is still useful for history download.
#     # To display it, you would need more advanced custom component logic.
#     if msg["role"] == "user":
#         with st.chat_message("user"):
#             st.markdown(msg["content"])
#     else:
#         with st.chat_message("assistant"):
#             st.markdown(msg["content"])

# # ------------------ USER INPUT ------------------
# # The custom CSS ensures this input field looks rounded and glows on focus
# user_input = st.chat_input("Ask anything...")

# if user_input:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input,
#         "time": datetime.now().strftime("%H:%M")
#     })

#     # Display user message immediately
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Process and display assistant response
#     with st.chat_message("assistant"):
#         # Changed st.spinner style (it inherits the new dark theme)
#         with st.spinner("Umar AI is thinking..."): 
#             try:
#                 response = chain.invoke({"question": user_input})
#             except Exception as e:
#                 response = f"⚠️ **Error:** Could not connect to the model. Details: `{e}`"
#                 # Log error details for debugging
#                 print(f"API Error: {e}") 

#         st.markdown(response)

#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response,
#         "time": datetime.now().strftime("%H:%M")
#     })
    
#     # Removed the st.rerun() here as displaying the user message earlier handles the double-posting issue, 
#     # and the next message is appended right after the response, which is cleaner.
#     # (Keeping the original st.rerun() if you prefer its behavior, but typically it is not needed if messages are displayed right away.)
#     # st.rerun() # Keep your original rerun
#     pass

# # ------------------ TEXT-TO-SPEECH ------------------
# if tts_enabled and st.session_state.messages:
#     # Check if the last message was from the assistant to avoid reading the user's input
#     if st.session_state.messages[-1]["role"] == "assistant":
#         last_msg = st.session_state.messages[-1]["content"].replace('"', '\\"')
        
#         # NOTE: Using a try/except for the speech synthesis to prevent errors if the string is too complex
#         st.components.v1.html(
#             f"""
#             <script>
#             try {{
#                 const msg = "{last_msg}";
#                 if ('speechSynthesis' in window) {{
#                     const utter = new SpeechSynthesisUtterance(msg);
#                     utter.rate = 1.1; // Slightly faster for a modern feel
#                     utter.volume = 0.9;
#                     // Optional: Try setting a preferred voice
#                     // utter.voice = window.speechSynthesis.getVoices().find(v => v.lang === 'en-US');
#                     speechSynthesis.speak(utter);
#                 }}
#             }} catch(e) {{
#                 console.error("TTS Error:", e);
#             }}
#             </script>
#             """,
#             height=0
#             # REMOVED: key="tts_trigger"
#         )

# *#*#**#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#**#*#*#*#*#*#*#*#*#*#**#**#*#*#*#*#*#*#**#*#*#*#*#*#*##**#*#*#*#*#**#*#*#*#*#*#**#*#*#*#*#**#*#




# This is The Final Modified Code For Gemini Custom Chatbot Using Langchain and Streamlit

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# import os
# from datetime import datetime
# import json
# import base64

# # ------------------ CONFIG ------------------
# # NOTE: The API key is exposed here. In a real-world app, use st.secrets or environment variables securely.
# os.environ["GOOGLE_GENAI_API_KEY"] = ""

# MODEL_NAME = "gemini-2.5-flash"

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful and friendly chatbot powered by Google's Gemini model. Be concise."),
#     ("user", "Question: {question}")
# ])

# # Correct: use the environment variable NAME here
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     temperature=0.7,
#     google_api_key=os.environ["GOOGLE_GENAI_API_KEY"]
# )

# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# # Set layout *before* any other Streamlit calls
# st.set_page_config(page_title="Coustom ChatBot", page_icon="🤖", layout="wide")

# # ------------------ CUSTOM CSS FOR COOL UI (Updated for Constrained View) ------------------
# st.markdown(
#     """
#     <style>
#     html, body {
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }

#     .stApp {
#         background-color: #1e1e2f;
#         color: #e0e0e0;
#     }

#     .main > div {
#         max-width: 900px;
#         margin-left: auto;
#         margin-right: auto;
#         padding-left: 1rem;
#         padding-right: 1rem;
#     }

#     .css-1d3f9ho {
#         background-color: #171725;
#         border-right: 2px solid #4b0082;
#         box-shadow: 2px 0 10px rgba(0, 0, 0, 0.5);
#     }

#     .stHorizontalSeparator {
#         display: none;
#     }

#     .stChatInput {
#         padding: 5px 0 10px 0;
#         background-color: #1e1e2f;
#     }

#     [data-testid="stChatInput"] {
#         max-width: 900px;
#         margin-left: auto;
#         margin-right: auto;
#         border-top: 1px solid #3a3a55;
#         box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.3);
#     }

#     .stTextInput > div > div > input {
#         border-radius: 25px !important;
#         border: 2px solid #3a3a55;
#         background-color: #252537;
#         color: white;
#         padding: 10px 20px;
#         transition: border-color 0.3s, box-shadow 0.3s;
#     }

#     .stTextInput > div > div > input:focus {
#         border-color: #8a2be2;
#         box-shadow: 0 0 10px rgba(138, 43, 226, 0.6);
#         outline: none;
#     }

#     [data-testid="stChatMessage"] div:first-child > div:nth-child(2) > div {
#         background-color: #3a3a55;
#         color: #e0e0e0;
#         border-radius: 18px 18px 18px 5px;
#         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
#         animation: fadeIn 0.3s ease-out;
#     }

#     [data-testid="stChatMessage"][data-state="rendered"] div:last-child > div:nth-child(2) > div {
#         background-color: #4b0082;
#         color: white;
#         border-radius: 18px 18px 5px 18px;
#         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
#         margin-left: auto;
#         text-align: right;
#         animation: fadeIn 0.3s ease-out;
#     }

#     .stButton>button {
#         width: 100%;
#         border-radius: 10px;
#         background-color: #8a2be2;
#         color: white;
#         border: none;
#         padding: 10px;
#         transition: background-color 0.2s, transform 0.1s;
#     }

#     .stButton>button:hover {
#         background-color: #6a11cb;
#         transform: translateY(-1px);
#         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
#     }

#     .stCheckbox label span {
#         color: #cfcfcf;
#     }

#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(10px); }
#         to { opacity: 1; transform: translateY(0); }
#     }

#     .block-container:first-of-type > div:first-of-type > div:first-of-type {
#         padding-top: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ------------------ LOGO & SESSION STATE (UNCHANGED) ------------------
# ROBOT_SVG = """
# <svg width="84" height="84" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
#     <defs>
#         <linearGradient id="g1" x1="0" x2="1">
#             <stop offset="0" stop-color="#4b0082"/>
#             <stop offset="1" stop-color="#8a2be2"/>
#         </linearGradient>
#     </defs>
#     <circle cx="64" cy="64" r="60" fill="url(#g1)"/>
#     <rect x="36" y="44" width="56" height="36" rx="8" fill="white" opacity="0.95"/>
#     <circle cx="56" cy="62" r="6" fill="#333"/>
#     <circle cx="80" cy="62" r="6" fill="#333"/>
#     <rect x="44" y="76" width="40" height="6" rx="3" fill="#e6e6e6"/>
#     <rect x="57" y="30" width="14" height="8" rx="4" fill="#fff" opacity="0.9"/>
# </svg>
# """

# ROBOT_SVG_HTML = f"""<div style="width:84px;height:84px; transform: scale(0.85); transform-origin: top left;">{ROBOT_SVG}</div>"""

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": f"Hello! I am your **Umar-AI Assistant**, powered by **{MODEL_NAME}**.\nHow can I assist you today?",
#             "time": datetime.now().strftime("%H:%M")
#         }
#     ]

# # ------------------ SIDEBAR (UNCHANGED) ------------------
# with st.sidebar:
#     st.markdown("""
#         <div style="text-align:center; margin-top:8px; margin-bottom:20px; padding: 10px; border-bottom: 1px solid #3a3a55;">
#             <h3 style="margin-bottom:0px; color:#8a2be2; font-weight:700; letter-spacing:1px;">
#                 🤖 Umar-AI Assistant
#             </h3>
#             <p style="margin-top:0px; font-size:13px; color:#a0a0a0;">
#                 Made by <b>Umar Imam</b>
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

#     st.markdown("### ⚙️ Options", unsafe_allow_html=True)

#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

#     st.markdown("---")

#     tts_enabled = st.checkbox("🔊 Enable Text-to-Speech", value=False)

#     st.download_button(
#         label="⬇️ Download Chat History (.txt)",
#         data=json.dumps(st.session_state.messages, indent=2, ensure_ascii=False),
#         file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
#         mime="text/plain"
#     )

# # ------------------ CHAT HISTORY ------------------
# st.markdown("""
#     <div style='text-align:center; margin-bottom:25px;'>
#         <h2 style='color:#ffffff; font-weight:700;'>Umar-AI Assistant</h2>
#         <p style='opacity:0.6;'>Developed by <b>Umar Imam</b> • Powered by Gemini</p>
#     </div>
# """, unsafe_allow_html=True)

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # ------------------ USER INPUT ------------------
# user_input = st.chat_input("Ask anything...")

# if user_input:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input,
#         "time": datetime.now().strftime("%H:%M")
#     })

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     with st.chat_message("assistant"):
#         with st.spinner("Umar AI is thinking..."):
#             response = chain.invoke({"question": user_input})
#         st.markdown(response)

#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response,
#         "time": datetime.now().strftime("%H:%M")
#     })

# # ------------------ TEXT-TO-SPEECH ------------------
# if tts_enabled and st.session_state.messages:
#     if st.session_state.messages[-1]["role"] == "assistant":
#         last_msg = st.session_state.messages[-1]["content"].replace('"', '\\"')
#         st.components.v1.html(
#             f"""
#             <script>
#                 const msg = "{last_msg}";
#                 if ('speechSynthesis' in window) {{
#                     const utter = new SpeechSynthesisUtterance(msg);
#                     utter.rate = 1.1;
#                     utter.volume = 0.9;
#                     speechSynthesis.speak(utter);
#                 }}
#             </script>
#             """,
#             height=0
#         )

# The above Code Was Using my name Umar Imam.Now This is the Final Modified Code For Gemini Custom Chatbot Using Langchain and Streamlit

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from datetime import datetime
import json
import os
from PIL import Image 
from io import BytesIO
import base64 
from langchain_core.messages import HumanMessage # NEW IMPORT

# ================== CONFIG ==================
MODEL_NAME = "gemini-2.5-flash" 

GOOGLE_API_KEY = st.secrets.get("GOOGLE_GENAI_API_KEY") or os.getenv("GOOGLE_GENAI_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Google API key not found. Please set GOOGLE_GENAI_API_KEY.")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# ================== PAGE ==================
st.set_page_config(
    page_title="NovaMind AI",
    page_icon="🤖",
    layout="wide"
)

# ================== CSS ==================
st.markdown("""
<style>
html, body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.stApp { background-color: #1e1e2f; color: #e0e0e0; }

section.main > div {
    max-width: 900px !important;
    margin: auto !important;
    padding: 1rem;
}

[data-testid="stAppViewContainer"] {
    justify-content: center;
}

.stHorizontalSeparator { display: none; }
</style>
""", unsafe_allow_html=True)

# ================== SESSION ==================
WELCOME_MESSAGE = (
    "👋 Hello! I’m **NovaMind AI** — an intelligent AI assistant powered by **Gemini**.\n\n"
    "**Developed by Umar Imam**.\n\nHow can I help you today? You can now **upload an image** in the sidebar for me to analyze!"
)

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": WELCOME_MESSAGE,
        "time": datetime.now().strftime("%H:%M")
    }]
if "uploaded_image" not in st.session_state: 
    st.session_state.uploaded_image = None

# ================== SIDEBAR ==================
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding-bottom:15px; border-bottom:1px solid #3a3a55;">
        <h3 style="color:#8a2be2;">🤖 NovaMind AI</h3>
        <p style="font-size:13px; opacity:0.7;">
            An intelligent AI assistant powered by Gemini<br>
            <b>Developed by Umar Imam</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": WELCOME_MESSAGE,
            "time": datetime.now().strftime("%H:%M")
        }]
        st.session_state.uploaded_image = None
        st.rerun()

    st.markdown("---")

    tts_enabled = st.checkbox("🔊 Enable Text-to-Speech", value=False)

    voice_type = st.selectbox(
    "🎙️ Voice",
    ["Female", "Male"],
    index=0
)
    
    # ------------------ NEW FEATURE: Image Upload ------------------
    st.markdown("---")
    st.subheader("🖼️ Image/File Upload")
    
    uploaded_file = st.file_uploader(
        "Upload an image or file for analysis",
        type=["png", "jpg", "jpeg", "webp"],
        key="file_uploader"
    )

    if uploaded_file is not None:
        st.session_state.uploaded_image = Image.open(uploaded_file)
        st.image(st.session_state.uploaded_image, caption="Image Ready for Analysis", width=200)
    else:
        st.session_state.uploaded_image = None
    
    # ------------------ END NEW FEATURE ------------------

    st.download_button(
        "⬇️ Download Chat History",
        json.dumps(st.session_state.messages, indent=2),
        f"novamind_chat_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        "text/plain"
    )

# ================== HEADER ==================
st.markdown("""
<div style="text-align:center; margin-bottom:25px;">
    <h2>NovaMind AI</h2>
    <p style="opacity:0.6;">
        An intelligent AI assistant powered by Gemini<br>
        <b>Developed by Umar Imam</b>
    </p>
</div>
""", unsafe_allow_html=True)

# ================== CHAT ==================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Helper function to convert PIL Image to base64
def pil_to_base64(img):
    buffered = BytesIO()

    # ✅ Convert RGBA / P / LA / etc. to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()


# ================== INPUT (FIXED FOR 'role' and 'content' ERROR) ==================
user_input = st.chat_input("Ask anything...")

if user_input:
    # 1. Build the list of content parts (multimodal dictionaries)
    content_parts = []
    
    if st.session_state.uploaded_image:
        base64_img = pil_to_base64(st.session_state.uploaded_image)
        
        # Image part dictionary
        image_content = {
            "type": "image_url",
            "image_url": {
                # Use data URL scheme for passing base64
                "url": f"data:image/jpeg;base64,{base64_img}" 
            }
        }
        content_parts.append(image_content)
        
        user_message_content = f"**User Question:** {user_input} (Image included in the prompt)"
    else:
        user_message_content = user_input
        
    # Text part dictionary (always included)
    text_content = {
        "type": "text",
        "text": user_input
    }
    content_parts.append(text_content)
    
    # 2. **CRUCIAL FIX:** Wrap the content parts into a HumanMessage object
    # This provides the necessary 'role' and 'content' structure.
    human_message = HumanMessage(
        content=content_parts,
    )
    
    # 3. Define System Instruction and the final input list for invoke()
    system_instruction = "You are NovaMind AI — a helpful, intelligent assistant powered by Google's Gemini model. Be concise."
    
    final_input = [human_message] # The model expects a list of messages

    # 4. Append the user message to session state
    st.session_state.messages.append({
        "role": "user",
        "content": user_message_content,
        "time": datetime.now().strftime("%H:%M")
    })

    with st.chat_message("user"):
        st.markdown(user_message_content)

    with st.chat_message("assistant"):
        with st.spinner("NovaMind AI is thinking..."):
            try:
                # Invoke the model with the list of HumanMessage objects
                response_obj = llm.invoke(final_input, system_instruction=system_instruction)
                response = response_obj.content
            except Exception as e:
                response = f"An error occurred during generation: {e}"

        st.markdown(response)

    # 5. Append the assistant response to session state
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": datetime.now().strftime("%H:%M")
    })
    
# ================== TEXT TO SPEECH ==================
if tts_enabled and st.session_state.messages:
    last_msg = st.session_state.messages[-1]

    if last_msg["role"] == "assistant":
        # Create two columns to place the buttons side-by-side
        col1, col2 = st.columns([0.4, 0.6]) # Adjust ratios as needed

        with col1:
            if st.button("🔊 Speak last response", key="speak_button_main_app"):
                safe_text = (
                    last_msg["content"]
                    .replace('"', "'")
                    .replace("\n", " ")
                )

                js_voice = """
                <script>
                const text = "%s";
                let voices = [];

                function loadVoices() {
                    voices = window.speechSynthesis.getVoices();
                }
                loadVoices();
                window.speechSynthesis.onvoiceschanged = loadVoices;

                function pickVoice(gender) {
                    const femaleKeywords = ["zira", "samantha", "female", "woman", "english uk", "google uk"];
                    const maleKeywords = ["david", "alex", "male", "man"];

                    if (gender === "female") {
                        for (let v of voices) {
                            const name = v.name.toLowerCase();
                            if (femaleKeywords.some(k => name.includes(k))) {
                                return v;
                            }
                        }
                    }

                    if (gender === "male") {
                         for (let v of voices) {
                            const name = v.name.toLowerCase();
                            if (maleKeywords.some(k => name.includes(k))) {
                                return v;
                            }
                        }
                    }

                    return voices.find(v => v.lang.startsWith("en")) || voices[0];
                }

                const msg = new SpeechSynthesisUtterance(text);
                msg.rate = 1.05;
                msg.pitch = %s;
                msg.voice = pickVoice("%s");

                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(msg);
                </script>

                """ % (
                    safe_text,
                    "1.2" if voice_type == "Female" else "0.9",
                    voice_type.lower()
                )

                st.components.v1.html(js_voice, height=0)

        with col2:
            # --- NEW STOP BUTTON ---
            if st.button("🛑 Stop Speech", key="stop_button_main_app"):
                js_stop = """
                <script>
                // This command cancels any ongoing speech synthesis
                window.speechSynthesis.cancel();
                </script>
                """
                st.components.v1.html(js_stop, height=0)

            # --- END NEW STOP BUTTON ---
