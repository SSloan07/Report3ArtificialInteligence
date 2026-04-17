# 📄 Experto en "Attention Is All You Need"

Asistente conversacional basado en el paper *"Attention Is All You Need"* utilizando **Google Gemini (google-genai)** y una interfaz web con **Gradio**.

El sistema permite hacer preguntas sobre el contenido del paper y obtener respuestas **estrictamente fundamentadas en el documento**.

---

## 🚀 Características

* 📚 Lectura automática de PDF (`pypdf`)
* 🤖 Integración con modelos Gemini (`google-genai`)
* 💬 Interfaz conversacional con Gradio
* 📌 Respuestas restringidas al contenido del documento
* 🔄 Soporte para múltiples turnos (chat con historial)
* ⚡ Streaming de respuestas en tiempo real

---

## 🧠 Arquitectura

El sistema sigue este flujo:

1. **Extracción de texto del PDF**
2. **Construcción de system prompt** con el contenido del paper
3. **Recepción de preguntas del usuario**
4. **Conversión del historial al formato Gemini**
5. **Generación de respuesta vía API**
6. **Renderizado en interfaz Gradio**

---

## 📂 Estructura del proyecto

```bash
.
├── app.py                # Aplicación principal (Gradio + lógica)
├── .env                  # Variables de entorno (API key, modelo)
├── attention_is_all_you_need.pdf
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

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

## 🔑 Variables de entorno

Crear archivo `.env`:

```env
API_KEY=tu_api_key_de_gemini
MODELO_ID=gemini-1.5-flash
```

---

## ▶️ Ejecución

```bash
python app.py
```

Luego abre:

```
http://localhost:7860
```

---

## 🧪 Ejemplo de uso

Preguntas sugeridas:

* ¿Qué es el mecanismo de Multi-Head Attention?
* ¿Cuál es la arquitectura propuesta?
* ¿Qué son los Positional Encodings?

---

## ⚠️ Consideraciones técnicas

### 1. Consumo de tokens

El sistema envía el documento completo en cada consulta, lo que puede:

* aumentar costos
* generar errores de cuota (`429 RESOURCE_EXHAUSTED`)

### 2. Optimización recomendada

* Reducir `max_output_tokens`
* Limitar historial de conversación
* Implementar **chunking + retrieval (RAG)**

---

## 🐛 Problemas comunes

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

## 📈 Mejoras futuras

* 🔍 Implementación de RAG (embeddings + búsqueda semántica)
* 📊 Soporte para múltiples documentos
* 🧠 Memoria de conversación optimizada
* 🌐 Deploy en servidor público

---

## 🛠️ Tecnologías usadas

* Python
* Gradio
* Google Gemini API (`google-genai`)
* PyPDF
* dotenv

---

## 👤 Autores

Hever Alfonso 
Simón Sloan García Villa
Moíses Arturo Vergara Garcez 

Estudiantes de Ingeniería de Sistemas
Proyecto académico – Inteligencia Artificial

---

## 📜 Licencia

Uso académico y educativo.
