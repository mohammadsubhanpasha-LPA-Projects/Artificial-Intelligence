package knight.gawain

violation[msg] {
    input.request.kind.kind == "Deployment"
    replicas := input.request.object.spec.replicas
    replicas < 3
    msg = "Gawain never falls alone: replicas must be >= 3"
}
