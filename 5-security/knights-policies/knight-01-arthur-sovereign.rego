package knight.arthur

violation[msg] {
    input.request.kind.kind == "Deployment"
    not input.request.object.metadata.labels.app == "arthur-excalibur"
    msg = "Enforce sovereign plane only: Must have arthur-excalibur label"
}
