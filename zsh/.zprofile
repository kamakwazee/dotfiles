
if [ -z "$DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ] && [ "$(tty)" = "/dev/tty1" ]; then
	exec startx
fi
