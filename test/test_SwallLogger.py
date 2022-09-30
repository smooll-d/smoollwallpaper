import pytest

@pytest.mark.parametrize("message", [
        "This is a debug message.",
        "This is an info message.",
        "This is a warning message.",
        "This is an error message.",
        "This is a critical message."
    ])
def test_SwallLogger(message):
    from src.SwallLogger import SwallLogger

    sl = SwallLogger("test_Swalllogger")
 
    sl.debug(message[0])
    sl.info(message[1])
    sl.warning(message[2])
    sl.error(message[3])
    sl.critical(message[4])
