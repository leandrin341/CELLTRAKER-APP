# UroScan AI — Diagnóstico Diferencial de Calcificaciones Pélvicas

### Servicio de Urología · Hospital Italiano de Buenos Aires
**Congreso I+I+I 2026 · Hackathon Biociencias 2026**  
*Desafío clínico:* **Diferenciación entre Litos Ureterales Distales vs Flebolitos Pélvicos en Tomografía Computada sin contraste.**

---

## 1. Planteamiento Clínico del Problema

La **tomografía computada (TC) sin contraste** constituye el estándar de referencia para evaluar pacientes con sospecha de urolitiasis. Sin embargo, en el sector distal del uréter (estrecho pélvico y segmento yuxtavesical), es frecuente encontrar pequeñas calcificaciones cuya diferenciación anatómica es altamente desafiante:

1. **Litos Ureterales Distales:**
   - Ubicados dentro de la luz del uréter.
   - Producen riesgo de uropatía obstructiva, cólico renal, deterioro de función renal o sepsis urinaria.
   - Requieren seguimiento activo, Tratamiento Expulsivo Médico (MET con alfa-bloqueantes) o intervención quirúrgica (Ureteroscopia / URS).
   - **Signos radiológicos característicos:** Signo del halo o rodete de partes blandas (*Soft-Tissue Rim Sign*), dilatación ureteral proximal, hidronefrosis ipsilateral, estriación perirrenal/periureteral.

2. **Flebolitos Pélvicos:**
   - Calcificaciones venosas benignas del plexo venoso pélvico.
   - No generan obstrucción urinaria ni requieren intervención ni tratamiento.
   - **Signos radiológicos característicos:** Signo de la cola de cometa (*Comet-Tail Sign*), morfología redondeada u oval con lucencia central, ausencia de dilatación del sistema colector.

*Objetivo de la herramienta:* Asistir la toma de decisión médica mediante un modelo explicable que combina la **plantilla clínica del paciente** y el **análisis de la imagen tomográfica por visión computacional / radiomics**, entregando probabilidades continuas y desglose de criterios.

---

## 2. Características de la Interfaz (Diseño Colony In Vitro Modo Claro)

La aplicación implementa un diseño de grado médico institucional siguiendo la identidad visual y paleta de **Colony In Vitro en modo claro**:
- **Paleta de Color:** Fondos limpios en Slate (`#F8FAFC`, `#FFFFFF`), acentos en Cyan (`#0891B2`, `#0E7490`) y Teal, bordes sutiles en `#E2E8F0`, y badges en tonalidades suaves (Cyan, Emerald, Amber).
- **Tipografía:** `Inter` para jerarquías y textos clínicos, junto a `JetBrains Mono` para identificadores de historia clínica, densidades en unidades Hounsfield (HU), porcentajes y metadatos.
- **Iconografía Profesional:** 100% vectores SVG limpios y médicos. **Sin uso de emojis**, garantizando un estándar hospitalario estricto.
- **Estructura en Doble Panel:**
  - **Panel Izquierdo (Plantilla Clínica del Paciente):** Historia clínica, edad, sexo, caracterización del dolor lumbosacro/flanco (cólico renal unilateral), tiempo de evolución, hematuria (micro/macro), antecedentes litiásicos, función renal (creatinina) y sedimento urinario. Permite actualización dinámica en tiempo real de la probabilidad clínica pre-test.
  - **Panel Derecho (Estudio Tomográfico & Análisis IA):**
    - Carga interactiva drag-and-drop o explorador de archivos (imágenes de cortes axiales tomográficos pélvicos).
    - Selector rápido de cortes de muestra reales del caso (Lito con Rim Sign, Flebolito venoso con cola de cometa, Scout View pélvico y Control de catéter doble J).
    - Visor médico interactivo con zoom progresivo, ajuste de ventana tomográfica (*Windowing:* Ósea/Cálculos, Tejidos Blandos, Filtro Halo radiómico), y retícula de Región de Interés (ROI) con sonda de medición en unidades Hounsfield (HU).
    - Motor de análisis asistido por IA que calcula la probabilidad diferencial calibrada (Lito vs Flebolito).
    - Desglose explicable de los 5 criterios radiológico-clínicos clave.
    - Conducta terapéutica urológica sugerida.
    - Módulo de generación de Informe Clínico Estandarizado (con soporte de impresión y exportación a PDF).

---

## 3. Instrucciones de Ejecución

### Opción A — Ejecutar con Servidor Local (Recomendado)
```bash
# Con Python
python server.py
# O con Node.js
npm run dev
```
La aplicación se abrirá automáticamente en tu navegador predeterminado en `http://localhost:3000`.

### Opción B — Apertura Directa
Simplemente abre el archivo `index.html` en cualquier navegador web moderno (Google Chrome, Microsoft Edge, Firefox, Safari).

---

## 4. Rama Git
- Rama: `feature/urologia-lito-vs-flebolito`
