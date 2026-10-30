# Pepkio Sequence Property Calculator

Containerized CLI access to sequence-property, dilution, and ligation calculations through the Pepkio Tools API.

# What It Does

This image runs the `pepkio-sequence-property-calculator` CLI against the hosted API backend. It supports manifest discovery, sequence property workflows from FASTA text, dilution planning, and ligation insert-mass estimation using the same input structure as the web tool.

Use it when you want a reproducible runtime in CI jobs, shared servers, or scripted command-line workflows without installing Python dependencies directly on the host.

# Features

- CLI commands for `manifest` and `run`
- Manifest example execution (`--example`)
- JSON input execution (`--input-json`)
- API base URL override for environment switching
- Structured run responses with `run_id`, `status`, and `result`

# Quick Start

```bash
docker pull pepkio/sequence-property-calculator:<tag>
docker run --rm -it pepkio/sequence-property-calculator:<tag>
```

Run a manifest example:

```bash
docker run --rm \
  -e PEPKIO_API_KEY="YOUR_PEPKIO_API_KEY" \
  pepkio/sequence-property-calculator:<tag> \
  pepkio-sequence-property-calculator run --example mixed_fasta
```

# Quick Example

```bash
docker run --rm \
  -e PEPKIO_API_KEY="YOUR_PEPKIO_API_KEY" \
  pepkio/sequence-property-calculator:<tag> \
  pepkio-sequence-property-calculator run --input-json '{"mode":"ligation","vector_length_bp":5000,"insert_length_bp":1500,"vector_mass_ng":50,"molar_ratio":3}'
```

# Typical Use Cases

- Running sequence property checks from FASTA in containerized pipelines
- Validating dilution calculations in reproducible assay-prep jobs
- Computing ligation insert mass in automation scripts
- Reusing manifest examples as smoke tests in CI

# Scientific Background

Sequence mode reports molecular properties such as MW, pI, GC%, and extinction-related values, with options for mass type, topology, and strand handling. Dilution mode follows concentration-volume relations, and ligation mode computes insert mass from vector/insert length ratios and molar ratio inputs.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/sequence-property-calculator

The web interface offers interactive forms and shareable run links for protocol review.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-sequence-property-calculator

Web Application: https://www.pepkio.com/tools/sequence-property-calculator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).
