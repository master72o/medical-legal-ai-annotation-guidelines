# Module 1: Task Definition & SME Operational Scope

## 1.1 Objective
This document governs the annotation and evaluation of LLM outputs in high-stakes domain-specific applications: **Biomedical/Clinical Healthcare** and **Legal/Regulatory Compliance**.

Given the severe risks associated with erroneous medical recommendations or incorrect legal counsel, annotations in these domains MUST be conducted or audited by Subject Matter Experts (SMEs—MDs, PharmDs, JDs, or certified paralegals).

---

## 1.2 Core Domain Annotation Tasks

### Medical AI Task: Clinical QA & Information Safety
- Evaluate model responses to clinical queries, symptom checkers, drug-drug interaction checks, and patient education.
- Enforce mandatory **Diagnostic & Medical Disclaimers**.
- Verify that recommendations align with peer-reviewed medical consensus (e.g. PubMed, PubMed Central, UpToDate, WHO, FDA guidelines).

### Legal AI Task: Statutory Analysis & Contract Review
- Evaluate model outputs for statutory interpretation, case law retrieval, contract clause summary, and regulatory compliance.
- Enforce explicit **Jurisdiction Grounding** (e.g. US Federal Law vs California State Law vs EU GDPR).
- Ensure model explicitly disclaims providing formal legal advice (Unauthorized Practice of Law refusal).
