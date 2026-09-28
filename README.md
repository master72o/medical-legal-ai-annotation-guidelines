# Domain-Specific Medical & Legal AI Data Annotation Guidelines

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest](https://img.shields.io/badge/PyTest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A 25-page, high-rigor Annotation Guideline Manual & Subject Matter Expert (SME) Standard Operating Procedure (SOP) tailored for domain-specific evaluation of Healthcare/Biomedical and Legal/Regulatory LLMs.

---

## 📖 Manual Modules & Domain Structure

1. [**Task Definition & SME Operational Scope**](./manual/01_task_definition.md) — Scope definition for clinical decision support QA and legal statutory analysis annotation.
2. [**Domain Taxonomy & Specialized Ontology**](./manual/02_taxonomy_and_ontology.md) — Clinical safety, diagnostic disclaimers, legal citation precision, statutory jurisdiction boundaries.
3. [**Domain Rubric Examples & Counter-Examples**](./manual/03_rubric_examples_and_counterexamples.md) — Side-by-side medical symptom triage and legal contract clause evaluation.
4. [**Critical Edge Cases & High-Risk Scenarios**](./manual/04_edge_cases_and_risk_scenarios.md) — Off-label drug recommendations, emergency medical triage, cross-jurisdictional legal advice.
5. [**QA Checklist & SME Verification Rules**](./manual/05_qa_checklist_sme_rules.md) — Pre-submission checklists for board-certified physicians and legal annotators.
6. [**Disagreement & SME Adjudication Workflow**](./manual/06_disagreement_sme_adjudication.md) — Resolution mechanics for conflicting medical literature or legal precedents.
7. [**Escalation Rules & High-Risk Domain Hazards**](./manual/07_escalation_rules_high_risk_hazards.md) — Escalation protocols for lethal medical advice or unauthorized practice of law (UPL).

---

## 🛠️ Validation Tooling

- **Schema Config**: [`schemas/domain_annotation_schema.json`](./schemas/domain_annotation_schema.json)
- **SME Gold Dataset**: [`data/sme_gold_dataset.json`](./data/sme_gold_dataset.json)
- **Validator**: Run `python validator.py --dataset data/sme_gold_dataset.json`
- **Tests**: Run `pytest tests/`
