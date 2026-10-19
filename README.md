# Missing-Semester-Git-Challenge

Tiny broken calculator for the Missing Semester Git workshop.

```bash
python3 calculator.py
```

Format: `<number> <op> <number>` - ops: `+ - * /`

# Git CTF
When you finish the broken calculator problem, move onto the git-themed CTF challenge. Most flags are on a different branch formatted as challenge-[flag #], e.g. challenge-69
When you pwn a flag, put it in a flags.txt file in this format:
```txt
COMP_SOC{flag1}
COMP_SOC{flag2}
...
```

Once you have pwned all the flags run the following:
```bash
python3 flag_checker.py <your_flags.txt file>

#Ex:
python3 flag_checker.py flags.txt
```
