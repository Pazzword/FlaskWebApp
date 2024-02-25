from flask import (
    Blueprint,
    render_template,
    send_from_directory,
    url_for,
    redirect,
    session,
    flash,
    request,
)
import os

views = Blueprint("views", __name__)

main_bio = """
Abu Pashaev, born on June 9, 1966, in the village of Chechen-Aul, Chechen-Ingush ASSR, initiated his artistic journey at an early age. Following the completion of his secondary education, he served as an instructor in drawing and drafting at his hometown school. In 1984, he was conscripted into the Soviet Army.

Post his military service, he enrolled in an art school and graduated with distinction, specializing in graphic design. Embarking on a professional trajectory, he explored diverse organizational roles, honing his artistic style, and eventually establishing himself as a freelance artist. Pashaev sought guidance from esteemed artists in the Chechen Republic, including I.N. Petrov, B.G. Radchenko, V.S. Grigoriev, among others.

In 1997, he earned his degree in art and graphic design from Chechen State Pedagogical Institute, obtaining certification as an artist. Concurrently, in the early 1980s, he delved into Eastern martial arts, coupled with a profound interest in philosophy.

By 1990, Pashaev had completed Ushu instructor courses in the "Gymnastics" section, securing diplomas as a judge and instructor. Distinctively, he crafted his own style, "Wind," amalgamating elements from the jaguar and hawk within the framework of the "Hung Gar" style.

In 1984, Pashaev unveiled a series of works titled "You Don't Know How Painful It Is!" primarily comprised of graphic pieces utilizing 3 to 7 colors. Functioning as a graphic artist, many of Pashaev's creations depict a intricate inner world, bearing titles like "Scream," "Pain," "Apocalypse," "The Reverse Side of the Day," "Flickering Shadow of the Wind," "You Don't Know How Painful It Is," and "Requiem for Mozart." These pieces serve as monologues, dialogues, and reflections on self.

For Pashaev, art metamorphosed into an expression of pain and sorrow. His works exude a cold and desolate ambiance – lonely moths navigating towards light, confronting imminent demise; a body mourning the soul; a mother's visage marked by sorrow; an unborn child destined to comprehend evil and embrace goodness. His figures, weathered by life, embody solitude.

In his works, A. Pashaev communicates succinctly, yet behind his silence lies a depth of emotions and talent. The uniqueness of each piece demands substantial effort and considerable creative tension. Pashaev's creations encapsulate a process of self-discovery.

Abu Pashaev's inaugural solo exhibition in 1992 at Chechen State Pedagogical Institute, titled "Atomic Heart of My Mom," drew significant attention due to its distinctive nomenclature.
"""
bio_gallery = """

Participation in Exhibitions:
1992: Solo exhibition "Atomic Heart of My Mom," Grozny.

1993: First exhibition "Premonition of the Civil War," Grozny.

1996: Solo exhibition "Silent Protest Against Violence," Chechen-Aul.

1997: Solo exhibition "Wounded Flowers," Chechen-Aul.

1993: Solo exhibition "The Face of War," Nazran.

2003: Solo exhibition "The Face of War," Czech Republic, Prague.

2004: Reporting exhibition "Optimistic Reflection of the Past," Grozny.

2007: Regional exhibition "Peace to the Caucasus," Grozny.

2008: Zonal exhibition "Sochi - 2008," Sochi.

2009: Joint exhibition of Chechen artists at the State Duma, Moscow.

2011: Joint exhibition of artists from the Chechen Republic, City Duma, Saratov.

2011: Exhibition "Apotheosis of History," National Museum of the Chechen Republic (with Merited Artist of the Chechen Republic V.V. Zauraev), Grozny.

2011: Exhibition-competition "The Scream in Art," Maykop.

2012: Zonal exhibition, Rostov-on-Don.

2013: Participation in the VIII International Art Symposium "Tales of Love" (presentation of 2 works), Yelabuga.

2013: Exhibition-competition "Hand in Art," Maykop.

2013: XI Regional Exhibition "Southern Russia," Grozny.
All-Russian exhibition, Moscow. Honorary diploma from the Ministry of Russia.
"""
about = """Структура HTML:
Ваш HTML-код использует базовый шаблон с использованием Flask-шаблонизатора. Это обеспечивает удобство в поддержке и масштабировании вашего веб-приложения. 
Шаблон включает в себя основные элементы, такие как навигационное меню, контейнер для контента и подключение внешних библиотек, таких как Bootstrap и Font Awesome.

Навигационное меню:
Навигационное меню включает в себя четыре пункта - "Главная", "Биография", "Галерея" и "Контакты". Эти пункты предоставляют ссылки на различные разделы вашего веб-сайта. 
На мобильных устройствах навигационное меню можно скрывать и разворачивать с помощью кнопки-бургера.

Основной контент:
Основной контент размещен в блоке {% block content %}{% endblock %}. Это место, где будет вставляться уникальный контент для каждой страницы, 
расширяющей базовый шаблон. Ваш пример страницы "Главная" содержит заголовок и изображение.

Изображение:
Для вставки изображения на страницу "Главная" вы используете тег <img>. Важно убедиться, что изображение "mount.jpg" расположено в правильной директории, 
и путь к нему указан верно.

Статические файлы и скрипты:
Вы подключаете статические файлы, такие как CSS и JavaScript, для Bootstrap и Font Awesome, обеспечивая правильное оформление и интерактивность вашего веб-сайта. 
Также включен собственный скрипт "index.js".

Flask-роутинг:
В вашем Flask-приложении определен маршрут для домашней страницы ("/"), который рендерит шаблон "home.html". Это означает, 
что содержимое "home.html" будет отображаться, когда пользователь посещает главную страницу.

Этот код предоставляет основу для создания различных страниц и разделов вашего веб-сайта. Вы можете расширить его, добавляя новые страницы, контент и функциональность. 
Например, вы можете создать отдельные HTML-шаблоны для страниц "Биография", "Галерея" и "Контакты", реализовать логику обработки форм на странице "Контакты" 
с использованием Flask и т.д."""
bio1 = """Abu Pashaev, born in 1966 in Chechen-Aul, is a distinguished artist whose life journey shapes 
his profound creations. From serving in the Soviet Army to graduating in graphic design, Pashaev's diverse 
experiences manifest in his artwork. Seeking guidance from renowned Chechen artists and integrating martial arts philosophy, 
he crafted his style, "Wind." His graphic series, like "You Don't Know How Painful It Is!," explores inner worlds 
with titles such as "Scream" and "Apocalypse." Pashaev's works express universal themes of pain, solitude, and the human condition, 
showcasing his ability to convey deep emotions through a meticulous artistic process. His inaugural exhibition, 
"Atomic Heart of My Mom" (1992), marked the beginning of a significant artistic journey. Abu Pashaev emerges as an artist 
whose profound expressions resonate with the complexities of human existence."""


@views.route("/")
def home():
    return render_template("home.html", mod=about)


@views.route("/bio")
def bio():
    return render_template("bio.html", text=main_bio, bio=bio1)


@views.route("/view_image/<filename>")
def view_image(filename):
    path = os.path.join("static", "larger_images", filename)
    print("Trying to serve image from path:", path)
    return send_from_directory("static/larger_images", filename)


@views.route("/gallery")
def gallery():
    gallery_images = ["blue.jpg", "yellow.jpg", "bridge.jpg"]
    return render_template("gallery.html", gallery_images=gallery_images)


@views.route("/contacts")
def contacts():
    return render_template("contacts.html")


@views.route("/lang/<lang>")
def set_language(lang):
    session["lang"] = lang
    flash(_("Your changes have been saved."))
    referrer = request.referrer or url_for("views.home")
    return redirect(f"{referrer}?lang={lang}")
