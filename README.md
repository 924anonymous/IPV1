Execution Steps To Run DockerFile To Get Image Running

    Note : Start Docker Engine before Executing Below Commands
    Steps:
        - Step 1:
            Start the terminal at the location where DockerFile is.
        - Step 2:
            Execute below commands :
                - "docker build -t streamlit ."
                - "docker run -p 8501:8501 streamlit"