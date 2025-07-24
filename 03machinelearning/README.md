# Módulo de Machine Learning
## SIC AI 2025 - Junio

### Descripción

Este módulo contiene material completo de aprendizaje de Machine Learning, diseñado para proporcionar una comprensión integral de los conceptos fundamentales y aplicaciones prácticas de la inteligencia artificial y el aprendizaje automático.

### Contenido del Curso

#### Estructura Principal

```
03machinelearning/
├── clase_06.ipynb         # Introducción a ML con Scikit-learn
├── clase_07.ipynb         # Preprocesamiento de datos
├── clase_08.ipynb         # Algoritmos de clasificación
├── clase_09.ipynb         # Regresión lineal y logística
├── clase_10.ipynb         # Validación cruzada y métricas
├── clase_11.ipynb         # Árboles de decisión
├── clase_12.ipynb         # Ensambles y Random Forest
├── clase_13.ipynb         # Support Vector Machines
├── clase_16.ipynb         # Clustering y aprendizaje no supervisado
├── clase_17.ipynb         # Reducción de dimensionalidad
├── clase_18.ipynb         # Análisis de componentes principales (PCA)
├── clase_19.ipynb         # Proyectos integrador grupal
└── clase_20.ipynb         # Proyectos integrador propios
```

#### 📖 Capítulo 5 - Material Especializado
```
chapter5/
├── SIC_AI_Ch05_Unit01.ipynb    # Unidad principal del capítulo 5
├── ejercio_clase10.ipynb       # Ejercicios prácticos
├── data_Iris.csv              # Dataset clásico para clasificación
├── FinalResult.csv            # Resultados finales de ejercicios
└── final_model.pickle         # Modelo entrenado serializado
```

#### 🎓 Contribuciones de Estudiantes
```
contribuciones_estudiantes/
├── Actividades grupales de diferentes datasets
├── Ejercicios de clustering con vinos y dígitos
├── Implementaciones de SVM por equipos
├── Proyectos de análisis de datos diversos
└── Soluciones creativas a problemas planteados
```

### 🔧 Tecnologías y Bibliotecas

- **Python 3.x**
- **Scikit-learn** - Algoritmos de Machine Learning
- **Pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **Matplotlib/Seaborn** - Visualización de datos
- **Jupyter Notebooks** - Entorno de desarrollo interactivo

### 🚀 Temas Cubiertos

#### 🏗️ Fundamentos
- [ ] Introducción a Machine Learning
- [ ] Preprocesamiento de datos y limpieza
- [ ] División de datasets (train/test/validation)
- [ ] Métricas de evaluación

#### 🎯 Aprendizaje Supervisado
- [ ] **Clasificación:**
  - Regresión Logística
  - Árboles de Decisión
  - Random Forest
  - Support Vector Machines (SVM)
  - K-Nearest Neighbors (KNN)

- [ ] **Regresión:**
  - Regresión Lineal
  - Regresión Polinomial
  - Regularización (Ridge, Lasso)

#### 🔍 Aprendizaje No Supervisado
- [ ] **Clustering:**
  - K-Means
  - Clustering Jerárquico
  - DBSCAN

- [ ] **Reducción de Dimensionalidad:**
  - Análisis de Componentes Principales (PCA)
  - t-SNE

#### ⚡ Temas Avanzados
- [ ] Ensambles de modelos
- [ ] Validación cruzada
- [ ] Selección de hiperparámetros
- [ ] Introducción a redes neuronales

### Datasets Utilizados

1. **Iris Dataset** - Clasificación de especies de flores
2. **Breast Cancer Wisconsin** - Diagnóstico médico  
3. **Wine Dataset** - Clasificación de vinos
4. **California Housing** - Predicción de precios inmobiliarios
5. **Diabetes Dataset** - Predicción de progresión de diabetes
6. **Digits Dataset** - Reconocimiento de dígitos escritos a mano

### 🛠️ Configuración del Entorno

#### Instalación de dependencias:
```bash
pip install -r requirements.txt
```

#### Dependencias principales:
```python
scikit-learn>=1.0.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
```

### 📝 Cómo Usar Este Material

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/davidlealo/sic_ai_2025_jun.git
   cd sic_ai_2025_jun/03machinelearning
   ```

2. **Ejecuta Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **Sigue la secuencia de clases:**
   - Comienza con `clase_06.ipynb`
   - Avanza secuencialmente hasta `clase_20.ipynb`
   - Explora el material del `chapter5/` para profundización
   - Revisa las `contribuciones_estudiantes/` para ver diferentes enfoques

### Objetivos de Aprendizaje

Al completar este módulo, los estudiantes serán capaces de:

- ✅ Comprender los conceptos fundamentales de Machine Learning
- ✅ Implementar algoritmos de clasificación y regresión
- ✅ Realizar preprocesamiento y limpieza de datos
- ✅ Evaluar modelos usando métricas apropiadas
- ✅ Aplicar técnicas de clustering y reducción de dimensionalidad
- ✅ Desarrollar proyectos completos de Machine Learning
- ✅ Interpretar y comunicar resultados de modelos

### Proyectos Destacados

#### Proyecto Integrador - Análisis de Datos Médicos
- Implementación completa de pipeline de ML
- Desde exploración de datos hasta modelo final
- Evaluación rigurosa con métricas médicas relevantes

#### Análisis de Calidad de Vinos
- Clasificación multi-clase de calidad de vinos
- Análisis de características químicas
- Visualización avanzada de resultados

#### Predicción de Precios Inmobiliarios
- Regresión con múltiples variables
- Ingeniería de características
- Optimización de hiperparámetros

### Contribuciones

Las contribuciones de estudiantes se encuentran organizadas en `contribuciones_estudiantes/` e incluyen:

- Soluciones alternativas a ejercicios propuestos
- Análisis exploratorios adicionales
- Implementaciones creativas de algoritmos
- Proyectos grupales colaborativos

### Métricas de Desempeño

Los notebooks incluyen evaluaciones comprehensivas usando:
- **Clasificación:** Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Regresión:** MSE, RMSE, MAE, R²
- **Clustering:** Silhouette Score, Inertia, Calinski-Harabasz Index

### Enlaces Útiles

- [Documentación de Scikit-learn](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

### Contacto

Para preguntas sobre el contenido del curso o dudas técnicas:
- **Profesor:** David Leal
- **Repositorio:** [SIC AI 2025 Jun](https://github.com/davidlealo/sic_ai_2025_jun)



---

**¡Disfruta aprendiendo Machine Learning! 🚀🤖**

> *"El Machine Learning es como la cocina: necesitas buenos ingredientes (datos), las herramientas correctas (algoritmos), y mucha práctica para crear algo delicioso (modelos precisos)."*
