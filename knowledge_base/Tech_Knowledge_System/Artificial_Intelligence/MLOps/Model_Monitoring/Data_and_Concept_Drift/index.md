# Data and Concept Drift

**Path:** Tech_Knowledge_System/Artificial_Intelligence/MLOps/Model_Monitoring/Data_and_Concept_Drift
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Data drift refers to changes in the statistical properties of input data over time, while concept drift denotes changes in the relationship between input features and the target variable. Both phenomena cause machine learning models to become outdated and perform poorly in production, necessitating continuous monitoring and adaptation.

## Key Concepts
- Data Drift → Changes in input data distribution (e.g., feature values).
- Concept Drift → Changes in the underlying relationship between features and target.
- Model Degradation → Decline in model performance due to drift.
- Monitoring Metrics → Statistical tests and performance indicators used for detection.
- Retraining Strategies → Methods for updating models to counteract drift.
- Adaptive Learning → Algorithms designed to continuously adjust to changing data.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Evidently AI | Library | Open-source tool for data and model monitoring. |
| Fiddler AI | Platform | Enterprise-grade MLOps platform for model monitoring and explainability. |
| WhyLabs | Platform | AI observability platform for data and model health. |
| Seldon Core | Framework | Open-source platform for deploying, monitoring, and managing ML models. |

## Retrieval Keywords
data drift, concept drift, model monitoring, MLOps, machine learning, model degradation, covariate shift, label shift, concept shift, virtual drift, real drift, retraining, adaptive learning, anomaly detection, statistical process control, A/B testing, model validation, data quality, feature engineering, production ML

## Related Nodes
- → Tech_Knowledge_System/Artificial_Intelligence/MLOps/Model_Monitoring (parent)
- → Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Model_Evaluation (related to performance assessment)
- → Tech_Knowledge_System/Data_Science/Data_Quality (foundational for understanding data issues)

## Fast Queries This Node Should Answer
- "What is the difference between data drift and concept drift?"
- "How does data drift affect machine learning models?"
- "When should I retrain my model due to drift?"
- "What are the main tools for detecting concept drift?"
- "What are common failure modes in model monitoring for drift?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations