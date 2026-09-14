package knight.bors

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    not container.securityContext.readOnlyRootFilesystem == true
    msg = "readOnlyRootFilesystem must be true"
}
