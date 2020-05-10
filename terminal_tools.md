
# Tmux
## Create new session
### without specifying a name
```
tmux
```
### specifying a name
```
tmux new -s <name>
```

## Display open sessions
```
tmux ls
```

## Quit tmux screen without stopping sessions
These 2 commands are done sequentially
```
ctrl+b, d
```
Or equivalently if it is possible to enter a command
```
tmux detach
```

## Come back to the session commands
```
tmux attach -t <name>
```

## Kill session
### by name
```
tmux kill-session -t <name>
```
### all and quit tmux
```
tmux kill-server
```
### all but the last activated
```
tmux kill-session -a
```
