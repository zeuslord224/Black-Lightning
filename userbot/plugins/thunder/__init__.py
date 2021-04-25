ASSISTANT_HELP = {}
import os 
ASSISTANT_CMD_HNDLR = os.environ.get("ASSISTANT_CMD_HNDLR", None)
if ASSISTANT_CMD_HNDLR is None:
    ASSISTANT_CMD_HNDLR = "/"
else:
   ass_cmd_hndlr = ASSISTANT_CMD_HNDLR