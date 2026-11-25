# API de predicción de precios de vivienda

API para generar en línea predicciones de `SalePrice` con el pipeline de inferencia entrenado en este proyecto.

**Estado:** estructura inicial. Los endpoints todavía no están implementados.

## Estructura

```
api
├── main.py              <- Punto de entrada de FastAPI
├── config.py            <- Rutas al modelo y a la configuración del proyecto
├── routes               <- Endpoints HTTP
│   ├── health.py        <- Estado del servicio
│   └── predictions.py   <- Predicciones
├── schemas
│   └── prediction.py    <- Esquemas de entrada y salida
├── services
│   └── predictor.py     <- Carga del modelo y cálculo de predicciones
└── tests                <- Pruebas automatizadas
```

## Recursos del proyecto que reutiliza

| Recurso | Uso |
|---|---|
| `models/pipeline_inferencia.joblib` | Recibe datos crudos y devuelve el precio en dólares |
| `pipeline_config.yaml` | Lista `MODEL_FEATURES` con las 30 variables de entrada |
| `ejercicio_clases/config.py` | Rutas del proyecto |
| `requirements.txt` | Dependencias, en la raíz del proyecto |
