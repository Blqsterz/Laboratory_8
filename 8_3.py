students = {
    "Иван": {"английский", "французский", "немецкий"},
    "Коля": {"китайский", "английский", "немецкий"},
    "Петя": {"испанский", "китайский"},
    "Катя": {"английский", "китайский"},
}

all_langs = set()
for langs in students.values():
    all_langs.update(langs)

print(f"Количество различных языков: {len(all_langs)}")
print(f"Отсортированный список: {sorted(all_langs)}")


target = "китайский"
chinese = []
for key, values in students.items():
    if target in values:
        chinese.append(key)


print(f"Студенты, знающие {target}: {chinese}")
