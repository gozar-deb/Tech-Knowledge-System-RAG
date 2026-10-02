# Unsupervised TS Anomaly

**Path:** Tech_Knowledge_System/Artificial_Intelligence/Time_Series_Analysis/Anomaly_Detection_TS/Unsupervised_TS_Anomaly
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Unsupervised time series anomaly detection identifies unusual patterns in sequential data without relying on pre-labeled anomalies. It learns normal behavior from the data itself and flags deviations as potential anomalies, making it suitable for scenarios where labeled data is scarce.

## Key Concepts
- Novelty Detection → identifying unseen patterns as anomalies
- Outlier Detection → finding data points significantly different from the majority
- Reconstruction Error → high error in autoencoders indicates an anomaly
- Density-Based Methods → anomalies based on local data density (e.g., LOF)
- Distance-Based Methods → anomalies based on distance from neighbors or centroids
- Sequential Patterns → analyzing temporal order for deviations
- Concept Drift → changes in normal data distribution over time

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Isolation Forest | Algorithm | Tree-based outlier detection |
| One-Class SVM | Algorithm | Finds a hyperplane to separate normal data from origin |
| Autoencoders | Deep Learning | Learns data representation; high reconstruction error implies anomaly |
| LOF (Local Outlier Factor) | Algorithm | Density-based anomaly detection |
| PyOD | Library | Comprehensive Python library for outlier detection |
| Prophet | Library | Time series forecasting, can be adapted for anomaly detection |

## Retrieval Keywords
unsupervised, time series, anomaly detection, outlier, novelty, sequential data, machine learning, deep learning, clustering, autoencoder, isolation forest, one-class SVM, LOF, statistical, multivariate, univariate, real-time, streaming, concept drift, reconstruction error, pattern recognition, deviation, abnormal behavior, data science, AI, ML

## Related Nodes
- → Tech_Knowledge_System/Artificial_Intelligence/Time_Series_Analysis/Anomaly_Detection_TS (parent)
- → Tech_Knowledge_System/Artificial_Intelligence/Time_Series_Analysis (grandparent)
- → Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Clustering (related)
- → Tech_Knowledge_System/Artificial_Intelligence/Deep_Learning/Autoencoders (related)

## Fast Queries This Node Should Answer
- "What is unsupervised time series anomaly detection?"
- "How do unsupervised anomaly detection algorithms work for time series?"
- "When should I use unsupervised methods for time series anomalies?"
- "What are the main tools for unsupervised time series anomaly detection?"
- "What are common failure modes in unsupervised time series anomaly detection systems?"
- "How can I optimize unsupervised time series anomaly detection models?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations