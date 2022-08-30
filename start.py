import os
import termo_defs

os.system("cls") or None

termo_defs.title(6)

print("""
[1] COMEÇAR O JOGO
[2] FINALIZAR O JOGO
""")

start = int(input())

termo = 'termo.py'

if (start == 1):
    exec(open(termo, encoding = "utf-8").read())
