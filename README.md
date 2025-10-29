
# BioOmicsHub

Plataforma modular para análisis de datos ómicos en Python. Incluye **tres módulos** principales:

1. `miRNA_mRNA_networks` — construcción y análisis de redes miRNA-mRNA (Carolina).
2. `variant_classification` — clasificación de variantes y riesgo clínico en LLA pediátrica (Francisco).
3. `noncoding_RNA` — análisis exploratorio y visualización de RNAs no codificantes (Violeta).

## Instalación (Poetry)

```bash
pip install poetry
poetry install
poetry run python -m ipykernel install --user --name bioomicshub
```

## Estructura
```
BioOmicsHub/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   └── bioomicshub/
│       ├── core/
│       └── modules/
└── tests/
```

## Uso rápido
```bash
poetry run python -m bioomicshub.scripts.demo_run
```

> Genera `bubble_example.png` como ejemplo.

© 2025 BioOmicsHub – MIT License.
