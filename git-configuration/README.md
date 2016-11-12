## Enhanced git log

1. Add the following block in ```gitconfig``` file :  

```
[alias]  
    graph1 = log --graph --abbrev-commit --decorate --format=format:'%C(blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(bold white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
    graph2 = log --graph --abbrev-commit --decorate --format=format:'%C(blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''%C(bold white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
```

2. Now run ```git graph1``` or ```git graph2``` in your project folder.  
3. The log will now be condensed with better visibility and branch network will also be displayed.