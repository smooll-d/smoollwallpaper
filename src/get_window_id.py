import subprocess

def get_window_id():
    output = subprocess.check_output("xprop -root | grep \"window id\"", shell=True, encoding="utf8")
    result = {}
    
    for row in output.split("\n"):
        if ": " in row:
            key, value = row.split(": ")
            result[key] = value.strip()

    get_window_id.dwid = result["_NET_CLIENT_LIST(WINDOW)"].strip("window id # ").split(",", 1)[0]
    get_window_id.awid = result["_NET_ACTIVE_WINDOW(WINDOW)"].strip("window id # ")
