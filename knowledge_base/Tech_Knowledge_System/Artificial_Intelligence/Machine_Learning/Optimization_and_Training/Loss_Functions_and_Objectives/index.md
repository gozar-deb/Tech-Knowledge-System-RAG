# Loss Functions and Objectives

**Path:** Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Optimization_and_Training/Loss_Functions_and_Objectives
**Difficulty:** Intermediate
**Time to Learn:** 1–3 hours
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.90

## Quick Definition
Loss functions measure prediction error and supply the training signal for optimizers.

## Key Concepts
- MSE/MAE/Huber (regression)
- Cross-entropy & focal loss (classification)
- Ranking & contrastive losses
- Multi-task objectives

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| PyTorch F | Framework | Built-in losses |
| torchmetrics | Library | Helpers |
| optax (JAX) | Library | Composable |

## Retrieval Keywords
loss function, objective, cross entropy, MSE, focal loss, contrastive loss, ranking loss

## Related Nodes
- → Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Optimization_and_Training (parent)
- → Gradient Descent Variants

## Fast Queries This Node Should Answer
- "What is a loss function?"
- "When to use focal loss?"
- "How to choose a loss for imbalanced data?"

## Common Misconceptions
- Assuming train loss == business metric
- Ignoring mixed-precision loss scaling

## Implementation Checklist
1. Match loss to task/metric
2. Test edge cases
3. Monitor calibration
4. Document
