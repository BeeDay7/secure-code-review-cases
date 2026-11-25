import base64, pickle

def load_session(cookie: str):
    # Flaw: pickle executes callables embedded in the data.
    return pickle.loads(base64.b64decode(cookie))
