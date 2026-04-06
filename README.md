# 🐍 Fundamentos de Python para Principiantes II

---

## 📑 Índice

- [🐍 Fundamentos de Python para Principiantes II](#-fundamentos-de-python-para-principiantes-ii)
  - [📑 Índice](#-índice)
  - [🔹 ¿Para qué usamos Clases en Python?](#-para-qué-usamos-clases-en-python)
    - [⚙️ Sintaxis](#️-sintaxis)
    - [💻 Ejemplo: Clase Coche](#-ejemplo-clase-coche)
  - [🔹 ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#-qué-método-se-ejecuta-automáticamente-cuando-se-crea-una-instancia-de-una-clase)
    - [**init**()](#init)
    - [⚙️ Sintaxis](#️-sintaxis-1)
  - [🔹 ¿Cuáles son los tres verbos de API?](#-cuáles-son-los-tres-verbos-de-api)
  - [🔹 ¿Es MongoDB una base de datos SQL o NoSQL?](#-es-mongodb-una-base-de-datos-sql-o-nosql)
    - [💻 Ejemplo](#-ejemplo)
  - [🔹 ¿Qué es una API?](#-qué-es-una-api)
    - [📡 Protocolos de API](#-protocolos-de-api)
    - [Ventajas:](#ventajas)
    - [💻 Ejemplo](#-ejemplo-1)
    - [Diferencia entre API y Aplicación Web](#diferencia-entre-api-y-aplicación-web)
  - [🔹 ¿Qué es Postman?](#-qué-es-postman)
    - [🧪 ¿Cómo funciona Postman?](#-cómo-funciona-postman)
    - [🚀 Ventajas de Postman](#-ventajas-de-postman)
  - [🔹 ¿Qué es el polimorfismo?](#-qué-es-el-polimorfismo)
    - [💻 Tipos de poliformismo:](#-tipos-de-poliformismo)
      - [1. Polimorfismo por métodos con el mismo nombre (duck typing)](#1-polimorfismo-por-métodos-con-el-mismo-nombre-duck-typing)
      - [2. Polimorfismo con herencia (sobrescritura de métodos - Overriding)](#2-polimorfismo-con-herencia-sobrescritura-de-métodos---overriding)
      - [3. Polimorfismo con funciones y operadores](#3-polimorfismo-con-funciones-y-operadores)
      - [💡 Para que no olvides](#-para-que-no-olvides)
  - [🔹 ¿Qué es un método dunder?](#-qué-es-un-método-dunder)
  - [🔹 ¿Qué es un decorador de python?](#-qué-es-un-decorador-de-python)
    - [💻 Ejemplo](#-ejemplo-2)
      - [Salida:](#salida)

---

## 🔹 ¿Para qué usamos Clases en Python?

Una clase es una plantilla que define cómo se creará un objeto. Los objetos son instancias de una clase. Las clases son una de las características más poderosas de Python y son fundamentales para la programación orientada a objetos (POO).
Quiere decir, que las clases sirven para crear nuestros propios tipos de datos, a partir de ese molde o plantilla podemos crear objetos, de esa manera organizamos mejor el código porque podemos agrupar funciones, variables, etc., dentro de una clase que representa una idea concreta con atributos (características) y métodos (acciones). También nos permite modelar problemas complejos, cuando el proyecto crece, las clases permiten dividirlo en piezas manejables. Podemos crear nuevas clases basadas en otras, reutilizando y extendiendo funcionalidades.
Para crear una clase usamos la palabra reservada class y siempre debe ir en minúsculas, seguido va el nombre de la clase. Te explico con más detalle en este gráfico.

### ⚙️ Sintaxis

![visual](/img/clases.png)

### 💻 Ejemplo: Clase Coche

```python
class Coche:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def Arrancar(self):
        print("El coche está arrancando")


c1 = Coche("Dacia", "Gris", 200)
c2 = Coche("Audi", "Rojo", 250)
```

## 🔹 ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

### **init**()

Se llama automáticamente cuando se crea una nueva instancia de una clase. Su función principal es inicializar los atributos del objeto que creamos.
Características:

- No puede retomar datos.
- Puede recibir parámetros que se utilizan normalmente para iniciar atributos.
- Es un método opcional, de todos modos es muy común declararlo.

### ⚙️ Sintaxis

![visual](/img/init.png)

## 🔹 ¿Cuáles son los tres verbos de API?

Obtener información(GET), pedir datos.
Crear un nuevo recurso(POST),  
Actualizar un recurso existente (PUT o PATCH), aunque también algunos incluyen DELETE.

Los verbos (GET, POST, PUT, DELETE) son acciones que tú usas para hablar con una API, y la API es la que se comunica con el servidor.

![visual](/img/verbos-api.png)

---

## 🔹 ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL que funciona bien dentro de ese ecosistema, pero también está diseñada para interactuar con otros tipos de sistemas de gestión de bases de datos a través de varias herramientas y conectores de integración de datos. Disponible para los sistemas operativos Windows, GNU/Linux, OS X y Solaris

MongoDB almacena datos en documentos flexibles similares a JSON, por lo que los campos pueden variar entre documentos y la estructura de datos puede cambiar con el tiempo.
A diferencia de bases de datos tradicionales (como SQL), MongoDB:
👉 No usa tablas
👉 Usa documentos tipo JSON

### 💻 Ejemplo

![Comprension](/img/mongodb.png)

MongoDB es un recurso muy interesante para desarrolladores pero no es perfecto. Por ejemplo:
VENTAJAS
• Validación de documentos
• Motores de almacenamiento integrado
• Menor tiempo de recuperación ante fallos

DESVENTAJAS
• No es una solución adecuada para aplicaciones con transacciones complejas
• No tiene un reemplazo para las soluciones de herencia
• Aún es una tecnología joven

---

## 🔹 ¿Qué es una API?

API significa: Application Programming Interface
Una API, o interfaz de programación de aplicaciones, es un conjunto de reglas y protocolos que permite a las aplicaciones intercambiar datos, realizar acciones e interactuar de una manera bien documentada.
En pocas palabras, es un intermediario que permite que dos programas se comuniquen.

### 📡 Protocolos de API

Son formas o reglas que usan las APIs para que los programas se comuniquen entre sí.
Los principales:

**RPC:** Permite que un programa pida algo a otro como si estuviera en su propio sistema.
(cliente pide → servidor responde)

**SOAP:** Usa reglas estrictas y mensajes en XML para intercambiar datos.
✔️ Muy organizado
❌ Más complicado

**REST:** El más usado hoy. Funciona con HTTP y trata los datos como recursos (URLs).
✔️ Más simple y rápido
✔️ Fácil de usar

**GraphQL:** El cliente pide solo los datos que necesita.
✔️ Más eficiente
✔️ Ideal para apps modernas

### Ventajas:

**Flexibilidad**: permiten que los sistemas intercambien datos sin complicaciones.
**Más alcance**: la información puede llegar a distintas apps o usuarios al mismo tiempo.
**Personalización**: se pueden adaptar para ofrecer experiencias diferentes según lo que necesite cada usuario.
**Eficiencia**: automatizan procesos, así que todo funciona más rápido y con menos trabajo manual.
**Adaptabilidad**: es más fácil hacer cambios o actualizar sistemas sin romper todo.

### 💻 Ejemplo

Algunos de los ejemplos de API más conocidas:

📍 **Google Maps:** gracias a los estándares aplicados por Google, la mayoría de los sitios web pueden usar las APIs de Google Maps para integrar mapas.
✈️ **Skyscanner:** esta plataforma de metabúsqueda facilita que viajeros puedan encontrar mejores tarifas para sus vuelos. Además, proporciona una API para aliados comerciales compatible con XML y JSON para el intercambio de datos.
🌦️ **Weather API:** un proveedor de servicios de geolocalización e información meteorológica con diversas APIs que van desde el pronóstico del clima, hasta búsquedas de zonas horarias, astronomía y más.

### Diferencia entre API y Aplicación Web

| Aspecto                  | API 🧩                                       | Aplicación web 🌐                                        |
| ------------------------ | -------------------------------------------- | -------------------------------------------------------- |
| **Propósito**            | Permite que programas se comuniquen entre sí | Permite a los usuarios usar funciones desde un navegador |
| **Interfaz de usuario**  | ❌ No tiene interfaz                         | ✅ Tiene interfaz visual (pantallas, botones, etc.)      |
| **Interacción**          | Entre sistemas (automática / programática)   | Entre persona y sistema (uso humano)                     |
| **Intercambio de datos** | Se centra en enviar y recibir datos          | Usa datos y además los muestra de forma visual           |
| **Usuarios**             | Desarrolladores                              | Usuarios finales                                         |

**Resumen:**

- **API** → conecta sistemas
- **Aplicación web** → la usa el usuario

---

## 🔹 ¿Qué es Postman?

Postman es una herramienta de software muy popular utilizada para probar, documentar y compartir APIs (Interfaces de Programación de Aplicaciones).
Permite enviar peticiones a servidores web (como GET, POST, PUT, DELETE) y ver las respuestas sin necesidad de escribir código.

![Visualmente](/img/postman.png)

#### 🧪 ¿Cómo funciona Postman?

Postman funciona como una herramienta con interfaz visual (GUI) que permite probar APIs enviando solicitudes y viendo las respuestas.

**Enviar solicitudes** 📤
👉 Puedes hacer peticiones a una API (GET, POST, PUT, DELETE) para pedir o enviar datos.
**Gestionar entornos** ⚙️
👉 Puedes cambiar entre diferentes ambientes como desarrollo, pruebas o producción.
**Organizar solicitudes** 📁
👉 Permite agrupar peticiones en colecciones para tener todo ordenado.
**Pruebas automáticas** 🤖
👉 Puedes verificar automáticamente si una API funciona correctamente.
**Documentación** 📝
👉 Genera información automática para entender cómo usar la API.

![Visualmente](/img/post_postman.jpg)

#### 🚀 Ventajas de Postman

**Fácil de usar** 👌
👉 Tiene una interfaz gráfica simple e intuitiva.
**Compatible con muchas APIs** 🔗
👉 Funciona con HTTP, REST, SOAP, GraphQL, etc.
**Todo en uno** 🧰
👉 Permite diseñar, probar y documentar APIs en un solo lugar.
**Trabajo en equipo** 👥
👉 Facilita compartir información y colecciones con otros desarrolladores.
**Integraciones** 🔌
👉 Se conecta con herramientas como GitHub o Jenkins.
**Automatización** 🤖
👉 Permite crear scripts para pruebas y tareas automáticas.
**Organización** 📁
👉 Puedes agrupar solicitudes en colecciones para mantener todo ordenado.

---

## 🔹 ¿Qué es el polimorfismo?

El polimorfismo es uno de los principios fundamentales de la Programación Orientada a Objetos (POO).
La palabra proviene del griego y significa "muchas formas" (poly = muchas, morph = forma).

En programación, el polimorfismo permite que un mismo objeto, método o función se comporte de diferentes maneras según el contexto en el que se utilice.
Una misma acción → diferentes resultados dependiendo del contexto.

![Visualmente](/img/poliformismo.png)
El mismo nombre ("reproducir") hace cosas diferentes según el tipo de objeto con el que trabajas.

### 💻 Tipos de poliformismo:

#### 1. Polimorfismo por métodos con el mismo nombre (duck typing)

Distintas clases pueden tener un método con el mismo nombre, pero cada una lo implementa a su manera.

```python
class Perro:
    def hablar(self):
        return "Guauu"

class Gato:
    def hablar(self):
        return "Miauu"

for animal in [Perro(), Gato()]:
    print (animal.hablar())
```

#### 2. Polimorfismo con herencia (sobrescritura de métodos - Overriding)

Una clase hija puede redefinir un método de la clase padre.
Desinstalar

```python
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

```

#### 3. Polimorfismo con funciones y operadores

Python aplica polimorfismo incluso en funciones nativas.

```python
len("Hola") #Resultado 4
len(1, 2, 3) #Resultado 3

"Hola" + "mundo"  #Concatenación
3 + 5   #Suma
```

#### 💡 Para que no olvides

![Visualmente](/img/cuadros_poli.png)

---

## 🔹 ¿Qué es un método dunder?

Un método dunder (de “double underscore”) en Python es un método especial que tiene dos guiones bajos antes y después del nombre.
Los métodos dunder son clave para el polimorfismo porque permiten que los mismos operadores o funciones funcionen distinto según el objeto.

💻 Ejemplo:
**init**, **str**, **len**

Sirven para definir comportamientos especiales de los objetos y cómo interactúan con Python.
Es decir, permiten que las clases:
• Se inicialicen
• Se impriman bonito
• Usen operadores como +
• Respondan a funciones como len()

1. **init** (constructor): Se ejecuta al crear un objeto.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
```

2. **str** (representación en texto): Define como se muestra el texto.

```python
class Persona:
    def __str__(self):
        return "Soy una persona"
```

---

## 🔹 ¿Qué es un decorador de python?

Un decorador en Python es una función que envuelve otra función (o clase) para modificar o ampliar su comportamiento sin cambiar su código original.

Es como ponerle un “extra” a una función sin cambiarla por dentro.
👉 Como ponerle una funda a un móvil: el móvil es el mismo, pero ahora tiene algo extra.

![Visualmente](/img/decorador.png)

### 💻 Ejemplo

```python
def decorador_suma(func):
    def envolvente(a, b):
        print(f"Sumando {a} + {b}")
        resultado = func(a, b)
        print(f"Resultado de la suma: {resultado}")
        return resultado
    return envolvente


@decorador_suma
def suma(a, b):
    return a + b

#Llama a la función suma y el resultado es almacenado en la variable resultado
resultado = suma(3, 5)
```

#### Salida:

Sumando 3 + 5
Resultado de la suma: 8
