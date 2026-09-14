package knight.galahad

violation[msg] {
    input.request.kind.kind == "Deployment"
    container := input.request.object.spec.template.spec.containers[_]
    not contains(container.image, "distroless")
    msg = "Pure images only: image must be distroless"
}
