from langchain_google_genai import ChatGoogleGenerativeAI
from app.models.boq_schema import BOQList

def extract_with_ai(messy_text):
    # 1. Wake up the Gemini AI 
    # (gemini-1.5-pro is great for this because it reads lots of text easily!)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0) 
    
    # 2. Give the AI our rules (the Pydantic schema)
    smart_ai = llm.with_structured_output(BOQList)
    
    # 3. Tell it what to do
    instructions = f"Look at this messy Excel data and extract the building materials into a neat list: {messy_text}"
    
    # 4. Get the neat list back!
    neat_list = smart_ai.invoke(instructions)
    
    return neat_list
