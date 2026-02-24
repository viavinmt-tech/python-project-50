Вычислитель отличий — это консольная утилита для сравнения двух конфигурационных файлов и наглядного отображения различий между ними. Программа поддерживает форматы JSON и YAML, включая файлы с вложенной структурой данных.

Утилита анализирует содержимое файлов и показывает, какие ключи были добавлены, удалены или изменены во втором файле относительно первого. Для удобства восприятия предусмотрено три формата вывода: стилизованное дерево (stylish), плоский список изменений (plain) и структурированный JSON.

Как установить?

Чтобы установить вычислитель отличий, достаточно выполнить в терминале команду pip install hexlet-code. После завершения установки убедитесь, что всё прошло успешно, вызвав справку командой gendiff --help — вы должны увидеть описание программы и список доступных опций.

Для первого запуска подготовьте два небольших JSON-файла. Создайте файл first.json с содержимым:
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
} 
и файл second.json с содержимым:
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
Сохраните их.

Теперь выполните команду gendiff first.json second.json. Программа проанализирует оба файла и покажет, чем они отличаются. Символ "- " означает, что ключ есть только в первом файле или был удалён, символ "+" — что ключ есть только во втором файле или был добавлен, а пробел означает, что ключ присутствует в обоих файлах с одинаковым значением.

Можно попробовать и другие форматы вывода: gendiff --format plain first.json second.json покажет различия в виде плоского списка, а gendiff --format json first.json second.json выдаст структурированный результат в JSON. Все эти команды работают и с YAML-файлами.



The diff calculator is a console utility for comparing two configuration files and visually displaying the differences between them. The program supports JSON and YAML formats, including files with nested data structures.

The utility analyzes the contents of the files and shows which keys have been added, removed, or modified in the second file compared to the first. For ease of perception, there are three output formats: a stylized tree (stylish), a flat list of changes (plain), and structured JSON.

How to install?

To install the diff calculator, simply run the command pip install hexlet-code in the terminal. Once the installation is complete, verify that everything went smoothly by issuing the command gendiff --help, which should display a description of the program and a list of available options.

To get started, prepare two small JSON files. Create a file called first.json with the content:
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
and a second.json file with the content:
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
Save them.

Now run the command gendiff first.json second.json. The program will analyze both files and show you what they have in common. The "-" symbol means that the key is only in the first file or has been deleted, the "+" symbol means that the key is only in the second file or has been added, and the space symbol means that the key is present in both files with the same value.

You can also try other output formats: gendiff --format plain first.json second.json will display the differences as a flat list, while gendiff --format json first.json second.json will produce a structured result in JSON. These commands also work with YAML files.



### Hexlet tests and linter status:
[![Actions Status](https://github.com/viavinmt-tech/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/viavinmt-tech/python-project-50/actions)
[![asciicast](https://asciinema.org/a/aJFV7nfZAJKHw3Kh.svg)](https://asciinema.org/a/aJFV7nfZAJKHw3Kh)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=viavinmt-tech_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=viavinmt-tech_python-project-50)
[![asciicast](https://asciinema.org/a/IPs2DNG6xDfzRpfY.svg)](https://asciinema.org/a/IPs2DNG6xDfzRpfY)
[![asciicast](https://asciinema.org/a/9uL8jBaikKwK4vQK.svg)](https://asciinema.org/a/9uL8jBaikKwK4vQK)
[![asciicast](https://asciinema.org/a/qPjIOL5qJ12UdMLe.svg)](https://asciinema.org/a/qPjIOL5qJ12UdMLe)
