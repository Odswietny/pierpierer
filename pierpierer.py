import pyperclip
import time
import sys

sys.set_int_max_str_digits(0)

print("PierPierer v1.0.1")
try:
    howmany = int(input("Ile chcesz powtorzen czesci 'pier'?: "))
except ValueError:
    print("ERROR: nie mozesz wstawic nic innego niz liczbe! Zamkniecie za 5 sekund...")
    time.sleep(5)
    exit(1)
before = input("Czy chcesz cos wstawic na poczatku? (nie wpisuj nic jesli nie): ")
after = input("Czy chcesz cos wstawic na koncu? (nie wpisuj nic jesli nie): ")

newstring = before + "pier" * abs(howmany) + after
print(newstring)
pyperclip.copy(newstring)
print("Tekst zostal skopiowany do schowka. Zamkniecie za 5 sekund...")
time.sleep(5)
exit(0)