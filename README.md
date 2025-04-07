# AI-Email-Parser-LangGraph
Build a stateful AI agent in Python using LangGraph to automate email classification and summarization. This project walks through creating a multi-step workflow where an agent processes raw email text, classifies its intent, and generates a response or summary accordingly.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/uday-bhaskar-patsamatla/AI-Email-Parser-LangGraph.git
   cd AI-Email-Parser-LangGraph
   ```

2. **Install Dependencies:**
   Make sure you have Python 3.x installed. Then, install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Ensure you have the necessary API keys and configurations. You can use a `.env` file to set these up.
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the Application:**
   Execute the main scripts to start the email processing.
   ```bash
   python main1.py
   python main2.py
   python main3.py
   ```

5. **Usage:**
   - Add any specific instructions on how to use the features of your application.
   - Explain how the email classification and summarization works.
   - Provide examples of input and expected output.

6. **Contribution Guidelines:**
   If you wish to contribute, please follow our [contribution guidelines](CONTRIBUTING.md).

7. **License:**
   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




# 1. Project Overview:
    The AI-Email-Parser-LangGraph is a Python project that uses LangGraph to create a stateful AI agent for automating email classification and summarization. It processes raw email text, classifies its intent, and generates appropriate responses or summaries.

# 2. Project Structure:

### readme.md - Documentation
    This file provides an overview of the project, setup instructions, usage guidelines, and other important information.

# 3. Main Scripts:
    main1.py
    main2.py
    main3.py
    These are the entry points for the application. They likely contain different implementations or variations of the email processing workflow.

# 4.Modules:
##    a. chains/ ---> This module contains various chain components for processing emails:
    init.py
    binary_questions.py
    escalation_check.py
    notice_extraction.py

###   binary_questions.py: Probably handles yes/no questions in emails.
###   escalation_check.py: Likely checks if an email needs to be escalated to a higher authority.
###   notice_extraction.py: Possibly extracts important notices or information from emails.

##    b. graphs/ ---> This module to contain the graph structures for the LangGraph implementation:
    init.py
    email_agent.py
    notice_extraction.py

###   email_agent.py: Likely defines the main email processing agent.
###    notice_extraction.py: Probably implements a graph for extracting notices from emails.

##    c. utils/ ---> Utility functions and configurations:
    init.py
    graph_utils.py
    logging_config.py
    
###    graph_utils.py: Helper functions for working with graphs.
###    logging_config.py: Logging configuration for the application.

#   5. Additional Files:
###     email_agent_graph.png: visual representation of the email agent graph structure.
###     notice_extraction_graph.png: a diagram of the notice extraction process.
###     example_email.py:  contains sample email data for testing or demonstration.

#   6. Workflow:

Based on the project structure and README, the general workflow appears to be:

a. The user runs one of the main scripts (main1.py, main2.py, or main3.py).
b. The script initializes the email processing agent using the graph structures defined in the graphs/ module.
c. Raw email text is input into the system.
d. The email goes through various processing steps, which may include:
Intent classification
Binary question handling
Escalation checking
Notice extraction
e. Depending on the classification and extracted information, the system generates an appropriate response or summary.
f. The result is returned to the user or stored for further processing.

#   7. Usage:
Users are instructed to clone the repository, install dependencies, set up environment variables (particularly the OpenAI API key), and then run one of the main scripts to start processing emails.

#   8. Contribution and Licensing:
The project welcomes contributions (guided by a CONTRIBUTING.md file) and is licensed under the MIT License.
This project seems to be a comprehensive solution for automated email processing, leveraging AI and graph-based workflows to handle various aspects of email classification and response generation. The modular structure allows for easy expansion and modification of different components of the email processing pipeline.

For further information on this project read https://realpython.com/langgraph-python/