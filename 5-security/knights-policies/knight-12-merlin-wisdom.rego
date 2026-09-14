package knight.merlin

violation[msg] {
    input.request.kind.kind == "Deployment"
    not input.request.object.metadata.annotations["cosign.signature"]
    msg = "Deny if no cosign signature annotation"
}
