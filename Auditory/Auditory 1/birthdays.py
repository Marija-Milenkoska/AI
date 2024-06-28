"""Во оваа задача се чуваат родендените на пријатели, кои треба да се пронајдат според имињата на пријателите.
 Креирајте речник (dictionary) со имиња и родендени. Потоа, додадете функционалност со која од стандарден влез
се чита име на пријател, и вратете го неговиот роденден (односно испечатете го на стандарден излез)."""

bithdays = {
"Ana": "13/03/1999",
    "Marija": "17/01/1991",
    "Stefan": "11/08/1896",
    "Aleksandar": "25/10/1992"
}

print ("Welcome to the birthday dictionary. We know these birthdays:")
print("\n".join(bithdays.keys()))
print("Who's birthday would you like to know?")
user = input()
bithday = bithdays[user]
print(f"{user}'s birthday is on {bithday}")
