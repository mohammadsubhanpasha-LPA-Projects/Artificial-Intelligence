package knight.bedivere

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    not container.resources.limits
    msg = "Must have resource limits"
}
