# SHAP and LIME

**Path:** Tech_Knowledge_System/Artificial_Intelligence/AI_Ethics_and_Safety/Explainable_AI/SHAP_and_LIME
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) are leading Explainable AI (XAI) techniques. They provide insights into how machine learning models make predictions, enhancing transparency and trust by attributing feature contributions to model outputs.

## Key Concepts
- SHAP → Game-theoretic approach for global and local model interpretability.
- LIME → Local, interpretable surrogate models to explain individual predictions.
- Shapley Values → Fair allocation of feature contributions based on cooperative game theory.
- Model-Agnostic → Applicable to any machine learning model without internal access.
- Local Explanations → Understanding feature impact for a single prediction.
- Global Explanations → Understanding overall feature importance across the entire dataset.
- Feature Importance → Quantification of how much each input feature influences a model\'s output.
- Perturbation → Systematic modification of inputs to observe prediction changes, used by LIME.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| SHAP library | Python Package | Calculates Shapley values for model explanations |
| LIME library | Python Package | Generates local interpretable explanations for predictions |
| scikit-learn | ML Library | Provides various machine learning models to be explained |
| TensorFlow/PyTorch | Deep Learning Frameworks | Used for building complex models that require explanation |
| Jupyter Notebooks | Development Environment | Interactive environment for XAI experimentation and visualization |

## Retrieval Keywords
SHAP, LIME, Explainable AI, XAI, model interpretability, machine learning explanations, local explanations, global explanations, feature importance, Shapley values, surrogate models, AI ethics, AI safety, model transparency, black-box models, post-hoc interpretability, model debugging, AI auditing, feature attribution, game theory, perturbation methods

## Related Nodes
- → Tech_Knowledge_System/Artificial_Intelligence/AI_Ethics_and_Safety/Explainable_AI (parent)
- → Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning (foundational concept)
- → Tech_Knowledge_System/Artificial_Intelligence/AI_Ethics_and_Safety/Bias_and_Fairness_in_AI (application area)
- → Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Model_Evaluation_and_Validation (complementary techniques)

## Fast Queries This Node Should Answer
- "What is SHAP and LIME?"
- "How do SHAP and LIME work?"
- "When should I use SHAP vs LIME?"
- "What are the main tools for Explainable AI?"
- "What are common failure modes in XAI using SHAP and LIME?"
- "How can SHAP and LIME improve AI model transparency?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations