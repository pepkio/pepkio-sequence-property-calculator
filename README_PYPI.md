# Pepkio Sequence Property Calculator

Python interface for running sequence-property, dilution, and ligation calculations through the Pepkio Tools API from scripts and notebooks.

# What It Does

This package calls the `sequence-property-calculator` API and returns structured results for three workflows: sequence property analysis from FASTA text, dilution planning, and ligation insert-mass estimation. It is designed for researchers who want reproducible programmatic runs instead of manual copy/paste between calculators.

# Features

- Fetches and caches the live tool manifest
- Runs manifest examples directly (`mixed_fasta`, `dilution_simple`, `ligation_1to3`)
- Supports API run options (`idempotency_key`, `label`)
- Retrieves run records by `run_id` and can poll until terminal status
- Includes a CLI (`manifest` and `run`) for shell workflows

# Installation

```bash
pip install pepkio-sequence-property-calculator
```

# Quick Example

```python
from pepkio_sequence_property_calculator import PepkioClient

with PepkioClient(api_key="YOUR_PEPKIO_API_KEY") as client:
    payload = client.get_example_input("protein_insulin_b")
    run = client.run(payload)
    print(run.status)
    print(run.result.get("valid_count"))
```

# Typical Use Cases

- Batch sequence property checks for DNA, RNA, and protein FASTA sets
- Scripted pI/MW lookups in analysis notebooks
- Serial dilution planning from stock and target concentrations
- Ligation insert mass calculations for cloning prep sheets
- CI smoke tests that validate expected result shape from manifest examples

# Scientific Background

Sequence mode reports molecular properties such as MW, pI, GC%, and extinction-related values based on provided sequence and calculation settings. Dilution mode follows concentration-volume relations (C1V1=C2V2), while ligation mode applies ratio-based insert/vector mass relationships.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/sequence-property-calculator

The web interface provides interactive forms and shareable run links for collaborative protocol review.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-sequence-property-calculator

Web Application: https://www.pepkio.com/tools/sequence-property-calculator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and provides bioinformatics analysis services for life science research. Additional tools and analysis services are available at https://www.pepkio.com/cro.

# Keywords

sequence property calculator, FASTA calculator, molecular weight calculator, protein pI calculator, GC content calculator, sequence analysis API, DNA RNA protein calculator, oligo molecular weight, dilution calculator, serial dilution planning, ligation insert mass, cloning calculator, bioinformatics Python package, Pepkio tools API, laboratory calculation automation, sequence workflow scripting, notebook-ready sequence calculations, run Pepkio sequence calculator from Python, FASTA to MW and pI in API workflow, API-based dilution and ligation planning
