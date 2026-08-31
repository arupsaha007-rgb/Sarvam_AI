# from pathlib import Path
from dotenv import load_dotenv
from langchain_sarvam import ChatSarvam

from langchain.agents import create_agent

from langchain.messages import HumanMessage

from pprint import pprint



# load_dotenv(Path(__file__).resolve().parents[1] / ".env")
load_dotenv()
llm = ChatSarvam(model="sarvam-105b")

agent = create_agent(model=llm)

# query = "Extract enties and designate them from below : Krishna Pyde paid money to Arup Saha in India and Srilanka?"
query = "Extract enties and designate them from below. Try extract names of Individual, Business, Places : PROCESS PAYMENT UNDER LC 13752036\r\nISSUING BANK REF IBR-PQS-860140\r\nNOMINATED BANK MERIDIAN TRADE BANK\r\nNOMINATED BANK BIC MTRDPKXX\r\nREIMBURSING BANK NORTHSTAR BANKING CORP\r\nREIMBURSING BIC NSBCARXX\r\nCLAIM REF RMB-BUE-960140\r\nPAY GBP 211060.00 AT MATURITY\r\nCREDIT ACCOUNT 7100000140\r\nAPPLICANT SOLE TRADER SANA KHAN\r\nTRADING NAME STEEL DRUM IMPORTS\r\nBENEFICIARY SOLE TRADER MATEO ALVAREZ\r\nTRADING NAME STEEL DRUM EXPORTS\r\nADVISE DISCREPANCIES BY AUTHENTICATED SWIFT\r\nRETAIN A COPY OF THE SANCTIONS SCREENING RESULT"
# query = "Translate to hindi : I am going to Kolkata."
print(query)
print("Thinking......................")

response = agent.invoke(
    {"messages": [HumanMessage(content=query)]}
)


pprint(response)

print(response['messages'][-1].content)

