countries = dict(Россия = "Москва", США = "Вашингтон", Япония = "Токио", Италия = "Рим", Канада = "Оттава", Германия = "Берлин" )

print("Страны и их столицы:")
for key, value in countries.items():
    print(f"{key} - {value}")


target = "Россия"
capital = countries.get(target, "Такой страны нет в списке")
print(f"Столица страны {target}: {capital}")


print("Страны в алфавитном порядке:")
for country in sorted(countries):
    print(f"{country} - {countries[country]}")