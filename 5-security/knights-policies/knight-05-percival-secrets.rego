package knight.percival

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    env := container.env[_]
    contains(lower(env.name), "password")
    msg = "Must use Vault: env contains password"
}

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    env := container.env[_]
    contains(lower(env.name), "secret")
    msg = "Must use Vault: env contains secret"
}
