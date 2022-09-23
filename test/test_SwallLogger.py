def test_SwallLogger():
    from src.SwallLogger import SwallLogger

    sl = SwallLogger("test_Swalllogger")

    sl.debug("This is a debug message.")
    sl.info("This is an info message.")
    sl.warning("This is a warning message.")
    sl.error("This is an error message.")
    sl.critical("This is a critical message.")
