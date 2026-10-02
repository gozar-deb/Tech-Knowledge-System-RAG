# Physically Based Rendering

**Path:** Tech_Knowledge_System/Computer_Graphics_and_Visualization/Rendering_Fundamentals/Physically_Based_Rendering
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Physically Based Rendering (PBR) is a modern computer graphics paradigm that aims to render images by accurately simulating the physical properties of light and materials. It produces highly realistic visuals by adhering to real-world optical principles, ensuring consistent and believable appearance under diverse lighting conditions.

## Key Concepts
- Energy Conservation → Surfaces reflect less light than they receive, a fundamental principle for realism.
- Microfacet Theory → Models surfaces as microscopic facets, influencing roughness and specular reflections.
- BRDF (Bidirectional Reflectance Distribution Function) → Defines how light is reflected from an opaque surface.
- Albedo → The base color of a surface, representing its diffuse reflectance.
- Fresnel Effect → Light reflection intensity varies with viewing angle, more pronounced at grazing angles.
- Metallic Workflow → A common PBR material setup using metallic and roughness maps.
- Specular/Glossiness Workflow → An alternative PBR material setup using specular and glossiness maps.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Unreal Engine | Game Engine | Real-time PBR rendering and development |
| Unity | Game Engine | Real-time PBR rendering and development |
| Substance Painter | Texturing Software | Creating PBR material textures |
| Blender | 3D Software | 3D modeling, rendering (Cycles/Eevee PBR) |
| Marmoset Toolbag | Real-time Renderer | PBR material authoring and presentation |
| V-Ray | Render Engine | High-quality offline PBR rendering |

## Retrieval Keywords
Physically Based Rendering, PBR, photorealism, computer graphics, rendering, light simulation, material properties, energy conservation, microfacet, BRDF, BxDF, real-time, offline, shading, lighting, texture maps, albedo, specular, metallic, roughness, Fresnel, global illumination, path tracing, game development, architectural visualization, VFX

## Related Nodes
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/Rendering_Fundamentals (parent)
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/Rendering_Fundamentals/Real-Time_Rendering (core application)
- → Tech_Knowledge_System/Computer_Graphics_and_Visualization/Shading_Languages (implementation detail)

## Fast Queries This Node Should Answer
- "What is Physically Based Rendering?"
- "How does PBR work?"
- "When should I use PBR?"
- "What are the main tools for PBR?"
- "What are common failures in PBR?"
- "What are the core concepts of PBR?"
- "How does energy conservation apply in PBR?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations