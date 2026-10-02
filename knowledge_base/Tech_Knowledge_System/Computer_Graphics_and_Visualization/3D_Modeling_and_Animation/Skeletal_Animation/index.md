# Skeletal Animation

**Path:** Tech_Knowledge_System/Computer_Graphics_and_Visualization/3D_Modeling_and_Animation/Skeletal_Animation
**Difficulty:** Intermediate
**Time to Learn:** 3–6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Skeletal animation is a 3D computer animation technique where a surface mesh is deformed by an underlying hierarchical structure of bones (a rig). By animating the bones, the attached mesh automatically updates its vertices based on assigned weights, enabling efficient and realistic character movement.

## Key Concepts
- Rigging → Creating the bone hierarchy and control systems for a model.
- Skinning → Binding mesh vertices to bones with specific influence weights.
- Forward Kinematics (FK) → Rotating parent joints to move child joints down the chain.
- Inverse Kinematics (IK) → Positioning an end effector to automatically calculate parent joint rotations.
- Linear Blend Skinning (LBS) → The standard algorithm for calculating vertex positions based on bone transforms.
- Animation Retargeting → Transferring animations from one skeletal structure to a different one.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Autodesk Maya | DCC Software | Industry standard for rigging and keyframe animation |
| Blender | DCC Software | Open-source alternative for full animation pipelines |
| Unreal Engine | Game Engine | Real-time animation blending, retargeting, and state machines |
| MotionBuilder | Animation Software | Specialized tool for motion capture editing and retargeting |

## Retrieval Keywords
skeletal animation, rigging, skinning, inverse kinematics, IK, forward kinematics, FK, linear blend skinning, dual quaternion skinning, bone hierarchy, vertex weights, animation retargeting, motion capture, blend shapes, avatar animation

## Related Nodes
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/3D_Modeling_and_Animation/Rigging (prerequisite)
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/3D_Modeling_and_Animation/Motion_Capture (data_source)
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/Rendering/Real_Time_Rendering (application)

## Fast Queries This Node Should Answer
- "What is skeletal animation?"
- "How does inverse kinematics work in character animation?"
- "When should I use dual quaternion skinning over linear blend skinning?"
- "What are the main tools for rigging and animating 3D characters?"
- "What are common failures in skinning like the candy wrapper effect?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations