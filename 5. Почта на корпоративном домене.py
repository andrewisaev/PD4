user_email = input()
free_domain = ["yandex.ru", "mail.ru", "gmail.com", "yahoo.com", "rambler.ru"]


if "." not in user_email.split("@")[1]:
    print("Это вообще не почта")
elif user_email.split("@")[1] in free_domain:
    print("Это почта, она на бесплатном домене")
else:
    print("Это почта, она на корпоративном домене")

