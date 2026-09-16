# ADR 001: Why Buildpacks over Dockerfile
**Context:** Need fast deployment pipeline under 62s. Dockerfile taking 12min to build.
**Decision:** Selected Paketo Buildpacks over manual Dockerfile.
**Why Buildpacks:** Achieves 18s build time and 11.2MB image via caching.
**Why NOT Dockerfile:** Manual, slow (12min build), resulted in 500MB images.
**Trade-off:** Buildpacks are blackbox; a default to Python 3.10 instead of 3.11 caused a prod crash and 2hrs debugging. Fixed by explicitly pinning version in project.toml.
