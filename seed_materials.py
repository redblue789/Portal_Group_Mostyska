import os
import django

# Налаштування оточення Django (замініть 'Portal.settings' на вашу назву, якщо вона відрізняється)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portal.settings')
django.setup()

from django.contrib.auth.models import User
from materials.models import Material

def run():
    # Отримуємо першого користувача або створюємо тестового адміна
    user = User.objects.filter(is_superuser=True).first()
    if not user:
        user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

    materials_data = [
        # --- 1-3: YouTube Відео ---
        {
            "title": "Основи Python для початківців",
            "description": "Чудовий вступний курс з основ синтаксису Python.",
            "material_type": "youtube",
            "external_link": "https://www.youtube.com/watch?v=rfscVs0vvhw",
        },
        {
            "title": "Урок з Django Web Framework",
            "description": "Повне практичне керівництво зі створення веб-додатків на Django.",
            "material_type": "youtube",
            "external_link": "https://www.youtube.com/watch?v=F5mRW0jo-U4",
        },
        {
            "title": "Швидкий курс з Git та GitHub",
            "description": "Як працювати з гілками, робити push, pull та вирішувати конфлікти.",
            "material_type": "youtube",
            "external_link": "https://www.youtube.com/watch?v=RGOj5yH7evE",
        },

        # --- 4-6: Зовнішні корисні посилання ---
        {
            "title": "Офіційна документація Django",
            "description": "Головне джерело відповідей на всі питання по роботі з Django.",
            "material_type": "link",
            "external_link": "https://docs.djangoproject.com/en/stable/",
        },
        {
            "title": "Шпора з маркдауну (Markdown Cheat Sheet)",
            "description": "Зручний довідник із синтаксису Markdown для оформлення README.md.",
            "material_type": "link",
            "external_link": "https://www.markdownguide.org/cheat-sheet/",
        },
        {
            "title": "Інтерактивний тренажер SQL",
            "description": "Платформа для практики написання складних SQL-запитів у браузері.",
            "material_type": "link",
            "external_link": "https://www.w3schools.com/sql/",
        },

        # --- 7-8: Зображення (з онлайн-заглушками) ---
        {
            "title": "Схема архітектури Django (MTV Pattern)",
            "description": "Наочна схема взаємодії Model, Template та View у Django.",
            "material_type": "image",
            "external_link": "https://picsum.photos/800/400?random=1",
        },
        {
            "title": "Розклад сесії та заліків",
            "description": "Попередній графік складання підсумкових робіт за поточний семестр.",
            "material_type": "image",
            "external_link": "https://picsum.photos/800/400?random=2",
        },

        # --- 9-10: Файли / Документи ---
        {
            "title": "Методичка з виконання курсової роботи",
            "description": "Вимоги до оформлення, структури та змісту підсумкового проекту.",
            "material_type": "file",
            "external_link": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        },
        {
            "title": "Приклад оформлення технічного завдання (ТЗ)",
            "description": "Зразок правильно складеного ТЗ для командного IT-проєкту.",
            "material_type": "file",
            "external_link": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        },
    ]

    for item in materials_data:
        Material.objects.create(
            title=item["title"],
            description=item["description"],
            material_type=item["material_type"],
            external_link=item["external_link"],
            author=user
        )

    print("Успішно створено 10 матеріалів!")

if __name__ == '__main__':
    run()