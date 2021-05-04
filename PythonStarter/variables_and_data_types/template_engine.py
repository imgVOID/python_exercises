# Дополнительное задание для знакомых с HTML студентов:
# 1. Узнайте, что такое шаблонизатор.
# 2. Пофантазируйте на тему создания собственного шаблонизатора.
# Пример выполнения задания:
title = "title"
head_section = """
  <head>
    <{}>{}</{}>
  </head>
""".format(title, "Template engine test", title)

div = "div"
h = "h3"
body_section = """
  <body>
    <{}>
      <{}>{}</{}>
    </{}>
  </body>
""".format(div, h, "I've made a template engine!", h, div)

print("<html>", head_section, body_section, "</html>", sep="")
