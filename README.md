# Experto en "Attention Is All You Need"

Asistente conversacional basado en el paper *"Attention Is All You Need"* utilizando **Google Gemini (google-genai)** y una interfaz web con **Gradio**.

El sistema permite hacer preguntas sobre el contenido del paper y obtener respuestas **estrictamente fundamentadas en el documento**.

---

## Características

* Lectura automática de PDF (`pypdf`)
* Integración con modelos Gemini (`google-genai`)
* Interfaz conversacional con Gradio
* Respuestas restringidas al contenido del documento
* Soporte para múltiples turnos (chat con historial)
* Streaming de respuestas en tiempo real
* Citas textuales del paper que respaldan cada respuesta (Paso 6 — Opción C)

---

## Arquitectura

El sistema sigue este flujo:

1. **Extracción de texto del PDF**
2. **Construcción de system prompt** con el contenido del paper
3. **Recepción de preguntas del usuario**
4. **Conversión del historial al formato Gemini**
5. **Generación de respuesta vía API**
6. **Renderizado en interfaz Gradio**

---

## Estructura del proyecto

```bash
.
 Report.ipynb          # Notebook principal del proyecto
 set_kernel.py         # Script para asociar el notebook al kernel correcto
 .env                  # Variables de entorno (API key, modelo)
 attention_is_all_you_need.pdf
 requirements.txt
 README.md
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/SSloan07/Report3ArtificialInteligence.git
cd Report3ArtificialInteligence
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Registrar el entorno como kernel

```bash
python -m ipykernel install --user --name=report3env --display-name "Python (report3env)"
```

### 5. Asociar el notebook al kernel correcto

```bash
python set_kernel.py Report.ipynb report3env "Python (report3env)"
```

> **Importante:** instalar las dependencias con `requirements.txt` no garantiza por sí solo que el notebook use ese mismo entorno.
> Por eso se incluye `set_kernel.py`, que permite asociar `Report.ipynb` al kernel correcto (`report3env`) y asegurar que el proyecto se ejecute con las librerías instaladas en el entorno virtual.

---

## Variables de entorno

Crear archivo `.env`:

```env
API_KEY=tu_api_key_de_gemini
MODELO_ID=gemini-2.5-flash-lite
```

---

## Ejecución

Ejecute cada celda en orden. Al llegar a la celda de Gradio del **Paso 4**, la interfaz base se lanza en `http://localhost:8083`. Al ejecutar la celda del **Paso 6**, la interfaz con citas se lanza en `http://localhost:8084`. En ambas puede hacer preguntas propias o usar los ejemplos pre-cargados.

---

## Ejemplo de uso

Preguntas sugeridas:

* ¿Qué es el mecanismo de Multi-Head Attention?
* ¿Cuáles fueron los resultados en tareas de traducción?
* Explica el concepto de Positional Encoding.

---

## Paso 5 — Prueba y Reflexión

Con la interfaz corriendo en `http://localhost:8083` se probaron las seis preguntas propuestas en el ejercicio. Los resultados fueron los siguientes:

| Pregunta | Resultado |
|---|---|
| ¿Cuál es la arquitectura principal propuesta en el paper? | Correcto — identificó el Transformer con encoder-decoder de N=6 capas |
| ¿Qué es el mecanismo de atención? | Correcto — describió Scaled Dot-Product Attention con la formula de suma ponderada |
| ¿Cuántas capas tiene el encoder del modelo base? | Correcto — extrajo el dato exacto: N=6 |
| ¿Quiénes son los autores del paper? | Correcto — listó los ocho autores sin omitir ninguno |
| ¿Cuál es el resultado en WMT 2014 English-to-German? | Correcto — reportó 28.4 BLEU del modelo grande |
| ¿Qué es GPT-4? (pregunta trampa) | Correcto — respondió que la información no está en el documento |

La pregunta trampa confirmó que el system prompt funciona como barrera de contención: el modelo no recurrió a su conocimiento general.

**Reflexión sobre las limitaciones del enfoque:**

1. **Limitación principal:** el sistema envía el documento completo en cada consulta. Con un paper de 15 páginas (~39,000 caracteres) esto funciona, pero no escalaría a documentos de cientos de páginas sin superar el límite del context window o disparar los costos.

2. **Por qué existe RAG:** en lugar de inyectar el documento completo, RAG recupera únicamente los fragmentos relevantes para cada pregunta. Eso resuelve el problema de escalabilidad y reduce el consumo de tokens por consulta.

3. **Filtración de conocimiento externo:** el modelo fue entrenado con información sobre el paper de Transformers, por lo que en teoría podría responder desde su entrenamiento en lugar del documento. Para verificar que está usando el texto inyectado y no su conocimiento previo se puede modificar el paper antes de cargarlo y comprobar que el modelo refleja los cambios.

---

## Paso 6 — Mejora: Citas del documento (Opción C)

Se implementó la **Opción C** del ejercicio adicional: el system prompt se modificó para que el modelo incluya siempre una cita textual del paper que respalde su respuesta.

**Ejemplo de respuesta con la mejora:**

> **Respuesta:** El encoder del modelo base tiene 6 capas idénticas apiladas.
>
> **Cita del paper:** *"The encoder is composed of a stack of N = 6 identical layers."*

La mejora se implementó con dos funciones adicionales (`build_system_prompt_with_citations` y `chat_with_citations`) y una segunda interfaz Gradio que corre en el puerto `8084`, sin modificar la interfaz base del Paso 4.

---

## Consideraciones técnicas

### 1. Consumo de tokens

El sistema envía el documento completo en cada consulta, lo que puede:

* aumentar costos
* generar errores de cuota (`429 RESOURCE_EXHAUSTED`)

### 2. Optimización recomendada

* Reducir `max_output_tokens`
* Limitar historial de conversación
* Implementar **chunking + retrieval (RAG)**

---

## Problemas comunes

### Error: `429 RESOURCE_EXHAUSTED`

Solución:

* Esperar unos minutos
* Reducir tamaño del contexto
* Verificar cuota en Google AI Studio

---

### Error: `Input should be a valid string`

Causa:

* Gradio envía contenido estructurado

Solución:

* Normalizar `message` y `history` antes de enviarlos al modelo

---

## Tecnologías usadas

* Python
* Gradio
* Google Gemini API (`google-genai`)
* PyPDF
* dotenv

---

## Autores

* Hever Andre Alfonso Jimenez
* Simón Sloan García Villa
* Moíses Arturo Vergara Garcez

Estudiantes de Ingeniería de Sistemas
Proyecto académico – Inteligencia Artificial

---

## Licencia

Uso académico y educativo.
