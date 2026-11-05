# llm-error-cost-frontier

## Français

Construire une frontière coût erreur avec abstention explicite.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m llm_error_cost_frontier examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Rejoue des seuils sur jugements figés avec coûts d’appel, erreur et revue explicites ; affiche aussi couverture et abstentions pour éviter un gain artificiel par silence.

### Limites

La revue est supposée parfaite dans ce modèle de coût, pas mesurée. Seuils évalués sur cet échantillon, pas calibrés pour production ; pas de nouvel appel LLM.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Build a cost error frontier with explicit abstention.

Synthetic data; no network access or secret required.

```sh
python -m llm_error_cost_frontier examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Replays thresholds on frozen judgments with explicit call, error and review costs; displays coverage and abstentions to avoid artificial wins through silence.

### Limits

Review assumed perfect in this cost model, not measured. Thresholds evaluated on this sample, not production-calibrated; no new LLM call.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Construir una frontera coste error con abstención explícita.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m llm_error_cost_frontier examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Reproduce umbrales sobre juicios fijos con costes explícitos de llamada, error y revisión; muestra cobertura y abstenciones para evitar mejoras por silencio.

### Límites

Revisión supuesta perfecta en este modelo de coste, no medida. Umbrales evaluados en muestra, no calibrados para producción; sin llamadas LLM nuevas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://scikit-learn.org/stable/modules/classification_threshold.html
