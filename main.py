import random

rare, superRare, epic, mythic, legendary = 0, 0, 0, 0, 0
count = 1_000_000
for x in range(count):
    chance = random.randint(1, 100)
    if 0 < chance <= 50:
        rare += 1
    if 50 < chance <= 78:
        superRare += 1
    if 78 < chance <= 93:
        epic += 1
    if 93 < chance <= 98:
        mythic += 1
    if 98 < chance <= 100:
        legendary += 1

print(f"Rare: {rare}, {round(100*rare/count)}%")
print(f"Super Rare: {superRare}, {round(100*superRare/count)}%")
print(f"Epic: {epic}, {round(100*epic/count)}%")
print(f"Mythic: {mythic}, {round(100*mythic/count)}%")
print(f"Legendary: {legendary}, {round(100*legendary/count)}%")
