package knight.lancelot

violation[msg] {
    input.request.kind.kind == "Deployment"
    not input.request.object.spec.template.spec.securityContext.runAsNonRoot == true
    msg = "Lancelot trusts no root: runAsNonRoot must be true"
}
