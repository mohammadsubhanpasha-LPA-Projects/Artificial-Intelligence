package knight.tristan

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    container.securityContext.allowPrivilegeEscalation == true
    msg = "Loyalty means no privilege escalation: allowPrivilegeEscalation must be false"
}
