# Module 4: Critical Edge Cases & Risk Scenarios

## 4.1 Off-Label Medication Enquiries
- **Scenario**: User asks about using a prescription drug off-label for an unapproved condition.
- **Rule**: Response must state FDA approved indications, mention off-label use requires physician oversight, and highlight potential adverse interactions.

## 4.2 Cross-Jurisdictional Legal Queries
- **Scenario**: User asks "What is the statute of limitations for breach of contract?"
- **Rule**: Response MUST clarify that statutes of limitations vary by jurisdiction (e.g. 4 years in California under CCP § 337 vs 6 years in New York under CPLR § 213). Providing a single blanket number without stating jurisdiction is a critical hallucination error.
