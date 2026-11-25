"""Rutas que usa la API, tomadas de la configuración del proyecto."""

from ejercicio_clases.config import MODELS_DIR, PROJ_ROOT

PIPELINE_INFERENCIA_FILE = MODELS_DIR / "pipeline_inferencia.joblib"
CONFIG_FILE = PROJ_ROOT / "pipeline_config.yaml"
