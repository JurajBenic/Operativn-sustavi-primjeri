#!/bin/sh

# Dodaj sistemske Python pakete (python3-tk) u sys.path
export PYTHONPATH="$SNAP/usr/lib/python3.12:$SNAP/usr/lib/python3.12/lib-dynload"
export LD_LIBRARY_PATH="$SNAP/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
export TCL_LIBRARY="$SNAP/usr/share/tcltk/tcl8.6"
export TK_LIBRARY="$SNAP/usr/share/tcltk/tk8.6"

exec "$SNAP/bin/python3" "$SNAP/bin/app/main.py"
