from graphs.notice_extraction import NOTICE_EXTRACTION_GRAPH
from example_email import EMAILS
from utils.logging_config import LOGGER

initial_state = {
    "notice_message": EMAILS[3],
    "notice_email_extract": None,
    "escalation_text_criteria": """There's a risk of fire or
    water damage at the site""",
    "escalation_dollar_criteria": 100_000,
    "requires_escalation": False,
    "escalation_emails": ["brog@abc.com", "bigceo@company.com"],
}

final_state = NOTICE_EXTRACTION_GRAPH.invoke(initial_state)



LOGGER.info(f"{final_state["notice_email_extract"]}")


final_state =  final_state["requires_escalation"]

if final_state == True:
    LOGGER.warning("Immediate escalation required")
else:
    LOGGER.info("No immediate escalation required") 