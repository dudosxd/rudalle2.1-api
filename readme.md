# Неофициальный API для Kandinsky v2.1

## Python
1. Положите файл из py/api.py рядом с вашим
2. Импортируйте его
```
from api import generate as kandinsky # api поменяйте на название файла `api.py` без `.py` в конце
```
3. Используйте
```
kandinsky('Кот','./') # Промпт, путь
```
4. Пример - py/example.py

## Nodejs
1. ```npm i axios```
2. Положите файл из nodejs/api.js рядом с вашим
3. Импортируйте его
```
const { generate } = require(`./api.js`); # api поменяйте на название файла `api.js`
# Или так
import generate from './api.js';
```
4. Используйте
```
await generate('Кот','./') # Промпт, путь
```
5. Пример - nodejs/example.js